from __future__ import print_function
from array import *
#import tempfile

a = 0
ctr = 0 #counter
#Vars
acc = 0
tgl = 1
sel = 0
#splitting
s1 = 0
s2 = 0
e1 = 0
e2 = 0

#Regs (10)
ax = '11'
bx = '12'
#cx = '13'
#dx = '14'
bp = '15'
sp = '16'

#Ops (20)
ld = '20' #Load from Memory location
ldr = '25' #Load using REG reference
ldi = '21' #Loads Immediate Value to REG
st = '22' #Store Reg to Location in memory
str = '26' #Store REG using REG reference
mov = '23' #Moves Reg to Reg
cmp = '24' #Compares values to set flag

#Math (30) - Between Regs Only (for now)
adi = '30'
add = '31'
inc = '32'
sub = '33'
mul = '34'
div = '35'
dec = '36'

#Stack Ops (40)
push = '41'
pop = '42'

#Branching
jmp = '1000'
je = '1001'
jg = '1002'
jl = '1003'

#Other
nop = '99'

outarray = [0 for x in range(0)] #Create arrays with NOTHING in them
outarray2 = [0 for x in range(0)]

output = open('outfile','w')
#with open('outfile2', 'w') as filehandle:
#    filehandle.writelines("%s\n" % ctr for ctr in outarray)

with open('infile', 'r') as filehandle:
    input = [ctr.rstrip() for ctr in filehandle.readlines()]


def remafterellipsis(intext):
    where_ellipsis = intext.find(' #')
    if where_ellipsis == -1:
        return intext
    return intext[:where_ellipsis + 0]

#Main Functions here

for line in input:
    a = remafterellipsis(line)
    if a.rstrip():
        outarray2.append(a)

#========== Diagnostic Printing
#print ("====================")
#print(">> input <<")
#print(input)
#print ("====================")
#print(">> input2 <<")
#print(input2)
#print ("====================")
#print(">> outarray2 <<")
#print(outarray2)
#print ("====================")
#====== MAIN Part of Program
#print (a)


#a = outarray2

while tgl == 1:
    a = outarray2[acc]
    acc+=1 #increment the counter
    if a == '0': #not actual value but ASCII value...
        tgl = 0 #Stops the While loop when a == 0!
#Split lines to process Commands
    try:
        s1, s2 = a.split(' ')
        print (s1+" <- s1")
        print (s2+" <- s2")
    except:
        print ("Exception Processed B.")
###
    try:
        e1, e2 = s2.split(',')
        print (e1+" <- e1")
        print (e2+" <- e2")
    except:
        print ("Exception Processed B.")
#### Instruction Processing ####
#### Load Immediate AX & BX
    if s1 == 'ldi' and e1 == 'ax':
        outarray.append(ldi+ax+'.'+e2)
    if s1 == 'ldi' and e1 == 'bx':
        outarray.append(ldi+bx+'.'+e2)

### Load & Store from Memory
### Load AX & BX
    if s1 == 'ld' and e1 == 'ax':
        outarray.append(ld+ax+'.'+e2)
    if s1 == 'ld' and e1 == 'bx':
        outarray.append(ld+bx+'.'+e2)
### Store AX & BX
    if s1 == 'st' and e1 == 'ax':
        outarray.append(st+ax+'.'+e2)
    if s1 == 'st' and e1 == 'bx':
        outarray.append(st+bx+'.'+e2)

### Load REG Referenced by REG
### Normally reference are handled like ld bx,[ax]. Feature request
    if s1 == 'ldr' and e1 == 'ax' and e2 == 'bx':
        outarray.append(ldr+ax+bx+'.0')
    if s1 == 'ldr' and e1 == 'bx' and e2 == 'ax':
        outarray.append(ldr+bx+ax+'.0')

### Store REG by REG
    if s1 == 'str' and e1 == 'ax' and e2 == 'bx':
        outarray.append(str+ax+bx+'.0')
    if s1 == 'str' and e1 == 'bx' and e2 == 'ax':
        outarray.append(str+bx+ax+'.0')

### Stack Operations
### PUSH
    if s1 == 'push' and s2 == 'ax':
        outarray.append(push+ax+'.0')
    if s1 == 'push' and s2 == 'bx':
        outarray.append(push+bx+'.0')
