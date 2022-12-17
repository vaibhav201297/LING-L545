import sys
counter = 0 
counter_o = 0 
for c in sys.stdin.read():
    if c == '0':
        counter_o +=1
    if c in 'aeiou':
        counter = counter + 1
print(counter_o)
print(counter)
