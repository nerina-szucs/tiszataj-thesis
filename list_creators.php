<h2>Szerző választása</h2>
<p>
<form method="POST" action="choose_creator.php" accept-charset="utf-8">
    <div class="form-group">
<select class="form-control form-control-lg" name="chosenCreator">

<?php
require "functions.php";

if ($handle = opendir('./scripts/txtoutputs/mloutputs')) {
    $shownAuthors = Array();

    while (false !== ($entry = readdir($handle))) {

        if ($entry != "." && $entry != "..") {
            // $chopped = str_replace("_", " ", $entry);
            // $name = before_last('___', $chopped);
            $chopped = before_last('___', $entry);
            $name = str_replace("_", " ", $chopped);
            //echo "$entry\n";
            if (!in_array($name, $shownAuthors)) {
                echo '<option value="' . $chopped . '">' . $name . '</option>';
                $shownAuthors[] = $name;
            }
        }
    }

    closedir($handle);
}
?>

</select>
    </div>
    <div class="form-group justify-content-center">
    <input class="btn btn-primary btn-lg btn-block" style="width:20%;margin:0 auto;" type="submit" value="Tovább" />
    </div>
</form>
</p>