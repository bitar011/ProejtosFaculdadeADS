#Bem Vindo a máquina de ingessos!
idade = int(input("Por favor, digite sua idade: "))

#Verificando idade para recomendar filme
if idade < 12:
    print("Recomendamos o filme infantil FILME 1.")
elif 12 <= idade < 18:
    print("Recomendamos o filme adolescente FILME 2.")
else:
    print("Recomendamos o emocionante FILME 3")

#Verifica ingressos disponíveis
quantidade_ingressos = 1190
if quantidade_ingressos > 0:
    print("Ingressos estão disponníveis! Divirta-se no cinema!")
else:
    print("Desculpe, todos os ingressos estão esgotados para hoje.")