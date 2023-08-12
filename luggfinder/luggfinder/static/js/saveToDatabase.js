const row = document.querySelectorAll(".table-data");
const saveToDataBaseBtn = document.querySelector("#save-changes");


function sendToServer(jsonPayload) {
    fetch("http://127.0.0.1:5000/update_process", {
    method: "POST",
    body: JSON.stringify(jsonPayload),
    headers: {
        "Content-type": "application/json; charset=UTF-8"
        }
    });
}


// Get Changed Data:
let id = 0;
let changedDataReady = {};

row.forEach(cell => {
    cell.addEventListener("change", (e) => {
        saveToDataBaseBtn.style.display = "inline-block";  
        let changedRow = e.currentTarget.querySelectorAll("td");        
        let changedData = {};

        
        changedRow.forEach(changedCell => {
            Object.assign(changedData, {[changedCell.children[0].name] : changedCell.children[0].value});
        })

        if(changedDataReady[0] == undefined) {

            Object.assign(changedDataReady, {0 : changedData});
            console.log(changedDataReady);
    
            id++;
        }
        else {
            let data_exists = [false, 0];

            for(let i in changedDataReady){
                if(changedDataReady[i].process == changedData.process){
                    data_exists = [true, i]
                }        
            }

            if (data_exists[0] == true) {
                Object.assign(changedDataReady, {[data_exists[1]] : changedData});
                console.log(changedDataReady);
            }
            else {
                Object.assign(changedDataReady, {[id] : changedData});
                console.log(changedDataReady);
                id++;                
            }
        }
    })
});


saveToDataBaseBtn.addEventListener("click", ()=> {
    console.log("sending data...");
    sendToServer(changedDataReady);
    saveToDataBaseBtn.style.display = "none";
});
