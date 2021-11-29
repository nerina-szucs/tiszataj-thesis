<?php
require "functions.php";
require "choose_creator.php";
$arg = $_GET["creatorname"];
$files = glob("./scripts/txtoutputs/mloutputs/{$arg}*.txt", GLOB_BRACE);
echo '<h2>Cím választása</h2>';
echo '<p>';
echo '<form method="POST" action="go_to_analysis.php" accept-charset="utf-8">';
echo '<div class="form-group">';
echo '<select class="form-control form-control-lg" name="chosenTitle">';
foreach($files as $file) {
    $formatted = after_last_3('___', basename($file));
    $formatted = str_replace('_', ' ', $formatted);
    $formatted = str_replace('out.txt', '', $formatted);
    echo '<option value="'.basename($file).'">'.$formatted.'</option>';
}
echo '</select></div>';
echo '<div class="form-group justify-content-center"><input class="btn btn-primary btn-lg btn-block" style="width:20%;margin:0 auto;" type="submit" value="Elemzés" /></div>';
echo '</form></p>';