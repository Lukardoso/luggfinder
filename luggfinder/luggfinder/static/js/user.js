import { sendToServer } from "./modules.js";


const row = document.querySelectorAll(".table-data");
const saveToDataBaseBtn = document.querySelector("#save-changes");


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

// Send it to server:
saveToDataBaseBtn.addEventListener("click", ()=> {
    console.log("sending data...");
    sendToServer(changedDataReady);
    saveToDataBaseBtn.style.display = "none";
});



// // Supplier Dropdown:
// const supplierInput = $("input[name=supplier]");
// const supplierDropdown = $(".supplier-selection");

// supplierInput.click(function () {
//     supplierInput.each(function () {
//         $(this).css("display", "none")
//     })
// })

