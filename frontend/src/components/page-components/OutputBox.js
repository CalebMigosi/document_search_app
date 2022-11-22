import React from "react";
import FrissBox from "../ui/Box";

export default function OutputBox(props){
    return (
        <FrissBox height="60" width="80">
            {props.content}
        </FrissBox>
    )
}