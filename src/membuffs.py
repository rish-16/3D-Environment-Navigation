import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, LSTM, Dense

def get_lstm(dim, n_actions):
    model = Sequential()
    model.add(Input(shape=dim))
    model.add(Dense(64, activation="relu"))
    model.add(Dense(128, activation="relu"))
    model.add(LSTM(128))
    model.add(Dense(n_actions, activation="linear"))
    
    model.compile(optimizer="adam", loss="mse")
    
    return model