#TF-IDF : 단어의 빈도와 역 문서 빈도를 사용하여 DTM내의 각 단어들마다 중요한 정도를 가중치로 주는 방법, 문사의 유사도를 구하는 작업
#단어 카운트 가중치
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.io import mmwrite, mmread
import pickle

df_contents = pd.read_csv('./refined_data/cleaned_data.csv')
# df_contents.dropna(inplace=True)
# # df_contents.to_csv('./refined_data/cleaned_data.csv',
# #                   index=False)
df_contents.info()

#데이터 벡터라이징
Tfidf = TfidfVectorizer(sublinear_tf=True)
    #sublinear_tf = True  : TF(단어빈도)값의 스무딩(아웃라이어 심한 데이터 스무딩)True or False
Tfidf_matrix = Tfidf.fit_transform(df_contents['cleaned_sentences'])

#pickle로 저장
with open('./models/tfidf01.pickle', 'wb') as f:
    pickle.dump(Tfidf, f)
mmwrite('./models/Tfidf_tour.mtx', Tfidf_matrix)
print('end')




