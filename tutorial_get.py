from unittest import result
import requests


headers = {
    'Authorization': 'Token 9279b6d40f57f4517be3fe14569656d57ec88b2a'
}

url_base_courses = "http://localhost:8000/api/v2/cursos"

url_base_evaluations = "http://localhost:8000/api/v2/avaliacoes"

results = requests.get(
    url=url_base_courses,
    headers=headers
)

# Testando se o endpoint está correto
assert results.status_code == 200

# Testando a quantidade de registros
# assert results.json()['count'] == 2

#Testando o titulo do curso
# assert results.json()['titulo'] == "Geografia Maricana"