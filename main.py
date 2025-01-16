"""
AES加密
变量说明：
msg：消息（message）
key：密钥（key）
enc：加密（encrypt）
dec：解密（decrypt）
c_msg：密文（ciphertext）
p_msg：填充后的消息（padded message）
"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


# 加密
def enc(msg, key):
    key = key.encode('utf-8')
    key = key.ljust(32, b'\0')[:32]  # 填充密钥至32字节
    cipher = AES.new(key, AES.MODE_ECB)

    # 填充消息
    p_msg = pad(msg.encode('utf-8'), AES.block_size)

    # 加密
    return cipher.encrypt(p_msg)


# 解密
def dec(c_msg, key):
    key = key.encode('utf-8')
    key = key.ljust(32, b'\0')[:32]  # 填充密钥至32字节
    cipher = AES.new(key, AES.MODE_ECB)

    # 解密并去填充
    p_msg = cipher.decrypt(c_msg)
    return unpad(p_msg, AES.block_size).decode('utf-8')


if __name__ == '__main__':
    action = input("选择操作（1-加密，2-解密）：")

    if action == '1':
        msg = input("输入加密消息：")
        key = input("输入密钥：")
        c_msg = enc(msg, key)
        print(f"密文：{c_msg.hex()}")

    elif action == '2':
        c_msg = bytes.fromhex(input("输入密文："))
        key = input("输入密钥：")
        msg = dec(c_msg, key)
        print(f"解密消息：{msg}")
