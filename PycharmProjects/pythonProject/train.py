import re
import os
import pickle
from n_gram import NGram

# def save(model_path='model'):


if __name__ == '__main__':
    data_path = 'data/dvor-shipov-i-roz.txt'
    first_data = []
    with open(data_path, 'r') as file:
        first_data = file.readlines()

    data = []
    for line in first_data:
        for word in re.findall(r'\w+|\.', line.lower()):
            data.append(word)
    n_gram = NGram()
    n_gram.fit(data)

    model_path = 'model.pkl'
    with open(model_path, 'wb') as file:
        pickle.dump(n_gram, file)
    #print(data)