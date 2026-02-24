import smtplib
from email.mime.text import MIMEText

# MailHog の SMTP に接続（TLS・認証なし）
smtp = smtplib.SMTP('localhost', 1025)

msg = MIMEText('テスト本文')
msg['Subject'] = 'テスト'
msg['From'] = 'sender@example.com'
msg['To'] = 'receiver@example.com'

smtp.send_message(msg)
smtp.quit()