from array import *
from time import sleep
#Vars
acc = 0
tgl = 1
sel = 0
x = 0
#Command Processing
e1 = 0
e2 = 0
s2 = 0
#Opcodes
ax = 0
bx = 0
#cx = 0
#dx = 0
cmp = 0
#Counters
pc = 0
clk = 0
on = 1
#########
#Memory Variable, EDIT MEMORY SIZE HERE
m = 25
#Stack init
bp = m-1
sp = m-1
###
flag = 0 #Use an int use str(flag) to convert it to a string
#Flag for CMP  values

#Local Memory for CPU, set for as much as needed
mem = [0 for x in range(m)]

lines = [line.rstrip('\n') for line in open('outfile')] #creates array with char values from text file

while on == 1:
    while tgl == 1:
        sleep(0.1) #Sleep 0.10 == 10 Cycles per Second, 0.001 = 1 ms (1khz), Sleep 0.0001 = 0.1ms (10khz)
        a = lines[acc] #Array + value in [slot]
        acc = acc + 1
        if a == '0':
            tgl = 0 #mod
        try:
            e1, e2 = a.split(".")
        except:   #This will Exit the Program if it gets something unknown
            print("====================")
            print("End of Program or")
            print ("Unknown Opcode Below")
            on = 0 #on/off for CPU
########
        if e1 == "99": #NOP
            pc = pc + 1
            clk = clk + 1
##### Load Immediate
        if e1 == "2111": #LDI AX,#
            ax = int(e2)
            pc = pc + 1
            clk =clk + 1
        if e1 == "2112": #LDI BX,#
            bx = int(e2)
            pc = pc + 1
            clk += 1
### Load and Store from Memory
### Load AX & BX
        if e1 == "2011": #LD AX,[#]
            e2 = int(e2)
            ax = mem[e2]
            pc = pc + 1
            clk =clk + 1
        if e1 == "2012": #LD BX,[#]
            e2 = int(e2)
            bx = mem[e2]
            pc = pc + 1
            clk += 1
### Store AX & BX
        if e1 == "2211": #ST AX,[#]
            e2 = int(e2)
            mem[e2] = ax
            pc = pc + 1
            clk =clk + 1
        if e1 == "2212": #ST BX,[#]
            e2 = int(e2)
            mem[e2] = bx
            pc = pc + 1
            clk += 1
### Load REG by REG
        if e1 == "251112": #LDR AX,BX
            #e2 = int(e2)
            ax = mem[bx]
            pc = pc + 1
            clk =clk + 1
        if e1 == "251211": #LDR BX,AX
            #e2 = int(e2)
            bx = mem[ax]
            pc = pc + 1
            clk += 1
### Store REG by REG
        if e1 == "261112": #STR AX,BX
            e2 = int(e2)
            mem[ax] = bx
            pc = pc + 1
            clk =clk + 1
        if e1 == "261211": #STR BX,AX
            e2 = int(e2)
            mem[bx] = ax
            pc = pc + 1
            clk += 1
### PUSH & POP
        if e1 == "4111": #PUSH AX
            mem[sp] = ax
            pc = pc + 1
            clk = clk + 1
            sp = sp - 1
        if e1 == "4112": #PUSH BX
            mem[sp] = bx
            pc = pc + 1
            clk = clk + 1
            sp = sp - 1
### POP
        if e1 == "4211": #POP AX
            sp = sp + 1
            ax = mem[sp]
            pc = pc + 1
            clk = clk + 1
        if e1 == "4212": #POP BX
            sp = sp + 1
            bx = mem[sp]
            pc = pc + 1
            clk = clk + 1

### Modify SP & BP with REG


#### Math Operations Go Here:
##### Increment
        if e1 == "3211": #INC AX
            ax = ax + 1
            pc = pc + 1
            clk = clk + 1
        if e1 == "3212": #INC BX
            bx = bx + 1
            pc = pc + 1
            clk = clk + 1
##### Decrement
        if e1 == "3611": #DEC AX
            ax = ax - 1
            pc = pc + 1
            clk = clk + 1
        if e1 == "3612": #DEC BX
            bx = bx - 1
            pc = pc + 1
            clk = clk + 1
##### ADD REG
        if e1 == "311112": #ADD AX,BX
            ax = int(ax)+int(bx)
            pc = pc + 1
            clk = clk + 1
        if e1 == "311211": #ADD BX,AX
            bx = int(bx)+int(ax)
            pc = pc + 1
            clk = clk + 1
