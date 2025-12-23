import requests
import json
import hashlib
import random
import uuid
import os
import time
import datetime
import struct


def get_device_id(file_path=".imei"):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            device_id = f.read().strip()
    else:
        device_id = str(uuid.uuid1())
        with open(file_path, "w") as f:
            f.write(device_id)
    return device_id


def sha1_rotate_left(n, b):
    """循环左移"""
    return ((n << b) | (n >> (32 - b))) & 0xffffffff

def sha1_pad_message(message):
    """对消息进行填充"""
    if isinstance(message, str):
        message = message.encode('utf-8')
    
    length = len(message)
    message += b'\x80'
    message += b'\x00' * ((56 - (length + 1) % 64) % 64)
    message += struct.pack('>Q', length * 8)
    return message

def pb708254367a7ef59438e57fbb6a94d4f(message):
    """计算 SHA-1 哈希值"""
    # 初始化哈希值
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0
    
    # 填充消息
    message = sha1_pad_message(message)
    
    # 处理消息块
    for i in range(0, len(message), 64):
        chunk = message[i:i+64]
        w = [0] * 80
        
        # 将块分解为16个32位字
        for j in range(16):
            w[j] = struct.unpack('>I', chunk[j*4:j*4+4])[0]
        
        # 扩展16个字为80个字
        for j in range(16, 80):
            w[j] = sha1_rotate_left(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1)
        
        # 初始化工作变量
        a, b, c, d, e = h0, h1, h2, h3, h4
        
        # 主循环
        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:  # 60-79
                f = b ^ c ^ d
                k = 0xCA62C1D6
            
            temp = (sha1_rotate_left(a, 5) + f + e + k + w[j]) & 0xffffffff
            e = d
            d = c
            c = sha1_rotate_left(b, 30)
            b = a
            a = temp
        
        # 更新哈希值
        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff
    
    # 生成最终哈希值
    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

# ==================== SHA-256 实现 ====================

def sha256_rotate_right(n, b):
    """循环右移"""
    return ((n >> b) | (n << (32 - b))) & 0xffffffff

def sha256_pad_message(message):
    """对消息进行填充"""
    if isinstance(message, str):
        message = message.encode('utf-8')
    
    length = len(message)
    message += b'\x80'
    message += b'\x00' * ((64 - (length + 9) % 64) % 64)
    message += struct.pack('>Q', length * 8)
    return message

def u97175417f4909295ea98cdbc4fa99df5(message):
    """计算 SHA-256 哈希值"""
    # 初始化哈希值（前8个质数的平方根的小数部分的前32位）
    h = [
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
    ]
    
    # 初始化常数（前64个质数的立方根的小数部分的前32位）
    k = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]
    
    # 填充消息
    message = sha256_pad_message(message)
    
    # 处理消息块
    for i in range(0, len(message), 64):
        chunk = message[i:i+64]
        w = [0] * 64
        
        # 将块分解为16个32位字
        for j in range(16):
            w[j] = struct.unpack('>I', chunk[j*4:j*4+4])[0]
        
        # 扩展16个字为64个字
        for j in range(16, 64):
            s0 = sha256_rotate_right(w[j-15], 7) ^ sha256_rotate_right(w[j-15], 18) ^ (w[j-15] >> 3)
            s1 = sha256_rotate_right(w[j-2], 17) ^ sha256_rotate_right(w[j-2], 19) ^ (w[j-2] >> 10)
            w[j] = (w[j-16] + s0 + w[j-7] + s1) & 0xffffffff
        
        # 初始化工作变量
        a, b, c, d, e, f, g, h_temp = h
        
        # 主循环
        for j in range(64):
            S1 = sha256_rotate_right(e, 6) ^ sha256_rotate_right(e, 11) ^ sha256_rotate_right(e, 25)
            ch = (e & f) ^ ((~e) & g)
            temp1 = (h_temp + S1 + ch + k[j] + w[j]) & 0xffffffff
            S0 = sha256_rotate_right(a, 2) ^ sha256_rotate_right(a, 13) ^ sha256_rotate_right(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) & 0xffffffff
            
            h_temp = g
            g = f
            f = e
            e = (d + temp1) & 0xffffffff
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xffffffff
        
        # 更新哈希值
        h[0] = (h[0] + a) & 0xffffffff
        h[1] = (h[1] + b) & 0xffffffff
        h[2] = (h[2] + c) & 0xffffffff
        h[3] = (h[3] + d) & 0xffffffff
        h[4] = (h[4] + e) & 0xffffffff
        h[5] = (h[5] + f) & 0xffffffff
        h[6] = (h[6] + g) & 0xffffffff
        h[7] = (h[7] + h_temp) & 0xffffffff
    
    # 生成最终哈希值
    return ''.join(format(x, '08x') for x in h)

