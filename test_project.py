import pytest
import sys
from datetime import datetime
from project import generate_person, get_file_name, get_award_from_dict, generate_awards, validate_date, Person, Award

def test_get_award_from_dict():
    dict = {
        'first_name_student': 'Julio',
        'last_name_student': 'Matamoros',
        'first_name_professor': 'Edward',
        'last_name_professor': 'Meza',
        'date': '2024-05-23',
        'institution': 'base/company_slogan.png',
        'signature': 'base/signature.png',
        'congrats': 'Your ability to inspire, motivate, and guide others has made a significant impact, and we are proud to recognize your achievements.'
    }
    student = Person(dict['first_name_student'],dict['last_name_student'])
    professor = Person(dict['first_name_professor'],dict['last_name_professor'])
    award = Award(student, professor)
    award.date = dict['date']
    award.institution = dict['institution']
    award.signature = dict['signature']
    award.congrats = dict['congrats']
    assert get_award_from_dict(**dict) == award


def test_validate_date():
    assert validate_date('')==datetime.today().strftime('%Y-%m-%d')

def test_generate_person():
    with pytest.raises(ValueError):
        generate_person('Carlos','')

def test_get_file_name(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['project.py', '-f', 'students.csv'])
    assert get_file_name() == 'students.csv'

def test_generate_awards():
    dict = {
        'first_name_student': 'Fatima',
        'last_name_student': 'Mata',
        'first_name_professor': 'Edward',
        'last_name_professor': 'Meza',
        'date': '2024-05-23',
        'institution': 'base/company_slogan.png',
        'signature': 'base/signature.png',
        'congrats': 'Your ability to inspire, motivate, and guide others has made a significant impact, and we are proud to recognize your achievements.'
    }
    student = Person(dict['first_name_student'],dict['last_name_student'])
    professor = Person(dict['first_name_professor'],dict['last_name_professor'])
    award = Award(student, professor)
    award.date = dict['date']
    award.institution = dict['institution']
    award.signature = dict['signature']
    award.congrats = dict['congrats']
    assert generate_awards([award])

