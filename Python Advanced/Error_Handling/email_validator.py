import re

class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbol(Exception):
    pass


class InvalidNameError(Exception):
    pass


VALID_DOMAINS = ("com", "bg", "org", "net")
NAME_MIN_LENGTH = 4


email = input()
pattern = r"[a-z0-9]+"
while email != "End":
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @ symbol")
    elif email.count("@") > 1:
        raise MoreThanOneAtSymbol("Email cannot contain more than one @ symbol")
    elif len(email.split("@")[0]) <= NAME_MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")
    elif email.split(".")[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(VALID_DOMAINS)}")
    elif re.findall(pattern,email.split("@")[0])[0] != email.split("@")[0]:
        raise InvalidNameError("Email must contains lowercase letters and digits only")

    print("Email is valid")

    email = input()


