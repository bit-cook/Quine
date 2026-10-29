/*
 * JavaScript Quine - classic self-reproducing program.
 * Verify: node quine.js | diff - quine.js
 */
(function q(){console.log('/*'+String.fromCharCode(10)+' * JavaScript Quine - classic self-reproducing program.'+String.fromCharCode(10)+' * Verify: node quine.js | diff - quine.js'+String.fromCharCode(10)+' */'+String.fromCharCode(10)+'('+q+')()')})()
