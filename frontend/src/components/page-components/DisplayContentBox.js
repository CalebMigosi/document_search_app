import React from "react";
import styled from "styled-components";
import BoxContainer from "../ui/BoxContainer";
import OutputBox from "./OutputBox"
import ContentParameters from "./ContentParameters"
import UpdateContent from "../../services/APICalls"
import { useState } from "react";

export default function DisplayContentBox(props){
    const [content, setContent] = useState('')

    return (
        <BoxContainer>
            <ContentParameters id="content-parameter-box" displayContent={props.displayContent}></ContentParameters>
            <OutputBox content={content} ></OutputBox>
            <Button onClick={e => UpdateContent(e, setContent, props.displayContent)}> RUN </Button>
        </BoxContainer>        
    )
}

const Button = styled.button`
    color: #050a30;
    font-family: Montserrat;
    font-weight: 600;
    font-size: 15px;
    background-color: transparent;
    border-radius: 24px;
    border: 2px solid orange;
    width: 12rem;
    height: 2.7rem;
    text-transform: capitalize;
    float: left;

    &:hover{
        background-color: orange;
    }
`