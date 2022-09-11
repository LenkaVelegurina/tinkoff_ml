import pickle

if __name__ == "__main__":
    model_path = "model.pkl"
    with open(model_path, 'rb') as file:
        n_gram = pickle.load(file)
    result = []
    length = 200
    for i in range(length):
        result.append(n_gram.generate(tuple(result)))
    print(' '.join(result))