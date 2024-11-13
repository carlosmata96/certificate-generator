import csv
import argparse
from fpdf import FPDF, enums
from datetime import datetime
from art import text2art
import os.path

def main():
    file_name = get_file_name()
    list_awards = []
    if file_name:
        with open(file_name) as file:
            reader = csv.DictReader(file)
            for row in reader:
                award = get_award_from_dict(**row)
                if award:
                    list_awards.append(award)
    else:
        print(text2art('=====Generator of Certificates===',font="small"))
        print(text2art('=====Student info==='))
        while True:
            first_name_student = input("What is the first name of the student? ")
            last_name_student = input("What is the last name if the student? ")
            try:
                student = generate_person(first_name_student, last_name_student)
                break
            except ValueError as e:
                print(e)
        print(text2art('=====Professor info==='))
        while True:
            first_name_professor = input("What is the first name of the professor? ")
            last_name_professor = input("What is the last name of the professor? ")
            try:
                professor = generate_person(first_name_professor, last_name_professor)
                break
            except ValueError as e:
                print(e)
        print(text2art('=====Award info==='))
        while True:
            try:
                award = Award(student, professor)
                break
            except ValueError as e:
                print(e)
            except FileNotFoundError as e:
                print(e)
        while True:
            try:
                date_aux = input("What is the date of the award? (format: Y-m-d default NOW): ")
                award.date = validate_date(date_aux)
                break
            except ValueError as e:
                print(e)
            except FileNotFoundError as e:
                print(e)
        while True:
            try:
                award.institution = input("Add the file name of the institution logo: ")
                break
            except ValueError as e:
                print(e)
            except FileNotFoundError as e:
                print(e)
        while True:
            try:
                award.signature = input("add the file name of the signature professor: ")
                break
            except ValueError as e:
                print(e)
            except FileNotFoundError as e:
                print(e)
        while True:
            try:
                award.congrats = input("add the congrats to the student: ")
                break
            except ValueError as e:
                print(e)
            except FileNotFoundError as e:
                print(e)
        list_awards.append(award)
    generate_awards(list_awards)

def get_award_from_dict(**kwargs):
    """
    Generate an award from a dict

    :param kwargs: parameters neccesaries to create an award
    :type  kwargs: dict
    :return: an award object builded from the parameters send
    :rtype: Award
    """
    try:
        student = generate_person(kwargs['first_name_student'],kwargs['last_name_student'])
        professor = generate_person(kwargs['first_name_professor'],kwargs['last_name_professor'])
        award = Award(student, professor)
        award.date = kwargs['date']
        award.institution = kwargs['institution']
        award.signature = kwargs['signature']
        award.congrats = kwargs['congrats']
    except ValueError:
        return None
    except FileNotFoundError:
        return None
    return award

def validate_date(date_aux):
    """
    validate the string typed per the user, in case want the default option now
    """
    return date_aux if date_aux else datetime.today().strftime('%Y-%m-%d')

def generate_person(first_name:str, last_name:str):
    """
    Generate a person from the parameters neccesaries

    :first_name: first name of the person
    :last_name: last name of the person
    :return: return a person builder
    :rtype: Person
    """
    return Person(first_name, last_name)

def get_file_name():
    """
    Detect if the award will create with command via

    :return: the file name path of csv file in case the user added
    :rtype: str,None
    """
    parser = argparse.ArgumentParser(prog="Award Generator",description="help to generate an award")
    parser.add_argument("-f", "--file", help="define the file origen of data")
    return parser.parse_args().file

def generate_awards(list_awards):
    """
    Generate the Awards neccesaries from a list of Instancies of Awards

    :list_awards: list of instancies of awards
    :type: list
    :rtype: boolean
    """
    for n,award in enumerate(list_awards):
        pdf = FPDF(orientation='landscape')
        pdf.allow_images_transparency = True
        pdf.set_page_background('base/backgroud.png')
        pdf.add_page()
        pdf.set_margins(5,20,5)
        pdf.image(award.institution, x=238, y=5, w=50, h=50)
        pdf.set_font('helvetica', size=16)
        pdf.cell( text=f"This certificate is awarded to ", center=True)
        pdf.ln(25)
        pdf.set_font_size(25)
        pdf.set_font(family='Courier', style='B')
        pdf.cell( text=f"{award.student}", center=True)
        pdf.set_font_size(20)
        pdf.set_font(family='Courier', style='')
        pdf.ln(30)
        pdf.multi_cell(text=f"{award.congrats}", w=250, h=20, align=enums.Align.J, center=True)
        pdf.set_font_size(15)
        pdf.cell(text=f"On {award.date.strftime('%d, %b %Y')}", center=True)
        pdf.image(award.signature, x=130, y=150, w=50, h=25)
        pdf.line(x1=125, y1=175, x2=175, y2=175)
        pdf.text(x=125, y=180, text=f"Prof. {award.professor}")
        pdf.set_font_size(15)
        pdf.set_text_color(0,0,0)
        name_file = f"{str(award.student).replace(' ','_')}.pdf"
        pdf.output(name_file)
        print(name_file, '..created..')
    return True

class Person:
    def __init__(self, first_name:str, last_name:str):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @first_name.setter
    def first_name(self, first_name):
        if not first_name:
            raise ValueError("First name is required")
        self._first_name = first_name

    @last_name.setter
    def last_name(self, last_name):
        if not last_name:
            raise ValueError("Last name is required")
        self._last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other):
        return self.first_name==other.first_name and self.last_name==other.last_name

class Award:
    def __init__(self, student, professor):
        self.student = student
        self.professor = professor
    @property
    def student(self):
        return self._student

    @property
    def professor(self):
        return self._professor

    @property
    def date(self):
        return self._date

    @property
    def institution(self):
        return self._institution

    @property
    def congrats(self):
        return self._congrats

    @property
    def signature(self):
        return self._signature

    @student.setter
    def student(self, student:Person):
        self._student = student

    @professor.setter
    def professor(self, professor: Person):
        self._professor = professor

    @date.setter
    def date(self, date):
        if not date:
            raise ValueError("Date is required")
        try:
            d = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError('Date format invalid')
        self._date = d

    @institution.setter
    def institution(self, institution):
        if not institution:
            raise ValueError("Institution logo file name is required")
        if os.path.exists(institution):
            self._institution = institution
        else:
            raise FileNotFoundError("File not found, try again")

    @signature.setter
    def signature(self, signature):
        if not signature:
            raise ValueError("Signature logo file name is required")
        if os.path.exists(signature):
            self._signature = signature
        else:
            raise FileNotFoundError("File not found, try again")
    @congrats.setter
    def congrats(self, congrats):
        if not congrats:
            raise ValueError("Congrats is required")
        self._congrats = congrats

    def __eq__(self, other):
        return self.student==other.student and self.professor==other.professor and self.date==other.date and self.institution==other.institution and self.signature==other.signature and self.congrats==other.congrats

if __name__ == "__main__":
    main()
