#import "template.typ": *

#show: project.with(
  title: "CSAPP Notes",
  authors: (
    "Leonardo", 
  )
)
#show image: set align(center)

= Number representations
Byte = 8 bits

- Decimal
- Binary
- Octal
- Hexadecimal
In C, numeric constants starting with "0x" or "0X" are interpreted as being in hexadecimal. The letters A to F is not Case-sensitive.


#image("2024-04-06-20-48-26.png")
= Unsigned and signed

== signed
The most common computer representation of signed numbers is known as two's-complement form. This is defined by interpreting the most significant bit of the word to have negative weight.

$-x = ~x+1$

When the sign bit is set to 1, the represented value is negative, and when set to 0 the value is nonnegative.

Consider the range of values that can be represented as a w-bit two'scomplement number.
The least representable value is given by bit vector 10 ... 0 (set the bit with negative weight, but clear all others), having integer value TMin(w bits) $= - 2^(w-1)$.
The greatest value is given by bit vector 01 ... 1 (clear the bit with negative weight, but set all others as "1"), having integer value TMax(w bits) $= 2^(w-1) - 1$.

So you can see:

- The two's-complement range is asymmetric: |TMin| = |TMax| + 1, that is, there is no positive counterpart to TMin.
- The maximum unsigned value is just over twice the maximum two's-complement value: UMax = 2TMax + 1.
- -1 has the same bit representation as UMax---a string of all ones.

#image("2024-04-06-20-56-38.png", width: 20em)
#image("2024-04-06-20-56-47.png", width: 20em)
When do calculation or comparison between  unsigned and signed values, signed values implicitly cast to unsigned.

To convert an unsigned number to a larger data type, we can simply add leading zeros to the representation; this operation is known as *zero extension*.
For converting a two's- complement number to a larger data type, the rule is to perform a *sign extension*, adding copies of the most significant bit to the representation.


= Floating-point
#image("2024-04-06-21-07-44.png")
#image("2024-04-06-21-08-37.png")
#image("2024-04-06-21-09-01.png")

Shift operations
- Left shift
- Logical right shift: zero-extend
- Arithmetic right shift: sign-extend

Different effects for signed (2's complement) and unsigned numbers
when simply throwing away the MSB in the overflow results

== Array
- Multi-Dimensional Arrays
  - Row-major ordering in C
    - Each row is allocated contiguously, and all rows are allocated contiguously
- Multi-Level Arrays
  - The second-level arrays are not necessarily contiguous in memory
 
Satisfy alignment in structures with padding
- Within structure: each field satisfies its own alignment requirement
- Overall structure: align to the largest alignment requirement of all fields

== Big and little endian

Array not affected by byte ordering.
Big Endian: Least significant byte has highest address.
Little Endian: Least significant byte has lowest address.
#image("2024-04-06-20-51-12.png")

== Thread
A thread is a single unique execution context including registers, PC, stack pointer, memory, ...

Threads are independently scheduled by the OS.

Web server with Thread Pools
