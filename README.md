
---
```markdown
# 🎥 YouTube Manager CLI App

This is a simple **YouTube Video Manager** CLI-based Python application that allows users to **Add**, **View**, **Update**, and **Delete** video details. All data is stored persistently in a `youtube.txt` file using JSON format.

---

## ✨ Features

- 📥 Add new video (name and duration)
- 📃 List all saved videos
- ✏️ Update existing video details
- ❌ Delete any video
- 💾 Persistent storage using `youtube.txt`
- 🧠 Clean, modular code structure

---

## 🛠️ Tech Stack

- Python 3
- File Handling
- JSON module

---

## 📂 Project Structure

```

youtube\_manager/
├── youtube.txt           # Data file storing videos (auto-created)
├── youtube\_manager.py    # Main Python script

````

---

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/youtube-manager.git
cd youtube-manager
````

### 2. Run the application

```bash
python youtube_manager.py
```

---

## 📸 Sample Usage

```text
----Youtube Manager----| Enter your choice
1. Add a youtube video
2. List all videos
3. Update a youtube video
4. Delete a youtube video
5. Exit the application
```

---

## 📄 File Format (`youtube.txt`)

Data is stored in JSON format:

```json
[
    {"name": "Python Tutorial", "time": "12:30"},
    {"name": "React Crash Course", "time": "20:45"}
]
```

---

## 🧪 Functions Overview

| Function Name        | Description                                 |
| -------------------- | ------------------------------------------- |
| `load_data()`        | Loads video data from `youtube.txt`         |
| `save_data_helper()` | Saves video data to file                    |
| `add_video()`        | Adds a new video                            |
| `list_all_videos()`  | Displays all saved videos                   |
| `update_video()`     | Updates video name/duration by index        |
| `delete_video()`     | Deletes a video by index                    |
| `main()`             | Main driver loop using match-case structure |

---

## ✅ Requirements

* Python 3.10 or later (for `match-case` syntax)

---

## Acknowledgement

- I would like to thank the youtube channel chai aur code which helped me throughout the journey of building this application via his youtube video.

  
## 👨‍💻 Author

**Bhavya Singh**
[GitHub](https://github.com/your-username)
Feel free to contribute or suggest improvements!


```
