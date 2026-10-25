<?php
function greet($name) {
    return "Hello, " . $name . "!";
}
function addNumbers($a, $b) {
    return $a + $b;
}
function isEven($number) {
    return $number % 2 === 0;
}
$names = ["Alice", "Bob", "Carol"];
foreach ($names as $name) {
    echo greet($name) . "\n";
}
$total = 0;
for ($i = 1; $i <= 5; $i++) {
    $total = addNumbers($total, $i);
    if (isEven($total)) {
        echo "Total is even: " . $total . "\n";
    } else {
        echo "Total is odd: " . $total . "\n";
    }
}
$counter = 0;
while ($counter < 3) {
    $counter++;
}
echo "Final total: " . $total . "\n";
echo "Done.\n";
