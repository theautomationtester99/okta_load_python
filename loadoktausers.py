import json
import time
from typing import List

import indian_names
import pandas as pd
import requests
from faker import Faker
from jproperties import Properties
import warnings
from datetime import datetime
import random
import math

warnings.filterwarnings('ignore', message='Unverified HTTPS request')


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


def fake_phone_number(fake1: Faker, faker_locale1) -> str:
    if faker_locale1 == 'ja_JP':
        return f'+81 {fake1.msisdn()[3:]}'
    elif faker_locale1 == 'ko_KR':
        return f'+82 {fake1.msisdn()[3:]}'
    elif faker_locale1 == 'hi_IN' or faker_locale1 == 'or_IN' or faker_locale1 == 'ta_IN' or faker_locale1 == 'en_IN':
        return f'+91 {fake1.msisdn()[3:]}'
    elif faker_locale1 == 'fr_FR':
        return f'+33 {fake1.msisdn()[3:]}'
    elif faker_locale1 == 'ru_RU':
        return f'+7 {fake1.msisdn()[3:]}'
    elif faker_locale1 == 'zh_CN':
        return f'+86 {fake1.msisdn()[3:]}'
    elif faker_locale1 == 'en_GB':
        return f'+44 {fake1.msisdn()[3:]}'
    elif faker_locale1 == 'sv_SE':
        return f'+46 {fake1.msisdn()[3:]}'
    elif faker_locale1 == 'it_IT':
        return f'+39 {fake1.msisdn()[3:]}'
    elif faker_locale1 == 'de_DE':
        return f'+45 {fake1.msisdn()[3:]}'
    elif faker_locale1 == 'ar_SA':
        return f'+966 {fake1.msisdn()[3:]}'
    else:
        return f'+1 {fake1.msisdn()[3:]}'


configs = Properties()
with open('input.properties', 'rb') as config_file:
    configs.load(config_file)
title = ['Material Manager', 'Sales Executive', 'Manufacturing', 'High Tech', 'Retail']
indian_english_names = configs.get("indian_english_names").data
faker_locale = configs.get("faker_locale").data

# Instantiate Faker with multiple locales
# fake = Faker(['en_US', 'de_DE', 'pt_BR', 'ja_JP', 'zh-CN', 'hi_IN', 'or_IN', 'ta_IN', 'ru_RU'])
fake = Faker([faker_locale])


