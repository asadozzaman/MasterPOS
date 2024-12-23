import random
import string


# def unique_code(n: int) -> int:
#     '''
#     ♻Reuseable function that generate random unique code based on input value.
#     param: n (int)
#         n: number of characters in the code
#     return:
#         code: unique code based on input value
#     '''
#     allowed_digits = ''.join((string.digits))
#     unique_code = ''.join(random.choice(allowed_digits) for _ in range(n))
#     return unique_code


import uuid

def unique_code(length):
    unique_id = str(uuid.uuid4()).replace('-', '')[:length]
    return unique_id