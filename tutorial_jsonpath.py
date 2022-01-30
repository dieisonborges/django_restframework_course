import requests
import jsonpath



evaluations = requests.get('http://localhost:8000/api/v2/avaliacoes/')
print(evaluations)
print("\n\n")

# Todas as Avaliações com dict
resultss = jsonpath.jsonpath(evaluations.json(), 'results')
print(resultss)
print("\n\n")

# Nomes de todas pessoas que avaliaram
all_names = jsonpath.jsonpath(evaluations.json(), 'results[*].name')
print(all_names)
print("\n\n")