def create_data(x):
    # dictionary
    b_user = {}
    if indian_english_names == 'yes' and faker_locale == 'en_US':
        for i in range(0, x):
            em = fake.email()
            # fn = fake.first_name()
            fn = indian_names.get_first_name(gender='female')
            # mn = fake.first_name()
            mn = ""
            # ln = fake.last_name()
            ln = indian_names.get_last_name()
            email = ln[0].lower() + fn.lower() + gen_rand_numb_str(5) + "@" + em.split("@", 1)[1]
            phn = fake_phone_number(fake, faker_locale)
            addr = fake.street_address()
            cty = fake.city()
            st = fake.state()
            zipc = str(fake.zipcode())
            cntry = fake.country()
            postalad = addr + ", " + cty + ", " + st + ", " + cntry + ", " + zipc
            b_user[i] = {}
            b_user[i]['firstName'] = fn
            b_user[i]['lastName'] = ln
            b_user[i]['middleName'] = mn
            b_user[i]['email'] = email
            b_user[i]['title'] = fake.random_element(title)
            b_user[i]['login'] = email
            b_user[i]['mobilePhone'] = phn
            b_user[i]['primaryPhone'] = phn
            b_user[i]['streetAddress'] = addr
            b_user[i]['city'] = cty
            b_user[i]['state'] = st
            b_user[i]['zipCode'] = zipc
            b_user[i]['countryCode'] = cntry
            b_user[i]['postalAddress'] = postalad

    elif faker_locale == 'en_US':
        for i in range(0, x):
            em = fake.email()
            fn = fake.first_name()
            mn = fake.first_name()
            ln = fake.last_name()
            email = fn.lower() + ln[0].lower() + gen_rand_numb_str(5) + "@" + em.split("@", 1)[1]
            phn = fake_phone_number(fake, faker_locale)
            addr = fake.street_address()
            cty = fake.city()
            st = fake.state()
            zipc = str(fake.zipcode())
            cntry = fake.country()
            postalad = addr + ", " + cty + ", " + st + ", " + cntry + ", " + zipc
            b_user[i] = {}
            b_user[i]['firstName'] = fn
            b_user[i]['lastName'] = ln
            b_user[i]['middleName'] = mn
            b_user[i]['email'] = email
            b_user[i]['title'] = fake.random_element(title)
            b_user[i]['login'] = email
            b_user[i]['mobilePhone'] = phn
            b_user[i]['primaryPhone'] = phn
            b_user[i]['streetAddress'] = addr
            b_user[i]['city'] = cty
            b_user[i]['state'] = st
            b_user[i]['zipCode'] = zipc
            b_user[i]['countryCode'] = cntry
            b_user[i]['postalAddress'] = postalad

    elif faker_locale == 'hi_IN' or faker_locale == 'or_IN' or faker_locale == 'ta_IN':
        for i in range(0, x):
            em = fake.email()
            fn = fake.first_name()
            mn = ""
            ln = fake.last_name()
            email = em
            phn = fake_phone_number(fake, faker_locale)
            addr = fake.street_address()
            cty = fake.city()
            st = fake.state()
            zipc = str(fake.postcode())
            cntry = fake.current_country()
            postalad = addr + ", " + cty + ", " + st + ", " + cntry + ", " + zipc
            b_user[i] = {}
            b_user[i]['firstName'] = fn
            b_user[i]['lastName'] = ln
            b_user[i]['middleName'] = mn
            b_user[i]['email'] = email
            b_user[i]['title'] = fake.random_element(title)
            b_user[i]['login'] = email
            b_user[i]['mobilePhone'] = phn
            b_user[i]['primaryPhone'] = phn
            b_user[i]['streetAddress'] = addr
            b_user[i]['city'] = cty
            b_user[i]['state'] = st
            b_user[i]['zipCode'] = zipc
            b_user[i]['countryCode'] = cntry
            b_user[i]['postalAddress'] = postalad

    elif faker_locale == 'ja_JP' or faker_locale == 'ko_KR' or faker_locale == 'fr_FR' or faker_locale == 'ru_RU' or \
            faker_locale == 'zh_CN' or faker_locale == 'en_GB' or faker_locale == 'sv_SE' or faker_locale == 'it_IT' or \
            faker_locale == 'de_DE' or faker_locale == 'ar_SA' or faker_locale == 'en_IN':
        for i in range(0, x):
            em = fake.email()
            fn = fake.first_name()
            mn = ""
            ln = fake.last_name()
            if faker_locale == 'en_GB' or faker_locale == 'fr_FR' or faker_locale == 'sv_SE' or faker_locale == 'it_IT' \
                    or faker_locale == 'de_DE' or faker_locale == 'en_IN':
                email = fn.lower() + ln[1].lower() + gen_rand_numb_str(5) + "@" + em.split("@", 1)[1]
            else:
                email = em
            phn = fake_phone_number(fake, faker_locale)
            addr = fake.street_address()
            cty = fake.city()
            if faker_locale == 'ja_JP':
                st = fake.town()
            elif faker_locale == 'ko_KR':
                st = fake.province()
            elif faker_locale == 'fr_FR' or faker_locale == 'ru_RU':
                st = fake.region()
            elif faker_locale == 'zh_CN':
                st = fake.district()
            elif faker_locale == 'en_GB':
                st = ""
            elif faker_locale == 'sv_SE' or faker_locale == 'it_IT' or faker_locale == 'de_DE' \
                    or faker_locale == 'en_IN':
                st = fake.state()
            else:
                st = ""
            zipc = str(fake.postcode())
            cntry = fake.current_country()
            postalad = addr + ", " + cty + ", " + st + ", " + cntry + ", " + zipc
            b_user[i] = {}
            b_user[i]['firstName'] = fn
            b_user[i]['lastName'] = ln
            b_user[i]['middleName'] = mn
            b_user[i]['email'] = email
            b_user[i]['title'] = fake.random_element(title)
            b_user[i]['login'] = email
            b_user[i]['mobilePhone'] = phn
            b_user[i]['primaryPhone'] = phn
            b_user[i]['streetAddress'] = addr
            b_user[i]['city'] = cty
            b_user[i]['state'] = st
            b_user[i]['zipCode'] = zipc
            b_user[i]['countryCode'] = cntry
            b_user[i]['postalAddress'] = postalad

    return b_user


class Password(dict):
    value: str

    def __init__(self, value: str) -> None:
        self.value = value
        dict.__init__(self, value=value)


class Credentials(dict):
    password: Password

    def __init__(self, password: Password) -> None:
        self.password = password
        dict.__init__(self, password=password)


class Profile(dict):
    firstName: str
    lastName: str
    middleName: str
    email: str
    title: str
    login: str
    mobilePhone: str
    primaryPhone: str
    streetAddress: str
    city: str
    state: str
    zipCode: str
    countryCode: str
    postalAddress: str

    def __init__(self, firstName: str, lastName: str, middleName: str, email: str, title: str, login: str,
                 mobilePhone: str, primaryPhone: str, streetAddress: str, city: str, state: str, zipCode: str,
                 countryCode: str, postalAddress: str) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.middleName = middleName
        self.email = email
        self.title = title
        self.login = login
        self.mobilePhone = mobilePhone
        self.primaryPhone = primaryPhone
        self.streetAddress = streetAddress
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.countryCode = countryCode
        self.postalAddress = postalAddress

        dict.__init__(self, firstName=firstName, lastName=lastName, middleName=middleName, email=email,
                      title=title, login=login, mobilePhone=mobilePhone, primaryPhone=primaryPhone,
                      streetAddress=streetAddress, city=city,
                      state=state, zipCode=zipCode, countryCode=countryCode, postalAddress=postalAddress)


