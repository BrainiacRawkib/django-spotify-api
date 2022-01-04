import React, {useState, useEffect} from "react";
import {Link} from "react-router-dom";
import {Grid, Button, Typography, IconButton} from "@material-ui/core";
import NavigateBeforeIcon from "@material-ui/icons/NavigateBefore";
import NavigateNextIcon from "@material-ui/icons/NavigateNext";

export default function Info(props) {
    return (
        <Grid container spacing={1}>
            <Grid item xs={12} align='center'>
                <Typography component='h4' variant='h4'>
                    What Django Spotify API?
                </Typography>
            </Grid>
        </Grid>
    )
}