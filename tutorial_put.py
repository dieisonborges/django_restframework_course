import requests

headers = {'Authorization': 'Token 9279b6d40f57f4517be3fe14569656d57ec88b2a'}

url_base_courses = "http://localhost:8000/api/v2/cursos/"

url_base_evaluations = "http://localhost:8000/api/v2/avaliacoes/"

update_course = {
    "title": "Evolução dos Animais da Extratosfera Netuniana",
    "url": "https://www.tripadvisor.com.br/Attraction_Review-g304027-d21292844-Reviews-Asdasd-Qaanaaq_Qaasuitsup_Municipality.html"
}

id_course = 4

results = requests.put(url=f'{url_base_courses}{id_course}/', headers=headers, data=update_course)

print("\n\n")
print(results.__dict__)
print("\n\n")
print(results.status_code)
print("\n\n")



# Testar Status Code
assert results.status_code == 200

# Testando se o título do curso retorna o memso informado
assert results.json()['title'] == update_course['title']
