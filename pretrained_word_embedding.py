import numpy as np
from scipy import spatial
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

def get_word_embedding_dict(file_path):
    embeddings_dict = {}
    with open(file_path, 'r', encoding="utf-8") as f:
        for line in f:
            values = line.split()
            word = values[0]
            vector = np.asarray(values[1:], "float32")
            embeddings_dict[word] = vector
    return embeddings_dict
        
def find_closest_embeddings(embedding):
    return sorted(embeddings_dict.keys(), key=lambda word: spatial.distance.euclidean(embeddings_dict[word], embedding))

def visualizing_vectors(embeddings_dict):
    tsne = TSNE(n_components=2, random_state=0)
    words =  list(embeddings_dict.keys())
    vectors = [embeddings_dict[word] for word in words]
    Y = tsne.fit_transform(vectors[:1000])
    plt.scatter(Y[:, 0], Y[:, 1])
    for label, x, y in zip(words, Y[:, 0], Y[:, 1]):
        plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords="offset points")
    plt.show()
