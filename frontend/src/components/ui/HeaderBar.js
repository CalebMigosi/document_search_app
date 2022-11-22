import React from 'react';
import styled from 'styled-components' 
import Logo from "../../assets/img/logo.png"

export default function HeaderBar(){
    return (
        <Header>
            <LogoContainer>
                <Image src={Logo}></Image>
            </LogoContainer>
        </Header>
    )

}

const Header = styled.div`
    width: 100vw;
    height: 7vh;
    background-color: #abb8c3;
    padding-left: 1rem;
    border-bottom: 1px solid silver;
`

const Image = styled.img`
    width: 10rem;
    height: 4rem;
    padding-left: 0rem;
    filter: grayscale(1.0);
    &:hover{
        filter: grayscale(0);
    }
`
const LogoContainer = styled.div`
    width: 10vw;
    &:hover{
        cursor: pointer;
    }
`