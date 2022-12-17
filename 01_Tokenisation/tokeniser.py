import sys
import re
sent_id=1
word_count=1
file = sys.stdin.read()
#Store original file 
temp_file = file
file=file.replace(","," , ")
file=file.replace(":"," : ")
file=file.replace("("," ( ")
file=file.replace(")"," ) ")
lines= file.split("\n")
#print(lines)
for line in lines:
    if line == '':
        break
    sys.stdout.write("\n# sent_id = {}{}".format(sent_id,"\n"))
    sys.stdout.write("# text =  {}{}".format(lines[sent_id-1],"\n"))
    for word in line.split(" "):
        #If word is empty, then ignore it
        if word == "":
            pass
        else:
            sys.stdout.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(word_count,word,"-","-","-","-","-","-","-","-"))
            word_count+=1
    #Add a newline after each sentence is done
    sys.stdout.write("\n")
    #After a sentence has been read, setting  count back to 1
    word_count=1
    sent_id+=1
