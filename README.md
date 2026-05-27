# Snake AI 🐍

A modular Snake AI platform built with Python and Pygame.

The project evolved from a simple Snake implementation into a flexible environment for experimenting with:

- Multiple agents
- Graph search algorithms
- Benchmarking
- Random map generation
- Reinforcement Learning (future work)

---

# Features

## Agents

- Human Agent
- Simple Agent
- BFS Agent
- Safe BFS Agent (tail-aware pathfinding)

## Maps

- Empty Map
- Obstacle Map
- Random Map Generation

## Additional Features

- Dynamic FPS controls
- Path visualization
- Agent selection menu
- Map selection menu
- Benchmark mode
- Multiple game environments

---

# Project Structure

```text
snake-ai/

├── agents/
│   ├── agent_factory.py
│   ├── bfs_agent.py
│   ├── human_agent.py
│   └── simple_agent.py
│
├── game/
│   ├── environment.py
│   ├── food.py
│   ├── input_handler.py
│   ├── maps.py
│   ├── renderer.py
│   ├── settings.py
│   └── snake.py
│
├── benchmark.py
├── main.py
├── menu.py
└── requirements.txt
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/dscastillol/snake-ia.git

cd snake-ia
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Run Game

```bash
python main.py
```

You will be prompted to select:

- Agent
- Map

Example:

```text
Choose Agent

1 Human
2 Simple
3 BFS

Choose Map

1 Empty
2 Obstacles
3 Random
```

---

# Controls

## Human Agent

Arrow Keys:

```text
↑ ↓ ← →
```

## FPS Controls

Increase speed:

```text
SPACE
```

Decrease speed:

```text
LEFT SHIFT
```

---

# Benchmark Mode

Run:

```bash
python benchmark.py
```

Example output:

```text
Game 1 | Score: 46 | Steps: 953

Game 2 | Score: 110 | Steps: 2715

===== RESULTS =====

Average Score: 50.4

Max Score: 110

Min Score: 2
```

---

# Current Results

Safe BFS on Random Maps:

```text
Average Score ≈ 50

Maximum Score >100

Supports random environments
```

---


# Technologies

- Python
- Pygame
- Graph Search Algorithms (BFS)