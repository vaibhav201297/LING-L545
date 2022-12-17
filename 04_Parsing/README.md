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