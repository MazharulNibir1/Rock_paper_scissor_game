# ✂️ Rock Paper Scissors — Python CLI Game

> One round. Three choices. Beat the machine.

---

## 🚀 Quick Start

```bash
git clone https://github.com/MazharulNibir1/rock_paper_scissor.git
cd rock_paper_scissor
python main.py
```

No dependencies. Pure Python standard library.

---

## 🎮 How to Play

- Type `rock`, `paper`, or `scissor`
- Program picks randomly
- Result: win / lose / draw

---

## ⚙️ Features

- ✅ Case-insensitive input
- ✅ Whitespace trimmed automatically
- ✅ Invalid input rejected with reprompt
- ✅ Instant result with program's choice revealed

---

## 🧠 Game Logic

```
beats = { rock → scissor, paper → rock, scissor → paper }

user == program  → draw
beats[user] == program → win
else             → lost
```

---

## 🖼️ Preview

```
Choose between Rock, Paper and Scissor: rock
You have win, program chose scissor
```

---

## 🗂️ Project Structure

```
rock_paper_scissor/
├── main.py
└── README.md
```

---

## 🛠️ Built With

- Python 3
- `random` module (stdlib)

---

## 📌 What I Learned

- Dictionary-based logic over if/elif chains
- Input sanitisation with `.lower().strip()`
- Loop-until-valid input pattern

---

## 🔮 Potential Improvements

- [ ] Score tracker across multiple rounds
- [ ] Best of 3 / 5 mode
- [ ] Replay prompt
- [ ] Lizard & Spock variant

---

## 👤 Author

**Mazhar** — [@MazharulNibir1](https://github.com/MazharulNibir1)
