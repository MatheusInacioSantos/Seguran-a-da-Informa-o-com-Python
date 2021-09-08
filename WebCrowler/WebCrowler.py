from bs4 import BeautifulSoup
import requests
import operator
from collections import Counter

def start(url):

    wordList = []
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, 'html.parser')

    # text in given web-page is stored under
    # the <dib> tags with class <entry-contet>
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text

    words = content.lower().split()

    for each_word in words:
        wordList.append(each_word)
    clean_wordList(wordList)

def clean_wordList(wordList):
    clean_list = []
    for word in wordList:
        symbols = '!@#$%^&*()_-+={[}]:/?.,;'

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

            if len(word) > 0:
                clean_list.append(word)
        create_dictionary(clean_list)

def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


    for key, value in sorted(word_count.items(),
                         key = operator.itemgetter(1)):
        print("% S : % S " % (key, value))

    c = Counter(word_count)

    top = c.most_common(10)
    print(top)


if __name__ == '__main__':
    start('https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar')














