import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from scipy.io import mmread, mmwrite
import pickle
from gensim.models import Word2Vec

df_contents = pd.read_csv('./refined_data/cleaned_data.csv')
df_contents.info()
def getRecommendation(cosine_sim):
    simScore = list(enumerate(cosine_sim[-1]))
    # print(len(simScore))
    # print(simScore)
    simScore = sorted(simScore, key=lambda x:x[1],
                      reverse=True)
    simScore = simScore[1:11]
    touridx = [i[0] for i in simScore]

    recTourList = df_contents.iloc[touridx]    #print용 코드
    return recTourList.iloc[:,0]

    # recTourList = df_contents.iloc[touridx, :]   #to_json용 코드
    # return recTourList

Tfidf_matrix = mmread('./models/Tfidf_tour.mtx').tocsr()
with open('./models/tfidf01.pickle', 'rb') as f:
    Tfidf = pickle.load(f)

# 영화 제목을 이용
tour_idx = df_contents[df_contents['title']=='서울대공원'].index[0]
print(tour_idx)
# 영화 index를 이용
# movie_idx = 566
print(df_contents.iloc[tour_idx, 0])

# key_word 이용
embedding_model = Word2Vec.load('./models/word2vecModel.model')
key_word = '데이트'
sim_word = embedding_model.wv.most_similar(key_word, topn=10)
sentence = [key_word] * 11
words = []
for word, _ in sim_word:
    words.append(word)
for i, word in enumerate(words):
    sentence += [word] * (10 - i)
#
sentence = ' '.join(sentence)
sentence = '데이트'
sentence_vec = Tfidf.transform([sentence])
# cosine_sim = linear_kernel(sentence_vec, Tfidf_matrix)

cosine_sim = linear_kernel(Tfidf_matrix[tour_idx], Tfidf_matrix)
recommendation = getRecommendation(cosine_sim)
# recommendation.info()
print(recommendation)
recommendation.to_json('./output/recommendation2.json') #제이슨파일 생성