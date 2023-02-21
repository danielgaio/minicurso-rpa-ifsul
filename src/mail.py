import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from decouple import config
from email.mime.base import MIMEBase

class Mail:
    def __init__(self):
        self.message = MIMEMultipart('')
        self.message['Subject'] = 'Planilha de jobs linkedin'
        self.message['From'] = config('SENDER_EMAIL')
        self.message['To'] = config('RECEIVER_EMAIL')
        self.message.add_header('Content-Type', 'text/plain')
        self.html_body = """\
        <html>
          <body>
            <p>Hi,<br>
              Este email foi enviado automaticamente pela automação de coleta de dados.<br>
              A planilha encontra-se em anexo.<br>
            </p>
          </body>
        </html>
        """

    def send_mail(self):
        mail_body = MIMEText(self.html_body, 'html')
        with open(config('EXCEL_PATH_NAME'), 'rb') as attachment:
            annex = MIMEBase("application", "octet-stream")
            annex.set_payload(attachment.read())
        encoders.encode_base64(annex)
        annex.add_header(
            "Content-Disposition",
            f"attachment; filename= {config('EXCEL_PATH_NAME')}",
        )

        self.message.attach(mail_body)
        self.message.attach(annex)

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(config('SENDER_EMAIL'), config('PS'))
            server.sendmail(
                config('SENDER_EMAIL'), config('RECEIVER_EMAIL'), self.message.as_string()
            )
        print('Email enviado.')
