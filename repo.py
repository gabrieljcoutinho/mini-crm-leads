from pathlib import Path
import json

DATA_DIR = Path(__file__).resolve().parent
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "leads.json"


def _load():
    if not DB_PATH.exists():
        return []

    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

def _save(leads):
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")

def create(lead_dict):
    read_leads = _load()
    read_leads.append(lead_dict)
    _save(read_leads)

