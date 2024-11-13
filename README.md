# Certificate of Achievements Generator
#### Video Demo:  <[URL HERE](https://youtu.be/Bzaz2EoZMIo?si=qkNjclzVC5IGGbDY)>
#### Description:
the main purpose of this program is creating in an dynamic way recognitions PDF files to students who are recognized by a reached goal or when this person completed differets task in an institution or company.

The main idea was to create the files by entering a csv file, however it was too easy, so I concluded that I could add the certificate information one by one via command

The pdf file is created with the fpdf2 library that we saw in task set 8, also use the massive loading of information through the csv library that was mainly dealt with in the "File I/O" class.

Without leaving behind for a better defensive code I used the object-oriented paradigm to create the "Award" class that contains the different attributes of the certificate file.

you can run this project with

```
python project.py
```
that command allow create a certificate-student only

but you have the another alternative:

```
python project.py -f [file path]
```

## Input project (Attributes of an certificate achievement)

> First name of student or employed

> last name of student or employed

> professor's first name

> professor's last name

> institution file path

> professor's signature file path

> certificate date

## Output project
The name of the final document will be the name of the person who owns the certificate, for example:
> Carlos_mata.pdf

## Required external libraries

### art
The [ART](https://pypi.org/project/art/) library is also used to title the progress of income from student or employee data.

### fpdf2
this is a PDF creation library for python, the used version for this project is: 2.7.9




## The different functions of the project are described below:
### get_award_from_dict
This function is to be able to build the different certified awards that come from some csv file, what this function does is iterate each of the columns and rows of the document to build the different awards.

### validate_date
The sole purpose of this function is to verify if the date was entered and to verify if it has not been entered, to set the program execution date by default.

### generate_person
As the name of the function says, the purpose of this function is to generate "Person" type instances for either the student or employee or the teacher who share different attributes such as first name and last name.

### get_file_name
The purpose of this function is to verify if the user has entered the -f parameter in his invocation to the project. If true, it will return the file path that is allowed to be entered to use the alternative for generating certificates with csv.

### generate_awards
The objective of this function is to generate files in PDF format according to the instances of the "Award" class generated with the previous functions already mentioned. A blue background has been chosen by default, but everything else can be generated dynamically according to the attributes entered by the user.

## Testing
As has been seen in the classes of this course, pytest was used to carry out the different unit tests for each of the aforementioned functions.
```
pytest test_project.py
```

>>> greetings to the cs50 team mainly to Professor David J. Malan