import string
import collections

fileref = open("98-0.txt","r")
words = fileref.read().lower().split()
for word in words:
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace("\"","")
    word = word.replace("“","")

#check by printing the first 30 to see if it works
#print(words[:100])

# checking against the stopwords list

fileref = open("stopwords","r")
stop_words = fileref.read()
sw_list = stop_words.split()
new_word_list = []
for c in words:
    if c not in sw_list:
        new_word_list.append(c)
#check by printing the first 30 to see if it works by comparing against the initial list
#print(new_word_list[:30])

# #check by printing the first 10 to see if it works
# print(new_word_list[:10])

# count dictionary function
counts = {} # start with an empty dictionary
for c in new_word_list:
    if c not in counts:
        # we have not seen this character before, so initialize a counter for it
        counts[c] = 0

    #whether we've seen it before or not, increment its counter
    counts[c] = counts[c] + 1

d = collections.Counter(counts)
for word, count in d.most_common(50):
	print(word, ": ", count)
