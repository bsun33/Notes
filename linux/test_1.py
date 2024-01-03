import qrcode
import base64, hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def gen_fernet_key(password:bytes) -> bytes:
        assert isinstance(password, bytes)
        hlib = hashlib.md5()
        hlib.update(password)
        return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))

pwd = "red-blue-green-yellow"
key = gen_fernet_key(pwd.encode('utf-8'))
fernet = Fernet(key)

encrypted_msg = b'gAAAAABlk6vyMGxLYcfoxQvNDJgNJyS6XhdRq21LKdOhOMQ5UaIitT8Zk7Mk1uWZLWIQlz-Wa58_8MoTNBip_D3TR1V6IYutsfd7KKEwm_8M5eFvb51eo3U='
msg = fernet.decrypt(encrypted_msg).decode('utf-8')

print(msg)

