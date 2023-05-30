# 대문자, 소문자, 문자열조작 새로운 메소드✅

#Answer1
word = list(input())
result = ''

for i in range(len(word)):
  if(word[i].isupper()):
    word[i] = word[i].lower()
  else:
    word[i] = word[i].upper()

  result += word[i]

print(result)

#Answer2
word = list(input())
#result = ''

for i in range(len(word)):
  if(word[i].isupper()):
    word[i] = word[i].lower()
  else:
    word[i] = word[i].upper()

  
result = ''.join(word)

print(result)