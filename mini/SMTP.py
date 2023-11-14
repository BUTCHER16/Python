import smtplib

sender_mail = 'ravidossalbert@gmail.com'
receivers_mail = ['santaravidoss@gmail.com']
message = """Subject: Your Subject

Your email body goes here.
"""

try:
    password = input('Enter the password: ')
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login(sender_mail, password)
    smtpObj.sendmail(sender_mail, receivers_mail, message)
    print("Msg Sent")
except Exception as e:
    print("Error: Unable to send mail. Error details:", str(e))
finally:
    smtpObj.quit()
