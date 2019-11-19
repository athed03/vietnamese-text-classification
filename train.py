import os
import argparse
import pandas as pd

from src.helper import load_file, undersampling, preprocess
from src.vectorizer import Vectorizer
from tqdm import tqdm


def train(
        trainset_path=os.path.join('data', 'train'), 
        stopword_path=os.path.join('data', 'vietnamese-stopwords.txt'),
        test_path=os.path.join('data', 'test'),
        output_name=os.path.join('model', 'model.pkl')
        ):

    dataframe = pd.read_csv(trainset_path)
    dataframe = undersampling(dataframe)

# ana nambah dari sini

    stopwords = open(stopword_path,'r',encoding="UTF8").read().split('\n')
    stopwords.append("\n")

    for i in tqdm(range(dataframe['text'].count()), desc="preprocess"):
        dataframe.iloc[i,1] = preprocess(dataframe.iloc[i,1], stopwords)
    
    vectorizer = Vectorizer()
    vectorizer.fit(dataframe)
    vectorizer.save(output_name)
    
    model = vectorizer.load(output_name)
    
    # to show accuracy
    vectorizer.show_report(model,stopwords, test_path )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Gleematic Sentiment Analysis. Training')
    parser.add_argument('--trainset_path', default=os.path.join('data', 'train','export_dataframe.csv'),
                        help='Trainset path')
    parser.add_argument('--stopword_path', default=os.path.join('data', 'vietnamese-stopwords.txt'),
                        help='Vietnamese stopword')
    parser.add_argument('--test_path', default=os.path.join('data', 'test'),
                        help='Output name')
    parser.add_argument('--output_name', default=os.path.join('model', 'model.pkl'),
                        help='Output name')
    args = parser.parse_args()

    train(
        args.trainset_path, 
        args.stopword_path,
        args.test_path,
        args.output_name)
