from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP_SSL


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
SMTP_USER_MAIL = "junhee914@gmail.com"
SMTP_USER = "junhee914"
SMTP_PASSWORD = "wnsgml554"


def send_mail(target_mail, subject, contents, attachment=False):
    msg = MIMEMultipart("alternative")

    if attachment:
        msg = MIMEMultipart('mixed')

    msg['From'] = SMTP_USER_MAIL
    msg['to'] = target_mail
    msg['Subject'] = subject

    text = MIMEText(contents)
    msg.attach(text)

    smtp = SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    smtp.sendmail(SMTP_USER_MAIL, target_mail, msg.as_string())
    smtp.close()


send_mail('junh_eee@naver.com',  # 메일을 받을 주소
          '메일이 도착했습니다.',  # 메일 제목
          '파이썬을 사용한 메일자동화입니다.')  # 메일 내용
