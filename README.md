# 🗺️ India States Guessing Game (Python)

An interactive Python game where you guess the names of Indian states on a blank map — built using **Turtle Graphics** and **Pandas**.

This project is part of my learning journey in **Python**, **data handling**, and **basic GUI programming** as a **2nd-year Computer Science student**.


## 🎮 Game Overview

The game displays a map of India and asks you to type the names of states.
If you guess correctly, the state name appears on the map at its correct location.
You have limited lives, and the goal is to name as many states as you can before running out!


## 🧠 Features

✅ Interactive GUI using the `turtle` module
✅ CSV-based state coordinate data handling with `pandas`
✅ Keeps track of guessed and remaining states
✅ “Exit” option that creates a `states_to_learn.csv` file (so you can review missed states)
✅ Optional refinements (if added):

* Duplicate-guess prevention
* Case-insensitive and typo-tolerant input
* Hints and improved prompts
* Normalized name matching for states like *“Jammu & Kashmir”*


## 🗂️ Project Structure


📦 India-States-Game/
├── main.py                 # Main Python script
├── 50_states.csv           # State names with X, Y coordinates
├── Outline-Map-of-India-with-States.gif  # Map background
├── states_to_learn.csv     # Generated automatically (missed states)
└── README.md               # Project description
```

---

## ⚙️ Requirements

**Python 3.8+**
**Libraries:**

```
pandas
turtle (built-in)
```

Install dependencies using:

```bash
pip install pandas
```

---

## 🚀 How to Run

1. Clone or download this repository
2. Make sure all files (`main.py`, `50_states.csv`, and the map image) are in the same folder
3. Run the script:

   ```bash
   python main.py
   ```
4. A window will open showing a blank India map
5. Enter the names of states in the input box and try to guess all of them!
6. Type `Exit` anytime to quit and see a list of unguessed states in `states_to_learn.csv`.

---

## 🧩 Example Gameplay


> You have guessed 5 states
> Lives left: 3
> Guess the state:

**Output:**
Correct guesses appear directly on the map!

---

## 🧰 Technical Concepts Used

* **Turtle Graphics** for rendering text and visuals
* **CSV File Handling** via Pandas
* **String normalization** for flexible input
* **Event-driven loop** for gameplay
* **Data persistence** using exported CSV


## 🏗️ Future Improvements

* Add fuzzy string matching for small typos
* Add hints or regional levels (North, South, etc.)
* Include capitals or major cities for learning
* Use a GUI framework (e.g., Tkinter or PySimpleGUI) for a more modern interface
* Timer or scoring system to increase difficulty


## 👨‍💻 Author

Sahil pahuja
🎓 2nd Year B.Tech CSIT Student
💡 Interested in Python, Data Visualization, and Game Development

🔗 [LinkedIn Profile](https://www.linkedin.com/in/sahil-pahuja-789224367/)

---

## 🏁 License

This project is for educational and personal use.
Feel free to fork, modify, and learn from it — but please give credit if you share it publicly!

