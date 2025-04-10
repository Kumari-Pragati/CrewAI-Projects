
# 🧠 AI Blog Creator with CrewAI

This project leverages **CrewAI agents** to automate blog creation by combining a **Blog Researcher** and a **Blog Writer**, both backed by LLMs. These agents work together to produce an SEO-optimized, insightful blog post based on a given topic — starting from idea generation to writing full content.

---

## 📁 Project Structure

```
├── crew.py               # Main script to run the Crew
├── MyAgents.py           # Agent definitions (roles, goals, tools)
├── MyTasks.py            # Tasks assigned to the agents
├── MyTools.py            # Custom tool: Medium search
├── requirements.txt      # Required dependencies
├── output.txt            # Sample console output
└── new_blog_post.md      # Final generated blog post
```

---

## 🚀 Features

- 🤖 Two AI agents (researcher + writer)
- 📚 Research powered by Medium search
- 🧠 Agent memory and delegation
- 📄 Markdown output generation
- ✅ Fully automated multi-agent pipeline

---

## ⚙️ Setup Instructions

> 💡 **Note**: Python 3.11+ is required due to use of `typing.Self`. This project uses **Conda** for environment management.

### 🔧 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 🏗️ Step 2: Create a Conda Environment

```bash
conda create -p venv python=3.11
```

### ▶️ Step 3: Activate the Environment

```bash
conda activate ./venv
```

### 📦 Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### 🧪 Step 5: Add Your OpenAI API Key

Create a `.env` file in the root directory and add:

```
OPENAI_API_KEY=your_openai_key_here
```

---

## 🚀 Run the Project

```bash
python crew.py
```

> This will initiate the agents, who will collaborate to research and write a blog on the topic **"AI in Healthcare"**. The final blog will be saved as `new_blog_post.md`.

---

## 📄 Sample Output

The result will look like this:

- ✍️ Title: **Emerging Trends and Innovations in AI-Driven Healthcare**
- 📄 Location: `new_blog_post.md`
- 📑 Logs: View detailed execution steps in `output.txt`

---

## 🔐 Dependencies

Listed in `requirements.txt`:

```txt
crewai
crewai_tools
load_dotenv
```

Install them anytime with:

```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Agents Used

| Agent          | Description                                      |
|----------------|--------------------------------------------------|
| Blog Researcher| Suggests 10 blog ideas for the given topic       |
| Blog Writer    | Generates a complete blog post from the research |

---

## 🔎 Tool Used

- `WebsiteSearchTool` is configured to fetch context from:
  ```
  https://medium.com/
  ```

---

## 📌 Notes

- Works best with an active internet connection for search tools.
- Ensure the `.env` file contains a valid OpenAI API key.
- Run the project in Python 3.11+ Conda environment.

---

## 💡 Want to Contribute?

Feel free to fork and contribute!

