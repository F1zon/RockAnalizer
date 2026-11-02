import json
import statistics as st

from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class Stat:
    sample_size: float
    average: float
    standard_deviation: float
    coefficient_variation: float
    min: float
    max: float
    median: float
    moda: float
    excess: float
    asymmetry: float

path = Path(__file__).resolve().parent.parent / "data.json"


def analiz(records):
    values = [float(r["value"]) for r in records]
    # Массив выглядит примерно вот так: values = [67.0, 42.5, 90.0]
    # Вот тут писюкать...

    n = len(values)
    mean = sum(values) / n

    ###

    return Stat(
        sample_size=n,
        average=mean,
        standard_deviation=0,
        coefficient_variation=0,
        min=min(values),
        max=max(values),
        median=st.median(values),
        moda=st.mode(values),
        excess=0.0,
        asymmetry=0.0,
    )

data = {}
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

records = data.get("data", [])

if records:
    stats = analiz(records)
    data["stat"] = asdict(stats)
else:
    print("Блок 'data' пустой или отсутствует")
    stats = Stat(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    data["stat"] = asdict(stats)

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)