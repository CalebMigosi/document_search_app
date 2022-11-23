import Papa from "papaparse";

export default async function FileReader(file){
    return new Promise((resolve)=>{
        Papa.parse(file, {
            header: true,
            skipEmptyLines: true,
            complete: function (results) {
                resolve(results.data)
            }
        }) 

    })
}