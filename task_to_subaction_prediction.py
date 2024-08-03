import tensorflow as tf
import numpy as np
from task_config import *

# Load pre-trained word embeddings (example using GloVe)
embeddings_index = {}
embedding_dim = 100
with open('glove.6B.100d.txt', encoding='utf-8') as f:
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = coefs

# Function to get word embeddings for tasks
def get_task_embeddings(tasks):
    task_embeddings = []
    for task in tasks:
        words = task.lower().split()
        word_embeddings = []
        for word in words:
            if word in embeddings_index:
                word_embeddings.append(embeddings_index[word])
            else:
                word_embeddings.append(np.zeros(embedding_dim))  # OOV words represented as zero vectors
        task_embeddings.append(np.mean(word_embeddings, axis=0))  # Averaging word embeddings for the task
    return np.array(task_embeddings)

# Load the trained model
model = tf.keras.models.load_model('task_model.h5')

# New task for prediction
new_task = "give me the glass of water first pour the water from the bottle"
new_task_embedding = get_task_embeddings([new_task])

# Prediction
prediction = model.predict(new_task_embedding)
print(prediction)

# Interpret the prediction
predicted_sub_action_indices = np.argmax(prediction, axis=-1)
predicted_sub_actions = [sub_actions[idx] for idx in predicted_sub_action_indices[0]]
print("Predicted Sub-Actions:", predicted_sub_actions)
