from collections import defaultdict
import numpy as np


def add_zero():
    return 0


def add_zero_dict():
    return defaultdict(add_zero)


class NGram:
    def __init__(self):
        self.dictionary = defaultdict(add_zero_dict)

    def fit(self, data):
        data_size = len(data)
        cnt = defaultdict(add_zero)
        for i in range(data_size - 2):
            self.dictionary[(data[i], data[i + 1])][data[i + 2]] += 1
            cnt[(data[i], data[i + 1])] += 1
        for key in self.dictionary.keys():
            for value in self.dictionary[key].keys():
                self.dictionary[key][value] /= cnt[key]

    def generate(self, sample=''):
        if sample[-2:] in self.dictionary:
            return np.random.choice(list(self.dictionary[sample[-2:]].keys()),
                                    p=list(self.dictionary[sample[-2:]].values()))
        temp = np.random.choice(list(self.dictionary.values()))
        return np.random.choice(list(temp.keys()), p=list(temp.values()))
