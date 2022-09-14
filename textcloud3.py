import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS
import sys,os
os.chdir(sys.path[0])

text=open("bow.txt",mode ="r",encoding='utf8').read()
stopwords=STOPWORDS
#print(stopwords)

wc=WordCloud(
    background_color='black',
    stopwords=stopwords,
    height=600,
    width=400
)

wc.generate(text)
wc.to_file('ouput3.png')