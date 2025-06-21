<?php
function isPalindrome($input) {
    $revers = strrev($input);
    if ($input == $revers) {
        return "Palindrome String";
    } else {
        return "Non Palindrome String";
    }
}
$input = "madam";
echo isPalindrome($input);
?>