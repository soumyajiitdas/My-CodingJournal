n = int(input().strip())
word_dict = {}
for _ in range(n):
    word = input().strip()
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
        
print(len(word_dict))
print(' '.join(map(str, word_dict.values())))