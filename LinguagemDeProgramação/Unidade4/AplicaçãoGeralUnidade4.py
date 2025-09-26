#============================================================
# MACHINE LEARNING COM PYTHON - CLASSIFICAÇÃO IRIS
#============================================================

#Importações necessárias
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#------------------------------------------------------------
# Carregar dataset Iris
#------------------------------------------------------------
iris = load_iris()
X = iris.data
y = iris.target

#Normalizar os dados
scaler = StandardScaler()
X = scaler.fit_transform(X)

#Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#------------------------------------------------------------
# Construir modelo
#------------------------------------------------------------
model = Sequential([
    Dense(12, activation='relu', input_shape=(4,)),  #camada oculta 1
    Dense(8, activation='relu'),                     #camada oculta 2
    Dense(3, activation='softmax')                   #camada de saída (3 classes)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#Treinar modelo
model.fit(X_train, y_train, epochs=50, validation_split=0.2, verbose=0)

#Avaliar modelo
loss, acc = model.evaluate(X_test, y_test, verbose=0)
print(f"✅ Precisão final do modelo nos dados de teste: {acc*100:.2f}%")

#------------------------------------------------------------
# Função para prever com entrada do usuário
#------------------------------------------------------------
def prever_iris():
    while True:
        print("\nDigite os valores das características da flor Iris:")

        sepal_length = float(input("Comprimento da sépala (cm): "))
        sepal_width  = float(input("Largura da sépala (cm): "))
        petal_length = float(input("Comprimento da pétala (cm): "))
        petal_width  = float(input("Largura da pétala (cm): "))

        #Normalizar entrada do usuário
        amostra = [[sepal_length, sepal_width, petal_length, petal_width]]
        amostra_scaled = scaler.transform(amostra)

        #Fazer previsão
        probs = model.predict(amostra_scaled)
        classe = probs.argmax(axis=1)[0]
        print(f"\n🌸 A flor foi classificada como: {iris.target_names[classe]}")

        #Perguntar se deseja continuar
        continuar = input("\nDeseja testar outra flor? (s/n): ").lower()
        if continuar != 's':
            print("Encerrando previsões...")
            break

#------------------------------------------------------------
# Chamar função
#------------------------------------------------------------
prever_iris()

#Aplicação não sendo rodada no VSCode por diferença em versão suportada pelo Tensorflow e a versão instalada do Python
#Atividade construída e realiada com sucesso através do Google Colab