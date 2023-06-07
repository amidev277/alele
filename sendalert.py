
import requests

# Pegar a informação

requisicao=requests.get("https://economia.awesomeapi.com.br/last/EUR-USD")
requisicao_dic=requisicao.json()
cotacao=float(requisicao_dic['EURUSD']['bid'])
print(cotacao)

import smtplib
import email.message

def enviar_email(cotacao):  
    corpo_email = f"""
    <p>Dólar está a baixo de 5.10. Cotação atual: R${cotacao}</p>
   
    """

    msg = email.message.Message()
    msg['Subject'] = "Atualização do dólar"
    msg['From'] = 'alisboagamer7@gmail.com'
    msg['To'] = 'alisboagamer7@gmail.com'
    password = 'jfqtkdryqgvdghih' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

if cotacao < 5.10:
    enviar_email(cotacao)

# Deploy com heroku    
