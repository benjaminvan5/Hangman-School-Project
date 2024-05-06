word_list = []
# Converts words.txt to an array that can be used
with open('words.txt', 'r') as words:
  word_list = words.readlines()
for i in range(len(word_list)):
    word_list[i]=word_list[i].replace('\n','')