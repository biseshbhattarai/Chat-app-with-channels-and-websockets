from django.test import TestCase, Client


c = Client()
response = c.post('/', {'username':'''your username''', 'password': '''your password'''})
print(response.status_code)
response = c.get('/chat')
if response.status_code != 404: 
    print(response.content)
response = c.get('/')
print(response.status_code)
print(response.content)


