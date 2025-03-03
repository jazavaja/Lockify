import base64
import hashlib

from cryptography.fernet import Fernet


def generate_or_load_key(seed):
    """
    Generate a key from the seed or derive a key deterministically.
    This function uses the seed to create a reproducible key.
    """

    key = hashlib.sha256(seed.encode()).digest()  # Derive a key from the seed
    return base64.urlsafe_b64encode(key[:32])  # Fernet requires a 32-byte key


def process_encrypt(string, seed, result_label):
    """
    Encrypts the input string using AES (Fernet) and displays the result.
    """
    try:
        key = generate_or_load_key(seed)
        cipher_suite = Fernet(key)
        encrypted_message = cipher_suite.encrypt(string.encode())
        result = f"{encrypted_message.decode()}"
        result_label.setText(result)
    except Exception as e:
        result_label.setText(f"Error during encryption: {str(e)}")


def process_decrypt(encrypted_string, seed, result_label):
    """
    Decrypts the input string using AES (Fernet) and displays the result.
    """
    try:
        key = generate_or_load_key(seed)
        cipher_suite = Fernet(key)
        decrypted_message = cipher_suite.decrypt(encrypted_string.encode())
        result = f"{decrypted_message.decode()}"
        result_label.setText(result)
    except Exception as e:
        result_label.setText(f"Error during decryption: {str(e)}")
