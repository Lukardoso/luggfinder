// Filters to refined results

const search_bar = document.querySelector('#wtrTransaction');
const search_go = document.querySelector('#wtrTransactionSearchButton');

// WorldTracer loads every new process in a iframe.
const iFrameProcess = document.querySelector('#homeIframe');

const mainLabelColumns = ['File Reference Number', 'File Type', 'Number of bags', 'Creation Date', 'Names', 'Given Name', 'PNR #', 'Reason for loss', 'Fault Station', 'Amount', 'Address', 'Cell/Mobile Phone Number', 'City', 'Email Address', 'Tag #', 'Cost Remarks'];
const mainLabelColumnsClearData = {
    'File Reference Number': 'Process',
    'File Type': 'Tipo',
    'Number of bags': 'QntBags',
    'Creation Date': 'Data',
    'Names': 'Sobrenome',
    'Given Name': 'Nome',
    'PNR #': 'PNR',
    'Reason for loss': 'RL',
    'Fault Station': 'FS',
    'Amount': 'Custo',
    'Address': 'Endereco',
    'Cell/Mobile Phone Number': 'Telefone',
    'City': 'Cidade',
    'Email Address': 'Email',
    'Tag #': 'BagTag',
    'Cost Remarks': 'ObsCustos'
};


let process;
let aeroAndCia;
let firstProcessNumber = 0;
let lastProcessNumber = 0;
let processNumber = firstProcessNumber;
let processToString;
let range = 0;
let counter = 1;



// Search and Open Process
// DAH - search AHL | DDP - search DPR
function searchProcess(type, process) {
    search_bar.value = type + " " + process;
    search_go.click();
}


// Compile all the data of the actual process in search for future use.
function getProcessData() {

    let processFrame = document.querySelector('#homeIframe').contentDocument;

    let labels = processFrame.querySelectorAll('.displayLabelColumn');
    let processData = processFrame.querySelectorAll('.displayfieldvalue');

    let rawData = {};

        for (let c = 0; c < labels.length; c++) {
        let label = labels[c].innerText;
        let data = processData[c].innerText;

        // Clearing data
        if (label === "Amount") {data = data.slice(4)};

        if (label === "Creation Date") {data = data.slice(0,7)};

        if (label == "Tag #") {data = data.split(" ").join("")};
        
        if(data.includes("\n")) {data = data.split("\n")[0]};

        Object.assign(rawData, {[label]: data});

    }

    return rawData;
}


// If there are more than one process, then proceed to the next
function nextProcess() {
    if (counter < range) {
        let nextProcessNumber = aeroAndCia + (firstProcessNumber + counter).toString();
        counter += 1;
        searchProcess(processType.value, nextProcessNumber);
    }

    else {
        counter = 1;
        range = 0;
        iFrameProcess.removeEventListener("load", generateJson);
    }
}


// Refining and clearing labels
function clearMainLabels() {
    let cleanMainData = {}

    mainLabelColumns.forEach(label => {

        Object.assign(cleanMainData, {[mainLabelColumnsClearData[label]] : process[label]});

    })

    return cleanMainData;
}


// Generate Json Data
function generateJson() {

    process = getProcessData();
    let mainData = clearMainLabels();
    
    if (process['File Reference Number'] != undefined) {
        let jsonPayload = {
            mainData,
            month: monthSelector.value
        };

        return (            
            console.log(jsonPayload),
            sendToServer(jsonPayload),
            nextProcess()
        )
    }
}


// Send to Server
function sendToServer(jsonPayload) {
    fetch("https://app.lucaslannes.com.br/json/wt", {
    method: "POST",
    body: JSON.stringify(jsonPayload),
    headers: {
        "Content-type": "application/json; charset=UTF-8"
        }
    });
}



// Extension Panel

const pluginPanelHtml = `
<div class="wrapper">
<select name="tipo-de-processo" id="process-type">
    <option value="dah">AHL</option>
    <option value="ddp">DPR</option>
</select>
<select name="seletor-de-mes" id="month-selector">
    <option value="1">janeiro</option>
    <option value="2">fevereiro</option>
    <option value="3">marco</option>
    <option value="4">abril</option>
    <option value="5">maio</option>
    <option value="6">junho</option>
    <option value="7">julho</option>
    <option value="8">agosto</option>
    <option value="9">setembro</option>
    <option value="10">outubro</option>
    <option value="11">novembro</option>
    <option value="12">dezembro</option>
</select>
<input type="text" name="processo-inicial" id="initial-process-range" placeholder="N° do processo inicial">
<input type="text" name="processo-final" id="final-process-range" placeholder="N° do processo final">
<input type="submit" value="Gerar Relatório" id="report-btn">
</div>
`

const pluginPanel = document.createElement('div');
pluginPanel.setAttribute('id', 'plugin-panel');
pluginPanel.innerHTML = pluginPanelHtml;
document.body.append(pluginPanel);

const processType = document.querySelector('#process-type');
const initialProcessRange = document.querySelector('#initial-process-range');
const finalProcessRange = document.querySelector('#final-process-range');
const reportBtn = document.querySelector('#report-btn');
const actualMonth = new Date().getMonth() + 1;
const monthSelector = document.querySelector('#month-selector');

monthSelector.value = actualMonth.toString();


// Trigger to run the extension
reportBtn.addEventListener('click', ()=> {    
    // It takes a bit to the iframe to be ready.
    iFrameProcess.addEventListener('load', generateJson); 

    if (finalProcessRange.value != '') {

        aeroAndCia = initialProcessRange.value.slice(0,5);
        firstProcessNumber =  parseInt(initialProcessRange.value.slice(5));
        lastProcessNumber = parseInt(finalProcessRange.value.slice(5));
        range = lastProcessNumber - firstProcessNumber + 1;

    }
    
    searchProcess(processType.value, initialProcessRange.value);

});