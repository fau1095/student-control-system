class Student:
    def __init__(self, name: str, section: str, spanish: float, english: float, social: float, science: float):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social = social
        self.science = science
        self.average = (spanish + english + social + science) / 4

    def to_dict(self):
        return {
            "name": self.name,
            "section": self.section,
            "spanish": self.spanish,
            "english": self.english,
            "social": self.social,
            "science": self.science,
            "average": self.average
        }