##### SUB REG
        if e1 == "331112": #SUB AX,BX
            ax = int(ax)-int(bx)
            pc = pc + 1
            clk = clk + 1
        if e1 == "331211": #SUB BX,AX
            bx = int(bx)-int(ax)
            pc = pc + 1
            clk = clk + 1
##### MUL REG
        if e1 == "341112": #MUL AX,BX
            ax = int(ax)*int(bx)
            pc = pc + 1
            clk = clk + 1
        if e1 == "341211": #MUL BX,AX
            bx = int(bx)*int(ax)
            pc = pc + 1
            clk = clk + 1
##### DIV REG
        if e1 == "351112": #MUL AX,BX
            ax = int(ax)/int(bx)
            pc = pc + 1
            clk = clk + 1
        if e1 == "351211": #MUL BX,AX
            bx = int(bx)/int(ax)
            pc = pc + 1
            clk = clk + 1
##### ADD IMMEDIATE VALUE
        if e1 == "3011": #ADD AX,IMM
            ax = int(ax)+int(e2)
            pc = pc + 1
            clk = clk + 1
        if e1 == "3012": #ADD BX,IMM
            bx = int(bx)+int(e2)
            pc = pc + 1
            clk = clk + 1

#### Branching Instructions Go Here:
##### JMP Immediate
        if e1 == "1000": #JMP,PC
            x = int(e2)
            acc = acc+x #Jumps to the spot in the array!
            pc = acc
            clk = clk + 1
            e1 = e2 = 0  #Clear these if you do!
##JE - JMP ==
        if e1 == '1001' and flag == 1:
            x = int(e2)
            acc = acc+x
            pc = acc
            clk = clk + 1
            e1 = e2 = 0
            if e1 != '1001' and flag != 1:
                clk = clk +1
                acc = acc + 1
                pc = acc
                e1 = e2 = 0
##JG - JMP >
        if e1 == '1002' and flag == 12:
            x = int(e2)
            acc = acc+x
            pc = acc
            clk = clk + 1
            e1 = e2 = 0
            if e1 != '1002' and flag != 12:
                clk = clk +1
                acc = acc + 1
                pc = acc
                e1 = e2 = 0
###
        if e1 == '1002' and flag == 21:
            x = int(e2)
            acc = acc+x
            pc = acc
            clk = clk + 1
            e1 = e2 = 0
            if e1 != '1002' and flag != 21:
                clk = clk +1
                acc = acc + 1
                pc = acc
                e1 = e2 = 0
##JL - JMP <
        if e1 == '1003' and flag == 13:
            x = int(e2)
            acc = acc+x
            pc = acc
            clk = clk + 1
            e1 = e2 = 0
            if e1 != '1003' and flag != 13:
                clk = clk +1
                acc = acc + 1
                pc = acc
                e1 = e2 = 0
###
        if e1 == '1002' and flag == 23:
            x = int(e2)
            acc = acc+x
            pc = acc
            clk = clk + 1
            e1 = e2 = 0
            if e1 != '1002' and flag != 23:
                clk = clk + 1
                acc = acc + 1
                pc = acc
                e1 = e2 = 0
##### CMP ==
        if e1 == "241112" or e1 == "241211" and int(ax) == int(bx):
            flag = 1
            pc = pc + 1
            clk = clk + 1
##### CMP > & < (AX vs BX)
        if e1 == "241112" and int(ax) > int(bx):
            flag = 12
            pc = pc + 1
            clk = clk + 1
        if e1 == "241112" and int(ax) < int(bx):
            flag = 13
            pc = pc + 1
            clk = clk + 1
#####CMP > & < BX vs AX
        if e1 == "241211" and int(bx) > int(ax):
            flag = 21
            pc = pc + 1
            clk = clk + 1
        if e1 == "241211" and int(bx) < int(ax):
            flag = 23
            pc = pc + 1
            clk = clk + 1
############################################################

##### Status Print - Comment out for PERFORMANCE!
        print("=========================")
        print("AX = "+ str(ax), "BX = "+ str(bx))
        print("SP = "+ str(sp), "BP = "+ str(bp))
        print("CLK = "+str(clk), " PC = "+ str(pc))
        print("OpCode = "+str(e1) + " Param = " +str(e2))
        print("Array = " + str(acc) + " CMP F = " + str(flag))
        print("=========================")
        print(mem)
## Don't remove below this line
        e1 = e2 = s1 = s2 = 0 # Reset this to fix Execution Bug (extra clock at end of program)

###
