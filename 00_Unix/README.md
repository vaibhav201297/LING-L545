<h2> Lab 0 </h2>
<h3> Vaibhav Vishwanath </h3>

```
sudo apt-get update
sudo apt-get install git
sudo apt-get install icu-devtools
```

This repository was forked from ftyers/LING-L545

Since an SSH Key already exists ,

```
cat ~/.ssh/id_rsa.pub
```

I copied the SSH Key and pasted it my GitHub Profile ---> Settings ---> SSH and GPG Keys

```
git clone git@github.com:vaibhav201297/LING-L545.git
```

```
git status
git add . 
git commit -m "Initial Commit"
git push
```


<h4> Obtaining the Corpus </h4>

I chose a language between in the 1000+ articles range : "marathi"  which is the language used in my hometown
Language Code is "mr".

I downloaded the Marathi Articles from the wikimedia dumps page 

```
wget https://dumps.wikimedia.org/mrwiki/20221201/mrwiki-20221201-pages-articles-multistream.xml.bz2
```

```
python3 WikiExtractor.py --infn mrwiki-20221201-pages-articles-multistream.xml.bz2
```

Finally a wiki.txt file is generated which contains the corupus in a text file.
Since the corpus of Marathi Articles is too large, I reduced the file size by taking 50Mb data from the text file to create wiki_subset.txt

```
tail -c 50m wiki.txt > wiki_subset.txt
```

<hr>
<h3> Lab 0 - Class 1</h3>

<ol>
  <li> Count words in a text 
  The problem is to input a text file, and output a list of words in the file along with their frequency counts. The algorithm consists of three steps:
  <ul>
    <li>Tokenise the text into a sequence of words (sed),</li>
    <li>Sort the words (sort -r), </li>
    <li>Count duplicates (uniq -c).</li>
    We utilise the power of simple shell commands which help tokenize the corpus. 'SED' is used to replace all non-alphabetic characters with '\n'. It is easier to specify the alpabetic characters, hence we use the complement method '^' in our regular expression. Then, we sort the sequences in reverse order and finally display the sequences. The output of the final command is shown below
   
```
sed 's/[^अआइईउऊएऐओऔअंअःॲऑऋकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहळक्षज्ञ]\+/\n/g' < wiki_subset.txt | sort -r | uniq -c > wiki_subset.hist

```
```
sed 8q < wiki.txt
```
```
sed 's/[^अआइईउऊएऐओऔअंअःॲऑऋकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहळक्षज्ञ]\+/\n/g' < wiki.txt  | sed 8q
```
```
sed 's/[^अआइईउऊएऐओऔअंअःॲऑऋकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहळक्षज्ञ]\+/\n/g' < wiki.txt | sort -r | sed 10q
```
```
sed 's/[^अआइईउऊएऐओऔअंअःॲऑऋकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहळक्षज्ञ]\+/\n/g' < wiki.txt | sort -r| uniq -c  | sed 10q
```

    
<li>  
More Counting Exercises <br/>
<ul>
		<li>Count number of words after cnverting to upper case. </li>
		
```		
uconv -x upper < wiki.txt | sed 's/[^अआइईउऊएऐओऔअंअःॲऑऋकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहळक्षज्ञ]\+/\n/g'| sort -r| uniq -c  | sed 10q
```
			 
<li>Count vowel sequences </li>

```
uconv -x upper < wiki.txt | sed 's/[^अआइईउऊएऐओऔअंअःॲऑऋ]\+/\n/g'| sort -r| uniq -c  | sed 10q
```

<li> Count Consonant Sequences </li>

```
uconv -x upper < wiki.txt | sed 's/[^कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहळक्षज्ञ]\+/\n/g'| sort -r| uniq -c  | sed 10q
```
</ul>
</li>
	<li> Sort </li>  
Sort the words in Wikipedia by frequency 
```
sed 's/[^अआइईउऊएऐओऔअंअःॲऑऋकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहळक्षज्ञ]\+/\n/g' < wiki.txt | sort | uniq -c | sort -nr
```
Sort them by folding case

```
sed 's/[^अआइईउऊएऐओऔअंअःॲऑऋकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहळक्षज्ञ]\+/\n/g' < wiki.txt | sort | uniq -c | sort -f
```

Sort them by rhyming order.

```
sed 's/[^अआइईउऊएऐओऔअंअःॲऑऋकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहळक्षज्ञ]\+/\n/g' < wiki.txt | rev |  sort | uniq -c | sort -f
```

</li>
	<li> Bigrams </li>

```
sed 's/[^अआइईउऊएऐओऔअंअःॲऑऋकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहळक्षज्ञ]\+/\n/g' < wiki_subset.txt > wiki_subset.words
tail -n +2 wiki_subset.words > wiki_subset.nextwords
paste wiki_subset.words wiki_subset.nextwords | sort | uniq -c > wiki_subset.bigrams
```
The 15 most frequent bigrams in the corpus

```
sort -nr < wiki_subset.bigrams | sed 15q
```




</ol>

### Exercises with SED

I have used a test_file.txt for these exercises as inputting Marathi Language vowels is very tough

```
sed 's/[AEIOUaeiou][A-Za-z]*//g' < test_file.txt  | sort -r | uniq -c > initial-consonants.hist
```
#### Output
<pre>sed 10q initial-consonants.hist 
      2 v
      1 t 
      1 sc
      2 s 
      2 s
      1 P
      1 p
      1 N
      2 n
      4 m
</pre>

```
sed 's/[A-Za-z]*[aeiouAEIOU]//g' < test_file.txt  | sort -r | uniq -c > final-consonants.hist
```
#### Output
<pre>sed 10q final-consonants.hist 
      3 t 
      6 t
      1 sl
      4 s
      3 r 
      1 nt 
      1 ng 
      1 nc
      2 n
</pre>

