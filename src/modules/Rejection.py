import json
import statistics as st

from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class Reject:
    reject_data: []

path = Path(__file__).resolve().parent.parent / "data.json"


# Функция отбраковки
def rejection(records):
    values = [float(r["value"]) for r in records]


data = {}
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

records = data.get("data", [])

if records:
    rejects = rejection(records)
    data["reject_data"] = asdict(rejects)
else:
    print("Блок 'data' пустой или отсутствует")
    rejects = Reject([])
    data["reject_data"] = asdict(rejects)