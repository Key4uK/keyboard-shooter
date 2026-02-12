# Keyboard Shooter

A fun Linux-based Python soundboard that plays gun sound effects using your **keyboard and mouse**.

Built with:
- Python
- Pygame (audio)
- Pynput (keyboard & mouse listener)
- Bash launcher script

---

## Features

- Any key -> Shot sound
- Space -> Reload sound
- Enter -> BOOM sound
- Mouse Left / Right / Middle -> Secret Sounds
- Shift + M -> Toggle mute
- `./shooter start` -> Start
- `./shooter stop` -> Stop

---

## Requirements

- Linux (X11 session recommended)
- Python 3.10+
- pip
- Audio system (PulseAudio / PipeWire)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Key4uK/keyboard-shooter.git
cd keyboard-shooter
````

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install pygame pynput
```

Make the launcher executable:

```bash
chmod +x shooter
```

---

## Running the Program

### Start:

```bash
./shooter start
```

### Stop:

```bash
./shooter stop
```

---

## 📁 Project Structure

```
keyboard-shooter/
├── keyboardShooter.py
├── shooter
├── shot.wav
├── reload.wav
├── boom.wav
├── left.wav
├── right.wav
├── middle.wav
└── README.md
```

---

## Notes

* All sound files must be in the same folder as `keyboardShooter.py`
* Designed for Linux

---

## Disclaimer

This project is just for fun and learning purposes.

Enjoy responsibly!
