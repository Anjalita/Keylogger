# Python Keylogger (Educational Demo)

This is a basic keylogger written in Python using the `pynput` library.  
It captures keystrokes and logs them into a file (`keylog.txt`) with timestamps.

> ⚠️ This project is strictly for educational and ethical testing purposes only.  
> Please do not use it for illegal or unethical activities.

---

## How It Works

- Records letters, numbers, and special keys (like Enter, Space, Backspace, etc.)
- Saves words and full sentences based on space and enter keys
- Stores everything in a text file (`keylog.txt`) with date and time

---

## Getting Started

### Requirements
- Python 3.x installed
- `pynput` library

### Installation

You can install the required library using:

```bash
pip install pynput
```

> *Note: You can run this script directly, or use a virtual environment for better isolation if you're working on multiple Python projects.*

---

## How to Run

1. Clone or download this repository
2. Make sure `pynput` is installed (`pip install pynput`)
3. Run the script:
```bash
python3 keylog.py
```
4. Keystrokes will be recorded and saved in `keylog.txt`

---

## Sample Output

Here’s how the `keylog.txt` output might look:

```
2025-04-14 12:32:51 - Character pressed: h
2025-04-14 12:32:51 - Character pressed: i
2025-04-14 12:32:51 - Space pressed, current word: hi
2025-04-14 12:35:05 - Numeric pressed: 5
2025-04-14 12:35:05 - Character pressed: m
2025-04-14 12:35:05 - Character pressed: a
2025-04-14 12:35:05 - Character pressed: i
2025-04-14 12:36:14 - Special Character pressed: !
2025-04-14 12:36:14 - Enter pressed, sentence complete: hi 5 mai!
2025-04-14 12:36:42 - Complete sentence: hi 5 mai!
```

---

## Questions or Issues?

If you have any questions or face any issues, feel free to contact me.  
I'm happy to help!

---

> Disclaimer: This project is made only for learning and demonstration. Misusing this script for malicious purposes is strictly discouraged and may be illegal.
```
