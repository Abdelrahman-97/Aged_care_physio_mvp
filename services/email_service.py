import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from core import get_settings

def send_email(to_email:list[str], subject:str, body:str):
    settings = get_settings()
    msg = MIMEMultipart()
    msg["From"] = settings.email_sender
    msg["To"] = ",".join(to_email)
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(settings.email_sender, settings.email_password)
            server.sendmail(settings.email_sender, to_email, msg.as_string())
        return(f"Email sent to {to_email}")

    except Exception as e:
        return f"Email failed: {e}"
