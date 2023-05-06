import hashlib
from base64 import b64encode

from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes


def aes_encrypt(item):
    salt = get_random_bytes(AES.block_size)

    private_key = hashlib.scrypt(item.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    cipher_config = AES.new(private_key, AES.MODE_GCM)

    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(item, "utf-8"))
    return {
        "cipher_text": b64encode(cipher_text).decode("utf-8"),
        "salt": b64encode(salt).decode("utf-8"),
        "nonce": b64encode(cipher_config.nonce).decode("utf-8"),
        "tag": b64encode(tag).decode("utf-8"),
    }
