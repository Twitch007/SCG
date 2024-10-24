import os

if __name__ == "__main__":

   try:

       os.system("git pull")

       __import__("cookies").gen_page()

   except Exception as e: 

       exit(str(e))
