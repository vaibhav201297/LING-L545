from conllu import parse_incr
from conllu.models import TokenList, Token
import sys


if __name__ == "__main__":
    dictionary_path = sys.argv[1]
    t:TokenList=None
    data_file = open(dictionary_path, "r", encoding="utf-8")
    test_file = open(dictionary_path.replace('train','test'))
    sentences=[]
    for tokenlist in parse_incr(test_file):
        sentences.append(tokenlist)
    for t in sentences:
        for i in t:
            print(i)
        
       

    