def v0934358e3fdb59d81517ba7c0cdd647b(data: str) -> str:
    m = hashlib.md5()
    m.update(data.encode('utf-8'))
    return m.hexdigest()

def pba8bf0298e82598e96574620bd3861cb(data, key):
    def ksa(key):
        key_len = len(key)
        schedule = list(range(256))
        j = 0
        for i in range(256):
            j = (j + schedule[i] + key[i % key_len]) % 256
            schedule[i], schedule[j] = schedule[j], schedule[i]
        return schedule

    def prga(schedule, data_len):
        i = j = 0
        stream = []
        for _ in range(data_len):
            i = (i + 1) % 256
            j = (j + schedule[i]) % 256
            schedule[i], schedule[j] = schedule[j], schedule[i]
            stream.append(schedule[(schedule[i] + schedule[j]) % 256])
        return stream

    def process(data, key):
        schedule = ksa(key)
        stream = prga(schedule, len(data))
        return bytes([d ^ s for d, s in zip(data, stream)])
    if isinstance(key, str):
        key = key.encode('utf-8')
    if isinstance(data, str):
        data = data.encode('utf-8')
    return process(data, key).decode('utf-8')
    
def m169a58ff81a2b2f4c0b1378d0d37e903(data, key):
    def ksa(key):
        key_len = len(key)
        schedule = list(range(256))
        j = 0
        for i in range(256):
            j = (j + schedule[i] + key[i % key_len]) % 256
            schedule[i], schedule[j] = schedule[j], schedule[i]
        return schedule

    def prga(schedule, data_len):
        i = j = 0
        stream = []
        for _ in range(data_len):
            i = (i + 1) % 256
            j = (j + schedule[i]) % 256
            schedule[i], schedule[j] = schedule[j], schedule[i]
            stream.append(schedule[(schedule[i] + schedule[j]) % 256])
        return stream

    def process(data, key):
        schedule = ksa(key)
        stream = prga(schedule, len(data))
        return bytes([d ^ s for d, s in zip(data, stream)])
    if isinstance(key, str):
        key = key.encode('utf-8')
    if isinstance(data, str):
        data = data.encode('utf-8')
    return process(data, key)

def g142e45e32797c1ad51be14b778d0c19b(data):
    if isinstance(data, str):
        data = data.encode('utf-8')
    elif not isinstance(data, bytes):
        raise ValueError("Input must be of type str or bytes")
    return ''.join(f'{byte:02x}' for byte in data)

def j1731d4f0efc97ca1c2319cf5a024b1d9(hex_str):
    return bytes.fromhex(hex_str)

def dc7d60c1a48261ed1c5a4ac563337aad2(data: str) -> str:
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    byte_data = data.encode('utf-8')
    binary_data = ''.join(f'{byte:08b}' for byte in byte_data)
    base64_str = ""
    for i in range(0, len(binary_data), 6):
        chunk = binary_data[i:i+6]
        chunk = chunk.ljust(6, '0')
        index = int(chunk, 2)
        base64_str += base64_chars[index]
    while len(base64_str) % 4 != 0:
        base64_str += '='

    return base64_str

def q0d746f8e6955ecf9af7cb94287881b1a(data: str) -> str:
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    binary_data = ""
    data = data.rstrip('=')

    for c in data:
        index = base64_chars.index(c)
        binary_data += f'{index:06b}'
    byte_array = bytearray()
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) == 8:
            byte_array.append(int(byte, 2))
    return byte_array.decode('utf-8')

def u1bddec7bff7ca9b7c7c9ffd7be69c157(data: str, base64_chars: str) -> str:
    byte_data = data.encode('utf-8')
    binary_data = ''.join(f'{byte:08b}' for byte in byte_data)
    base64_str = ""
    for i in range(0, len(binary_data), 6):
        chunk = binary_data[i:i+6]
        chunk = chunk.ljust(6, '0')
        index = int(chunk, 2)
        base64_str += base64_chars[index]
    while len(base64_str) % 4 != 0:
        base64_str += '='

    return base64_str

def g4c63cd147c11cafb7468f58696a77a83(data: str, base64_chars: str) -> str:
    binary_data = ""
    data = data.rstrip('=')

    for c in data:
        index = base64_chars.index(c)
        binary_data += f'{index:06b}'
    byte_array = bytearray()
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) == 8:
            byte_array.append(int(byte, 2))
    return byte_array.decode('utf-8')


