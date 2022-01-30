import requests

headers = {'Authorization': 'Token 9279b6d40f57f4517be3fe14569656d57ec88b2a'}

url_base_courses = "http://localhost:8000/api/v2/cursos/"

url_base_evaluations = "http://localhost:8000/api/v2/avaliacoes/"

id_course = 4

results = requests.delete(url=f'{url_base_courses}{id_course}/', headers=headers)


# Testar Status Code
assert results.status_code == 204

# Testando se o tamamnho do conteudo retornado é Null / 0
assert len(results.text) == 0

