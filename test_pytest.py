import pytest
import requests
import random

"""
To run testes execute:
python3 -m pytest test_pytest.py
"""

class TestCourse:
    """
    Endpoint Test
    """
    headers = {'Authorization': 'Token 9279b6d40f57f4517be3fe14569656d57ec88b2a'}
    url_base_courses = "http://localhost:8000/api/v2/cursos/"   

    def test_get_courses(self):
        courses = requests.get(url=self.url_base_courses, headers=self.headers)

        assert courses.status_code == 200


    def test_get_course(self):
        id_course = 5
        course = requests.get(url=f'{self.url_base_courses}{id_course}/', headers=self.headers)

        assert course.status_code == 200

    def test_post_course(self):
        rand_num_test = random.randint(0, 50)
        new_course = {
            "title": "Curso de Programação Ruby",
            "url": f"http://www.google.com.br/rub{rand_num_test}y{rand_num_test}"
        }

        results = requests.post(url=self.url_base_courses, headers=self.headers, data=new_course)

        assert results.status_code == 201
        assert results.json()['title'] == new_course['title']

  
    def test_put_course(self):
        rand_num_test = random.randint(0, 50)
        id_course = 10
        update_course = {
            "title": "Novo Curso de Programação Ruby",
            "url": f'http://www.google.com.br/rubys{rand_num_test}{rand_num_test}{rand_num_test}'
        }

        results = requests.put(url=f'{self.url_base_courses}{id_course}/', headers=self.headers, data=update_course)

        assert results.status_code == 200
    
    def test_put_title_course(self):
        rand_num_test = random.randint(0, 50)
        id_course = 10
        update_course = {
            "title": 'Novo New Novo Curso de Programação Ruby',
            "url": f'http://www.google.com.br/rubys{rand_num_test}ok{rand_num_test}'
        }

        results = requests.put(url=f'{self.url_base_courses}{id_course}/', headers=self.headers, data=update_course)

        assert results.json()['title'] == update_course['title']

    def test_delete_course(self):

        courses = requests.get(url=self.url_base_courses, headers=self.headers)

        id_course = courses.json()['results'][-1]['id']

        results = requests.delete(url=f'{self.url_base_courses}{id_course}/', headers=self.headers)    

        assert results.status_code == 204 and len(results.text) == 0
