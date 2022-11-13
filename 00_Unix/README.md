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

I chose a language between in the 1000+ articles range : "Gaelg"  which is the Manx language also known as Manx Gaelic. 
Language Code is "gv".

I downloaded the Gaelic Articles from the wikimedia dumps page 

```
wget https://dumps.wikimedia.org/gvwiki/20221101/gvwiki-20221101-pages-articles-multistream.xml.bz2
```

```
python WikiExtractor.py --infn gvwiki-20221101-pages-articles-multistream.xml.bz2
```

Finally a wiki.txt file is generated which contains the corupus in a text file.

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
  sed 's/[^a-zA-Z]\+/\n/g' < wiki.txt | sort -r | uniq -c > wiki.hist
```
```
sed 8q < wiki.txt
```
```
sed 's/[^a-zA-Z]\+/\n/g' < wiki.txt | sed 8q
```
```
sed 's/[^a-zA-Z]\+/\n/g' < wiki.txt| sort -r | sed 10q
```
```
sed 's/[^a-zA-Z]\+/\n/g' < wiki.txt| sort -r| uniq -c  | sed 10q
 ```
  </ul>
     ![image](https://user-images.githubusercontent.com/40687848/201550864-e500a6df-bf2d-4be9-9487-25a8c59e95d9.png)
  </li>
  <li>  

    <li>More Counting Exercises 

 </ol>
