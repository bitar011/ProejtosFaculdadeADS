#Machine Learning
#Testes com tensoflow
#Supervisionado
# import tensorflow as tf
# from keras.models import Sequential
# from keras.layers import Dense
# import matplotlib.pyplot as plt

# x_train = tf.constant([[1.0], [2.0], [3.0], [4.0]])
# y_train = tf.constant([[2.0], [4.0], [6.0], [8.0]])

# model = Sequential()
# model.add(Dense(units=1, input_shape=(1,)))
# model.compile(optimizer='sgd', loss='mean_squared_error')

# history = model.fit(x_train, y_train, epochs=1000, verbose=0)

# x_new = tf.constant([[5.0]])
# prediction = model.predict(x_new)
# print("Predicação:", prediction[0][0])

# plt.plot(history.history['loss'])
# plt.title('Model Loss Over Training')
# plt.xlabel('Epoch')
# plt.ylabel('Loss')
# plt.show()

#Não Supervisionado
# import tensorflow as tf
# from keras.layers import Input, Dense
# from keras.models import Model

# X_unsupervisioned = tf.constant([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0], [4.0, 5.0]])

# input_layer = Input(shape=(2,))
# encoded = Dense(units=1)(input_layer)
# decoded = Dense(units=2)(encoded)

# autoenconder = Model(inputs=input_layer, outputs=decoded)
# autoenconder.compile(optimizer='adam', loss='mean_squared_error')

# autoenconder.fit(X_unsupervisioned, X_unsupervisioned, epochs=1000, verbose=0)

# prediction_unsupervised = autoenconder.predict(X_unsupervisioned)
# print("Predicação não supervisionada:", prediction_unsupervised)

#Esforço
# import tensorflow as tf
# import gym

# env = gym.make('CartPole-v1')

# model_reinforcement = tf.keras.Sequential([
#     tf.keras.layers.Dense(24, activation='relu', input_shape=(env.observation_space.shape[0],)),
#     tf.keras.layers.Dense(env.action_space.n, activation='linear')
# ])

# model_reinforcement.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='mse')

# max_episodes = 1000
# for episode in range(max_episodes):
#     state = env.reset
#     done = False

#     while not done:
#         action = env.action_space.sample()

#         next_state, reward, done, _, = env.step(action)

#         target = reward + 0.95 * tf.reduce_max(model_reinforcement.predict(next_state.reshape(1, -1)))

#         target_f = model_reinforcement.predict(state.reshape(1, -1))

#         target_f[0][action] = target

#         model_reinforcement.fit(state.reshape(1, -1), target_f, epochs=1, verbose=0)

#         state = next_state
    
#     if episode % 10 == 0:
#         avarage_reward = sum(reward for _ in range(10)) / 10.0
#         print(f'Episode {episode}, Avarage Reward: {avarage_reward}')

#         if avarage_reward == 1:
#             print(f'Solved after {episode} episodes!')
#             break

#-----------------------------------------------------------------
#Aplicação geral da aula
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import tensorflow as tf

np.random.seed(42)
meses = np.arange(1, 13)
vendas = np.array([200, 220, 250, 280, 300, 320, 350, 380, 400, 420, 450, 480])

dados = pd.DataFrame({'Mes': meses, 'Vendas': vendas})

X = dados[['Mes']]
y = dados[['Vendas']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = MinMaxScaler()
X_train_scaled = scaler.fit.transform(X_train)
X_test_scaled = scaler.fit.trasnform(X_test)

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),
    tf.keras.layers.Dense(units=8, activation='relu'),
    tf.keras.layers.Dense(units=1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(X_train_scaled, y_train, epochs=500, verbose=0)

predicitions_scaled = model.predict(X_test_scaled)

predicitons_inverse = scaler.inverse_transform(predicitions_scaled)
y_test_inverse = scaler.inverse_transform(np.array(y_test).reshape(-1, 1))

plt.scatter(X_test, y_test_inverse, label='Dados Reais')
plt.plot(X_test, predicitons_inverse, color='red', label='Previsões')
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.title('Previsões de Vendas com Regressão Linear(Tensorflow)')
plt.legend()
plt.show()

erro_mse = mean_squared_error(y_test_inverse, predicitons_inverse)
print(f'Erro Médio Quadrático (MSE): {erro_mse:.2f}')

proximo_mes_scaled = scaler.transform(np.array([[13]]))
previsao_proximo_mes_scaled = model.predict(proximo_mes_scaled)
previsao_proximo_mes = scaler.inverse_transform(previsao_proximo_mes_scaled)[0, 0]
print(f'Previsão de vendas para o próximo mês: {previsao_proximo_mes:.2f}')

#Testes dando errado no VSCode, foram refeitos no Google Colab com sucesso