## Report

For this practical, I have used test.txt as my corpus which contains the text from the Practical 1b page.

<ol>

<li> What is the difference between using print() and sys.stdout.write() <br/>

print() will automatically add a '\n' whereas it has to be added with the string in sys.stdout.write()
</li>
<li>
How should you segment sentences with semi-colon? As a single sentence or as two sentences? Should it depend on context? <br/>
Semi-Colon doesn't mark the end of a sentence, so it should be treated as a single sentence . However, there may be cases where we might have to treat the corpus sentence using clauses. In that case, we may have to treat it as multiple sentences as a semicolon(;) marks the end of a clause in a sentence.
</li>
<li>
Should sentences with ellipsis... be treated as a single sentence or as several sentences? <br/>
No, a sentence may contain an ellipsis in between the sentence in which case the sentence would be broken down into multiple sentences which is incorrect. We can ignore the ellipsis in most cases unless we want to generate transcriptions of audio, in which case we'll know that a pause has to be added to get the correct word-to-word transcriptions.
</li>

<li> If there is an exclamation after the first word in the sentence should it be a separate sentence? How about if there is a comma? <br/>
Neither an exclamation mark not a comma after the first word should be treated as a different sentence
</li>
<li> Can you think of some hard tasks for the segmenter?  <br/>
Some tasks that may be hard for the segmenter would be in case of Abbreviations or Timings or Dates written in the dot format.
For example , Mr. John Doe is the C.E.O of Abc Corp. LLC since 12.10.2020.

The above sentence should be considered as a single sentence, however, since there are periods spread throughout the sentence, the segmenter may get confused and treat it as separate sentences.

</li>

<li>
Why should we split punctuation from the token it goes with ? <br/>

We should split punctuation because it is not considered as part of a word. 
</li>
<li>
Should abbreviations with space in them be written as a single token or two tokens ?<br/>
How about numerals like 134 000 ? <br/>
Abbreviations and numerals should be treated as a single token.
</li>

<li>
If you have a case suffix following punctuation, how should it be tokenised ? <br/>
Case suffix should be treated as punctuation
</li>

<li>Should contractions and clitics be a single token or two (or more) tokens ? <br/>
We should treat contractions and clitics as a single token
</li>
</ol>
