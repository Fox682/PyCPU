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
cx = 0
dx = 0
cmp = 0
#Counters
pc = 0
clk = 0
on = 1
#####
###
flag = 0 #Use an int use str(flag) to convert it to a string
#Flag for CMP  values
# 1 "==", 2 "!=", 3 ">", 4 "<"


lines = [line.rstrip('\n') for line in open('outfile2')] #creates array with char values from text file
#print (lines)
#First Line is 0 not 1

while on == 1:
#    clk+=1   
#    pc  +=1        
    while tgl == 1:
        sleep(0.10) #Sleep 0.10 == 10 Cycles per Second, 0.001 = 1 ms (1khz), Sleep 0.0001 = 0.1ms (10khz)
        a = lines[acc] #Array + value in [slot]
#        print (lines) #print the array value
        acc = acc + 1
        if a == '0':
            tgl = 0 #mod
        try:
            e1, e2 = a.split(".")
#            print (e1+" <- e1")
#            print (e2+" <- e2")
        except:   #This will Exit the Program if it gets something unknown
            print("====================")
            print("End of Program or")
            print ("Unknown Opcode Below") 
            on = 0 #on/off for CPU

### Possible Optimization to use If Else rather than consecutive IF's

#####
        if e1 == "99": #NOP
            pc = pc + 1
            clk = clk + 1
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
##### Load Immediate
        if e1 == "2111": #LD AX,#
            ax = int(e2)
            pc = pc + 1
            clk =clk + 1
        if e1 == "2112": #LD BX,#
            bx = int(e2)
            pc = pc + 1
            clk += 1
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
##### ADD IMMEDIATE VALUE - AX <-> BX
##### Works, not sure if I want to implement this...
#        if e1 == "3111": #ADD AX,IMM
#            ax = int(bx)+int(e2)
#            pc = pc + 1
#            clk = clk + 1
#        if e1 == "3112": #ADD BX,IMM
#            bx = int(bx)+int(e2)
#            pc = pc + 1
#            clk = clk + 1
##### JMP Immediate
        if e1 == "1000": #JMP,PC
            x = int(e2)
            acc = acc+x #Jumps to the spot in the array!
            pc = acc
            clk = clk + 1
            e1 = e2 = 0  #Clear these if you do!
#JMP Branching
##JE - JMP if ==
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
##JG - JMP if >
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
                clk = clk +1
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
#####


##### Status Print - Comment out for PERFORMANCE!     
        print("=========================")
        print("AX = "+ str(ax), "BX = "+ str(bx))
        print("CLK = "+str(clk), " PC = "+ str(pc))
        print("OpCode = "+str(e1) + " Param = " +str(e2))
        print("Array = " + str(acc) + " CMP F = " + str(flag))  
## Don't remove below this line
        e1 = e2 = 0 # Reset this to fix Execution Bug (extra clock at end of program)
    
###
    
