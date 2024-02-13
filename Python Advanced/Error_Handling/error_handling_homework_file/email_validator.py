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


class InvalidEmailProviders(Exception):
    pass


class NameTooLong(Exception):
    pass


email = input()

VALID_DOMAINS = ("com", "bg")
VALID_EMAIL_PROVIDERS = ("gmail", "hotmail", "abv")
NAME_MIN_LENGTH = 4
NAME_MAX_LENGTH = 15
input_email_provider = email.split("@")[1].split(".")[0]
input_email_domain = email.split(".")[-1]

pattern = r"[a-z0-9]+"
while email != "End":
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @ symbol")
    elif email.count("@") > 1:
        raise MoreThanOneAtSymbol("Email cannot contain more than one @ symbol")
    elif len(email.split("@")[0]) <= NAME_MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")
    elif len(email.split("@")[0]) > NAME_MAX_LENGTH:
        raise NameTooLong("Name must be less or equal to 15 characters")
    elif email.split(".")[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(VALID_DOMAINS)}")
    elif re.findall(pattern, email.split("@")[0])[0] != email.split("@")[0]:
        raise InvalidNameError("Email must contains Latin lowercase letters and digits only")
    elif email.split("@")[1].split(".")[0] not in VALID_EMAIL_PROVIDERS:
        raise InvalidEmailProviders(f"Email provider must be one of the following :{', '.join(VALID_EMAIL_PROVIDERS)}")
    elif input_email_provider in VALID_EMAIL_PROVIDERS:
        if input_email_provider in VALID_EMAIL_PROVIDERS[:2] and input_email_domain != "com":
            raise InvalidDomainError(f"Domain must be '.com'")
        elif input_email_provider in VALID_EMAIL_PROVIDERS[2] and input_email_domain != "bg":
            raise InvalidDomainError(f"Domain must be '.bg'")

    print("Email is valid")

    email = input()
