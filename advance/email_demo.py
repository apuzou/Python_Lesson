import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# MailHog の SMTP に接続（TLS・認証なし）
smtp = smtplib.SMTP('localhost', 1025)

msg = MIMEMultipart()
msg['Subject'] = 'テスト'
msg['From'] = 'sender@example.com'
msg['To'] = 'receiver@example.com'
msg.attach(MIMEText('テスト本文'))

with open('advance/email_demo.py', 'r') as f:
    attachment = MIMEText(f.read(), 'plain', 'utf-8')
    attachment.add_header('Content-Disposition', 'attachment', filename='email_demo.py')
    msg.attach(attachment)
print(msg.as_string())

try:
    smtp.send_message(msg)
    print("メールを送信しました")
except Exception as e:
    print(f"メール送信に失敗しました: {e}")
finally:
    smtp.quit()