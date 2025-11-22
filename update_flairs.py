import praw
import json
import time
import re

# --- Regex that removes all emoji-like characters ---
EMOJI_PATTERN = re.compile(
    "[" 
    "\U0001F600-\U0001F64F"  # Emoticons
    "\U0001F300-\U0001F5FF"  # Symbols & pictographs
    "\U0001F680-\U0001F6FF"  # Transport & map symbols
    "\U0001F1E0-\U0001F1FF"  # Flags
    "\U00002702-\U000027B0"  # Dingbats
    "\U000024C2-\U0001F251" 
    "]+",
    flags=re.UNICODE
)

def remove_emojis(text: str) -> str:
    return EMOJI_PATTERN.sub("", text).strip()

def main():
    # --- Load configuration ---
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
        subreddit_name = config.get("subreddit")
        flair_map = config.get("flair_map", {})
        if not subreddit_name:
            raise ValueError("Subreddit name not found in config.json")
        if not flair_map:
            print("Warning: flair_map is empty in config.json")
    except FileNotFoundError:
        print("config.json not found! Please create it with your subreddit and flair_map.")
        return

    # --- Initialize Reddit ---
    reddit = praw.Reddit("default")
    subreddit = reddit.subreddit(subreddit_name)

    # --- Update posts ---
    updated_count = 0

    for submission in subreddit.new(limit=None):
        raw_flair = submission.link_flair_text or ""
        cleaned_flair = remove_emojis(raw_flair)

        if cleaned_flair in flair_map:
            new_id = flair_map[cleaned_flair]
            submission.mod.flair(flair_template_id=new_id)
            updated_count += 1
            print(f"✅ Updated: {submission.title} → '{raw_flair}' cleaned to '{cleaned_flair}', matched '{cleaned_flair}'")
            # Respect API limits
            # Reddit allows 100 requests per minute
            # So 1 second delay between requests is safe
            time.sleep(1)  

    print(f"\n🎉 Done! Updated {updated_count} posts in total.")

if __name__ == "__main__":
    main()
