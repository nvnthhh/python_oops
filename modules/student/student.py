class StudentClass:
    def __init__(
        self,
        full_name=None,
        date_of_birth=None,
        age=None,
        gender=None,
        mobile_number=None,
        email_address=None,
        password=None,
        preferred_language=None,
        school_college_name=None,
        class_grade=None,
        board_curriculum=None,
        academic_year=None,
        tuition_subjects=None,
        subject_levels=None,
        topics_needing_help=None,
        parent_guardian_name=None,
        parent_guardian_relationship=None,
        parent_guardian_mobile_number=None,
        parent_guardian_email_address=None,
        preferred_communication_method=None,
    ):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.age = age
        self.gender = gender
        self.mobile_number = mobile_number
        self.email_address = email_address
        self.password = password
        self.preferred_language = preferred_language
        self.school_college_name = school_college_name
        self.class_grade = class_grade
        self.board_curriculum = board_curriculum
        self.academic_year = academic_year
        self.tuition_subjects = tuition_subjects if tuition_subjects is not None else []
        self.subject_levels = subject_levels if subject_levels is not None else {}
        self.topics_needing_help = topics_needing_help if topics_needing_help is not None else []
        self.parent_guardian_name = parent_guardian_name
        self.parent_guardian_relationship = parent_guardian_relationship
        self.parent_guardian_mobile_number = parent_guardian_mobile_number
        self.parent_guardian_email_address = parent_guardian_email_address
        self.preferred_communication_method = preferred_communication_method

    def setUserNameAndPassword(self, email, password):
        self.email_address = email
        self.password = password

    def set_username_and_password(self, email, password):
        self.setUserNameAndPassword(email, password)

    def set_user_name_and_password(self, email, password):
        self.setUserNameAndPassword(email, password)


Studentclass = StudentClass