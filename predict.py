import os
import argparse

from src.helper import load_file, undersampling, preprocess
from src.vectorizer import Vectorizer


def predict(
        model_name=os.path.join('model', 'model.pkl'),
        stopword_path=os.path.join('data', 'vietnamese-stopwords.txt'),
        interactive=True
        ):
    
    print("Reading stopword")
    stopwords = open(stopword_path,'r',encoding="UTF8").read().split('\n')
    stopwords.append("\n")
    print("Finished reading stopword")
    
    vectorizer = Vectorizer()
    model = vectorizer.load(model_name=model_name)

    if interactive:
        print("Press !q to quit interactive mode")
        while(True):
            sent = input(">>")
            if sent == "!q":
                break
            sent = preprocess(sent, stopwords)
            res = model.predict([" ".join(sent)])
            print(res[0])
    else:
        sent = preprocess("your text here", stopwords)
        res = model.predict([" ".join(sent)])
        print(res[0])



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Gleematic Sentiment Analysis. Training')
    parser.add_argument('--model_name', default=os.path.join('model', 'model.pkl'),
                        help='Trainset path')
    parser.add_argument('--stopword_path', default=os.path.join('data', 'vietnamese-stopwords.txt'),
                        help='Vietnamese stopword')
    parser.add_argument('--interactive', action="store_true",
                        help='Output name')
    args = parser.parse_args()

    predict(
        args.model_name, 
        args.stopword_path,
        args.interactive)
