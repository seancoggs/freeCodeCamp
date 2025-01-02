import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class Decryptor:
    def __init__(self, private_key_path: str, password: bytes = None):
        self.private_key = self.load_private_key(private_key_path, password)

    @staticmethod
    def load_private_key(path: str, password: bytes = None):
        """Load an RSA private key from a PEM file."""
        with open(path, "rb") as key_file:
            return serialization.load_pem_private_key(
                key_file.read(),
                password=password,
                backend=default_backend()
            )

    def decrypt_session_key(self, encrypted_key: str) -> bytes:
        """Decrypt the AES session key using the RSA private key."""
        decoded_key = base64.b64decode(encrypted_key)
        return self.private_key.decrypt(
            decoded_key,
            asym_padding.OAEP(
                mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    @staticmethod
    def aes_decrypt(session_key: bytes, encrypted_data: str, iv: str, tag: str) -> bytes:
        """AES-GCM decryption."""
        cipher = Cipher(algorithms.AES(session_key), modes.GCM(base64.b64decode(iv), base64.b64decode(tag)))
        decryptor = cipher.decryptor()
        return decryptor.update(base64.b64decode(encrypted_data)) + decryptor.finalize()

    def execute(self, encrypted_key: str, encrypted_data: str, iv: str, tag: str) -> str:
        """Perform decryption."""
        session_key = self.decrypt_session_key(encrypted_key)
        decrypted_data = self.aes_decrypt(session_key, encrypted_data, iv, tag)
        return decrypted_data.decode('utf-8')

def main():
    decryptor = Decryptor("private-key.pem")

    encrypted_data = "INSERT_ENCODED_ENCRYPTED_DATA"
    encrypted_key = "INSERT_ENCODED_SESSION_KEY"
    iv = "INSERT_ENCODED_IV"
    tag = "INSERT_ENCODED_TAG"

    result = decryptor.execute(encrypted_key, encrypted_data, iv, tag)
    print(result)

if __name__ == "__main__":
    main()
