from faker import Faker
import numpy as np
import pandas as pd


def fake_phone_number(fake1: Faker) -> str:
    return f'+91 {fake1.msisdn()[3:]}'


title = ['Material Manager', 'Sales Executive', 'Manufacturing', 'High Tech', 'Retail']

# Instantiate Faker with multiple locales
#fake = Faker(['en_US', 'de_DE', 'pt_BR', 'ja_JP', 'zh-CN'])
fake = Faker(['en_US'])


def create_data(x):
    # dictionary
    b_user = {}
    for i in range(0, x):
        em = fake.email()
        cntry = fake.country()
        fn = fake.first_name()
        mn = fake.first_name()
        ln = fake.last_name()
        email = ln[1] + fn.lower() + "@" + em.split("@", 1)[1]
        phn = fake_phone_number(fake)
        addr = fake.street_address()
        cty = fake.city()
        st = fake.state()
        zipc = str(fake.zipcode())
        cntry = fake.country()
        postalad = addr + ", " + cty + ", " + st + ", " + cntry + ", " + zipc
        b_user[i] = {}
        b_user[i]['login'] = email
        b_user[i]['firstName'] = fn
        b_user[i]['middleName'] = mn
        b_user[i]['lastName'] = ln
        b_user[i]['email'] = email
        b_user[i]['title'] = fake.random_element(title)
        b_user[i]['mobilePhone'] = phn
        b_user[i]['primaryPhone'] = phn
        b_user[i]['streetAddress'] = addr
        b_user[i]['city'] = cty
        b_user[i]['state'] = st
        b_user[i]['zipCode'] = zipc
        b_user[i]['countryCode'] = cntry
        b_user[i]['postalAddress'] = postalad

    return b_user


df = pd.DataFrame(create_data(1000)).transpose()
df.head(10)
print(df)
