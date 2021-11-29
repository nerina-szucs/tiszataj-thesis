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

function after_last_3 ($what, $inwhat)
{
    if (!is_bool(strrevpos($inwhat, $what)))
        return substr($inwhat, strrevpos($inwhat, $what) + 3);
};