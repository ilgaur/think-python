# Chapter 5 Notes

## Key Concepts
Floor division vs regular division: floor division will output an integer and will always round down the result toward the negative infinite, regular division or decimal division will output the result in a decimal format

Modulus operator result: modulus operator will output the remainder of a division, for example if we do 10 % 3 it will give us 1, or if we do 100 % 60 it will give us 40.

number % 10 = last digit
Because division by 10 separates the tens from the ones, leaving only the ones as remainder. for example take this into account: 324 % 10 --> 4 (First digit from right), because: (321 / 10) = ((3 * 100) / 10) + ((2 * 10) / 10) + ((4 * 1) / 10) --> 300 + 20 + 4 --> 4 comes from 4 / 10 --> 0 which has the remainder of 4 because 4 / 10 is zero, 4 - 0 is 4 --> so with the modulus operator 4 % 10 we get the 4 which is right most digit, this stems from the natural properties of base 10 numbers.

3 Practical uses of the modulus operator:

## Examples

## Exercises

## Questions
I somehow get how the Cycling through days and Extracting digits from right using modulus works, but I need to look at them again later with a fresh eye, somehow doesn't click, calling it a session for now.
## Summary
