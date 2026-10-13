# College Help Chatbot (Rule-Based Python Project)

A beginner-friendly college information chatbot built with Python `if/elif/else` rules. The project has both a terminal version and a browser interface powered by Streamlit. It does not use a language model or require an API key.

## Features

- Admissions and application guidance
- Courses and programs
- Fees and payment guidance
- College timings
- Exams, timetable, and results
- Attendance and leave
- Library and books
- Scholarships and financial aid
- Hostel and mess
- Transport and bus routes
- Placements, careers, and internships
- College contact guidance
- Greeting, help, thanks, goodbye, and fallback replies

> This is a demonstration project. It intentionally does not invent a specific college's fee amounts, schedules, or contact numbers. Users should confirm current details with their college's official office or website.

## Files

- `chatbot.py` - chatbot logic and terminal program (uses `if/elif/else`)
- `app.py` - web chat UI for Streamlit
- `test_chatbot.py` - basic unit tests
- `requirements.txt` - web app dependency
- `College_Chatbot_Report.pdf` - project report and sample conversations (also provided separately in the download bundle)

## Run the terminal chatbot

1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Run:

   ```bash
   python chatbot.py
   ```

4. Type a college-related question. Type `exit` to stop.

No third-party package is needed for the terminal version.

## Run the web chatbot locally

1. Install Python 3.10 or newer.
2. In the project folder, run:

   ```bash
   python -m pip install -r requirements.txt
   streamlit run app.py
   ```

3. Open the local URL shown in the terminal (usually `http://localhost:8501`).

## Run tests

```bash
python -m unittest -v test_chatbot.py
```

## Publish to GitHub

The project is ready to upload, but a public repository URL does not exist until you create/publish it from your own GitHub account.

1. Sign in at https://github.com/new and create a repository named `college-help-chatbot`.
2. Upload the files in this folder, or use Git from a terminal:

   ```bash
   git init
   git add .
   git commit -m "Add college help chatbot project"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/college-help-chatbot.git
   git push -u origin main
   ```

3. Replace `YOUR-USERNAME` with your GitHub username. Your repository URL will then be `https://github.com/YOUR-USERNAME/college-help-chatbot`.

## Deploy a live web version

Streamlit Community Cloud can host the browser version from a GitHub repository:

1. Publish the project to GitHub using the instructions above.
2. Open https://share.streamlit.io/ and sign in with GitHub.
3. Choose **Create app**, select your repository and `main` branch, and set the app file path to `app.py`.
4. Choose an available app subdomain and deploy.
5. Copy the actual app URL shown after deployment. It will be under `https://...streamlit.app`.

Official deployment guide: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy

## Current publication status

- GitHub repository: not yet published; replace `YOUR-USERNAME` after creating the repository.
- Live web link: not yet deployed; Streamlit creates the actual URL after deployment.

These are deliberately marked as pending rather than presenting fabricated links.
