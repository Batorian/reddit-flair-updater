import praw
import json

def main():
    # --- Load configuration ---
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
        subreddit_name = config.get("subreddit")
        if not subreddit_name:
            raise ValueError("Subreddit name not found in config.json")
    except FileNotFoundError:
        print("config.json not found! Please create it with your subreddit and optional flair_map.")
        return

    # --- Initialize Reddit ---
    reddit = praw.Reddit("default")
    subreddit = reddit.subreddit(subreddit_name)

    # --- List all link flair templates ---
    print(f"\nLink flair templates for r/{subreddit_name}:")
    for flair in subreddit.flair.link_templates:
        print(f"{flair['text']} — {flair['id']}")

if __name__ == "__main__":
    main()
