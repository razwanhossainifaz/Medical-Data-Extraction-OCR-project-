import re

from lark.tools import flags

from backend.src.parser_generic import MedicalDocParser


class PatientDetailsParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            'patient_name' : self.get_patient_name(),
            'phone_number' : self.get_patient_phone_number(),
            'medical_problems' : self.get_medical_problems(),
            'hepatitis_b_vaccination' : self.get_hepatitis_b_vaccination()
        }

    def get_patient_name(self):
        pattern = r'Patient Information(.*?)\(\d{3}\)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        name = ''
        if matches:
            name = self.remove_noise_from_name(matches[0])
        return name

    def get_patient_phone_number(self):
        pattern = r'Patient Information(.*?)(\(\d{3}\) \d{3}-\d{4})'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0][-1]

    def get_hepatitis_b_vaccination(self):
        pattern = r'Have you had the Hepatitis B vaccination\?.*(Yes|No)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0].strip()

    def get_medical_problems(self):
        # pattern = r'List any Medical Problems \(asthma, seizures, headaches\)\:(.*)' - written by instructor
        pattern = r"List any Medical Problems \(asthma, seizures, headaches\)\:\s*([^\n\r]+)" # this regex correction done by me by helping AI, reason without this running extract file for patient did not work
        matches = re.findall(pattern, self.text , flags=re.DOTALL|re.IGNORECASE)
        if matches:
            return matches[0].strip()


    def remove_noise_from_name(self, name):
        name = name.replace('Birth Date', '').strip()
        date_pattern = r'((Jan|Feb|March|April|May|June|July|Aug|Sep|Oct|Nov|Dec)[ \d]+)'
        date_matches = re.findall(date_pattern, name)

        if date_matches:
            date = date_matches[0][0]
            name = name.replace(date, '').strip()

        return name


if __name__ == '__main__':
        document_text = '''
        17/12/2020

        Patient Medical Record

        Patient Information Birth Date
        Jerry Lucas May 2 1998
        (279) 920-8204 Weight:
        4218 Wheeler Ridge Dr 57

        Buffalo, New York, 14201

        United States Height:

        170

        In Case of Emergency
        ee

        Joe Lucas 4218 Wheeler Ridge Dr
        Buffalo, New York, 14201
        Home phone . United States
        Work phone

        General Medical History

        Chicken Pox (Varicelia): Measles:

        IMMUNE NOT IMMUNE

        Have you had the Hepatitis B vaccination?

        “Yes

        List any Medical Problems (asthma, seizures, headaches):
        N/A
        '''

        document_text_2 = '''
        17112/2020

        Patient Medical Record
        
        Patient Information Birth Date
        Kathy Crawford May 6 1972
        (737) 988-0851 Weight
        9264 Ash Dr 95
        New York City, 10005
        United States Height:
        190
        In Casc of Emergency
        ce a  E ee
        Simeone Crawford 9266 Ash Dr
        New York City, New York, 10005
        
        Home phone United States
        
        (990) 375-4621
        Work phone
        
        Genera! Medical History
        
        cree ete amegras mater
        
        ee
        
        Chicken Pox (Varicella): Meacies:
        
        IMMUNE IMMUNE
        
        Have you had the Hepatitis B vaccination?
        
        No
        List any Medical Problems (asthma, seizures, headaches):
        Migraine
        '''

        pp = PatientDetailsParser(document_text)
        print(pp.parse())

        pp = PatientDetailsParser(document_text_2)
        print(pp.parse())