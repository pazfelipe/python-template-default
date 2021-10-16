import re


class Validator:
    def __init__(self):
        self.__errors = []

    def isRequired(self, field, msg):
        print(msg)
        if not field:
            self.__errors.append(msg)

    def isValid(self):
        return len(self.__errors) == 0

    def isEmail(self, email, msg):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(regex, email):
            self.__errors.append(msg)

    def errors(self):
        return self.__errors
