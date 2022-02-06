# from os import chdir
# from sys import path
# chdir(path[0])

# from Keys import RSAPublicKey, RSAPrivateKey
# from pyasn1.codec.der.encoder import encode
# from pyasn1.codec.der.decoder import decode as der_decoder
# import base64

# def create_public_PEM(ASN1Object:RSAPublicKey, modulus:int, publicExponent:int):
#     ASN1Object['modulus'] = modulus
#     ASN1Object['publicExponent'] = publicExponent

#     # Encode ASN1Object via DER method
#     public_DER = encode(ASN1Object)
#     public_DER_Unicode = base64.encodebytes(public_DER).decode("utf-8")

#     return "-----BEGIN RSA PUBLIC KEY-----\n"+public_DER_Unicode+"-----END RSA PUBLIC KEY-----\n"

# def create_private_PEM(ASN1Object:RSAPrivateKey, modulus:int, publicExponent:int, 
#     privateExponent:int, prime1:int, prime2:int, exponent1:int, exponent2:int, coefficient:int,version=0
#     ):

#     ASN1Object['version'] = version # version of RFC 2313 standards used
#     ASN1Object['modulus'] = modulus
#     ASN1Object['publicExponent'] = publicExponent
#     ASN1Object['privateExponent'] = privateExponent
#     ASN1Object['prime1'] = prime1
#     ASN1Object['prime2'] = prime2
#     ASN1Object['exponent1'] = exponent1
#     ASN1Object['exponent2'] = exponent2
#     ASN1Object['coefficient'] = coefficient

#     # Encode ASN1Object via DER method
#     public_DER = encode(ASN1Object)
#     public_DER_Unicode = base64.encodebytes(public_DER).decode("utf-8")

#     return "\n-----BEGIN RSA PRIVATE KEY-----\n"+public_DER_Unicode+"-----END RSA PRIVATE KEY-----"

# def main():
#     print("============= RSA KEY AND PEM CERTIFICATE MAKER =============")

#     P = int(input("Enter Prime Number 1: ")) # Prime 1
#     Q = int(input("Enter Prime Number 2: ")) # Prime 2
#     E = int(input("PUBLIC Encoding Exponent [Recommended 65537]:")) # Public Exponent

#     # Initialise Variables
#     phiN = (P-1)*(Q-1) # phiFunction of RSA Modulus (N)
#     N = P * Q # RSA Modulus
#     D = pow(E, -1, phiN) # Private Exponent
#     dP = D % (P - 1) # Exponent 1
#     dQ = D % (Q - 1) # Exponent 2
#     coEff = pow(Q, -1, P) #Chinese Remainder Theorem coefficient

#     public_key_asn = RSAPublicKey()
#     private_key_asn = RSAPrivateKey()

#     public_key_PEM = create_public_PEM(public_key_asn, N, E)
#     private_key_PEM = create_private_PEM(private_key_asn, N, E, D, P, Q, dP, dQ, coEff)

#     with open("RSA_Public.pem", 'w') as infile:
#         infile.write(public_key_PEM + private_key_PEM)
    

# if __name__ == "__main__":
#     main()