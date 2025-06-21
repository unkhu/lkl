<?php
function triangle($n)
{
    for ($i = 0; $i < $n; $i++)
    {
        for ($j = 0; $j < $n - $i - 1; $j++)
            echo "&nbsp;";
        for ($j = 0; $j <= $i; $j++)
            echo "* ";
        echo "<br>";
    }
}
$n = 5;
triangle($n);
?>