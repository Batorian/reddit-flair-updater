# Reddit Flair Updater

Bulk-update post flairs in a subreddit using Python and PRAW. Designed for moderators to easily update existing posts after renaming or reorganizing flair templates.  

This repository contains **two separate scripts**:

1. `list_flairs.py` — Lists all flair templates and their IDs for a subreddit.  
2. `update_flairs.py` — Updates old flairs to new templates on posts based on a user-provided flair map.  

---

## Table of Contents

- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Configuration (`praw.ini` & `config.json`)](#configuration-prawini--configjson)  
- [Listing Flairs](#listing-flairs)  
- [Updating Post Flairs](#updating-post-flairs)  
- [Tips and Safety](#tips-and-safety)  
- [Security](#security)  

---

## Features

- Lists all link flair templates with their IDs  
- Updates old flairs to new templates on existing posts  
- Modular design with `main()` functions for clean code and safe importing  
- Fully configurable via `config.json`  

---

## Prerequisites

- Python 3.8+  
- A Reddit account with moderator permissions on the subreddit  
- A Reddit API app (script type)  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/reddit-flair-updater.git
cd reddit-flair-updater
````

2. Create a Python virtual environment and activate it:

```bash
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration (`praw.ini` & `config.json`)

### 1. Create `praw.ini` for Reddit credentials

Create a file named `praw.ini` in the project folder with the following content:

```ini
[default]
client_id=YOUR_CLIENT_ID
client_secret=YOUR_CLIENT_SECRET
username=YOUR_REDDIT_USERNAME
password=YOUR_REDDIT_PASSWORD
user_agent=FlairUpdater by u/YOUR_REDDIT_USERNAME
```

**Replace placeholders:**

* `YOUR_CLIENT_ID` → from your Reddit script app (string below your app name)
* `YOUR_CLIENT_SECRET` → from your Reddit script app
* `YOUR_REDDIT_USERNAME` → your Reddit username
* `YOUR_REDDIT_PASSWORD` → your Reddit password
* `user_agent` → can be any descriptive string, e.g., `"FlairUpdaterBot by u/YourUsername"`

**Test your credentials**:

```python
import praw
reddit = praw.Reddit("default")
print(reddit.user.me())  # Should print your Reddit username
```

---

### 2. Create `config.json` for subreddit & flair map

Create a file named `config.json` in the project folder with **placeholders**:

```json
{
  "subreddit": "YOUR_SUBREDDIT",
  "flair_map": {
    "OLD_FLAIR_1": "NEW_FLAIR_TEMPLATE_ID_1",
    "OLD_FLAIR_2": "NEW_FLAIR_TEMPLATE_ID_2"
  }
}
```

**How to replace placeholders:**

* `YOUR_SUBREDDIT` → the subreddit you want to update (without `r/`)
* `OLD_FLAIR_1`, `OLD_FLAIR_2` → the **current flair text** of posts you want to change
* `NEW_FLAIR_TEMPLATE_ID_1`, etc. → the **flair template IDs** for the new flairs (use `list_flairs.py` to get them)

**Example after replacing placeholders:**

```json
{
  "subreddit": "YourSubreddit",
  "flair_map": {
    "Old_Discussion_Flair": "d373b1ba-5e7e-11f0-870e-7aef208a0ad8",
    "Old_Video_Flair": "61220302-bbac-11ef-b53d-22870e36641c"
  }
}
```

---

### Notes:

* The scripts read `subreddit` and `flair_map` directly from `config.json`, so **no changes to the Python scripts are needed** for different subreddits.
* Always verify flair IDs using `list_flairs.py` before running `update_flairs.py`.

---

## Listing Flairs

If you don’t know your flair template IDs:

1. Run the listing script:

```bash
python list_flairs.py
```

2. It reads the `subreddit` from `config.json` and prints all link flair templates in the format:

```
New_Discussion_Flair — d373b1ba-5e7e-11f0-870e-7aef208a0ad8
New_Video_Flair — 61220302-bbac-11ef-b53d-22870e36641c
...
```

3. Copy the IDs into `config.json` to build your `flair_map`.

---

## Updating Post Flairs

1. Ensure `config.json` contains your `subreddit` and `flair_map`.
2. Run the update script:

```bash
python update_flairs.py
```

3. The script loops through posts and updates old flairs to new templates. Progress is printed to the console.

---

## Tips and Safety

* **Test first**: use `limit=10` in `update_flairs.py` during testing.
* **API rate limits**: the script includes `time.sleep(2)` between updates.
* **Filtering posts**: you can modify the script to target `.new()`, `.top()`, or `.search()` results.
* **Dry-run option**: modify the script to print matched posts without updating for safety.

---

## Security

* Never commit `praw.ini` or `config.json` to public repositories, they contain sensitive credentials and flair IDs.
* `.gitignore` is already configured to exclude them.

---

## License

MIT License – free to use, modify, and distribute.

---