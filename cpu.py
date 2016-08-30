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
#Counters
pc = 0
clk = 0
on = 1
#####

lines = [line.rstrip('\n') for line in open('outfile2')] #creates array with char values from text file
#print (lines)
#First Line is 0 not 1

while on == 1:
#    clk+=1   
#    pc  +=1        
    while tgl == 1:
        sleep(0.2)
        a = lines[acc] #Array + value in [slot]
#        print (lines) #print the array value
        acc = acc + 1
        if a == '0':
            tgl = 0 #mod
        try:
            e1, e2 = a.split(".")
#            print (e1+" <- e1")
#            print (e2+" <- e2")
        except:
            print ("Unknown Opcode Below") 
            on = 0 #on/off for CPU 
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
#        if e1 == "3111": #ADD AX,IMM
#            ax = int(bx)+int(e2)
#            pc = pc + 1
#            clk = clk + 1
#        if e1 == "3112": #ADD BX,IMM
#            bx = int(bx)+int(e2)
#            pc = pc + 1
#            clk = clk + 1
##### JMP
        if e1 == "1000": #JMP,PC
            x = int(e2)
            acc = acc+x #Jumps to the spot in the array!
            pc = acc
            clk = clk + 1
            e1 = e2 = 0  #Clear these if you do!
##### Status      
        print("=====================")
        print("AX= "+ str(ax), "BX= "+ str(bx))
        print("CLK= "+str(clk), " PC= "+ str(pc))
        print("OpCode= "+str(e1) )
        print("Param = "+str(e2) )
        print("Array = " + str(acc) )
        e1 = e2 = 0 # Reset this to fix Execution Bug (extra clock at end of program)
    
###
    
