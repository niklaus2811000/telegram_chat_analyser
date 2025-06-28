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

```bash
== Telegram Chat Analyzer ==
Enter path to exported Telegram .json file: /Users/ayn/Downloads/ChatExport_2025-06-28/result.json
Enter a keyword to search (or leave blank to skip): hello

--- Message Count per User ---
klaus: 25 messages
Kushal Home: 17 messages

--- Media Shared ---
Photos: 1

--- Messages Containing 'hello' ---
klaus [2025-06-27T22:34:42]: hello
Kushal Home [2025-06-27T22:35:04]: Hello
```
