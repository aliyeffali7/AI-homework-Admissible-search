# 🎮 Generalized Tic-Tac-Toe AI (m × m, k-in-a-row)

This repository contains a modular implementation of a generalized Tic-Tac-Toe game engine and an adversarial AI agent capable of playing on boards of **any size**.  
The system supports **Minimax**, **Alpha-Beta pruning**, and **depth-limited search** combined with a custom heuristic for scalable decision-making.

The project is structured for clarity, easy testing, and experimentation.

---

## 📁 Project Structure

```
core_game.py           # Game rules, move generation, turn logic, k-in-a-row detection
adversarial_search.py  # Minimax, Alpha-Beta, depth-limited search + move ordering
evaluation.py          # Threat-based heuristic scoring
run_game.py            # Human vs AI game runner (terminal)
test_logic.py          # Automated tests (pytest)
```

---

## 🧩 Components Overview

### 🟦 1. Game Engine — `core_game.py`
Implements the game mechanics:
- board creation  
- legal action generation  
- applying moves  
- determining whose turn it is  
- row/column/diagonal scanning  
- detecting winners or draws  
- computing utility values  

Designed to support any configuration of **m** and **k**.

---

### 🟥 2. Search Algorithms — `adversarial_search.py`
Includes three main decision-making strategies:

- **Minimax** — full adversarial search  
- **Alpha-Beta pruning** — optimized Minimax  
- **Depth-limited Alpha-Beta** — used for larger boards  
- **Move ordering** for deterministic and faster search  

All functions share a consistent interface and operate directly on the game engine.

---

### 🟩 3. Heuristic Evaluation — `evaluation.py`
Used when the search depth is exceeded.  
The heuristic identifies:
- near-winning formations  
- potential threats  
- forced defensive moves  
- opportunities for future alignment  

This allows the AI to handle larger boards intelligently.

---

### 🟨 4. Game Runner — `run_game.py`
Interactive terminal interface.

Start the game:
```bash
python run_game.py
```

Default configuration:
- Human plays **X**
- AI plays **O**
- Board: **3 × 3**
- AI uses full Alpha-Beta on 3×3, and depth-limited search on larger boards

To change board size:
```python
game = TicTacToe(4, 3)   # 4×4 board, 3-in-a-row wins
```

To adjust AI difficulty:
```python
DEPTH = 4
```

---

## 🧪 Test Suite — `test_logic.py`

The test file validates:
- board initialization  
- turn switching  
- winner detection logic  
- terminal/utility correctness  
- heuristic scoring correctness  
- Minimax vs Alpha-Beta consistency  
- depth-limited AI behavior  

Run tests:
```bash
pytest
```

If you don’t have pytest:
```bash
pip install pytest
```

---

## 🚀 Features
- Generalized board engine  
- Deterministic, reproducible AI decisions  
- Efficient search algorithm integration  
- Modular, readable code  
- Fully automated testing  

---

## 📌 Purpose
This project was designed for AI experimentation, game modeling, and adversarial search demonstrations.  
The implementation is extendable and can serve as a foundation for more advanced agents or research projects.


