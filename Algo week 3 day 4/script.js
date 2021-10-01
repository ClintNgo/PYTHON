// Use the bookIndex function below to receive a sorted array of page numbers
// and then return a string that combines consecutive pages to create ranges.

// Example: [1,3,4,5,7,8,10,12,13,14,15,16,17] returns "1, 3-5, 7-8, 10, 12, 14-17"
// [1,3,4,5,7,8,10,12,13,14,15,16,17]
// ['1', '3-5', '7-8', '10', '12', '14-17']
// "1, 3-5, 7-8, 10, 12, 14-17"

// HINTS: 
// You'll want a way to look at the current value and then look at the next one to see if it's one higher
// If it is, then you've found a range, if it's not, you haven't
// You could create a string and add to it, or get rid of the values in the array that aren't needed 
//   and convert to a string, or whatever way you come up with!

// function bookIndex(arr){
//         var startRange = [];
//         for (var i = 0; i < arr.length; i++) { //loop
//             if (arr[i]+1 == arr[i+1]) {  //checking for next number to see if its higher
//                 var startpage = arr[i]; 
//                 while (arr[i]+1 == arr[i+1]) {
//                     i++;
//                 }
//             var endpage = arr[i];
//             startRange.push(startpage + "-" + endpage);
//             } else {
//                 startRange.push(arr[i]);
//             }
//         }
//         var pageRanges = startRange.join(',');
//         return pageRanges
//     }
// console.log(bookIndex([1,3,4,5,7,8,10,12,14,15,16,17]))

// Use the generateCoinChange function below to receive a dollar (decimal) amount with change. 
// Covert that value to the number of quarters, dimes, nickels, and pennies it would have.
// It should count the number or quarters first then work it's way down from there
// This can return a string or an object or whatever you'd like

// Example: generateCoinChange(.67) would return 2 quarters, 1 dime, 1 nickel, 2 pennies
// Example: generateCoinChange(0.77) would return 3 quarters, 2 pennies
// Example: generateCoinChange(2.85) would return 11 quarters, 1 dime
// Example: generateCoinChange(4.57) would return 18 quarters, 1 nickel, 2 pennies


function generateCoinChange(input) {
    var coins = {
    'quarters': 0,
    'dimes': 0,
    'nickels': 0,
    'pennies': 0,
    }
    while (input >= .25){
        input -= .25 
        coins['quarters']++;
    } 
    while (input>= .10){
        input -= .10 
        coins['dimes']++;
    } 
    while (input >= .05){
        input -= .05 
        coins['nickels']++;
    } 
    while (input >= .01){
        input -= .01 
        coins['pennies']++;
    } 
    return coins
}

console.log(generateCoinChange(.67)) 
console.log(generateCoinChange(0.77))
console.log(generateCoinChange(2.85)) 
console.log(generateCoinChange(4.57))