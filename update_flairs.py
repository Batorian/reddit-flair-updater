import praw
import time

# Initialize Reddit instance (reads from praw.ini)
reddit = praw.Reddit("default")
subreddit = reddit.subreddit("DispatchAdHoc")

# Map old flair text → new template ID
flair_map = {
    "News": "d373b1ba-5e7e-11f0-870e-22870e36641c",
    "Discussion": "61220302-bbac-11ef-b53d-7aef208a0ad8",
    "Art": "6e28f7e0-bbac-11ef-b9f4-16810934b5ba",
    "Video": "79626ebc-c49d-11ef-8cea-8e895bdd6200",
    "Meme": "f19b90cc-09bf-11f0-99c2-5ee939dc1e29",
}

# List current flair templates
print("Fetching flair templates...")
for flair in subreddit.flair.link_templates:
    print(f"{flair['text']} — {flair['id']}")

# Update posts
for submission in subreddit.new(limit=10): # adjust limit as needed
    old_flair = submission.link_flair_text
    if old_flair in flair_map:
        new_id = flair_map[old_flair]
        submission.flair.select(new_id)
        print(f"Updated: {submission.title}")
        time.sleep(2)  # avoid rate limits