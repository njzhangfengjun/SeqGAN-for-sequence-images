import sys
import re
from collections import Counter
import pandas as pd
import pickle

file_name = sys.argv[1]
output_path = "2.data"
dict_path = "dict.pkl"

with open(file_name, 'r', encoding='utf-8') as f:
    corpus = f.readlines()

print("Read file")
print(len(corpus))
corpus = list(set(corpus))
print("Deduplicated")
print(len(corpus))
#
tokens = [list(filter(lambda x: x.isascii(), filter(lambda x: x != '', filter(lambda x: x != ' ', re.split("(\.|\(|\)|\[|\]|\{|\}|;|:|,|\'|\"|\+\+|\-\-|\^|\\\\|`|!|\?|===|==|<<|>>|<=|=>|>=|<|>|\*|=|\|&&|&|\||\||\s)", line.rstrip()))))) for line in corpus]
print("Acquired tokens")
#vocab = list(dict(Counter(sum(tokens, []))).items())
vocab = list(set(sum(tokens, [])))
n_token = len(vocab)
print("Generated vocab")
print(n_token)

df = pd.DataFrame(vocab)[0]
df.index += 1

id_to_word = df.to_dict()
df_2 = pd.Series(df.index.values, df.values)
word_to_id = df_2.to_dict()
print(id_to_word)
#print([i if not word.isascii() else 1 for i, word in enumerate(vocab, 1)])

dataset = []

for line in tokens:
    if 3 <= len(line) and len(line) <= 20:
        for i in range(len(line)):
            line[i] = word_to_id[line[i]]
        line.extend([n_token + 1] * (20 - len(line)))
        dataset.append(line)
dataset = dataset[:54000]

with open(output_path, 'w') as f:
    for row in dataset:
        f.write(" ".join(list(map(str, row))) + "\n")

id_to_word[n_token + 1] = ""
with open(dict_path, 'wb') as f:
    pickle.dump(id_to_word, f)

#for line in corpus:
#    print(jsparser3.parse(line))
#print(id_to_word)
#print(word_to_id)
