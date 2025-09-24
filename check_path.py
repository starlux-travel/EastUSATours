# check_path.py
import os
import sys
from pathlib import Path

# 專案根目錄 (manage.py 的位置)
BASE_DIR = Path(__file__).resolve().parent
print("BASE_DIR =", BASE_DIR)

# 確保根目錄在 sys.path 裡
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

print("\n=== sys.path ===")
for p in sys.path:
    print(p)

print("\n=== Import test ===")
try:
    import eastusatours
    print("✅ 成功匯入 eastusatours")
    print("eastusatours package 的位置:", eastusatours.__file__)
except Exception as e:
    print("❌ 匯入失敗:", e)
