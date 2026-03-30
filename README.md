# ACM San Francisco Bay Area AI Agent Workshop Setup Guide  

Hands-on Session Requirements:

Today, we will utilize LLM via API by signing up for GROQ Inference (which offers a free trial) or XAI-Grok2 API (which provides a free tier in exchange for sharing content).
Alternatively, you can run an LLM locally, but you'll also need to run the Colab Notebook locally. (Optional Tools: ollama, LLM Studio)


Colab is available here: https://gist.github.com/marscod/9e1cd2dfd07d8448d52214a63851a394

Follow these steps to set up your environment:  

## 1. Fork the Repository  
Click the **Fork** button on GitHub to create your own copy of the repository.  

## 2. Open the Forked Repository in GitHub Codespaces  
Modify the URL by replacing `github.com` with `github.dev`.  

## 3. Sign in to GitHub  
Sign in using your GitHub account to proceed.  

## 4. Select a Deployment  
A minimal resource allocation (e.g., **2 cores**) is sufficient.  

> ⚠️ **Note:** To avoid unnecessary charges, stop the server once you complete the task, even if it is idle.  
> Open [GitHub Codespaces](https://github.com/codespaces), select `...` for the codespace, and choose **Stop**.  

## 5. Wait for VS Code to Launch  
The environment will open in **Visual Studio Code**, and Python installation will begin automatically.  

## 6. Open the Terminal  
Access the terminal from the **VS Code** interface.  

## 7. Run the Required Commands  
Follow the instructions in the repository to set up your environment.  

```bash
./setup.sh
source venv/bin/activate
```

### Run Server
```bash
./run.sh
```

8. (Optional) Make the Server Public  
If needed, you can expose the port to the public, allowing others to access your server.  

# Contribution
We welcome contributions! Feel free to submit a Pull Request (PR) from your forked repository.

## Slack Loop (Codex-style) Setup

If you want to run the workshop agent from Slack using an event loop, you can wire it up with Slack Socket Mode.

1. Create a Slack app at https://api.slack.com/apps.
2. Enable **Socket Mode** and copy your app-level token (`xapp-...`).
3. Add bot token scopes: `app_mentions:read`, `channels:history`, and `chat:write`.
4. Install the app to your workspace and copy the bot token (`xoxb-...`).
5. Add the following keys to your `.env` file:

```bash
SLACK_BOT_TOKEN=xoxb-...
SLACK_APP_TOKEN=xapp-...
SLACK_DEFAULT_HOST=xai
XAI_API_KEY=...
# or GROQ_API_KEY=... if you set SLACK_DEFAULT_HOST=groq
```

Run the Slack loop:

```bash
source venv/bin/activate
python slack_codex_loop.py
```

Then mention the bot in Slack, for example: `@your-bot summarize today's AI news`.
