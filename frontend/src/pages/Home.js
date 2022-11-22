import React from "react";
import HeaderBar from "../components/ui/HeaderBar"
import styled from "styled-components"
import { useState } from "react";
import Screener from "../components/page-components/parameter-boxes/Upload";
import Upload from "../components/page-components/parameter-boxes/Screener";
import DisplayContentBox from "../components/page-components/DisplayContentBox";

export default function Home(){
    const [displayContent, setDisplayContent] = useState('upload-individual')

    return (
        <div className="App">
            <HeaderBar className="header-bar"></HeaderBar>
            <MainContainer className="main-content">
                <BoxContainer className="parameter-box">
                    <Screener className="screener" setDisplayContent={setDisplayContent}></Screener>
                    <Upload className="upload" setDisplayContent={setDisplayContent}></Upload>
                </BoxContainer>

                <DisplayContentBox displayContent={displayContent}></DisplayContentBox>
            </MainContainer>

        </div>
      );

}

const BoxContainer = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: rgb(171, 184, 195, 0.1);
    border: 1px solid rgb(171, 184, 195, 0.5);
    width: 40vw;
    height: 100%;
    border-radius: 40px;
    padding: 1rem;
`

const MainContainer = styled.div`
    display: flex;
    flex-direction: row;
    gap: 10rem;
    height: 82%;
    margin: 2rem;
`