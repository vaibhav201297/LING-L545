## Segmentation

For this lab, i have used an english paragraph generator to test for edge cases in Sentence Segmentation
## Pragmatic Segmenter

```
git clone https://github.com/diasks2/pragmatic_segmenter && cd pragmatic_segmenter/lib
```

The code given was added to segmenter.rb along with a counter to count the number of sentences.

To run the segmenter on a test text file

```
echo "This is a test.This is a test. This is a test." | ruby -I . segmenter.rb 
```

### Output
This is a test.
This is a test.
This is a test.


To run the segmenter on Custom Data corpus
```
cat wiki_subset.txt |  ruby -I . segmenter.rb
```
#### Output on Custom Data:
I just got back from the store and picked up some milk, eggs, and bread.
I also grabbed a few apples and some yogurt for breakfast tomorrow.
My coworker said she was running late because she had to drop her kids off at school before coming into the office.
I'm planning on going to the gym after work, but I'm not sure if I'll have enough energy.
I had a long day at the office and am feeling pretty tired.
The doctor told me to take two pills a day and to make sure I drink plenty of water.
I also need to avoid certain foods that could interfere with the medication.
My friend invited me to go to the movies with her tonight, but I'm not sure if I'll be able to make it.
I have a lot of work to do and need to finish up some projects before the end of the day.
Mr. John's package should arrive tomorrow.
The tracking info says it's been delivered to the post office and is out for delivery and it should be delivered by 5PM.
My boss asked me to send him a copy of the report by the end of the day.
I'll need to print it out and then scan it so I can email it to him.
I'm not sure what to wear to the party on Saturday.
It's supposed to be pretty casual, but I don't want to look too sloppy.
I think I left my keys in the car.
I'm not sure if I locked the doors or not.
I'll have to check when I get home.
The weather forecast says it's going to rain tomorrow, so I'll need to bring an umbrella with me to work.
I have a meeting with my boss at 10:00 a.m. on Friday.
The flight from LAX to JFK is scheduled for 3:00 p.m. on Tuesday.
Number of sentences in the corpus
21



## NLTK’s Punkt

```
sudo apt-get install python3-nltk
```

```
python custom_segmenter.py 
```
#### Output

['I just got back from the store and picked up some milk, eggs, and bread.', 'I also grabbed a few apples and some yogurt for breakfast tomorrow.', 'My coworker said she was running late because she had to drop her kids off at school before coming into the office.', "I'm planning on going to the gym after work, but I'm not sure if I'll have enough energy.", 'I had a long day at the office and am feeling pretty tired.', 'The doctor told me to take two pills a day and to make sure I drink plenty of water.', 'I also need to avoid certain foods that could interfere with the medication.', "My friend invited me to go to the movies with her tonight, but I'm not sure if I'll be able to make it.", 'I have a lot of work to do and need to finish up some projects before the end of the day.', "Mr.John's package should arrive tomorrow.", "The tracking info says it's been delivered to the post office and is out for delivery and it should be delivered by 5PM.", 'My boss asked me to send him a copy of the report by the end of the day.', "I'll need to print it out and then scan it so I can email it to him.", "I'm not sure what to wear to the party on Saturday.", "It's supposed to be pretty casual, but I don't want to look too sloppy.", 'I think I left my keys in the car.', "I'm not sure if I locked the doors or not.", "I'll have to check when I get home.", "The weather forecast says it's going to rain tomorrow, so I'll need to bring an umbrella with me to work.", 'I have a meeting with my boss at 10:00 a.m. on Friday.', 'The flight from LAX to JFK is scheduled for 3:00 p.m. on Tuesday.']
21


## Report

<li> Pragmatic Segmenter: <br/>
Pragmatic Segmenter is a rule-based sentence boundary detection written in Ruby on Rails . The main goal of Pragmatic Segmenter is to provide a segmenter that works with many languages and does a reasonable job when the format and domain of the input text is known. It does not use machine learning algorithms to segment the corpus. Instead, it has a set  of Golden Rules which include edge case scenarios for sentence disambiguation. Since, there is no machine learning algorithm , it has no training involved and relies solely on regex.
<br/>
Quantitative Evaluation : 100% accuracy was achieved <br/>
Qualitative Evaluation: Since the pragmatic segmenter is based on rules for each edge case, if a new edge case which hasn't been modeled is encountered, then the sentence segmentation task fails.
</li>
<li> Python NLTK
NLTK is the Natural Language Toolkit which uses lexical resources such as WordNet and over 50 corpora along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum.
NLTK's corpora is described in the link : https://www.nltk.org/nltk_data/
<br/>
Quantitative Evaluation : 100 % accuracy is achieved <br/>
Qualitative Evaluation: The code makes use of Punkt's sentence tokenizer which makes use of the pre-trained punkt model for english data

</li>


## Tokenisation

```
git clone https://github.com/UniversalDependencies/UD_Japanese-GSD.git
```
Install the package to read the dictionary.
```
pip install conllu
```

Python Shell

Allows you to run Python expressions on terminal.

#### Difference between print() and sys.stdout.write()

print() automatically adds a newline character whereas a newline character has to be added in the case of sys.stdout.write(). The '\n' stands for the newline character

#### Variables
In python, we can assign a variable any value 

<ul>
    <li> Boolean : a = True </li>
    <li> Integer: a=5 </li>
    <li> List : a=["hello","hi","home"]</li>
    <li> String: a="Hello World" </li>
</ul>
The variable can be assigned a value at any point in the program.
It wil be assigned a new variable value.
Behind the scenes, it is done be pointing the variable from 1 address in memory to another

#### Simple Arithmetic
The operator '+' adds an integer with another. If the variable is a string, the '+' operator will append the text to the variable on the left side of the operator. For example,
a = "Hello"
b = "World"
print(a+b) would print out HelloWorld
Hence, operator functionality may depend on the variable type. We cannot add variables which are not of the same type. It throws an exception.

#### Loops
###### For loops
import sys
for c in sys.stdin.read():
	print(c)

This program will print any file inputted 1 character at a time

To make it output the text without newline, we can use sys.stdout.write()

###### While Loops
import sys
c = sys.stdin.read(1)
while c: 
	print(c)
	c = sys.stdin.read(1)

While Loop allows to read the data 1 character or 1 line at a time

#### Flow Control

###### if statement

Counter.py will count the number of 'o' in the inputted text .
Since, Hola Mundo has 2 O's, the output of the program will be 2

Output of running wc.py on corpus and wc command on Linux

```
cat ../00_Unix/wiki.txt | python wc.py
```
Characters,  69167406
Lines,  586949
Tokens,  9340641
Consonants,  49696321
Vowels,  1765824

```
wc ../00_Unix/wiki.txt
```
586949  9802871 174242572


Number of lines matches, so reading number of '\n' will give us the number of lines.


