from enum import Enum


class Genders(Enum):
    female = "female"
    male = "male"

class Statuses(Enum):
    inactive = "inactive"
    active = "active"
    ACTIVE = "ACTIVE"
    BANNED = "BANNED"
    DELETED = "DELETED"
    INACTIVE = "INACTIVE"

class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn`t contain @"
