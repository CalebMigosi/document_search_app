import React from "react";
import FrissBox from "../../ui/Box";
import styled from "styled-components"

const _handleClick = (e, props, i) =>{
    // Get button text
    var buttonText = props["button" + i].toLowerCase().replace(" ", "-")
    props.setDisplayContent(buttonText)
}

export default function ParameterBox(props){
    return(
        <FrissBox height="40" width="80">
            <Image src={props.src}></Image>
            
            <Header>{props.header_text}</Header>

            <ButtonContainer>
                <Button onClick={e => _handleClick(e, props, "1")}>{props.button1}</Button>
                <Button onClick={e => _handleClick(e, props, "2")}>{props.button2}</Button>
            </ButtonContainer>

        </FrissBox>
    )
}

const Header = styled.h2`
    height: 2rem;
    font-weight: 600;
    font-size: 25px;
    margin-bottom: 1rem;
`

const Image = styled.img`
    width: 66%;
    height: 20vh;
    border-radius: 24px;
    margin-bottom: 1rem;
`

const ButtonContainer = styled.div`
    display: flex;
    gap: 5rem;
`
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