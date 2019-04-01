#!/usr/bin/env python
# coding: utf-8
import requests
import sys
 
id = "854666549"
 
token = "707039446:AAF3SjOcxUMklriKuiOpZCpwPMSgNtMnxgs"
 
url = "https://api.telegram.org/bot" + token + "/sendMessage"
#
params = {
'chat_id': id,
 
'text' : 'La ejecucion termino \nSe obtuvo la siguente grafica'
}
requests.post(url, params=params)


files = {
'document': open('datos.txt','rb')
}
params = {
'chat_id': id
}
 
requests.post(url, params=params, files=files)
