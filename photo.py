import wikipedia
import numpy as np
import sys
from wordcloud import WordCloud,STOPWORDS
from PIL import Image

title=str(input('Enter the title:'))
keyword=wikipedia.search(title)
page=wikipedia.page(keyword)
content=page.content

stopwords=set(STOPWORDS)
wordcloud=WordCloud(background_color='white',max_words=250,stopwords=stopwords)
wordcloud.generate(content)
wordcloud.to_file('output.jpg')