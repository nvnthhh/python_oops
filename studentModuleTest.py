# this python file is to test all functionality of the student class
# we are using this module for login/registration

from modules.student.student import StudentClass

# step 1: student registration test

email = input("enter your EMAIL: ")
password = input("enter your password: ")

s1 = StudentClass(email_address=email, password=password)
print("Student registered successfully.")

full_name=input("enter your name: ")
dob=input("enter your date of birth: ")
gender=input("enter your gender: ")
mobile_number=input("enter your mobile number: ")

preferred_language=input("enter your preferred language: ")
school_college_name=input("enter your school/college name: ")
board_curriculum=input("enter your board/curriculum: ")
academic_year=input("enter your academic year: ")