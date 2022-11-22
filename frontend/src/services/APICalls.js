import FillTable from "./FillTables"

export default async function UpdateContent(e, setContent, displayContent){
  switch(displayContent){
      case 'upload-individual':
          return uploadIndividual(setContent)

      case 'bulk-upload':
          return console.log("bulk upload to be done")

      case 'identify-individual':
          return searchIndividual(setContent)

      case 'identifier-settings':
          return console.log("identifier settings to be done")

      default:
          return uploadIndividual(setContent)
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
            JSONResult = FillTable(data)
            setContent(JSONResult)
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
      then(resp => resp.json()).
      then(data =>{
          JSONResult = FillTable(data)
          setContent(JSONResult)
      })
}