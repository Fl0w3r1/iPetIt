#iPetIt App
#Developer: Georgios Kalpakidis - LinkedIn: https://www.linkedin.com/in/georgios-kalpakidis-b775a6256/
#Project Manager: Paulos Kouskouridis
#Start Date: 2/3/2023

import math, cmath, statistics, random, datetime, time
from tkinter import *
from tkinter import messagebox

#import mysql.connector as mysqlc
#import mariadb as mdb
#import mariadb_sqlbuilder as mdbb
#import mongodb.connector as mongoc
#import postgresql.connector as pgresqlc

usernames = ["george", "paul", "jorge"]
passwords = [123, 321, 111]
emails = ["test@gmail.com", "test@outlook.com", "test@hotmail.com"]

print("Welcome To iPetIt.\n")
time.sleep(2)
eisodos = input("1. If you are a User and you want to log in, type: login\n2. If you are a Pet-Sitter and you want to log in, type: petsitter\n3.If you dont have an account and you want to make one, type: account\n4.If you want to learn about iPetIt, type: info\n5.If you want to quit, type: quit\n")
time.sleep(1)

if eisodos == "login":
    username = input("\nUsername or Email: ")
    password = input("Password: ")
    if username in usernames or username in emails and password in passwords:
        print("\nWelcome {}!".format(username))


elif eisodos == "petsitter":
    username_sitter = input("\nUsername or Email: ")
    password_sitter = input("Password: ")
    if username_sitter in usernames or username_sitter in emails and password_sitter in passwords:
        print("\nWelcome {}!".format(username_sitter))


elif eisodos == "account":
    username_account = input("\nPlease type a Username: ")
    if username_account not in usernames:
        usernames.append(username_account)
    else:
        username_account2 = input("\nUsername already exists. Try another one: ")

    password_account = input("Please type a Password: ")
    passwords.append(password_account)

    email_account = input("Please type your Email: ")
    if email_account not in emails:
        emails.append(email_account)
    else:
        email_account2 = input("\nEmail already exists. Try another one: ")
    time.sleep(1)
    print("\nYour account has been created successfully!")
    #print("\nIf you want to log in, type: login\n")

elif eisodos == "info":
    print("""\niPetIt is a free app that allows Pet Owners to find Pet Trainers and Pet Sitters in order to train or pet-sit their pets.
iPetIt also provides crucial information about your pet breed, such as: Suggested Foods, Medicine, Clothing and everything else specific to pets.
The app is fully supported and funded exclusively by ads. We dont charge for anything.
-Thought and Developed by two friends that started iPetIt as a fun project-""")

elif eisodos == "quit":
    print("\nThank you for trying iPetIt!")