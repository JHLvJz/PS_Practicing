import sys

howMany = int(sys.stdin.readline())
words = dict()

for i in range(howMany):
    word = sys.stdin.readline()
    words[word] = len(word)


sort_words = sorted(words.values())

for index in sort_words:
    temp = []
    flag = 0
    for k, v in words.items():
        if v == index:
            temp.append(k)
    
    if len(temp) > 1:
        for word in temp:
            ord(word[0])

    