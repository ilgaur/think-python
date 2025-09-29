# Chapter 5 Notes

## Key Concepts
Floor division vs regular division: floor division will output an integer and will always round down the result toward the negative infinite, regular division or decimal division will output the result in a decimal format

Modulus operator result: modulus operator will output the remainder of a division, for example if we do 10 % 3 it will give us 1, or if we do 100 % 60 it will give us 40.

number % 10 = last digit
Because division by 10 separates the tens from the ones, leaving only the ones as remainder. for example take this into account: 324 % 10 --> 4 (First digit from right), because: (321 / 10) = ((3 * 100) / 10) + ((2 * 10) / 10) + ((4 * 1) / 10) --> 300 + 20 + 4 --> 4 comes from 4 / 10 --> 0 which has the remainder of 4 because 4 / 10 is zero, 4 - 0 is 4 --> so with the modulus operator 4 % 10 we get the 4 which is right most digit, this stems from the natural properties of base 10 numbers.

3 Practical uses of the modulus operator:

When we have a limited cycle, if we are in that cycle and want to move but the steps we want to move plus the position we are in is more than the ovearll number of steps that cycle has it means that we are gonna go through the end of it however much we can and then go back to the beginning and go from there, meaning if the cycle has 5 positions, and we are at position 3 and want to move 2 times forward, (Positions: 0, 1, 2, 3, 4) we will go from 3 to 4 (1/2) and then from 4 we can't go to 5, so we go to 0 (2/2), and to calculate this modulus can help us achieve it, so (3+2) which is 5, then modulus on the positions number will give us the remainder after the division which is exactly how much after full cycle has been forward we should go forward, so 5 % 5 will be 0, so we are gonna be at position 0. this is completely apparent when we have a cycle of 7 days, and we are at day 5 (friday) and want to move 3 days forward, so (5 + 3) % 7 = 1, so we will be at day 1 (monday). also we saw this in the wrap-around example in the book.

## Examples

## Exercises

## Questions
I somehow get how the Cycling through days and Extracting digits from right using modulus works, but I need to look at them again later with a fresh eye, somehow doesn't click, calling it a session for now.

## Summary
