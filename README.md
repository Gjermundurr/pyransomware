# pyransomware
School project


# Setup and run HOWTO#
1. run create-keys.py # create public/private key pair
2. bundle script into EXE file with pyinstaller: pyinstaller --onefile --windowed --add-data "public.pem;." --add-data "bg.png;." ./run.py
3. send exe to target
