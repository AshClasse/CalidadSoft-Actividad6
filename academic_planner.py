class Subject:
    def __init__(self, name, credits, prerequisites=None):
        self.name = name
        self.credits = credits
        self.prerequisites = prerequisites or []


class Student:
    def __init__(self):
        self.approved_subjects = []
        self.current_subjects = []

    def approve_subject(self, subject_name):
        self.approved_subjects.append(subject_name)

    def can_register(self, subject):
        for prereq in subject.prerequisites:
            if prereq not in self.approved_subjects:
                return False
        return True

    def register_subject(self, subject):
        if not self.can_register(subject):
            raise Exception("Prerrequisitos no cumplidos")
        self.current_subjects.append(subject.name)


def simulate_semester(subjects, max_credits):
    total_credits = 0
    semester = []

    for subject in subjects:
        if total_credits + subject.credits <= max_credits:
            semester.append(subject.name)
            total_credits += subject.credits

    return semester
