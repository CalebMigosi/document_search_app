import React from "react"
import styled from "styled-components"
import Input from "../components/ui/Input"

const getUploadIndividualParameters =()=>{
    return (
        <ParameterContainer>
            <Header>Upload Individual Entry</Header>
            <Input type="text" label="First Name"></Input>
            <Input type="text" label="Last Name"></Input>
            <Input type="date" label="Birthdate"></Input>
            <Input type="text" label="Identification"></Input>
        </ParameterContainer>
    )
}

const getBulkUploadParameters =()=>{
    return (
        <ParameterContainer>
            <Header>Bulk Upload</Header>
            <FileInput type="file"></FileInput>
        </ParameterContainer>
    )

}

const getIdentifyIndividualParameters =()=>{
    return (
        <ParameterContainer>
            <Header>Identify Individual</Header>
            <Input type="text" label="First Name"></Input>
            <Input type="text" label="Last Name"> First Name</Input>
            <Input type="date" label="Birthdate"> Birthdate </Input>
            <Input type="text" label="Identification"> Identification</Input>
        </ParameterContainer>
    )

}

const getIdentifierSettingsParameters =()=>{
    return (
        <ParameterContainer>
            <Header>Define custom matching pattern</Header>
            <Input type="text" label="First Name"></Input>
            <Input type="text" label="Last Name"> First Name</Input>
            <Input type="date"> Birthdate </Input>
            <Input type="text"> Identification</Input>
        </ParameterContainer>
    )

}

export default function updateParameterContent(value){
    switch(value){
        case 'upload-individual':
            return getUploadIndividualParameters()

        case 'bulk-upload':
            return getBulkUploadParameters()

        case 'identify-individual':
            return getIdentifyIndividualParameters()

        case 'identifier-settings':
            return getIdentifierSettingsParameters()

        default:
            return getUploadIndividualParameters()
    }

}

const ParameterContainer = styled.div`
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    gap: 1rem;
    justify-content: center;
    align-items: center;
`

const Header = styled.div`
    width: 100%;
    height: 2rem;
    text-align: center;
    color: #000D4D;
    font-size: 18px;
    font-weight: 600;
`
const FileInput = styled.input`

`
