# Artificial Intelligence

This repository hosts my programming coursework for Artificial Intelligence. Each lab builds on the UC Berkeley Pacman projects and related Python exercises to practice fundamental AI search and decision-making techniques.

## Lab Summaries

### Lab 1 — Pacman Python Warm-Up
- Implemented the introductory Python utilities (`addition.py`, `buyLotsOfFruit.py`, `shopSmart.py`) to refresh language syntax and data handling.
- Extended the tutorial support code (`shopAroundTown.py`) with helpers that enumerate shop subsets and permutations to evaluate fruit-shopping routes under different gas prices.
- Collected autograder scripts and reference material so each exercise can be verified locally.

### Lab 2 — Search and Games
- Built a reusable `Node` wrapper plus breadth-first search and A* search in `search.py` to navigate Pacman mazes while tracking costs and predecessors.
- Hooked these algorithms into the provided `SearchAgent`, enabling maze-solving runs with heuristics drawn from `searchAgents.py`.
- Left additional agents (depth-first search, iterative deepening, uniform-cost search, and multi-agent adversarial logic) as marked work in progress for future checkpoints.

### Lab 3 — Multi-Agent Pacman
- Implemented a depth-limited minimax agent in `multiAgents.py` that cycles through Pacman and every ghost while propagating max/min values across the game tree.
- Began exploring alpha-beta pruning, expectimax, and an improved evaluation heuristic; the scaffolding is in place with TODO markers for continued development.
- Tracking remaining tasks in-line with the project files so requirements and testing guidance stay close to the code.

## Repository Notes
- Projects retain the Berkeley licensing headers; all changes here are strictly for CSEN 166 coursework and personal study.
