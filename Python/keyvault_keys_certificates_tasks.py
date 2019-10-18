#!/usr/bin/python3
import os
import datetime

def task1():
    # Create new soft RSA key "myRSAkey" with size 20148 and set it's expiration date for tomorrow
    print("Task 1 is complete---------------------------------------------------")

def task2():
    # Print key name and expiration date for each key in the elraikhm-kvault, enable all disabled keys
    print("Task 2 is complete---------------------------------------------------")

def task3():
    # Print all versions of the "myRSAkey" key
    print("Task 3 is complete---------------------------------------------------")

def task4a():
    # Encrypt provided string using rsa key "myRSAKey" , store the ecryption result
    my_secret = "ssn is 123-45-678"
    print("Task 4a is complete---------------------------------------------------")

def task4b():
    # Decrypt the string from the task4a and print the result
    print("Task 4b is complete---------------------------------------------------")

def task5():
    # Initiate operation to create self signed certificate with default policy named <yourname>_cert
    print("Task 5 is complete---------------------------------------------------")

def task6():
    # Print the status of the certificate from task5 (create operation status)
    # If already created, create a new version of that certificate which will be valid for 2 month only
    print("Task 6 is complete---------------------------------------------------")

def task7():
    # Create a new self signed certificate <yourname>-cert2, customize this certificate policy with
    # subject alternative names "CN=*.contoso.com" and "CN=*.apps.contoso",
    print("Task 7 is complete---------------------------------------------------")

def task8():
    # Create new self signed certificate with custom policy to ensure that this certificate
    # is valid for the next 3 month only
    print("Task 8 is complete---------------------------------------------------")

def task9():
    #Delete all versions of < yourname > _cert
    print("Task 9 is complete---------------------------------------------------")

def task10():
    # Delete all versions of key myRSAkey
    print("Task 10 is complete---------------------------------------------------")

def main(parameters):
    task1()
    task2()
    task3()
    task4a()
    task4b()
    task5()
    task6()
    task7()
    task8()
    task9()
    task10()

try:
    main("")
except  Exception as e:
    print("\n Error. {0}".format(e.message))
finally:
    print("\nAll tasks are done")
