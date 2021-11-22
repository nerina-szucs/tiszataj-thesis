<?php
require "choose_creator.php";
$arg = $_GET["xmlname"];
putenv("PYTHONIOENCODING=utf-8");
$output = shell_exec('python "./scripts/getXMLdata.py" "'.$arg.'" 2>&1');
$formatted_output = ltrim($output, 0);
$decodedJson = json_decode($formatted_output);
echo '<h2>Cím választása</h2>';
echo '<p>';
echo '<form method="POST" action="go_to_analysis.php" accept-charset="utf-8">';
echo '<div class="form-group">';
echo '<select class="form-control form-control-lg" name="chosenTitle">';
foreach($decodedJson as $value) {
    echo '<option value="'.$value.'//'.$arg.'">'.$value.'</option>';
}
echo '</select></div>';
echo '<div class="form-group justify-content-center"><input class="btn btn-primary btn-lg btn-block" style="width:20%;margin:0 auto;" type="submit" value="Elemzés" /></div>';
echo '</form></p>';