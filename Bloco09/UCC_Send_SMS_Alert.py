import http.client
import json
import time
import argparse
#Get information of the alarm to be issued
parser = argparse.ArgumentParser()
parser.add_argument("blocoid")
parser.add_argument("eventid")
args = parser.parse_args()
#
def postPayload(phoneNumber,msgText):
	str1 = '{\"numero_destino\":\"'
	str2 = phoneNumber
	str3 = '\",\"mensagem\":\"'
	str4 = msgText
	str5 = '\",\"resposta_usuario\":"false",\"multi_sms\":"false"}'
	jsonPayload = str1 + str2 + str3 + str4 + str5
	return(jsonPayload)
#
def sendSMS(jsonPayload):
	conn = http.client.HTTPSConnection("api.totalvoice.com.br")
	headers = {
		'content-type': "application/json",
		'accept': "application/json",
		'access-token': "5ed8f2b486c929871988dfc315c2b0ab"}
	conn.request("POST", "/sms", jsonPayload, headers)

	res = conn.getresponse()
	data = res.read()

	print(data.decode("utf-8"))
#
def AlarmTextMsg():
	msgCritical = 'uControl Alerta - Evento Critico Detectado no '
	msgLocation = 'Bloco ' + (str(args.blocoid)) + ": " +(str(args.eventid))
	msgFinal = ' Por favor, verifique em: http://life.ucontrol.net.br'
	msgText = msgCritical + msgLocation + msgFinal
	return(msgText)
#
def NormalTextMsg():
	msgCritical = 'uControl Informa - '
	msgLocation = 'Bloco ' + (str(args.blocoid)) + ": " +(str(args.eventid))
	msgFinal = ' Por favor, verifique em: http://life.ucontrol.net.br'
	msgText = msgCritical + msgLocation + msgFinal
	return(msgText)
#
with open("smsuserslife09.txt", "r") as smsLife:
#
			for numbers in smsLife:
				#Read the names of the SMS targets
				phoneNumber = (numbers.rstrip())
				if (str(args.eventid)) == ' Operando em Condicoes Normais!':
				#Preapare the sms text message
					msgText = NormalTextMsg()
				else:
					msgText = AlarmTextMsg()
				#Prepare the post payload
				jsonPayload = postPayload(phoneNumber,msgText)
				#Send SMS to each one on the list 
				sendSMS(jsonPayload)
				print(jsonPayload)
				time.sleep(2)
print("Warning SMS Command Executed")
