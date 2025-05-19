import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
from concurrent.futures import ThreadPoolExecutor
from code.config import load_config
from code.utils.logger import logger

executor = ThreadPoolExecutor(max_workers=5)
config = load_config()

def send_email(subject, message, receivers, sender_name=None, sender_email=None, html_content=None):
    try:
        if config['smtp']['port'] == 465:
            server = smtplib.SMTP_SSL(config['smtp']['server'], config['smtp']['port'])
        elif config['smtp']['port'] == 587:
            server = smtplib.SMTP(config['smtp']['server'], config['smtp']['port'])
            server.starttls()
        else:
            logger.error(f"Invalid SMTP port: {config['smtp']['port']}")
            return False

        server.login(config['smtp']['username'], config['smtp']['password'])

        for receiver in receivers:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = f"<{config['smtp']['username']}>"
            msg['To'] = receiver
            if sender_email:
                msg['Reply-To'] = sender_email
            msg.attach(MIMEText(message, 'plain'))
            if html_content:
                msg.attach(MIMEText(html_content, 'html'))
            server.sendmail(config['smtp']['username'], receiver, msg.as_string())

        server.quit()
        return True
    except Exception as e:
        logger.error(f"Failed to send email: {str(e)}")
        return False

def send_email_background(data):
    try:
        success = send_email(
            subject=data['subject'],
            message=data['message'],
            receivers=config['receivers'],
            sender_name=data.get('sender_name'),
            sender_email=data.get('sender_email'),
            html_content=data.get('html_content')
        )
        if success:
            logger.info(f"Email sent successfully: {config['receivers']}")
        else:
            logger.error(f"Failed to send email. Form data: {json.dumps(data)}")
    except Exception as e:
        logger.exception(f"Exception while sending email in background: {str(e)}\nForm Data: {json.dumps(data)}")
