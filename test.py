import os

localpath = os.environ['USERPROFILE']
exclude_dir = []
file_extensions = ['.txt', '.pdf', '.png', '.jpeg', '.docx', '.xlsx', '.doc', '.rtf', '.mp3']

for root, dirs, files in os.walk(localpath, topdown=True):
    dirs[:] = [d for d in dirs if not exclude_dir]
    for dir in dirs:
        print(os.path.join(root,dir))
    for file in files:
        print(os.path.join(root, file))
    # if dirs not in exclude_dir:
    #     for file in dirs:
    #         ext = os.path.splitext(file)[-1].lower()
    #         if ext in file_extensions:
    #             filepath = os.path.join(root, file)
    #             print(filepath)