#### POP
    if s1 == 'pop' and s2 == 'ax':
        outarray.append(pop+ax+'.0')
    if s1 == 'pop' and s2 == 'bx':
        outarray.append(pop+bx+'.0')

### Read BP and SP Registers



#### Maths
#### ADD AX  <-> BX
    if s1 == 'add' and e1 == 'ax' and e2 == 'bx':
        outarray.append(add+ax+bx+'.0')
    if s1 == 'add' and e1 == 'bx' and e2 =='ax':
        outarray.append(add+bx+ax+'.0')
##### SUB AX <-> BX
    if s1 == 'sub' and e1 == 'ax' and e2 == 'bx':
        outarray.append(sub+ax+bx+'.0')
    if s1 == 'sub' and e1 == 'bx' and e2 =='ax':
        outarray.append(sub+bx+ax+'.0')
#### MUL AX <-> BX
    if s1 == 'mul' and e1 == 'ax' and e2 == 'bx':
        outarray.append(mul+ax+bx+'.0')
    if s1 == 'mul' and e1 == 'bx' and e2 =='ax':
        outarray.append(mul+bx+ax+'.0')
#### DIV AX <-> BX
    if s1 == 'div' and e1 == 'ax' and e2 == 'bx':
        outarray.append(div+ax+bx+'.0')
    if s1 == 'div' and e1 == 'bx' and e2 =='ax':
        outarray.append(div+bx+ax+'.0')

#### ADD Immediate
    if s1 == 'adi' and e1 == 'ax' and e2 != 'bx':
#    if s1 == 'adi' and e1 == 'ax' and int(e2) > 0:
        outarray.append(adi+ax+'.'+e2)
    if s1 == 'adi' and e1 == 'bx' and e2 !='ax':
#    if s1 == 'adi' and e1 == 'bx' and int(e2) > 0:
        outarray.append(adi+bx+'.'+e2)

#### Other Operations

#### INC
    if s1 == 'inc' and s2 == 'ax':
        outarray.append(inc+ax+'.0')
    if s1 == 'inc' and s2 == 'bx':
        outarray.append(inc+bx+'.0')
#### DEC
    if s1 == 'dec' and s2 == 'ax':
        outarray.append(dec+ax+'.0')
    if s1 == 'dec' and s2 == 'bx':
        outarray.append(dec+bx+'.0')

#### Branching Instructions
#### JMP
    if s1 == 'jmp':
        outarray.append(jmp+'.'+s2) #Instead of str(s2)
#### Conditional JMPs
# JE - Jump if Equal
    if s1 == 'je':
        outarray.append(je+'.'+s2)
#JG - Jump if Greater
    if s1 == 'jg':
        outarray.append(jg+'.'+s2)
#JL - Jump if Less than
    if s1 == 'jl':
        outarray.append(jl+'.'+s2)
##
### NOP
    if s1 == 'nop':
        outarray.append(nop +'.0')
### CMP
    if s1 == 'cmp' and e1 == 'ax' and e2 == 'bx':
        outarray.append(cmp+ax+bx+'.0')
    if s1 == 'cmp' and e1 == 'bx' and e2 == 'ax':
        outarray.append(cmp+bx+ax+'.0')
####
####


#### Other
outarray.pop() #Fixes duplicate entry at end of array (bug)
outarray.append('0') #Tells the CPU & Compiler to stop
print ("====================")
print(">> outrray <<")
print(outarray)
### 2nd Pass for JMPs to have Labels
### Ensure Above works before doing this...
#while tgl == 1:
#    a = lines[acc] #Array + value in [slot]
# #   print (a) #print the array value
#    acc+=1 #increment the counter
#    if a == '0': #not actual value but ASCII value...
#        tgl = 0 #Stops the While loop when a == 0!
#
# Need to count the distance between the Labels
#
#
# Iterate over the Array
#Scan for Labels [Pick a format for them]
# Use the Split above to split the jmp and the Value
# if  a = "jmp"
# then Use s2 to track the labels


#Writes the "list" to the file!
for item in outarray:
  output.write("%s\n" % item)
