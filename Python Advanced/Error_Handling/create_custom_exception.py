class ValueTooSmallError(Exception):
    """raise a value if too small"""
    pass


num = int(input())
if num < 10:
    raise ValueTooSmallError("Number is below 10")
