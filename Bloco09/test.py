import requests

url = "https://api.totalvoice.com.br/sms"

payload = "{\"numero_destino\":\"21993329936\",\"mensagem\":\"teste totalvoice\",\"resposta_usuario\":false,\"multi_sms\":false}"
headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'Access-Token': "5ed8f2b486c929871988dfc315c2b0ab",
    'Cache-Control': "no-cache",
    'Postman-Token': "53993368-abec-43e0-bb64-c4024fe75ec5"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
