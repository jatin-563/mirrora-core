# Mirrora Core

Mirrora Core is an open-source engine that converts plain text (and later voice)
into structured visual flows such as diagrams, concept maps, and process charts.

The goal is to help learners *see* what is being explained.

This repository is the core logic behind Mirrora / FlowForge AI.

## What it does (v0.1)

* Takes simple explanatory text
* Extracts key steps or concepts
* Converts them into a basic flow structure (nodes + edges)

Example input:

```
User enters data. The system validates it. Then the result is shown.
```

Example output:

```json
{
  "nodes": ["User enters data", "System validates it", "Result is shown"],
  "edges": [
    ["User enters data", "System validates it"],
    ["System validates it", "Result is shown"]
  ]
}
```

## Why this exists

Most learning tools focus on *text*.
Mirrora focuses on *thinking in visuals*.

This project is the first step toward:

* Live diagram generation
* Speech-to-visual learning
* Interactive concept mapping

## Tech Stack

* Python 3

## Run Locally

```bash
git clone https://github.com/jatin-563/mirrora-core
cd mirrora-core
python main.py
```

## Roadmap

* [ ] Improve sentence parsing
* [ ] Support bullet-style input
* [ ] Export diagrams as SVG
* [ ] Add voice input
* [ ] Web interface

## Contributing

* Fork the repo
* Create a branch
* Make your changes
* Open a Pull Request

Beginner-friendly issues will be labeled as `good first issue`.
# mirrora-core
“A Python tool that converts text or voice input into structured diagrams (JSON / flow format).”
