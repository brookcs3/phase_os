# Digest Mailer
# Emails the loop digest report to your preferred inbox

import smtplib
from email.mime.text import MIMEText
import os

DIGEST_FILE = "./loop_digest_weekly.md"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"  # Use an app-specific password
RECIPIENT_EMAIL = "your_email@gmail.com"


def send_digest():
    if not os.path.exists(DIGEST_FILE):
        print("⚠️ Digest file not found.")
        return

    with open(DIGEST_FILE, 'r') as f:
        body = f.read()

    msg = MIMEText(body, "plain")
    msg["Subject"] = "🧠 Weekly Loop Digest"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        print("✅ Digest sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send digest: {e}")

if __name__ == "__main__":
    send_digest()
