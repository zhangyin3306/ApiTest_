from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import base64

def Encrypt(word, keyStr=None, ivStr=None):
    # 如果没有提供自定义的密钥和IV，使用默认值
    key = b'5gYlUuGq4fMTAcbf'
    iv = b'g2wzfqvMOeazgdfg'

    # 如果提供了自定义的密钥和IV，使用它们
    if keyStr and ivStr:
        key = keyStr.encode('utf-8')
        iv = ivStr.encode('utf-8')

    # 使用ZeroPadding进行填充
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(word.encode('utf-8')) + padder.finalize()

    # 创建AES加密器
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # 加密数据
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # 返回Base64编码的加密结果
    return base64.b64encode(ciphertext).decode('utf-8')

# 要加密的字符串
