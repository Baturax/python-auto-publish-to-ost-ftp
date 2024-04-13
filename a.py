import ftplib
import os
import pyperclip


HOSTNAME = "hostname"
USERNAME = "uname"
PASSWORD = "pass"
UPLOAD_DIRECTORY = "/httpdocs/baikral/"

ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

ftp_server.encoding = "utf-8"

directory = "/home/bai/Pictures/"

ftp_server.cwd(UPLOAD_DIRECTORY)

file_list = [f for f in os.listdir(directory) if f.endswith('.png')]

latest_file = max(file_list, key=lambda f: os.path.getmtime(os.path.join(directory, f)))

if latest_file in ftp_server.nlst():
    print(f"{latest_file} skipping.")
else:
    with open(os.path.join(directory, latest_file), "rb") as file:
        ftp_server.storbinary(f"STOR {latest_file}", file)
        print(f"{latest_file} uploaded.")

ftp_server.dir()

copy= "urlofhosttocopy/"+latest_file
pyperclip.copy(copy)

ftp_server.quit()
