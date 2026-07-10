import json
import re

transcript_path = r"C:\Users\12a5n\.gemini\antigravity-ide\brain\9384e8ca-e99d-4434-9ef4-d130f9fbe9d7\.system_generated\logs\transcript_full.jsonl"
with open(transcript_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

last_user_input = None
for line in reversed(lines):
    data = json.loads(line)
    if data.get('type') == 'USER_INPUT':
        last_user_input = data.get('content', '')
        break

print("Length of last user input:", len(last_user_input))

parts = re.split(r'\bTIẾNG ANH\b', last_user_input, flags=re.IGNORECASE)
print("Parts count:", len(parts))
if len(parts) > 1:
    en_part = parts[1].strip()
else:
    en_part = last_user_input.strip()

print("EN part sample (first 500 chars):")
print(en_part[:500])

en_weeks = re.split(r'\b(?:TUẦN|WEEK)\s+(\d+)\b', en_part, flags=re.IGNORECASE)
print("en_weeks length:", len(en_weeks))
for i in range(1, len(en_weeks), 2):
    w_num = int(en_weeks[i])
    w_content = en_weeks[i+1].strip()
    print(f"Week {w_num} parsed content length: {len(w_content)}")
