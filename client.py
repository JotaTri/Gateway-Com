import requests


while True:
    formula = raw_input("Indique a formula a ser enviada")
    topico = raw_input('Indique o topico a ser enviado o resultado da formula')

    post_data = {"formula": formula, "topico": topico}

    resposta = requests.post("http://localhost:5000", data=post_data)
    print resposta.json()
    # print resposta.message
