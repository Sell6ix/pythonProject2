# - `load_candidates_from_json(path)` – возвращает список всех кандидатов
# - `get_candidate(candidate_id)` – возвращает одного кандидата по его id
# - `get_candidates_by_name(candidate_name)` – возвращает кандидатов по имени
# - `get_candidates_by_skill(skill_name)` – возвращает кандидатов по навыку

import json
from candidate import Candidate


def load_candidates_from_json(filename: str) -> list[Candidate]:
    '''возвращает список всех кандидатов'''
    arr = []
    data = None
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for item in data:
        id_=item['id']
        name = item['name']
        picture = item['picture']
        position = item['position']
        gender = item['gender']
        age = item['age']
        skills = item['skills']
        arr.append(Candidate(id_,name,picture,position,gender,age,skills))
    return arr




def get_candidate(candidate_id: int , arr: list[Candidate])-> Candidate:
    '''возвращает одного кандидата по его id'''
    for item in arr:
        if item.id == candidate_id:
            return item


def get_candidates_by_name(candidate_name: str, arr: list[Candidate])->  list[Candidate]:
    '''возвращает кандидатов по имени'''
    name_list=[]
    for item in arr:
        if item.pk == candidate_name:
            name_list.append(item)
    return name_list

def get_candidates_by_skill(skill_name: str, arr: list[Candidate])->  list[Candidate]:
    '''возвращает кандидатов по навыку'''
    skill_list = []
    for item in arr:
        if skill_name in item.skills:
            skill_list.append(item)
    return skill_list