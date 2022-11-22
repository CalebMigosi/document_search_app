import * as React from 'react'
import Box from "@mui/material/Box"

export default function FrissBox(props){
    var styles = {
        "width": props.width/100, 
        "height": props.height/100,
        "margin": "1rem",
        "display": "flex",
        "justifyContent": "center",
        "flexDirection": "column",
    }
    return(
        <Box className="Box" sx={styles} id={props.id}>
            {props.children}
        </Box>
    )
}