import json
from collections import defaultdict, Counter

def load_telegram_chat(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['messages']

def analyze_chat(messages):
    user_msg_count = Counter()
    media_count = defaultdict(int)

    for msg in messages:
        if msg['type'] != 'message':
            continue
        sender = msg.get('from', 'Unknown')
        user_msg_count[sender] += 1

        if 'photo' in msg:
            media_count['photos'] += 1
        if 'video' in msg:
            media_count['videos'] += 1
        if 'file' in msg:
            media_count['files'] += 1

    print("\n--- Message Count per User ---")
    for user, count in user_msg_count.most_common():
        print(f"{user}: {count} messages")

    print("\n--- Media Shared ---")
    for media_type, count in media_count.items():
        print(f"{media_type.capitalize()}: {count}")

def search_keyword(messages, keyword):
    print(f"\n--- Messages Containing '{keyword}' ---")
    for msg in messages:
        if msg['type'] == 'message' and 'text' in msg:
            if isinstance(msg['text'], list):  
                text = ''.join(str(part) for part in msg['text'] if isinstance(part, str))
            else:
                text = str(msg['text'])

            if keyword.lower() in text.lower():
                print(f"{msg.get('from', 'Unknown')} [{msg['date']}]: {text}")

def main():
    print("== Telegram Chat Analyzer ==")
    file_path = input("Enter path to exported Telegram .json file: ").strip()
    keyword = input("Enter a keyword to search (or leave blank to skip): ").strip()

    messages = load_telegram_chat(file_path)
    analyze_chat(messages)

    if keyword:
        search_keyword(messages, keyword)

if __name__ == "__main__":
    main()
