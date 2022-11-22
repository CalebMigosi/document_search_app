import React from "react";
import styled from "styled-components";

export default function BoxContainer(props){
    return (
        <Box>
            {props.children}
        </Box>
    )

}

const Box = styled.div`
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