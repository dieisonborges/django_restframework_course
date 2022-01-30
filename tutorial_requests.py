from email import header
import requests


#GET Avaliacoes

evaluations = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Status Code HTTP
print(evaluations.status_code)

# Acessando os dados da resposta
print(evaluations.json())
print(type(evaluations.json()))

# Acessando a quantidade de registros
print(evaluations.json()['count'])

# Acessando a próxima página de resultados
print(evaluations.json()['next'])
# Acessando os resultados desta página
print(evaluations.json()['results'])
print(type(evaluations.json()['results']))

# Acessando o primeiro elemento da lista
print(evaluations.json()['results'][0])
print(type(evaluations.json()['results'][0]))

# Acessando o último elemento da lista
print(evaluations.json()['results'][-1])
print(type(evaluations.json()['results'][-1]))

# Acessando o nome do último elemento da lista
print(evaluations.json()['results'][-1]['name'])
print(type(evaluations.json()['results'][-1]['name']))

#GET Avaliacao

evaluations = requests.get('http://localhost:8000/api/v2/avaliacoes/5')
print(evaluations.json())

#GET Curso
headers = {
    'Authorization': 'Token 9279b6d40f57f4517be3fe14569656d57ec88b2a'
}
course = requests.get(
    url='http://localhost:8000/api/v2/cursos/3',
    headers=headers
)

print(course.json())