import React from "react";
import styled from "styled-components";

export default function Input(props){
    return (
        <Fieldset>
            <Label>{props.label}</Label>
            <CustomInput id={props.label}type={props.type}>
            </CustomInput>
        </Fieldset>
    )
}

const Fieldset = styled.fieldset`
    display: flex;
    width: 20rem;
    gap: 3rem;
    border: 0px;
`

const Label = styled.label`
    color: black;
    width: 8rem;
`

const CustomInput = styled.input`
    width: 10rem;
    height: 1rem;
    color: #000D4D;
    &:hover{
        box-shadow: 0 0 2px orange;
    }
    

`