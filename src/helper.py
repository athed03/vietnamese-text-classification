import imutils.paths as path
import numpy as np
import pandas as pd
import random
import os
import string
import re
from tqdm import tqdm


def load_file(dataset_path):
    list_dir = sorted(list(path.list_files(dataset_path)))
    random.seed(2)
    random.shuffle(list_dir)
    data = []
    labels = []
    print(dataset_path,len(list_dir))

    for item in tqdm(list_dir, desc="Loading File "):
        # utf16 for vietnamese
        with open(item,'r', encoding="UTF16") as fp:
            line = fp.read()
            data.append(line)
            label = item.split(os.path.sep)[-2]
            labels.append(label)
    return pd.DataFrame({'label': labels,
                         'text': data})


def preprocess(text, stopwords):
    table = str.maketrans(dict.fromkeys(string.punctuation))
    text = text.translate(table)
    text = text.lower()
    text = re.sub(r'\s?[0-9]+\.?[0-9]*', '', text)
    text = re.sub(r'[\n]*', '', text)
    text = text.split(" ")
    filtered_sentence = [w for w in text if not w in stopwords]
    return " ".join(filtered_sentence)

def undersampling(df):
    # table = str.maketrans(dict.fromkeys(string.punctuation))
    data = pd.DataFrame(columns = ['label','text'])
    columns = df.label.unique()
    x=df.label.value_counts().rename(index = 1).sort_values(ascending=True)

    for label in tqdm(columns, desc="Undersampling "):
        dataframe = df[df['label']==label]
        dataframe = dataframe.iloc[0:x[0],:]
        data = data.append(dataframe)

    return data
