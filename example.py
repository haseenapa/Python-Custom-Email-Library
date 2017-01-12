# Import SendMail class from custom package
from Mailer.SendMail import SendMail


if __name__ == '__main__':

    CONFIG = {}
    MSG = {}
    CONFIG['server'] = "smtp.gmail.com"
    CONFIG['port'] = 587
    CONFIG['server_mail'] = 'haseena.bridge@gmail.com'
    CONFIG['server_pass'] = 'h@$een@11@'

    MSG['To'] = ['haseenakhader.pa@gmail.com']      # ['example1@test.com','example2@test.com'] - if multiple users are there
    MSG['Subject'] = 'Test Subject'
    #MSG['From'] = ''                               # optional, otherwise it takes server mail
    #MSG['Cc'] = ['example1@test.com']              # ['example1@test.com','example2@test.com'] - if multiple users are there
    #MSG['Bcc'] = ['example1@test.com']             # ['example1@test.com','example2@test.com'] - if multiple users are there
    #MSG['Message_Type'] = 'plain'                  # two values : 'plain' or 'html'. By default it will take 'html'
    MSG['Message'] = """
            <html>
              <head></head>
              <body>
                <p>Hi!<br>
                   How are you?<br>
                   Here is the <a href="https://www.python.org">link</a> you wanted.
                </p>
              </body>
            </html>
            """

    #MSG['Filepath'] = 'C:\Users\Haseena\Downloads\output.txt'          #if any attachment is there

    #creating send mail obj
    OBJ = SendMail(CONFIG)
    OBJ.sendmail(MSG)
