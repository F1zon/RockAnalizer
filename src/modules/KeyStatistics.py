import json

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

sample_size = 0
average = 0
standard_deviation = 0
coefficient_variation = 0
min = 0
max = 0
median = 0
moda = 0
excess = 0
asymmetry = 0

# Тут код писюкать...



####

stats = Stat(sample_size=sample_size, average=average, standard_deviation=standard_deviation,
             coefficient_variation=coefficient_variation, min=min, max=max,
             median=median, moda=moda, excess=excess, asymmetry=asymmetry)

with open(path, "w", encoding="utf-8") as f:
    json.dump(asdict(stats), f, ensure_ascii=False, indent=2)