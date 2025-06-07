# 📘 Godot Docs Scraper

A Python tool for downloading and chunking [Godot Engine](https://godotengine.org/) documentation pages into clean, markdown-formatted files — ideal for AI project ingestion, offline reference, or structured knowledge bases.

---

## ✨ Features

- 🔎 Scrapes any number of Godot class documentation pages
- 📄 Converts HTML content to readable Markdown
- ✂️ Splits long docs into smaller `.md` chunks for better processing (Claude/GPT-friendly)
- 📁 Organizes output into folders with descriptive filenames
- 🔄 Auto-clears old output before each run

---

## 🧰 Requirements

- Python 3.7 or higher
- Internet connection (for scraping online docs)

---

## 🔧 Installation

### 1. Install Python (if not already installed)

Download and install Python from the official site:

**https://www.python.org/downloads/**

> ⚠️ Make sure to check the option: **“Add Python to PATH”** during installation.

### 2. Install Python dependencies

Open a terminal or PowerShell window and run:

```bash
pip install requests beautifulsoup4 markdownify
```

## 🚀 How to Use
### 1. Clone or download this repository

Download the ZIP or use Git:

```bash
git clone https://github.com/your-username/godot-docs-scraper.git
cd godot-docs-scraper
```

### 2. Edit the target class list

Open godot_docs_scraper.py in a code editor like VSCode. Near the top, you'll find this section:

```python
CLASSES_TO_FETCH = [
    "Node",
    "Area3D",
    "Camera3D",
    "Input",
    "CharacterBody3D"
]
```

Edit this list to include only the classes you want. Class names must match the official Godot docs exactly (case-sensitive).

### 3. Run the scraper

```bash
python godot_docs_scraper.py
```

### 4. View the output

The script will create a folder called godot_docs_md/, and inside it, you'll find subfolders like:

```
godot_docs_md/
├── Area3D/
│   ├── Area3D_part_1.md
│   ├── Area3D_part_2.md
├── Node/
│   └── Node_part_1.md
```

Each file contains a chunk of the documentation in Markdown format.

## 🔒 License

This project is licensed under the MIT License — feel free to modify, share, or use it for commercial and personal projects.

## 🙏 Credits
Built with:

🐍 Python

🥣 BeautifulSoup4

🔧 Markdownify

📚 Godot Engine Docs
