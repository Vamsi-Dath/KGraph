from pathlib import Path
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).parent.parent.parent

if Path(ROOT_DIR / ".env").exists():
    load_dotenv(ROOT_DIR / ".env")