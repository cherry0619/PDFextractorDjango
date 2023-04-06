

class PdfExtractor{
    constructor(element,requestMethodEx,requestUrlEx){
        this.element =element;
        this.requestMethodEx =requestMethodEx;
        this.requestUrlEx =requestUrlEx;
        this.element.addEventListener("click", (event) => this.extractor(event));
    }

    changeFicoValue(tb,cellValueArray){
        for (let i = 1; i < tb.rows.length; i++) {
            for (let j = 0; j < tb.rows[i].cells.length; j++) {
              const cell = tb.rows[i].cells[j];
              cell.innerHTML =cellValueArray[i-1][j];
            }
        }
    }

    changeBereauValue(tb,cellValueArray){
        var tbody = document.createElement("tbody");
        for(var i =0; i<cellValueArray.length;i++){
            var row = document.createElement("tr");
            var rowValues = cellValueArray[i];
            for(var j =0;j<rowValues.length;j++){
                var cell = document.createElement("td");
                cell.innerHTML =rowValues[j];
                row.appendChild(cell);
            }
            tbody.appendChild(row);
        }
        tb.replaceChild(tbody,tb.tBodies[0]);
    }

    extractor(event){
        // return the structured data
        fetch(this.requestUrlEx,{method:this.requestMethodEx})
        .then(response =>{
            if (!response.ok){throw new Error("Network response was not ok!")};
            return response.json();
        })
        .then(data =>{
            // change the value of html elements
            var tbFICO= document.getElementById('FICO-SCORE-SUMMARY');
            var FICOData =data.scoreSummary;
            this.changeFicoValue(tbFICO,FICOData);
            //
            var TbBereau =document.getElementById('BUREAU-SUMMARY');
            var bereauData =data.bereauSummary;
            this.changeBereauValue(TbBereau,bereauData);
        })
    }
}

const extractBotton = document.getElementById("extractorButton");
const viewUrl =extractBotton.dataset.viewurl;
const PdfExtract = new PdfExtractor(extractBotton,
                                    "GET",
                                    viewUrl);