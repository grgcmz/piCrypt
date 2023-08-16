from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import os
import logging

logger = logging.getLogger('root')

def generate_private_key():
    # Generate a random key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return (private_key, private_key.public_key())

def encrypt_file(encryption_key, filepath):
    # Read the contents of the file
    with open(filepath, 'rb') as file:
        content = file.read()

    # Encrypt the file contents public key
    ciphertext = encryption_key.encrypt(
        content,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Write the encrypted data to a new file
    encrypted_file_path = 'encrypted_file.bin'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(ciphertext)

    logger.info(f"File encrypted and saved as {encrypted_file_path}")

# Serialize the private key and save it for later decryption
def serialize_keys(private_key, public_key):
    private_key_path = './private_key.pem'
    public_key_path = './public_key.pem'
    
    with open(private_key_path, 'wb') as private_key_file:
        private_key_file.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))
    logger.info(f"Private key saved as {private_key_path}")
    
    with open(public_key_path, 'wb') as public_key_file:
        public_key_file.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    logger.info(f"Public key saved as {public_key_path}")