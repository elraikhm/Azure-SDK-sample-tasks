#!/usr/bin/python3
import os
import base64
import datetime

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.keyvault.keys import KeyClient
from azure.keyvault.keys.crypto import CryptographyClient, EncryptionAlgorithm
from azure.keyvault.certificates import CertificateClient, CertificatePolicy


# The key vault identity
vault_url = ""

# Set credentials using environment variables AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, AZURE_TENANT_ID
credential = DefaultAzureCredential()

# Create clients for interacting with key vault keys, secrets and certificates
key_client = KeyClient(vault_endpoint=vault_url, credential=credential)
secret_client = SecretClient(vault_endpoint=vault_url, credential=credential)
certificate_client = CertificateClient(vault_endpoint=vault_url, credential=credential)

def task1():
    # Create new soft RSA key "myRSAkey" with size 20148 and set it's expiration date for tomorrow
    expiry_date = datetime.datetime.now() + datetime.timedelta(days=1)
    rsa_key = key_client.create_rsa_key("myRSAkey", size=2048, expires_on=expiry_date)
    print("Task 1 is complete---------------------------------------------------")

def task2():
    # Print key name and expiration date for each key in the elraikhm-kvault, enable all disabled keys
    keys = key_client.list_properties_of_keys()
    for key in keys:
        print(key.name, key.expires_on)
        if (not key.enabled):
            key_client.update_key_properties(key.name, enabled=True)
    print("Task 2 is complete---------------------------------------------------")

def task3():
    # Print all versions of the "myRSAkey" key
    versions = key_client.list_key_versions("myRSAkey")
    for version in versions:
        print(version.version)
    print("Task 3 is complete---------------------------------------------------")

def task4a():
    # Encrypt provided string using rsa key "myRSAKey" , store the ecryption result
    my_secret = "ssn is 123-45-678"
    
    key_name = "myRSAkey"
    rsa_key = key_client.get_key(key_name)
    crypto_client = CryptographyClient(rsa_key, credential)
    cipher = crypto_client.encrypt(EncryptionAlgorithm.rsa_oaep, my_secret.encode())
    
    secret_name = "mysecret"
    secret = secret_client.set_secret(secret_name, base64.b64encode(cipher.ciphertext).decode('utf-8'))
    print("Task 4a is complete---------------------------------------------------")

def task4b():
    # Decrypt the string from the task4a and print the result
    key_name = "myRSAkey"
    rsa_key = key_client.get_key(key_name)
    crypto_client = CryptographyClient(rsa_key, credential)

    secret_name = "mysecret"
    cipher = secret_client.get_secret(secret_name)
    plaintext = crypto_client.decrypt(EncryptionAlgorithm.rsa_oaep, base64.b64decode(cipher.value))
    print(plaintext.decrypted_bytes.decode())
    print("Task 4b is complete---------------------------------------------------")

def task5():
    # Initiate operation to create self signed certificate with default policy named <yourname>_cert
    cert_name = "testcert"
    cert_policy = CertificatePolicy(subject_name="CN=" + cert_name, issuer_name="Self")
    certificate_poller = certificate_client.begin_create_certificate(name=cert_name, policy=cert_policy)
    print("Task 5 is complete---------------------------------------------------")

def task6():
    # Print the status of the certificate from task5 (create operation status)
    cert_name = "testcert"
    certificate_operation = certificate_client.get_certificate_operation(cert_name)
    print(certificate_operation.status)
    # If already created, create a new version of that certificate which will be valid for 2 month only
    if (certificate_operation.status == "completed"):
        cert_policy = CertificatePolicy(subject_name="CN=" + cert_name, issuer_name=certificate_operation.issuer_name, validity_in_months=2)
        certificate_poller = certificate_client.begin_create_certificate(name=cert_name, policy=cert_policy)
    print("Task 6 is complete---------------------------------------------------")

def task7():
    # Create a new self signed certificate <yourname>-cert2, customize this certificate policy with
    cert_name = "testcert2"
    # subject alternative names "CN=*.contoso.com" and "CN=*.apps.contoso",
    subject_alternative_names = ["*.contoso.com", "*.apps.contoso"]

    cert_policy = CertificatePolicy(subject_name="CN=" + cert_name, issuer_name="Self", san_dns_names=subject_alternative_names)
    certificate_poller = certificate_client.begin_create_certificate(name=cert_name, policy=cert_policy)
    print("Task 7 is complete---------------------------------------------------")

def task8():
    # Create new self signed certificate with custom policy to ensure that this certificate
    # is valid for the next 3 month only
    cert_name = "testcert3"
    cert_policy = CertificatePolicy(subject_name="CN=" + cert_name, issuer_name="Self", validity_in_months=3)
    certificate_poller = certificate_client.begin_create_certificate(name=cert_name, policy=cert_policy)
    print("Task 8 is complete---------------------------------------------------")

def task9():
    #Delete all versions of < yourname > _cert
    cert_name = "testcert"
    deleted_certificate = certificate_client.delete_certificate(cert_name)
    print("Task 9 is complete---------------------------------------------------")

def task10():
    # Delete all versions of key myRSAkey
    key_name = "myRSAkey"
    deleted_key = key_client.delete_key(key_name)
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
