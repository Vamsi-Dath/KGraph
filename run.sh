clear
kill $(lsof -t -i:7860)
uv run main.py