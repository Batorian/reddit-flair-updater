import praw
import json
import time

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
    for submission in subreddit.new(limit=None):
        old_flair = submission.link_flair_text
        if old_flair in flair_map:
            new_id = flair_map[old_flair]
            submission.mod.flair(flair_template_id=new_id)
            print(f"✅ Updated: {submission.title} → {old_flair}")
            time.sleep(2)

if __name__ == "__main__":
    main()
