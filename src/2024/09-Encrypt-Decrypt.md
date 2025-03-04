# Encrypt
# Decrypt

## Symmetric Encryption:
- Uses the same key for both encryption and decryption 
- **Encryption:** The plaintext is transformed into ciphertext using the secret key and a specific algorithm.
- **Decryption:** The ciphertext is transformed back into plaintext using the same secret key and the reverse of the encryption algorithm.
- **Examples:** Advanced Encryption Standard (AES), Triple DES, Blowfish, Twofish

## Asymmetric Encryption (Public Key Encryption):
- Uses two keys: a public key for encryption and a private key for decryption 
- **Encryption:** The plaintext is encrypted using the recipient's public key.
- **Decryption:** The ciphertext can only be decrypted using the recipient's private key.
- **Examples:** RSA, Diffie-Hellman, Boneh-Franklin scheme, Cramer-Shoup cryptosystem.



# Other[Hashing.]

- While not strictly encryption, hashing is a related concept used for data integrity.
- It transforms data of any size into a fixed-length hash value 
- Hashing is a one-way function; it's computationally infeasible to reverse the process and obtain the original data from the hash value.
- **Use:** Verifying data integrity, password storage.
- **Examples:** Message Digest Algorithm (MD5), Secure Hash Algorithm (SHA) .
