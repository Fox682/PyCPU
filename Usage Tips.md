## Usage Tips
---------

The CPU runs a variant of Assembly modeled after the NASM style, if you've ever used NASM this should be a cake walk.
The format for the instructions can be a little strange if you've never worked with Assembly before.

```
instruction destination,source
```

Most Assembly follows this format in more or less the same way, the main differences would be the destination/source arrangement
and the instructions available.

An example of a valid instruction would be

```
ldi ax,10
```
The instruction ```ldi``` (LoaD Immediate value) into the destination ```ax``` (a register) with the value of ```10```. In other words it will load 
into ```ax``` register the value of ```10```, so if you ran that single line on the CPU (add a zero on the newline!) you will end 
up with this output:

```
=========================
AX = 10 BX = 0
SP = 24 BP = 24
CLK = 1  PC = 1
OpCode = 2111 Param = 10
Array = 1 CMP F = 0
=========================
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
...
```

You can see in the output the registers (AX and BX) and their current values (AX = 10). The default mode to run the cpu is a basic
debugging mode where you can see the status of Registers. Lets go over the interface while were here.

A "Fill the memory" program running

```
=========================
AX = 4 BX = 24
SP = 23 BP = 24
CLK = 32  PC = 8
OpCode = 1001 Param = 2
Array = 8 CMP F = 13
=========================
[99, 99, 99, 99, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 99]
```

The first line ```AX = 4 BX = 24``` Shows us the status of both registers available for basic operations. 

The next line shows the status of the Stack Pointer and the Base Pointer, These handle the stack. You can manipulate the stack 
using ```push``` and ```pop```.

The Next line is ```CLK = 32  PC = 8```, this shows the CLocK and Program Counter. The Clock is a running cycle counter, as long 
as this number is incrementing, everything should be running fine and should be going up, never skipping or going in reverse. If
it's not going forward, something is wrong... really... really wrong. 

Next up is the Program Counter, this points to the instruction that it's following if you're using a numbered editor, this number
should correspond to the line number. The PC will go wherever you've told it, especially if you've got jumps in the code.

The next line ```Array = 8 CMP F = 13```, Array was for debugging, I've not removed it yet. the ```CMP F = 13``` however is 
actually useful, it tells us what flag CMP was used for (ie. Greater than, Less than, Equal, etc.).

And finally, the very bottom, with the numbers "99" in this example. This is actually the "RAM" in the CPU, the value here is pretty
small and is updated to show you the raw contents of the memory. As of current, the Registers and other values are not stored in the
same memory (future note here). 

- Later we will Add labels when they're available.

[To be Continued]



