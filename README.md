# Overview and Data
As can be inferred from my other projects, I am interested in Japanese media. This interest has inspired me to try and learn a bit of Japanese. One of the most difficult parts is learning the necesary Kanji to understand a written sentence. Many say that to be fluent, one must know about 2000 Kanji. To start my learning journey, I went for the old fashioned flashcard method to memorize the characters.

The data I started with was a list of ~2500 kanji characters ordered by their popularity in newspaper usage. Below is a small snippet of the beginning of the list.
```
1: 日
2: 一
3: 国
4: 会
5: 人
6: 年
7: 大
```
Information about the character meanings and different pronunciations were gathered off the web by web scraping and structured in a way to easily create all of the flashcards at once using Quizlet.

# Tools used
I scraped the data and organized it using Python 3.6.5. The libraries used were BeautifulSoup, re, and requests. After scraping the data, a dictionary was made and this resulting file was saved as a pickle file. Therefore, pickle was used to reload the dictionary object back into Python if for some reason it was needed again.

# The Process
A dictionary entry for each kanji in the list was searched for using jisho.org.
