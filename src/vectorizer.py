from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix

from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from tqdm import tqdm
from .helper import load_file, preprocess

import os
import pickle


class Vectorizer:
    def __init__(self):
        # I use pipline insteadof use simple data
        self.pipeline = Pipeline([('vect', CountVectorizer()),
                    ('tfidf', TfidfTransformer()),
                    ('clf', MultinomialNB()),
                    ])

    def fit(self, df):
        self.pipeline.fit(df['text'], df['label'])
            
    def save(self, output_name='model10topics.pkl'):
        pickle.dump(self.pipeline, open(output_name, 'wb'))

    def load(self, model_name="model10topics.pkl"):
        return pickle.load(open(model_name, 'rb'))

    def show_report(self, model, stopwords, test_path=os.path.join('data','test')):
        from sklearn.metrics import classification_report
    
        
        dftest = load_file(test_path)
        # ana tambahin ini
        for i in tqdm(range(dftest['text'].count()), desc="preprocess"):
            dftest.iloc[i,1] = preprocess(dftest.iloc[i,1], stopwords)
        # sampe sini
        y_pred = model.predict(dftest['text'])

        classes = dftest.label.unique()
        print('accuracy %s' % accuracy_score(y_pred, dftest['label']))
        print(classification_report(dftest['label'], y_pred,target_names=classes))
        # print(dftest['label'], y_pred, classes)
