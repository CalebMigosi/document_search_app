import React from "react";
import ParameterBox from "./ParameterBox";
import UploadImage from "../../../assets/img/upload.svg";

export default function Upload(props){
    return(
        <ParameterBox src={UploadImage}
            setDisplayContent= {props.setDisplayContent}
            header_text="Upload Details"
            button1 = "Upload Individual"
            button2 = "Bulk Upload">
            This is a test
        </ParameterBox>
    )
}


