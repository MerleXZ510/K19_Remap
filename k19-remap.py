#!/usr/bin/env python3
from evdev import InputDevice, ecodes, UInput
import os, time

def find_k19_device():
    base = "/dev/input/by-id"
    for fname in os.listdir(base):
        if "Keycool" in fname and "kbd" in fname:
            return os.path.join(base, fname)
    return None

DEVICE = None
while DEVICE is None:
    DEVICE = find_k19_device()
    if DEVICE is None:
        print("Waiting for K19 keyboard...")
        time.sleep(1)

print("Using device:", DEVICE)
dev = InputDevice(DEVICE)

dev = InputDevice(DEVICE)
ui = UInput()
dev.grab()  # 搶佔裝置，避免原始輸入送到系統

# 定義映射表
keymap = {
    ecodes.KEY_KP0: ecodes.KEY_0,
    ecodes.KEY_KP1: ecodes.KEY_1,
    ecodes.KEY_KP2: ecodes.KEY_2,
    ecodes.KEY_KP3: ecodes.KEY_3,
    ecodes.KEY_KP4: ecodes.KEY_4,
    ecodes.KEY_KP5: ecodes.KEY_5,
    ecodes.KEY_KP6: ecodes.KEY_6,
    ecodes.KEY_KP7: ecodes.KEY_7,
    ecodes.KEY_KP8: ecodes.KEY_8,
    ecodes.KEY_KP9: ecodes.KEY_9,
    ecodes.KEY_KPENTER: ecodes.KEY_LEFTCTRL,
    ecodes.KEY_KPPLUS: ecodes.KEY_LEFTALT,
    # 建議可再加：
    # ecodes.KEY_KPMINUS: ecodes.KEY_LEFTSHIFT,
    # ecodes.KEY_KPASTERISK: ecodes.KEY_LEFTMETA,  # Super / Win
    # ecodes.KEY_KPSLASH: ecodes.KEY_ESC,
}

print("K19 remapper running... using", DEVICE)

for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        code, val = event.code, event.value
        if code in keymap:
            ui.write(ecodes.EV_KEY, keymap[code], val)
        ui.syn()


