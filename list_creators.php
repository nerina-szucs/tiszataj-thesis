<h2>Szerző választása</h2>
<p>
<form method="POST" action="choose_creator.php" accept-charset="utf-8">
    <div class="form-group">
<select class="form-control form-control-lg" name="chosenCreator">

<?php

function strrevpos($instr, $needle)
{
    $rev_pos = strpos (strrev($instr), strrev($needle));
    if ($rev_pos===false) return false;
    else return strlen($instr) - $rev_pos - strlen($needle);
};

function before_last ($what, $inwhat)
{
    if (!is_bool(strrevpos($inwhat, $what)))
        return substr($inwhat, 0, strrevpos($inwhat, $what));
};

if ($handle = opendir('./scripts/xmloutputs')) {

    while (false !== ($entry = readdir($handle))) {

        if ($entry != "." && $entry != "..") {
            $chopped = str_replace("_", " ", $entry);
            $name = before_last('.', $chopped);
            //echo "$entry\n";
            echo '<option value="'.$entry.'">'.$name.'</option>';
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