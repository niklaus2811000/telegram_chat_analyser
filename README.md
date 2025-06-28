# Telegram Chat Analyzer (Python)

A simple Python tool that analyzes exported Telegram chat data in `.json` format. Helps digital forensics investigators review message patterns, media activity, and search for keywords.

---

## Features

- Counts messages sent by each user
- Summarizes shared media (photos, videos, files)
- Supports keyword-based message search
- Lightweight and fast

---

## Requirements

- Python 3.x
- No external libraries

---

## How to Export Telegram Data

1. Open Telegram Desktop  
2. Go to **Settings > Advanced > Export Telegram Data**  
3. Select chat(s) and **choose JSON format**  
4. Place the exported `.json` file in your project folder

---

## How to Run

```bash
python3 telegram_chat_analyzer.py
```

Follow prompts to enter:

Path to the .json file

(Optional) Keyword to search


## Sample Output
