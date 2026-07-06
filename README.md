# 🔍 Port Scanner

A lightweight port scanner built in Python that identifies open ports and their running services on a target host. Built as a hands-on project to understand the fundamentals of network reconnaissance — the foundation of every security assessment.

---

## 📖 About

Port scanning is the first step in any security audit. Before a system can be secured (or tested), you need to know which ports are open and what services are running behind them.

This tool connects to a range of ports on a target machine, reports which ones are open, and identifies the service running on each, all from the command line.

I built this to move beyond simply *using* security tools like Nmap, and to actually understand *how* they work under the hood.

---

## ✨ Features

- Scans a target IP or hostname across a custom port range
- Identifies open ports in real time
- Detects the service running on each open port (SSH, HTTP, HTTPS, etc.)
- Displays scan start and finish timestamps
- Reports a summary of total open ports found
- Clean, readable command-line output

---

## 🛠️ Technologies Used

- **Python 3** — core language
- **socket** — for creating network connections and testing ports
- **datetime** — for timestamping scans

---

## 🚀 Usage

Clone the repository:

```bash
git clone https://github.com/AdesinaTimothy/port-scanner.git
cd port-scanner
```

Run the scanner:

```bash
python3 port_scanner.py
```

You'll be prompted to enter:
- The target IP or hostname
- The start port
- The end port

### Example

```
==================================================
       TIMOBEST PORT SCANNER
==================================================

Enter target IP or hostname: scanme.nmap.org
Enter start port: 1
Enter end port: 100

Scanning scanme.nmap.org from port 1 to 100
--------------------------------------------------
[OPEN] Port 22 --> ssh
[OPEN] Port 80 --> http
--------------------------------------------------

Scan complete!
Total open ports found: 2
==================================================
```

---

## 🔒 Legal & Ethical Disclaimer

This tool is intended **for educational purposes and authorised security testing only.**

Only scan systems that you **own** or have **explicit written permission** to test. Unauthorised port scanning may be illegal in your jurisdiction (for example, under the UK Computer Misuse Act 1990).

For safe practice, use:
- `scanme.nmap.org` (provided by the Nmap project for legal scanning practice)
- Your own machines and lab environments
- Platforms like TryHackMe and HackTheBox

The author accepts no responsibility for misuse of this tool.

---

## 🎯 What I Learned

- How TCP connections work at the socket level
- The relationship between ports and services
- The role of reconnaissance in security assessments
- Why tools like Nmap are structured the way they are
- Writing clean, reusable functions in Python

---

## 🔮 Future Improvements

- [ ] Multithreading for faster scans
- [ ] Banner grabbing to identify software versions
- [ ] Export results to a file (CSV / JSON)
- [ ] Command-line arguments instead of interactive prompts
- [ ] Common port presets (e.g. "top 1000")

---

## 👤 Author

**Timothy Adesina**
Cybersecurity enthusiast with a background in healthcare, building practical security tools while learning offensive and defensive fundamentals.

- GitHub: [@AdesinaTimothy](https://github.com/AdesinaTimothy)

---

*Built as part of an ongoing journey into cybersecurity — learning never ends.* 🚀
