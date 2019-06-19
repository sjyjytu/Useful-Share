from encrypt import encrypt_file
from decrypt import decrypt_file
encrypt_file('raw.jpg','encrypted','key')
decrypt_file('encrypted','key','output.jpg')