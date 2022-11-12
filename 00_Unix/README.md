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


