<?php

$chosen = false;

if ( isset($_POST["chosenTitle"]) ) {
    $chosen = $_POST["chosenTitle"];
    $sep = explode('//', $chosen);
    $title = $sep[0];
    $name = substr($sep[1], 0, -4);
    $titlesplit = array_map('trim', explode(':', $title));
    $realtitle = $titlesplit[0];
    $mloutput = $name . '_' . $realtitle . '.txt';
    print($mloutput);
    $mlencode = rawurlencode($mloutput);
    print($mlencode);

    header("Location: index.php?page=run_analysis&title=".$mlencode);
}