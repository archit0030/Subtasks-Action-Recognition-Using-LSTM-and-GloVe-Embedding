import tensorflow as tf
from collections import Counter
import numpy as np
from task_config import *

# Verify consistent sample sizes
assert len(tasks) == len(sub_action_sequences), "Mismatch between number of tasks and sub-action sequences."

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

# Get embeddings for tasks
task_embeddings = get_task_embeddings(tasks)

# Convert sub_action_sequences to NumPy array
padded_sub_action_sequences = tf.keras.preprocessing.sequence.pad_sequences(
    sub_action_sequences, maxlen=10, padding='post'
)
padded_sub_action_sequences = tf.keras.utils.to_categorical(padded_sub_action_sequences, num_classes=len(sub_actions))

# Verify consistent sample sizes again
assert task_embeddings.shape[0] == padded_sub_action_sequences.shape[0], "Mismatch between number of samples in embeddings and sub-action sequences."

# Model Creation
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(embedding_dim,)),
    tf.keras.layers.RepeatVector(10),  # Repeat the input to match the sequence length of 10
    tf.keras.layers.LSTM(128, return_sequences=True),
    tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(len(sub_actions), activation='softmax'))
])

# Training
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(task_embeddings, padded_sub_action_sequences, epochs=100)

# Save the trained model
model.save('task_model.h5')
