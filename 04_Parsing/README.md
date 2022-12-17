### Dependency Parsing

```
git clone https://github.com/ufal/udpipe
```

Download a treebank of your choosing : **UD_French-GSD** 

```
curl --remote-name-all https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-4923{/ud-treebanks-v2.11.tgz,/ud-documentation-v2.11.tgz,/ud-tools-v2.11.tgz}
```

Extracting the tgz file to get the training and testing data.


Train a model on the -train portion of the treebank, and test it on the -test portion.

```
udpipe  --tokenizer none --tagger none --train fr.udpipe < udpipe ud-treebanks-v2.11/UD_French-GSD/fr_gsd-ud-train.conllu
```

Parsing Test Data

```
udpipe --parse fr.udpipe < udpipe ud-treebanks-v2.11/UD_French-GSD/fr_gsd-ud-test.conllu > TESTINGOUT.conllu
```
<pre>
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |    100.00 |    100.00 |    100.00 |    100.00
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |    100.00 |    100.00 |    100.00 |    100.00
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |     95.15 |     95.15 |     95.15 |     95.15
LAS        |     93.34 |     93.34 |     93.34 |     93.34
</pre>

#### Report

The UD Dataset used in this UD Atis Corpora. It is a manually annotated treebank consisting of the sentences in the Atis (Airline Travel Informations) dataset which includes the human speech transcriptions of people asking for flight information on the automated inquiry systems.
We train the UDpipe with the dataset of Airline Travel and then generate the model which has a Labeled Attachment Accuracy of 95.15% and Unlabeled Attachment Score of 95.15%. 
The model correctly predicts parts of speech for most sentences. Even the temporal and nominal modifiers are predicted correclty.

One sentence where the model failed to identify the part of speech is  
**what 's the price of the least expensive first class round trip ticket on us air from cleveland to miami ?**

The model identified price as the nominal subject instead of identifying it as object of the sentence.


