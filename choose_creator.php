<?php

$xmlname = false;

if ( isset($_POST["chosenCreator"]) ) {
    $xmlname = $_POST["chosenCreator"];

    header("Location: index.php?page=get_creations&xmlname=".$xmlname);
}