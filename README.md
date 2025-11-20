# TG User Collector

A Telegram bot for collecting user data, built with Python (Aiogram) and PostgreSQL.

## Prerequisites

- Python 3.9+ and PostgreSQL (for local SQLite execution)

## Getting Started

1. **Environment Setup**
   Create a `.env` file in the root directory. You can use the example below:
   ```env
   BOT_TOKEN=your_telegram_bot_token
   DATABASE_URL=sqlite+aiosqlite:///./bot.db
   # Add other required variables here
   ```

## Running with Docker

The easiest way to run the bot is using Docker Compose. This will set up both the bot and the database automatically.

```bash
docker-compose up -d --build
```

- **Stop the bot:** `docker-compose down`
- **View logs:** `docker-compose logs -f`

## Running Locally

If you prefer to run without Docker:

1. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

2. **Activate virtual environment**
   ```bash
   source venv/bin/activate  # On Linux/Mac
   .\venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the bot**
   ```bash
   python main.py
   ```
