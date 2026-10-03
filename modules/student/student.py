class StudentClass:

    def __init__(self):
        self.full_name = ""
        self.date_of_birth = ""
        self.age = None
        self.gender = ""
        self.mobile_number = ""
        self.email_address = ""
        self.email = ""
        self.password = ""
        self.preferred_language = ""
        self.school_college_name = ""
        self.class_grade = ""
        self.board_curriculum = ""
        self.academic_year = ""

        self.tuition_subjects = []
        self.subject_levels = {}
        self.topics_needing_help = []
        self.parent_guardian_name = ""
        self.parent_guardian_relationship = ""
        self.parent_guardian_mobile_number = ""
        self.parent_guardian_email_address = ""
        self.preferred_communication_method = ""

    def setPrimaryDetails(self, full_name, date_of_birth, age, gender, mobile_number, preferred_language, school_college_name, class_grade, board_curriculum, academic_year):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.age = age
        self.gender = gender
        self.mobile_number = mobile_number
        self.preferred_language = preferred_language
        self.school_college_name = school_college_name
        self.class_grade = class_grade
        self.board_curriculum = board_curriculum
        self.academic_year = academic_year

    def savePrimaryDetailsToDB(self):
         import sqlite3
         conn = sqlite3.connect("tution.db")

            # Create a cursor
         cursor = conn.cursor()

         # Insert primary details into the students table
         cursor.execute("""
         INSERT INTO students (full_name, date_of_birth, age, gender, mobile_number, preferred_language, school_college_name, class_grade, board_curriculum, academic_year)
         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
         """, (self.full_name, self.date_of_birth, self.age, self.gender, self.mobile_number, self.preferred_language, self.school_college_name, self.class_grade, self.board_curriculum, self.academic_year))

         # Save changes
         conn.commit()
         conn.close()  


    def saveAcademicDetailsToDB(self):
        import sqlite3

        # Create/connect to database
        conn = sqlite3.connect("tution.db")

        # Create a cursor
        cursor = conn.cursor()

        # Insert academic details into the students table
        cursor.execute("""
            UPDATE studentClass
            SET tuition_subjects = ?, subject_levels = ?, topics_needing_help = ?, preferred_communication_method = ?
            WHERE email_address = ?
        """, (str(self.tuition_subjects), str(self.subject_levels), str(self.topics_needing_help), self.preferred_communication_method, self.email_address))

        # Save changes
        conn.commit()

        # Close connection
        conn.close()    