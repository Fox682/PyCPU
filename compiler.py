from __future__ import print_function
from array import *
#import tempfile

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
cx = '13'
dx = '14'
#Ops (20)
ld = '21' #Loads val to Reg
st = 22 #Store Reg to Location in array
mov = 23 #Moves Reg to Reg
#Math (30) - Between Regs Only (for now)
add = '31'
inc = '32'
sub = '33'
mul = '34'
div = '35'
dec = '36'
#Other
nop = '99'
jmp = '1000'

output = open('outfile2','w')
outarray = [0 for x in range(0)] #Create array with NOTHING in it

lines = [line.rstrip('\n') for line in open('infile2')] #creates array with char values from text file
#print (lines)

while tgl == 1:
    a = lines[acc] #Array + value in [slot]
 #   print (a) #print the array value
    acc+=1 #increment the counter
    if a == '0': #not actual value but ASCII value...
        tgl = 0 #Stops the While loop when a == 0!
#Split lines to process Commands
    try: 
        s1, s2 = a.split(' ')
#        print (s1+" <- s1")
#        print (s2+" <- s2")
    except:
        print ("Error processing Command")
    try:
        e1, e2 = s2.split(',')
#        print (e1+" <- e1")
#        print (e2+" <- e2")
    except:
        print ("Error processing Parameters.")
#### Instruction Processing ####
#### Load AX & BX
    if s1 == 'ld' and e1 =='ax':
        outarray.append(ld+ax+'.'+e2)
    if s1 == 'ld' and e1 =='bx':
        outarray.append(ld+bx+'.'+e2)
#### Store AX & BX
#    if a == 'st':
#        outarray.append(st)
#    if a == 'mov':
 #       outarray.append(mov)
#### Maths
#### ADD AX <-> BX
#    if s1 == 'add' and e1 == 'ax' and e2 != 'bx':
#        outarray.append(add+ax+'.'+e2)
#    if s1 == 'add' and e1 == 'bx' and e2 != 'ax':
#        outarray.append(add+bx+'.'+e2)
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
#### JMP & NOP
    if s1 == 'jmp':
        outarray.append('1000'+'.'+ e1)
    if s1 =='nop':
        outarray.append('99.0')
#### 
#### CMP EAX and EBX for ==, >, <
#### 


#### Other
outarray.pop() #Fixes duplicate entry and end of array (bug)
outarray.append('0') #Tells the CPU & Compiler to stop

#print(outarray)
###
# Write the array of numbers to the file
strarray = list(map(str, outarray)) #Makes a list
#print (strarray)

#Writes the "list" to the file!
for item in strarray: 
  output.write("%s\n" % item)


