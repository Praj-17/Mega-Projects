# Importing all the neccesary modules
import os
import ssl as secureSSL
from email.message import EmailMessage
import smtplib
# Do remember to add your Email-Id and Password In your environment variable.
# Or
# You Can directly put Credential here but only for learning purpose.
User = os.getenv("Gmail_User") # This will fetch User Credentials from your PC's environment variables (Used Just for Security Purpose)
print("User", User)
Pass = os.getenv("Gmail_Pass") # This will fetch User Credentials from your PC's environment variables (Used Just for Security Purpose)
print("pass: ", Pass)
msg = EmailMessage()
msg["From"] = User
msg["To"] = ['prajwal.waykos@flexiele.com'] # Can be used to send same mail to multiple users (Including You Also)
# msg["CC"] = "" # Can be used to send carbon copy same mail to multiple users (Including You Also)
# msg["BCC"] = "" # Can be used to send blind carbon copy (hidden mail to any anonymous person).
msg["Subject"] = "Python Mail App Test Port 465" # Set this Subject According to your needs
msg.set_content("Sending attachments using Python") #This Is basically the Body of your mail.


# File Attachment Concept
# Do remember to create a directory named media or rename it below or you can use the media folder in this repository.
filePath = 'sample.txt' # This will list all the files inside the media directory (** Only the Name of the files and folders --not path-- **)
if os.path.isfile(filePath):
    fileSize = os.path.getsize(filePath) / 10 ** 6 # This logic is used here to get the size of files in megabytes

    if fileSize > float(20):
        print(filePath, "Can't Be Uploaded As The Size Is Greater Than 20Mb") # To inform the user that file size is greater than 20MB
    else:
        fileAttach = open(filePath, "rb").read()
        msg.add_attachment(fileAttach,
                        maintype="application",
                        subtype="octet-stream", #Use "octet-stream" as subtype to send any kind of file to leave it's file type recognition on G-Mail.
                        )
else:
    print(filePath, "Is A Directory") # This is here to inform the user that the path provided is of a folder not a file.

# Below logic is used to send the mail
context = secureSSL.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(User, Pass) # This is used to setup a secure connection between the server and the owner
    smtp.send_message(msg) # This is used to send the message with all contents(i.e, the subject, body, file or attachments etc.)