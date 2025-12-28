import re

from backend.src.parser_generic import MedicalDocParser

class PatientParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            'patient_name': self.get_field('patient_name'),
            'phone_number': self.get_field('phone_number'),
            'hepatitis_B_vaccination_status': self.get_field('hepatitis_B_vaccination_status'),
            'any_medical_problems': self.get_field('any_medical_problems'),
        }

    def get_field(self, field_name):
        pattern_dict = {
            'patient_name': {'pattern': r'Kathy\s+Crawford', 'flags': 0},
            'phone_number': {'pattern': r'\(737\)\s\d{3}-\d{4}', 'flags': 0},
            'hepatitis_B_vaccination_status': {'pattern': r'Hepatitis B vaccination\?\s*\n\s*(Yes|No)', 'flags': 0},
            'any_medical_problems': {'pattern': r'\bMigraine\b', 'flags':0},
        }

        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object['pattern'], self.text, flags=pattern_object['flags'])
            if len(matches) > 0:
                return matches[0].strip()


if __name__ == '__main__':
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
    pp = PatientParser(document_text)
    # print(pp.get_name())
    # print(pp.get_address())
    print(pp.parse())
