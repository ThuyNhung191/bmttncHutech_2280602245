import ecdsa
import os

# Kiểm tra nếu thư mục không tồn tại thì tạo mới
if not os.path.exists('cipher/ecc/keys'):
    os.makedirs('cipher/ecc/keys')

class ECCCipher:
    def __init__(self):
        pass

    # Hàm tạo khóa và lưu vào file
    def generate_keys(self):
        sk = ecdsa.SigningKey.generate()  # Tạo khóa riêng tư
        vk = sk.get_verifying_key()       # Lấy khóa công khai từ khóa riêng

        # Lưu khóa riêng tư vào file
        with open('cipher/ecc/keys/privateKey.pem', 'wb') as p:
            p.write(sk.to_pem())

        # Lưu khóa công khai vào file
        with open('cipher/ecc/keys/publicKey.pem', 'wb') as p:
            p.write(vk.to_pem())

    # Hàm tải khóa từ file
    def load_keys(self):
        with open('cipher/ecc/keys/privateKey.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())

        with open('cipher/ecc/keys/publicKey.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())

        return sk, vk

    # Hàm ký dữ liệu bằng khóa riêng tư
    def sign(self, message, key):
        return key.sign(message.encode('ascii'))

    # Hàm xác thực chữ ký
    def verify(self, message, signature, key):
        _, vk = self.load_keys()
        try:
            return vk.verify(signature, message.encode('ascii'))
        except ecdsa.BadSignatureError:
            return False
