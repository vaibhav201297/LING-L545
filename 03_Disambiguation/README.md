### Morphological disambiguation

```
git clone https://github.com/ufal/udpipe
cd udpipe/src
make
```

Copying the compiled binary to /usr/local/bin to access them via terminal

```
sudo cp udpipe /usr/local/bin/
```

Downloading the UD_Finnish-TDT treebank

```
git clone https://github.com/UniversalDependencies/UD_Finnish-TDT
cd UD_Finnish-TDT
```

Training the UDpipe using the finnish conllu file

```
cat fi_tdt-ud-train.conllu | udpipe --tokenizer=none --parser=none --train fi.udpipe
```

A model file is generated which can be used to tag the parts of speech for sentences

```
cat fi_tdt-ud-test.conllu | udpipe --tag fi.udpipe > fi_tdt-ud-test_output.conllu
```

Evaluating the Tagger's performance

```
python3 ../eval/evaluation_script/conll17_ud_eval.py --verbose fi_tdt-ud-test.conllu fi_tdt-ud-test_output.conllu
```

<pre>
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     94.63 |     94.63 |     94.63 |     94.63
XPOS       |     95.77 |     95.77 |     95.77 |     95.77
Feats      |     90.86 |     90.86 |     90.86 |     90.86
AllTags    |     89.82 |     89.82 |     89.82 |     89.82
Lemmas     |     84.86 |     84.86 |     84.86 |     84.86
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00
</pre>

### Processing the above dataset with another tagger : Perceptron-based Tagger

Train the perceptron-tagger model with Finnish Data

```
git clone https://github.com/ftyers/conllu-perceptron-tagger.git 
cat fi_tdt-ud-train.conllu | python3 ../conllu-perceptron-tagger/tagger.py -t ../conllu-perceptron-tagger/model.dat
```

Predicting POS Tags for the Test data set 

```
cat fi_tdt-ud-test.conllu | python3 ../conllu-perceptron-tagger/tagger.py ../conllu-perceptron-tagger/model.dat > ../conllu-perceptron-tagger/output_perceptron
```

Evaluating Tagger's performance

```
python3 ../eval/evaluation_script/conll17_ud_eval.py --verbose fi_tdt-ud-test.conllu ../conllu-perceptron-tagger/output_perceptron
```


<pre>Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     90.29 |     90.29 |     90.29 |     90.29
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     90.29 |     90.29 |     90.29 |     90.29
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00
</pre>

### Report

If we see the Universal Part of Speech rows for both the taggers, we can see that the UDPipe tagger has the precision,recall and AlignedAcc as 94.63% whereas the perceptron tagger has a precision,recall of 90.29%.

Both the taggers make use of supervised machine learning to train the model on the annotated conllu files. The UDpipe makes use of a batch size chosen uniformly between 50 and 100 and the learning rate is chosen logarithmically from range of 0.0005 and 0.01

Perceptron tagger starts with an empty weights dictionary, and then performs the following steps iteratively
1) Receives a new (features, POS-tag) pair
2) Guess the value of the POS tag given the current “weights” for the features
3) If guess is wrong, add +1 to the weights associated with the correct class for these features, and -1 to the weights for the predicted class.

It is  one of the simplest learning algorithms in which whenever you make a mistake, it will increment the weights for the correct class, and penalise the weights that led to false prediction.


