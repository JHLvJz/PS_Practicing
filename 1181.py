### 미해결
import sys

howMany = int(sys.stdin.readline())
words = dict()

for i in range(howMany):
    word = sys.stdin.readline().rstrip()
    if word not in words:
        words[word] = len(word)

sort_words = sorted(words.items(), key = lambda item : item[1])
new_words = dict()

flag = 0

for i in range(len(sort_words)):
    if flag != sort_words[i][1]:
        new_words[sort_words[i][1]] = [sort_words[i][0]]
    else:
        new_words[sort_words[i][1]].append((sort_words[i][0], ord(sort_words[i][0][0])))
    flag = sort_words[i][1]
print(new_words)


    



