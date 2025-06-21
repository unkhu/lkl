<?php
$text = "Ruchita Jagdish Chaudhari";
$search_char = "a";
$count = 0;

for ($x = 0; $x < strlen($text); $x++) {
    if (substr($text, $x, 1) == $search_char) {
        $count = $count + 1;
    }
}

echo "The character occurs $count times.\n";
?>