import sys
#Initializing variables 
lines=0
tokens=0
characters=0
consonants=0
vowels=0
for c in sys.stdin.read():
    #Count '\n'(newline) characters and increment line counter
    if c =='\n':
        lines+=1
#Count ' '(space) characters and increment token counter        
    elif c ==' ':
        tokens+=1
    elif c in 'aeiouy':
        consonants+=1
    elif c in 'ऄअआइईउऊऋऌऍऎएऐऑॲऒओऔ':
        vowels+=1
#Increment character count for all characters
    characters+=1

#Print out the results
print("Characters, ",characters)
print("Lines, ",lines)
print("Tokens, ", tokens)
print("Consonants, ",consonants)
print("Vowels, ", vowels)