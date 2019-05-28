import requests
import json

r=requests.get("http://127.0.0.1:8000/api/encuestas/")

print (r.text)


url = 'https://onesignal.com/api/v1/notifications'
payload = {
        "app_id": "0a094478-26f7-4064-8d31-1c4a23e16402",
        "included_segments": ["Active Users", "Inactive Users"],        
        "contents": { "en": "INGLEEE", "es": "Por favor, contesta las preguntas recibidas"},
        "headings": { "en": " TITULO INGLEEE", "es": "CONSULTA SI TIENES ENCUESTAS NUEVAS"}
        }

headers = {'content-type': 'application/json',
            'Authorization': 'Basic MWU2YTdkZmUtMmJhMy00YjAxLThhMjYtYzlkY2JhMjFjYTVm'}

post = requests.post(url, data=json.dumps(payload), headers=headers)


print (post)

print ("ey")

print(payload)

print ("ey")

print(json.dumps(payload))