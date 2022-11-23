import FillTable from "./FillTables"
import FileReader from "./FileReader"

export default async function UpdateContent(e, setContent, displayContent){
    // Prevent reload
    e.preventDefault()

  switch(displayContent){
      case 'upload-individual':
          return uploadIndividual(e, setContent)

      case 'bulk-upload':
          return await uploadBulk(e, setContent)

      case 'identify-individual':
          return searchIndividual(e, setContent)

      case 'identifier-settings':
          return console.log("identifier settings to be done")

      default:
          return searchIndividual(e, setContent)
  }
}

async function searchIndividual(e, setContent){
    // Get parameters
    var firstName = document.getElementById("First Name").value
    var lastName = document.getElementById("Last Name").value
    var birthdate = document.getElementById("Birthdate").value
    var identification = document.getElementById("Identification").value
    
    // Convert to JSON
    var JSONBody = {
                    "first_name": firstName,
                    "last_name": lastName,
                    "birthdate": birthdate,
                    "identification": identification,
                }
    
    // Filter empty strings
    JSONBody = Object.fromEntries(Object.entries(JSONBody).filter(([key, value]) => ((value != null) && (value !== ""))));
    
    // Make API Call
    var JSONResult;
    await fetch("http://127.0.0.1:8000/check", {
                method: "POST",
                mode: "cors",
                credentials: 'same-origin', 
                headers: {
                  'Content-Type': 'application/json',
                  "Accept": "*/*",
                  "Access-Control-Allow-Origin": "*"
                },
                body: JSON.stringify(JSONBody)
        }).
        then(resp => resp.json()).
        then(data =>{
            console.log(data)
            JSONResult = FillTable(data)
            setContent(JSONResult)
        }).catch(e =>{
            setContent("ERROR: No individuals found.")
        })
}

async function uploadIndividual(e, setContent){
  // Get parameters
  var firstName = document.getElementById("First Name").value
  var lastName = document.getElementById("Last Name").value
  var birthdate = document.getElementById("Birthdate").value
  var identification = document.getElementById("Identification").value
  
  // Convert to JSON
  var JSONBody = {
                  "first_name": firstName,
                  "last_name": lastName,
                  "birthdate": birthdate,
                  "identification": identification,
              }
  
  // Filter empty strings
  JSONBody = Object.fromEntries(Object.entries(JSONBody).filter(([key, value]) => ((value != null) && (value !== ""))));
  
  // Make API Call
  var JSONResult;
  await fetch("http://127.0.0.1:8000/store", {
              method: "POST",
              mode: "cors",
              credentials: 'same-origin', 
              headers: {
                'Content-Type': 'application/json',
                "Accept": "*/*",
                "Access-Control-Allow-Origin": "*"
              },
              body: JSON.stringify(JSONBody)
      }).
      then(resp =>{
          setContent(`${JSONBody["first_name"]} ${JSONBody["last_name"]}' details successfully loaded`)
      }).catch(error =>{
            setContent("ERROR: Could not load details. Please  check inputs.")
      })
}

async function uploadBulk(e, setContent){
    e.preventDefault()

    var fileInput = document.getElementById("file-input").files[0]

    // Get parameters
    var bulkUpload = await FileReader(fileInput)

    // Make API Call
    var JSONResult;
    await fetch("http://127.0.0.1:8000/store_bulk", {
                method: "POST",
                mode: "cors",
                credentials: 'same-origin', 
                headers: {
                  'Content-Type': 'application/json',
                  "Accept": "*/*",
                  "Access-Control-Allow-Origin": "*"
                },
                body: JSON.stringify({"entries": bulkUpload})
        }).
        then(resp => resp.json()).
        then(data =>{
            console.log(data)
            setContent("Bulk upload succeeded")
        })
  }