if __name__ == "__main__":
    WEIURL = "http://wy.llua.cn/v2/"
    currentVersion = "3.0" #当前版本，用于检查更新

    notice_data = requests.post(WEIURL + "543ebab21c7c7265e25002a331ec744e",g142e45e32797c1ad51be14b778d0c19b(u1bddec7bff7ca9b7c7c9ffd7be69c157(g142e45e32797c1ad51be14b778d0c19b(m169a58ff81a2b2f4c0b1378d0d37e903(dc7d60c1a48261ed1c5a4ac563337aad2(u1bddec7bff7ca9b7c7c9ffd7be69c157(g142e45e32797c1ad51be14b778d0c19b(m169a58ff81a2b2f4c0b1378d0d37e903(dc7d60c1a48261ed1c5a4ac563337aad2("id=joOAMK0B55B"),"v37866858a23385237abf945a22")),"ihSPMbUG/kDcmWK51dleQjanA0Tfq26y7vJYt+LxsZOXwRp4H9C8I3zgVBoFruEN")),"de541e9bbf0ae9babe5a31b")),"3uOlNXZFnvtjSmAJWRrL0qKhxVBfCYz+7yPbG98sa4Me1Hc5EwUQk/6TDiI2pogd")))
    if notice_data.status_code == 200:
        notice_json = json.loads(pba8bf0298e82598e96574620bd3861cb(j1731d4f0efc97ca1c2319cf5a024b1d9(notice_data.text),"v5a18fbbefdbbad14ee363c46f0be28352e"))
        if notice_json["code"] == 18932:
            print("系统公告:")
            print(notice_json["msg"]["app_gg"])
        else:
            print(notice_json["msg"])
    else:
        print("网络异常")

    print("\n")

    print("正在检查更新...")
    ini_data = requests.post(WEIURL + "543ebab21c7c7265e25002a331ec744e",g142e45e32797c1ad51be14b778d0c19b(u1bddec7bff7ca9b7c7c9ffd7be69c157(g142e45e32797c1ad51be14b778d0c19b(m169a58ff81a2b2f4c0b1378d0d37e903(dc7d60c1a48261ed1c5a4ac563337aad2(u1bddec7bff7ca9b7c7c9ffd7be69c157(g142e45e32797c1ad51be14b778d0c19b(m169a58ff81a2b2f4c0b1378d0d37e903(dc7d60c1a48261ed1c5a4ac563337aad2("id=5slLGHlHLhg"),"v37866858a23385237abf945a22")),"ihSPMbUG/kDcmWK51dleQjanA0Tfq26y7vJYt+LxsZOXwRp4H9C8I3zgVBoFruEN")),"de541e9bbf0ae9babe5a31b")),"3uOlNXZFnvtjSmAJWRrL0qKhxVBfCYz+7yPbG98sa4Me1Hc5EwUQk/6TDiI2pogd")))
    if ini_data.status_code == 200:
        ini_json = json.loads(pba8bf0298e82598e96574620bd3861cb(j1731d4f0efc97ca1c2319cf5a024b1d9(ini_data.text),"v5a18fbbefdbbad14ee363c46f0be28352e"))	
        if ini_json["code"] == 87132:
            if ini_json["msg"]["version"] == currentVersion:
                print("已是最新版本")
            else:
                print("有新版本")
                print("当前版本:" + currentVersion)
                print("最新版本:" + ini_json["msg"]["version"])
                print("更新内容:" + ini_json["msg"]["updateshow"])
                print("更新地址:" + ini_json["msg"]["updateurl"])
                if ini_json["msg"]["updatemust"] == "y":
                    print("本次更新为强制更新，请更新后使用！")
                    exit()
        else:
            print(ini_json["msg"])
    else:
        print("网络异常")

    print("\n")

    while True:
        te02855f5c31d32b228a89d4a0a6b2be4 = input("请输入卡密:")
        f8bcf60fd4d46227c628aa2bc648515e0 = get_device_id()
        c4b9d0acbab128d81dd48ce1d31d898d6 = int(time.time())
        qd40200d3f1e647d59d28ab920328aaad = random.randint(100000, 999999)
        nf934dc39e1e2a2ce47388c453f532723 = v0934358e3fdb59d81517ba7c0cdd647b("kami=" + te02855f5c31d32b228a89d4a0a6b2be4 + "&markcode=" + f8bcf60fd4d46227c628aa2bc648515e0 + "&t=" + str(c4b9d0acbab128d81dd48ce1d31d898d6) + "&p1f01235dc00997f3fca1b8")
        r90be8041c7eef78a96c4b81441db8d02 = requests.post(WEIURL + "543ebab21c7c7265e25002a331ec744e",g142e45e32797c1ad51be14b778d0c19b(u1bddec7bff7ca9b7c7c9ffd7be69c157(g142e45e32797c1ad51be14b778d0c19b(m169a58ff81a2b2f4c0b1378d0d37e903(dc7d60c1a48261ed1c5a4ac563337aad2(u1bddec7bff7ca9b7c7c9ffd7be69c157(g142e45e32797c1ad51be14b778d0c19b(m169a58ff81a2b2f4c0b1378d0d37e903(dc7d60c1a48261ed1c5a4ac563337aad2("id=B4qgMxE0S2d&kami=" + te02855f5c31d32b228a89d4a0a6b2be4 + "&markcode=" + f8bcf60fd4d46227c628aa2bc648515e0 + "&t=" + str(c4b9d0acbab128d81dd48ce1d31d898d6) + "&sign=" + nf934dc39e1e2a2ce47388c453f532723 + "&value=" + str(qd40200d3f1e647d59d28ab920328aaad) +""),"v37866858a23385237abf945a22")),"ihSPMbUG/kDcmWK51dleQjanA0Tfq26y7vJYt+LxsZOXwRp4H9C8I3zgVBoFruEN")),"de541e9bbf0ae9babe5a31b")),"3uOlNXZFnvtjSmAJWRrL0qKhxVBfCYz+7yPbG98sa4Me1Hc5EwUQk/6TDiI2pogd")))
        if r90be8041c7eef78a96c4b81441db8d02.status_code == 200:
            u7cb6eb27df4a8cec2e8fef36383ea7a2 = json.loads(pba8bf0298e82598e96574620bd3861cb(j1731d4f0efc97ca1c2319cf5a024b1d9(q0d746f8e6955ecf9af7cb94287881b1a(q0d746f8e6955ecf9af7cb94287881b1a(g4c63cd147c11cafb7468f58696a77a83(g4c63cd147c11cafb7468f58696a77a83(pba8bf0298e82598e96574620bd3861cb(j1731d4f0efc97ca1c2319cf5a024b1d9(r90be8041c7eef78a96c4b81441db8d02.text),"l9d46086281d70d2fa86b76492816a48e451bc7"),"xt/iDmdBn9VOhPpbZXKFfuUACrY72kgH0w51eMSoqTyIW8zQRavjL6clsN+3GJE4"),"E8Z1WtvyRlUq7M03aGJPcOL6KFomrwfIHNehAjCD+k4zTYQbBXspxin5S9uV2d/g")))),"s376ae87c90d81221bb3479ecaec8cd"))
            if u7cb6eb27df4a8cec2e8fef36383ea7a2["xa790e86a909ab7a82aa122d2437ed17c"]==83830 and u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"]["w0cf085fae3fdfa57a551f93292f2d6fd"]=="1ebfcfa6b706b5beacc378d155c299cf":
                if u7cb6eb27df4a8cec2e8fef36383ea7a2["nd24058201fd279b48888502eb53faf82"]-c4b9d0acbab128d81dd48ce1d31d898d6>30 or u7cb6eb27df4a8cec2e8fef36383ea7a2["nd24058201fd279b48888502eb53faf82"]-c4b9d0acbab128d81dd48ce1d31d898d6<-30:
                    print("设备时间不准")
                else:
                    if u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"]["t271b27a22e0f3611"] != u97175417f4909295ea98cdbc4fa99df5(v0934358e3fdb59d81517ba7c0cdd647b(pb708254367a7ef59438e57fbb6a94d4f(""+str(c4b9d0acbab128d81dd48ce1d31d898d6)+""+nf934dc39e1e2a2ce47388c453f532723+""+str(c4b9d0acbab128d81dd48ce1d31d898d6)+""))) or u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"]["vb655d5bee4"] != pb708254367a7ef59438e57fbb6a94d4f(u97175417f4909295ea98cdbc4fa99df5(""+nf934dc39e1e2a2ce47388c453f532723+""+str(qd40200d3f1e647d59d28ab920328aaad)+""+"p1f01235dc00997f3fca1b8"+""+str(u7cb6eb27df4a8cec2e8fef36383ea7a2["xa790e86a909ab7a82aa122d2437ed17c"])+"")) or u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"]["v9b649048"] != v0934358e3fdb59d81517ba7c0cdd647b(u97175417f4909295ea98cdbc4fa99df5(""+str(u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"]["r36b999cb83d3c506379fd741727b651e"])+""+str(u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"]["r36b999cb83d3c506379fd741727b651e"])+""+str(u7cb6eb27df4a8cec2e8fef36383ea7a2["xa790e86a909ab7a82aa122d2437ed17c"])+"")):
                        print("校验失败")
                    else:
                        if u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"]["t45625b2115629c98645ca4aebf33fb65"] == "single":
                            print("登录成功\n剩余登录次数:" + u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"]["f03b32acce7db770eaba264b4fd6a5267"])
                        else:
                            print("登录成功\n到期时间:" + datetime.datetime.fromtimestamp(u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"]["bffc7c7fc7cf63ca1bb9138e74b517e49"]).strftime('%Y-%m-%d %H:%M:%S'))
                        break
            else:
                print(u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"])
        else:
            print("网络异常")