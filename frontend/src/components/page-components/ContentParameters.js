import React from "react";
import FrissBox from "../ui/Box";
import { useState, useEffect } from "react";
import updateParameterContent from "../../services/UpdateParameterContent";

export default function ContentParameters(props){
    const [content, setContent] = useState(updateParameterContent('upload-individual'))

    useEffect(()=>{
        // Get the selection
        var value = props.displayContent

        // Update parameters
        setContent(content => updateParameterContent(value))

    }, [content, props.displayContent])

    return (
        <FrissBox id={props.id} height="20" width="80">
            {content}
        </FrissBox>
    )
}