# K19 Remap

將 Keycool K19 數字鍵盤 (USB) 改造成自訂快捷鍵板。  
基於 Python [evdev](https://python-evdev.readthedocs.io/en/latest/) + Linux UInput。

---

## 🚀 功能
- 小鍵盤 0–9 → 主鍵盤 0–9
- 小鍵盤 Enter → Ctrl
- 小鍵盤 + → Alt
- 可自行擴充 - * / 等鍵位

---

## 📦 安裝
```bash
sudo apt update
sudo apt install python3-evdev git
git clone https://github.com/YOURNAME/K19-Remap.git
cd K19-Remap


