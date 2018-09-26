# Usage Tips
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
The instruction ```ldi``` (LoaD Immediate value) into the destination ```ax``` (a register) with the value of ```10```. In other words it will load into ```ax``` register the value of ```10```, so if you ran that single line on the CPU (add a zero on the newline!) you will end up with this output:

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

And finally, the very bottom, with the numbers "99" in this example. This is actually the "RAM" in the CPU, the value here is pretty small and is updated to show you the raw contents of the memory. As of current, the Registers and other values are not stored in the same memory (future note here). 

- Later we will Add labels when they're available.

If you get lost, crack open the compiler.py in your favorite editor (notepad++ is good) or atom (for linux) in my case, and see what instructions are there. Feel free to change stuff, if you got something even slightly interesting for the cpu or a program, feel free to send me the code, I'll put it here with your name (or alias) on it.

- The Troubleshooting section is below if you need it.

## Instruction Rundown
- Quick and dirty rundown of instructions (from the source)

```
#Regs (10)
ax = AX Register
bx = BX Register
bp = Base Pointer (unmodifyable at the moment)
sp = Stack Pointer (pop and push)

#Ops (20)
ld = Load from Memory location
ldr = Load using REG reference
ldi = Loads Immediate Value to REG
st = Store Reg to Location in memory
str = Store REG using REG reference
mov = Moves Reg to Reg (unimplemented at the moment)
cmp = Compares values to set flag

#Math (30)
adi = Add Immediate value, sum another value to a register
add = Add registers together, result in Destination Register
sub = Subtract registers together, result in Destination Register
mul = Multiply registers together, result in Destination Register
div = Divide registers together, result in Destination Register
inc = Increment value in Register
dec = Decrement value in Register


#Stack Ops (40)
push = PUSHes a Value in the Register to the stack (end of memory)
pop = POPs a Value from the stack to a register

#Branching
jmp = Jump, manipulates the Program Counter, jump to another instruction
je = Jump if Equal
jg = Jump if Greater than
jl = Jump if Less than

#Other
nop = A No OPeration instruction, useful if you need to burn time and/or for debugging
```


## Compiler Troubleshooting:

> "My responses are limited, you must ask the right questions." - Dr. Alfred Lanning - I, Robot

I've done what I can to make the compiler.py and the cpu.py have some minor robustness to them, however if you're going to spend some time with this, you're likely to hit on some odd points of irritation or just plain frustration. So in an effort to help alieviate some of the pain, here are some common Issues you may run into.

- Invalid instructions that follow the format will be ignored, the following will be successfully ignored by the compiler, and the resulting instruction list may be empty.

```
lol wat,wut
0
```

Yeah... I don't think so, makes an empty instruction list, hence the python error (we can't pop from an empty list, d'oh!):

```
lol <- s1
wat,wut <- s2
wat <- e1
wut <- e2
Exception Processed B.
wat <- e1
wut <- e2
Traceback (most recent call last):
  File "compiler.py", line 235, in <module>
    outarray.pop() #Fixes duplicate entry at end of array (bug)
IndexError: pop from empty list
```
If you've got more than one line some valid and some with invalid instructions, the result won't crash the compiler, but it won't process things right and you might end up with only one instruction processed after the broken ones. Double and triple check to make sure you've got the right instructions.

If you missed the math on the Stack OR writing to the wrong memory (ie, with the memory filling program in the ```infile```), we're gonna have a fun time with another error.

```
=========================
AX = 25 BX = 99
SP = 24 BP = 24
CLK = 77  PC = 2
OpCode = 0 Param = 0
Array = 2 CMP F = 0
=========================
[99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99]
Traceback (most recent call last):
  File "cpu.py", line 101, in <module>
    mem[ax] = bx
IndexError: list assignment index out of range
```

The "RAM" is just another list, so if you go outside the bounds, it's not gonna like it. 

> "Program Terminated"

## Tips and Tricks

Here's some trick and things you can do with the CPU instructions. Since this CPU isn't as full featured as say x86 Assembly, we'll need to use some extra steps to do equivilent things.

**XCHG (x86)**

The PyCPU doesn't have a way to exchange the registers using a single instruction however you can do it with the Stack! Say you loaded some values and you're doing some math, but you want the result in ```bx``` instead of ```ax``` (or any other register). You can exchange the values in both registers, using this:

```
ldi ax,10
ldi bx,20 #Load up the values
mul ax,bx #Multiply, result in ax
push ax #Exchange values!
push bx
pop ax
pop bx #Done!
0
```

Now the results should be in bx instead! Observant assemblers will note that this is exactly the opposite way you normally use the stack, by default you always pop the values in the exact opposite way you pushed them in the first place. But if you're purposefully exchanging the values, this is exactly ok.

**Add Multiple values**

The limitations of the PyCPU are in place for two reasons, Python code run minimization and the sheer challange, after all that is why we do assembly, we love the challenge (and occasionally we work with very limited Microcontrollers)!

Lets add 5 values together, since we only have 2 registers... we'll need, yup, the Stack. The Stack is extremely useful for this exact reason, we don't have a lot of registers available. Since addition is accumulative, this is fairly easy.

```
ldi ax,5 #Load up the Stack with the values we want to add together
ldi bx,10
push ax
push bx
ldi ax,20
ldi bx,30
push ax
push bx
ldi ax, 50
push ax #Done!
#
pop ax #Start with setting initial values
pop bx #Use bx for popping and adding
add ax,bx
pop bx
add ax,bx
pop bx 
add ax,bx
pop bx
add ax,bx #Done!
0
```

The same can be done from stored values instead. Both use the same amount of memory, the stack uses the end of the memory, the load instruction can be used from any location in memory (stack is just more consistent).

```
#After values are stored to memory locations (eg. 0-4)
ld ax,0
ld bx,1
add ax,bx
ld bx,2
add ax,bx
ld bx,3
add ax,bx
ld bx,4
add ax,bx
0
```
**More to come!**

[To be Continued]



