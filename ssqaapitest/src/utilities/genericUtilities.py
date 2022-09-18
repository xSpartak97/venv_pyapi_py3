import logging as logger
import random
import string


def generate_random_email_and_password(domain=None, email_prefix=None):
    logger.debug("Generating random email and password.")

    if not domain:
        domain = 'vilmate.com'

    if not email_prefix:
        email_prefix = 'testuser'

    random_email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))

    email = email_prefix + '_' + random_string + '@' + domain

    password_length = 10
    password_string = ''.join(random.choices(string.ascii_letters, k=password_length))

    random_info = {'email': email, 'password': password_string}
    logger.debug(f"Randomly generated email and password: {random_info}")

    return random_info


def generate_random_name_product(length=7, prefix=None, suffix=None):
    logger.debug("Generating random product")

    product_name = ''.join(random.choices(string.ascii_uppercase, k=length))

    if prefix:
        product_name = prefix + product_name

    if suffix:
        product_name = prefix + product_name

    return product_name


def generate_random_price():
    n = [str(i) for i in range(1, 101)]
    n1 = [random.choice(n), random.choice(n)]
    return '.'.join(n1)


def random_code_coupon(length=5):

    code_coupon = ''.join(random.choices(string.ascii_lowercase, k=length))

    return code_coupon



