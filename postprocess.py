import sys
import pickle

file_name = sys.argv[1]
dict_path = "dict.pkl"
output_path = "gene.js"

with open(file_name, 'r') as f:
    generation = f.readlines()

with open(dict_path, 'rb') as f:
    id_to_word = pickle.load(f)

for i in range(len(generation)):
    generation[i] = list(map(int, generation[i].split()))
    for j in range(20):
        generation[i][j] = id_to_word[generation[i][j]]

with open(output_path, 'w') as f:
    for line in generation:
        f.write(" ".join(line) + "\n")