import React from "react";
import ScreenerImage from "../../../assets/img/screener.svg";
import ParameterBox from "./ParameterBox";

export default function Screener(props){
    return(
        <ParameterBox src={ScreenerImage} 
                        setDisplayContent= {props.setDisplayContent}
                        header_text="Identity Screener" 
                        button1 = "Identify Individual"
                        button2 = "Identifier Settings">
            Screen for identity of users
        </ParameterBox>
    )
}
