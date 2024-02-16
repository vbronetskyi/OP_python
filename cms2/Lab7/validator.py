"""Lab_7.2_Validator"""
import re

class Validator:
    """class Validator"""
    def validate_name_surname(self, name_surname: str):
        """
        validate_name_surname
        """
        return len([word for word in re.split(' ', name_surname)\
            if re.search('^[A-Z][a-z]{2,30}$', word)\
            and len(re.split(' ', name_surname))==2]) == 2
    def validate_age(self, age: str):
        """validate_age"""
        if re.match('^[0-9][0-9]$', age) and int(age)>=16:
            return True
        else: return False
    def validate_country(self, country: str):
        """validate_country"""
        if re.search('^[A-Z]([a-z]|[A-Z]){1,9}$', country):
            return True
        else: return False
    def validate_region(self, region: str):
        """validate_region"""
        if re.search('^[A-Z]([a-z]|[A-Z]){1,9}[0-9]?$', region):
            return True
        else: return False
    def validate_living_place(self, living_place: str):
        """validate_living_place"""
        if re.search('^[A-Z][a-z]{2,29} (st|av|prosp|rd). [0-9]([0-9]|[a-z])$', living_place):
            return True
        else: return False
    def validate_index(self, index: str):
        """validate_index"""
        if re.match('^[0-9]{5}$', index):
            return True
        else: return False
    def validate_phone(self, phone: str):
        """
        valid phone - in format "+380951234567" or "+38 (095) 123-45-67"
        """
        if re.match('^\+[0-9]{2} ?\(?[0-9]{3}\)? ?[0-9]{3}-?[0-9][0-9]?-?[0-9]{2}?$', phone):
            return True
        else: return False
    def validate_email(self, email: str):
        """validate_email"""
        regex = r'^[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]{1,64}@[a-z\.]{1,255}\.(com|org|edu|gov|net|ua)$'
        return re.match(regex, email) is not None
    def validate_id(self, id_user: str):
        """validate_id"""
        return re.match(r'^[1-9]*0[1-9]*$', id_user) is not None and len(id_user)==6
    def validate(self, data: str):
        """validate"""
        tests = re.split('; |, |;|,', data)
        return self.validate_name_surname(tests[0]) and self.validate_age(tests[1])\
            and self.validate_country(tests[2]) and self.validate_region(tests[3])\
            and self.validate_living_place(tests[4]) and self.validate_index(tests[5])\
            and self.validate_phone(tests[6]) and self.validate_email(tests[7])\
            and self.validate_id(tests[8])
