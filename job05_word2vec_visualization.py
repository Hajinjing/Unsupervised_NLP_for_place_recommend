import pandas as pd
import matplotlib.pyplot as plt
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
from matplotlib import font_manager, rc #한글폰트적용
import matplotlib as mpl

#matplotlib의 rc에 한글폰트 적용
#폰트경로
font_path = './malgun.ttf'
#폰트이름 얻어오기
font_name = font_manager.FontProperties(
    fname=font_path).get_name()
print(type(font_name))
#rc를 통해 폰트 설정
mpl.rcParams['axes.unicode_minus']=False #한글폰트 적용시 마이너스기호 깨짐현상 해결
rc('font', family=font_name)

# # !apt -qq -y install fonts-nanum
# import matplotlib as mpl
# import matplotlib.font_manager as fm
# fontpath = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
# font = fm.FontProperties(fname=fontpath, size=9)
# plt.rc('font', family='NanumBarunGothic')
# mpl.font_manager._rebuild()

#저장해둔 model파일 불러오기
embedding_model = Word2Vec.load('./models/word2vecModel.model')
print(list(embedding_model.wv.index_to_key))
print(len(list(embedding_model.wv.index_to_key)))
key_word = '조용하다'
sim_word = embedding_model.wv.most_similar(key_word, topn=20) #TopN, 상위 20개로 지정
print('sim_word:',sim_word)
print(len(sim_word))

vectors = []  #vectors에는 유사도를 append
labels = []
for label, _ in sim_word:
    labels.append(label)
    vectors.append(embedding_model.wv[label])
df_vectors = pd.DataFrame(vectors)
print(df_vectors.head())

#word2vec의 결과를 시각화하기 위한 차원축소
tsne_model = TSNE(perplexity=40, n_components=2,
                  init='pca', n_iter=2500)
#perplexity:값이 크면 더 많은 이웃을 포함하여 작은 그룹은 무시, 기본값=30, 보통5~50사이의 깂을 가짐
#n_components:임베드 된 공간의 차원
#init: 임베딩초기화, random 또는 pca 및 numpy배열 형태(n_samples, n_components), random은 군집을 더 잘해줌, pca는 위치가 고정되어 보기 편함
#n_iter:최적화를 위한 최대 반복 횟수, 250이상이어야함

new_value = tsne_model.fit_transform(df_vectors)
# print('new_value',new_value)
#tsne모델에 적용후 열이름 설정, 각 값을 배정, (x,y)는 모든 행의 0열들, y는 모든행의 1열 값
df_xy = pd.DataFrame({'word':labels,
                      'x':new_value[:, 0],
                      'y':new_value[:, 1]})
print('df_xy : ',df_xy)
# print('df_xy.shape : ',df_xy.shape) #20행 3열  (20, 3)
# print(df_xy.shape[0]) = 20
df_xy.loc[df_xy.shape[0]] = (key_word, 0, 0)  #df_xy.loc[20] = (key_word, 0, 0), df 마지막행에 key_word단어 추가

#차트그리기
plt.figure(figsize=(8, 8))  #8*8 사이즈
plt.scatter(0, 0, s=1500, marker='*') #key_word를 표현할 별표를 중간에 그려줌

#df_xy.loc[20]을 추가했기때문에 for문에서는 -1
for i in range(len(df_xy.x) - 1):
    a = df_xy.loc[[i, (len(df_xy.x) - 1)], :]   # df_xy.loc[[i,20], :]  i행과 20행 모든열(word, x, y)
    plt.plot(a.x, a.y, '-D', linewidth=1)       # 20행(키워드)를 기준으로 거리를 그려줌
    #주석달기(s, xy)
    plt.annotate(df_xy.word[i], xytext=(1, 1),
                 xy=(df_xy.x[i], df_xy.y[i]),
                 textcoords='offset points',
                 ha='right', va='bottom')
plt.show()

#textcoords : 'offset points' 는 xy(좌표 측의 값)에서부터 xytext offset 위치(단위 point)에 출력, 'offset pixels'는 픽셀단위


