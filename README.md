# WhyPlusPlus

It's a dumb language I made, designed to have no structure whatsoever. It's somehow turing complete too.
The code is interpreted one symbol at a time, over a memory tape.

First Half  Second Half
vvvvvvvvvvvvvvvvvvvvvvv
\[C]\[O]\[D]\[E]\[D]\[A]\[T]\[A]

Other Values
\[Accumulator] \[Read/Write Mode]

Here's how to use it:

Numbers are written in base 32, like this:

ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678

Is the same as:

1 2 3 4 5 6...

The symbols:

+: Changes to add mode
-: Changes to subtract mode
=: Changes to set mode

^: Write
v: Read

\*: Set the code pointer to the accumulator
@: Set the data pointer to the accumulator

%: Prints the accumulator's ascii value
&: Prints the accumulator as an integer

?: Skips the next command unless the accumulator is 0

#: Adds one memory cell

!: Ends the program

#Please don't try and use this
