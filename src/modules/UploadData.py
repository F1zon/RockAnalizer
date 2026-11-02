import openpyxl
import json
from pathlib import Path
from tkinter import Tk, filedialog

# 1. Окно выбора файла
root = Tk()
root.withdraw()
file_path = filedialog.askopenfilename(
    title="Выберите файл Excel",
    filetypes=[("Excel файлы", "*.xlsx *.xlsm"), ("Все файлы", "*.*")],
)
if not file_path:
    print("Файл не выбран")
    exit()

# 2. Читаем Excel
wb = openpyxl.load_workbook(file_path)
ws = wb.active

samples = []
for row in ws.iter_rows(min_row=2, values_only=True):
    number, test_type, value = row
    if value is not None:
        samples.append({
            "number": number,
            "type": test_type,
            "value": float(value),
        })

# 3. Находим data.json
out_path = Path(__file__).resolve().parent.parent / "data.json"

# 4. Загружаем существующий файл (stat сохранится), добавляем data
with open(out_path, "r", encoding="utf-8") as f:
    data = json.load(f)

data["data"] = samples  # готовый блок с образцами

# 5. Сохраняем обратно
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Добавлено {len(samples)} записей в блок 'data'")