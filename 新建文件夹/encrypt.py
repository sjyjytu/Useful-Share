from secrets import token_bytes


def random_key(length):
    key = token_bytes(length)
    return int.from_bytes(key, 'big')


def encrypt(raw):
    raw_bytes = raw.encode()
    raw_int = int.from_bytes(raw_bytes, 'big')
    key_int = random_key(len(raw_bytes))
    return raw_int ^ key_int, key_int


def encrypt_file(raw_path, save_path, key_path):
    f = open(raw_path, 'rb')
    file_bytes = f.read()
    raw_int = int.from_bytes(file_bytes, 'big')
    key_int = random_key(len(file_bytes))
    f.close()
    save_file = open(save_path, 'wb')
    key_file = open(key_path, 'wb')
    encrypted_int = raw_int ^ key_int
    length = (encrypted_int.bit_length()+7)//8
    save_file.write(encrypted_int.to_bytes(length, 'big'))
    key_file.write(key_int.to_bytes(length, 'big'))
    save_file.close()
    key_file.close()

