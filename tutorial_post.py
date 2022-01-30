import requests

headers = {'Authorization': 'Token 9279b6d40f57f4517be3fe14569656d57ec88b2a'}

url_base_courses = "http://localhost:8000/api/v2/cursos/"

url_base_evaluations = "http://localhost:8000/api/v2/avaliacoes/"

new_course = {
    "title": "Evolução dos Animais da Extratosfera",
    "url": "https://www.wwf.org.br/natureza_brasileira/questoes_ambientais/camada_ozonio/"
}

results = requests.post(url=url_base_courses, headers=headers, data=new_course)

print("\n\n")
print(results)
print("\n\n")



# Testar Status Code
assert results.status_code == 201

# Testando se o título do curso retorna o memso informado
assert results.json()['title'] == new_course['title']