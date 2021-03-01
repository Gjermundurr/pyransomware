from Crypto.PublicKey import RSA


key = RSA.generate(2048)

privatekey = key.export_key(format='PEM')
with open('private.pem', 'wb') as f:
    f.write(privatekey)


publickey = key.publickey().export_key(format='PEM')
with open('public.pem', 'wb') as f:
    f.write(publickey)


print('public/private key files created.')