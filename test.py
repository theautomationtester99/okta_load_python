from faker import Faker
import indian_names
import math
import random

#
# def fake_phone_number(fake1: Faker) -> str:
#     return f'+91 {fake1.msisdn()[3:]}'
#
#
# fake = Faker('hi_IN')
# # print(fake.phone_number())
# em = fake.email()
# cntry = fake.country()
# fn = fake.first_name()
# # fn = indian_names.get_first_name(gender='female')
# # mn = fake.first_name()
# mn = ""
# ln = fake.last_name()
# # ln = indian_names.get_last_name()
# #email = ln[1] + fn.lower() + "@" + em.split("@", 1)[1]
# email = em
# phn = fake_phone_number(fake)
# addr = fake.street_address()
# cty = fake.city()
# st = fake.state()
# zipc = str(fake.postcode())
# cntry = fake.current_country()
# postalad = addr + ", " + cty + ", " + st + ", " + cntry + ", "  + zipc
# print(email)
# print(phn)
# print(postalad)

# from datetime import datetime
#
# now = datetime.now() # current date and time
#
# date_time = now.strftime("%m_%d_%Y_%H_%M_%S")
# print("date and time:",date_time)


def gen_rand_numb_str(numb_digits):
    digits = [i for i in range(0, 10)]

    # initializing a string
    random_str = ""

    # we can generate any length of string we want
    for j in range(numb_digits):
        # generating a random index
        # if we multiply with 10 it will generate a number between 0 and 10 not including 10
        # multiply the random.random() with length of your base list or str
        index = math.floor(random.random() * 10)

        random_str += str(digits[index])

    return random_str

a = gen_rand_numb_str(5)
print(a)
