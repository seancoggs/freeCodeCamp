import os
import base64
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asym_padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from typing import Dict

class Encryptor:
    def __init__(self, public_key):
        self.public_key = public_key

    @staticmethod
    def generate_aes_key_iv():
        """Generate a secure AES key and IV."""
        return os.urandom(32), os.urandom(12)  # 256-bit AES-GCM with a 96-bit IV

    def encrypt_data(self, data: bytes, key: bytes, iv: bytes) -> bytes:
        """Encrypt data with AES-GCM."""
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv))
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(data) + encryptor.finalize()
        return encrypted_data, encryptor.tag

    def encrypt_session_key(self, session_key: bytes) -> bytes:
        """Encrypt AES session key with RSA public key."""
        return self.public_key.encrypt(
            session_key,
            asym_padding.OAEP(
                mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def encrypt(self, data: bytes) -> Dict[str, str]:
        """Full encryption process: Encrypt data and session key."""
        session_key, iv = self.generate_aes_key_iv()
        encrypted_data, tag = self.encrypt_data(data, session_key, iv)
        encrypted_session_key = self.encrypt_session_key(session_key)

        # Base64-encode everything for transmission
        return {
            "encrypted_data": base64.b64encode(encrypted_data).decode('utf-8'),
            "session_key": base64.b64encode(encrypted_session_key).decode('utf-8'),
            "iv": base64.b64encode(iv).decode('utf-8'),
            "tag": base64.b64encode(tag).decode('utf-8')
        }