class Welcome10(dict):
    profile: Profile
    credentials: Credentials
    group_ids: List[str]

    def __init__(self, profile: Profile, credentials: Credentials, group_ids: List[str]) -> None:
        self.profile = profile
        self.credentials = credentials
        self.group_ids = group_ids

        dict.__init__(self, profile=profile, credentials=credentials, groupIds=group_ids)


# df = pd.read_csv(".\\import_OKTA_csv_template.csv", encoding='latin', dtype={"zipCode": "string"})
# df['middleName'] = df['middleName'].fillna('')
data = create_data(int(configs.get("number_of_users_to_load").data))
# print(data)
df = pd.DataFrame(data).transpose()
now = datetime.now()  # current date and time
date_time = now.strftime("%m_%d_%Y_%H_%M_%S")
df.to_excel("output_" + date_time + ".xlsx")
# print(df.head(2))
# url = 'https://dev-67659300.okta.com/api/v1/users?activate=true'
# url = 'https://dev-jnj-xiam.oktapreview.com/api/v1/users?activate=true'
url = 'https://stg-jnj-xiam.oktapreview.com/api/v1/users?activate=true'

'''
For staged user user url = 'https://dev-67659300.okta.com/api/v1/users?activate=false'
'''
# Headers = {"Authorization": "SSWS00EkrobpV51gXD_y0wYUAelSpj_EWIBipEbS8hcGk3", "Content-Type": "application/json",
#            "Accept": "application/json"}

# Headers = {"Authorization": "SSWS00mlLo5QCMHT6vknwKgizJAV7heAPOoT-Ytj3jUPBU", "Content-Type": "application/json",
#          "Accept": "application/json"}

Headers = {"Authorization": "SSWS 00xbR9Hc6ZSwpBMnP1rDJCUICYRIt1FMGUL6ehqmVn", "Content-Type": "application/json",
           "Accept": "application/json"}
count: int = 0
for i, row in df.iterrows():
    print("\n--------------------------------------------")
    print(str(i) + " of " + str(len(df.index)))
    # print(tuple(row))
    firstName, lastName, middleName, email, title, login, mobilePhone, primaryPhone, streetAddress, city, state, zipCode, countryCode, postalAddress = tuple(
        row)
    # city, countryCode, email, firstName, lastName, login, middleName, mobilePhone, postalAddress, primaryPhone, state, streetAddress, title, zipCode = tuple(row)
    print("--------------------------------------------\n")
    profile1 = Profile(firstName, lastName, middleName, email, title, login, mobilePhone, primaryPhone, streetAddress,
                       city, state, zipCode, countryCode, postalAddress)
    pwd = Password("Jnjforgot@12")
    cred = Credentials(pwd)
    # group_id = ['00g7u31jnoDcxUrov5d7']
    # group_id = ['00g86caqh3Px6hQXs1d7']
    group_id = ['00g8wv6tjj4ipRmqs1d7']
    wel = Welcome10(profile1, cred, group_id)
    response = requests.post(url, headers=Headers, data=json.dumps(wel), verify=False)
    print(json.dumps(wel))
    print("Status Code", response.status_code)
    print("JSON Response ", response.json())
    count = count + 1

    '''
    To deactivate users
    '''

    # if response.status_code == 200:
    #     deactivate_url = 'https://dev-67659300.okta.com/api/v1/users/' + response.json()["id"] + '/lifecycle/deactivate'
    #     deactivate_response = requests.post(deactivate_url, headers=Headers, verify=False)
    #     print("Deactivated")
    #     count = count + 1

    '''
        To suspend users
    '''

    # if response.status_code == 200:
    #     deactivate_url = 'https://dev-67659300.okta.com/api/v1/users/' + response.json()["id"] + '/lifecycle/suspend'
    #     deactivate_response = requests.post(deactivate_url, headers=Headers, verify=False)
    #     print("Suspended")
    #     count = count + 1

    '''
            To password
    '''

    # if response.status_code == 200:
    #     deactivate_url = 'https://dev-67659300.okta.com/api/v1/users/' + response.json()["id"] + '/lifecycle/expire_password'
    #     deactivate_response = requests.post(deactivate_url, headers=Headers, verify=False)
    #     print("Password over")
    #     count = count + 1

    '''
                To reset password
    '''

    # if response.status_code == 200:
    #     deactivate_url = 'https://dev-67659300.okta.com/api/v1/users/' + response.json()[
    #         "id"] + '/lifecycle/reset_password?sendEmail=true'
    #     deactivate_response = requests.post(deactivate_url, headers=Headers, verify=False)
    #     print("Password reset")
    #     count = count + 1

    '''
                    To forgot password
        '''

    # if response.status_code == 200:
    #     deactivate_url = 'https://dev-67659300.okta.com/api/v1/users/' + response.json()[
    #         "id"] + '/credentials/forgot_password?sendEmail=true'
    #     deactivate_response = requests.post(deactivate_url, headers=Headers, verify=False)
    #     print("Password reset")
    #     count = count + 1

    if count >= 49:
        count = 0
        time.sleep(35)
    # print(json.dumps(wel))
    # count = count + 1
