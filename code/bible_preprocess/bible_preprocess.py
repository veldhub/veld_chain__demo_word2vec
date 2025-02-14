import os
import re

import nltk
import string


print("-- bible preprocessing: start -------------------------------------------")
IN_FILE = "/veld/input/" + os.getenv("in_file")
OUT_FILE = "/veld/output/" + os.getenv("out_file")
print("in_file:", IN_FILE)
print("out_file:", OUT_FILE)


# load sentence splitting function
nltk.download('punkt')

# read file
with open(IN_FILE, "r") as f:
    content = f.read()

# transform content
print("make lowercase and clean from newlines")
content = content.lower()
content = content.replace("\r\n", " ")
content = content.replace("\n", " ")
print("remove chapter and verse indices")
content = re.sub("\d+:\d+ ", "", content)
print("tokenize to sentences, remove punctuation")
sentence_list = []
for sentence in nltk.sent_tokenize(content):
    word_list_new = []
    for word in nltk.word_tokenize(sentence):
        if word not in string.punctuation:
            word_list_new.append(word)
    sentence_list.append(" ".join(word_list_new))

# from line 29792 onwards, there is only gutenberg metadata left. So cut that
sentence_list = sentence_list[:29792]

# write to file, one sentence per line
with open(OUT_FILE, "w") as f:
    for sentence in sentence_list:
        f.write(sentence + "\n")

print("-- bible preprocessing: done --------------------------------------------")

