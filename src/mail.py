import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from decouple import config
from email.mime.base import MIMEBase

message = MIMEMultipart('')
message['Subject'] = 'Planilha de jobs linkedin'
message['From'] = config('SENDER_EMAIL')
message['To'] = config('RECEIVER_EMAIL')

text_body = """\
Hi,
Este email foi enviado automaticamente pela automação de coleta de dados.
A planilha encontra-se em anexo."""

html_body = """\
<html>
  <body>
    <p>Hi,<br>
       Este email foi enviado automaticamente pela automação de coleta de dados.<br>
       A planilha encontra-se em anexo.<br>
    </p>
  </body>
</html>
"""

part1 = MIMEText(text_body, 'plain')
part2 = MIMEText(html_body, 'html')

with open(config('EXCEL_PATH_NAME'), 'rb') as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {config('EXCEL_PATH_NAME')}",
)

message.attach(part1)
message.attach(part2)
message.attach(part)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(config('SENDER_EMAIL'), config('PS'))
    server.sendmail(
        config('SENDER_EMAIL'), config('RECEIVER_EMAIL'), message.as_string()
    )
