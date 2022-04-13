#데이터 전처리
#stopword 제거

import pandas as pd
from konlpy.tag import Okt
import re

df = pd.read_csv('crawling_data/tour_all.csv')
print(df.head())
df.info()

stopwords = pd.read_csv('./stopwords.csv', encoding='CP949')
stopwords_list = list(stopwords.stopword)

cleaned_sentences = []
for content in df.contents:
    content = re.sub('[^가-힣 ]', ' ', content) #한글, 띄어쓰기만 놔두고 제거
    content_word = content.split(' ') #split해서 list화

    words = []

    for word in content_word:
        if len(word)>1:
            if word not in stopwords_list:
                words.append(word)
    cleaned_sentence = ' '.join(words)
    cleaned_sentences.append(cleaned_sentence)
df['cleaned_sentences'] = cleaned_sentences
df = df[['title', 'cleaned_sentences']]
df.to_csv('./refined_data/refined_data.csv', index = False)
df.info()

