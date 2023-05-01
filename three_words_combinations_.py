word = input().split()  # apple is a fruit
word.sort()
#print(word)
length = len(word)
list_ = []
for i in range(length):
    for j in range(i+1,length):
        for k in range(j+1,length):
            three_words = word[i] + " " + word[j] + " " + word[k]
            list_.append(three_words)
set_words = list(set(list_))
#print(set_words)
set_words.sort()
for i in set_words:
    print(i)

# a apple fruit
#a apple is
#a fruit is
#apple fruit is