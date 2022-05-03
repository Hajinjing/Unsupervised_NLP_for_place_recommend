#단어간 유사도 계산
from gensim.models import Word2Vec
import pandas as pd

content_word = pd.read_csv('./refined_data/cleaned_data.csv')
content_word.info()

cleaned_token_content = list(content_word['cleaned_sentences'])
print(cleaned_token_content[0])
cleaned_tokens = []
for sentence in cleaned_token_content:
    token = sentence.split()
    cleaned_tokens.append(token)
print(cleaned_tokens[0])

embedding_model = Word2Vec(cleaned_tokens,
                           vector_size=100,
                           window=4, min_count=20,
                           workers=4, epochs=100, sg=1)
#size : 만들어질 워드 벡터의 차원
#window : 컨텍스트 윈도우의 크기. 컨텍스트 윈도우는 단어 앞과 뒤에서 몇개 단어를 볼것인지를 정하는 크기이다.
#min_count = 단어 최소 빈도수의 임계치(이 임계치보다 적은 단어는 훈련시키지 않는다.)
#workers = 학습에 이용하는 프로세스의 갯수 컴퓨터의 cpu에 따라 조절
#sg = 0 일 경우, CBOW, 1 일 경우 Skip-gram


embedding_model.save('./models/word2vecModel.model')
print(list(embedding_model.wv.index_to_key))
print(len(list(embedding_model.wv.index_to_key)))


