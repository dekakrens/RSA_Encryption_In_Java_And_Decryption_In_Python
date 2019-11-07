# RSA Encryption in Java POC

This is a very simple Java program (using Spring Boot, of course) to demonstrate how to
encrypt a string with the RSA algorithm. We use a public key to encrypt the data, and 
that public key will be read from a file.

# How to use

## Create the key pair

To create a key pair, we'll use the ```openssl``` CLI tool. Open up a terminal and run 
the following command to create a private key:

```shell script
openssl genrsa -out privateKey.pem 2048
```

As you can see, we created a 2048 bit key. Next, using this private key, we'll create public
key for this. For this, run the following command:

```shell script
openssl rsa -in privateKey.pem -outform PEM -pubout -out public.pem
```

# How to decrypt

In the ```resources``` directory, I have created a Python file called ```rsaDecrypt.py```, 
in which I have the Python code to decrypt the encrypted string we got from the Java code.