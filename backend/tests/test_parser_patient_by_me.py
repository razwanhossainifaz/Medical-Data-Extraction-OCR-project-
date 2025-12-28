from backend.src.parser_patient_by_me import PatientParser
import pytest

@pytest.fixture()
def doc_text():
    document_text = '''
    Patient Medical Record

    Patient Information
    Kathy Crawford

    (737) 988-0851

    9264 Ash DOr
    New York City, 10005
    United States

    In Casc of Emergency

    Simeone Crawford

    Home phone
    (990) 375-4621

    Genera! Medical History

    i

    Chicken Pox (Varicella):

    IMMUNE
    Have you had the Hepatitis B vaccination?

    No

    List any Medical P
    Migraine

    — Tae

    VINUZO2

    Birth Date
    Moy 6 1972

    Wright
    95

    Height:
    190

    9266 Ash Or
    New York City, New York, 10005

    United States

    Work phone

    a

    Meacitst

    IMMUNE

    roblems (asthma, seizures, headaches}:
    '''

    return PatientParser(document_text)

def test_get_name(doc_text):
    assert doc_text.get_field('patient_name') == 'Kathy Crawford'

def test_get_number(doc_text):
    assert doc_text.get_field('phone_number') == '(737) 988-0851'

def test_get_status(doc_text):
    assert doc_text.get_field('hepatitis_B_vaccination_status') == 'No'

def test_get_any_problem(doc_text):
    assert doc_text.get_field('any_medical_problems') == 'Migraine'
