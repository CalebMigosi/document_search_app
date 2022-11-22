import React from 'react';
import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/dist/styles/ag-grid.css';
import 'ag-grid-community/dist/styles/ag-theme-alpine.css';
import styled from 'styled-components';

export default function FillTable(data){

    const columnDefs = [
        { field: 'First Name' },
        { field: 'Last Name' },
        { field: 'Probability' }
    ]

    var rowData = []

    if(typeof(data) === "object"){
        if (data.hasOwnProperty("first_name")){
            rowData = [{"First Name": data["first_name"], 
                        "Last Name": data["last_name"], 
                        Probability: data["probability"]}]
        }else{
            return "ERROR: Please review inputs"
        }

    }else{
        data.forEach(row => {
            var rowLine = {"First Name": row["first_name"], 
                        "Last Name": row["last_name"], 
                        Probability: row["probability"]}
            
            // Add new line
            rowData.append(rowLine) 
        })
    }

    return (
        <TableContainer className="ag-theme-alpine">
            <Header>Result</Header>
            <AgGridReact rowData={rowData} columnDefs={columnDefs}>
            </AgGridReact>
        </TableContainer>
        
    )

}

// Styled components
const TableContainer = styled.div`
    height: 30%;
    width: 100%;
    padding-bottom: 5rem;
`

const Header = styled.h2`
    text-align: center;
    width: 100%;
    margin-bottom: 1rem;

`
