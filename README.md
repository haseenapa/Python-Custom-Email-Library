# Python-Mailer

Python library to ease sending emails from your application.

### Note
Things to change in gmail (If you are using gmail account as server)
  - Login to gmail
  - Go to this link https://www.google.com/settings/security/lesssecureapps
  - Click enable then try the code

### Example

```sh
# Import SendMail class from custom package
from Mailer.SendMail import SendMail

if __name__ == '__main__':
    CONFIG = {}
    MSG = {}
    CONFIG['server'] = "smtp.gmail.com"
    CONFIG['port'] = 587
    CONFIG['server_mail'] = 'example@gmail.com'
    CONFIG['server_pass'] = 'password'

    MSG['To'] = ['example1@test.com','example2@test.com']
    MSG['Subject'] = 'Test Subject'
    MSG['From'] = ''                               
    MSG['Cc'] = ['example1@test.com']         
    MSG['Bcc'] = ['example1@test.com']          
    MSG['Message_Type'] = 'plain'                
    MSG['Message'] = """
            <html>
              <head></head>
              <body>
                <p>Hi!<br>
                   Here is the <a href="https://www.python.org">link</a> you wanted.
                </p>
              </body>
            </html>
            """
    MSG['Filepath'] = 'C:\Users\Username\Downloads\output.txt' 
    #creating send mail obj
    OBJ = SendMail(CONFIG)
    OBJ.sendmail(MSG)
```
