import os

if __name__ == "__main__":

   try:

       os.system("git pull")

       __import__("profile").EditProfilePic()

   except Exception as e: 

       exit(str(e))
