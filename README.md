# RSA-Pem
RSA-Pem is a Python written script that asks for 2 random prime numbers of your choice, along with an encoding exponent chosen and creates a full RSA Pem file with both Public and
Private keys in base64.

The minimum standard for RSA keys nowadays are 2048 bits. Thus, the 2 random prime number must each be 1024 bits respectively.

# Decoding Base64 Info in PEM
If you're using Python to decode the Base64 info found inside the PEM file, first decode the string info from UTF-8 encoding. You will then be able to proceed decoding the bytes returned via Base64 encoding. This will then return an arbitrary byte sequence encoded in DER (Distinguished Encoding Rules), which upon decoding it somemore will return an ASN.1 data object following the RFC 2313 Standard. 

More on RFC 2313: https://www.ietf.org/rfc/rfc2313.txt
