def decrypt(encrypted, key_int):
    decrypted = encrypted ^ key_int
    length = (decrypted.bit_length() + 7) //8
    decrypted_bytes = int.to_bytes(decrypted, length, 'big')
    return decrypted_bytes.decode()


def decrypt_file(encrypted_path, key_path, output_path):
    encrypted_file = open(encrypted_path, 'rb')
    key_file = open(key_path, 'rb')
    encrypted = int.from_bytes(encrypted_file.read(), 'big')
    key_int = int.from_bytes(key_file.read(), 'big')
    encrypted_file.close()
    key_file.close()
    decrypted = encrypted ^ key_int
    length = (decrypted.bit_length() + 7) //8
    decrypted_bytes = int.to_bytes(decrypted, length, 'big')
    f = open(output_path, 'wb')
    f.write(decrypted_bytes)
    f.close()
