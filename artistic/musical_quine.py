#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
音乐 Quine

输出源代码，源代码中包含一个可以播放的旋律。

使用方法:
    python musical_quine.py           # 输出源代码（Quine 模式）
    python musical_quine.py --play    # 播放旋律
"""

import sys

# 旋律定义 (简谱表示)
MELODY = [
    ("1", 0.5), ("2", 0.5), ("3", 0.5), ("4", 0.5),
    ("5", 0.5), ("6", 0.5), ("7", 0.5), ("i", 1.0),  # 音阶上行
    ("i", 0.5), ("7", 0.5), ("6", 0.5), ("5", 0.5),
    ("4", 0.5), ("3", 0.5), ("2", 0.5), ("1", 1.0),  # 音阶下行
]

# 频率映射 (简化)
FREQS = {
    "1": 262,  # C4
    "2": 294,  # D4
    "3": 330,  # E4
    "4": 349,  # F4
    "5": 392,  # G4
    "6": 440,  # A4
    "7": 494,  # B4
    "i": 523,  # C5
}

SOURCE = '''#!/usr/bin/env python3
"""
音乐 Quine

输出源代码，源代码中包含一个可以播放的旋律。

使用方法:
    python musical_quine.py           # 输出源代码（Quine 模式）
    python musical_quine.py --play    # 播放旋律
"""

import sys

# 旋律定义 (简谱表示)
MELODY = [
    ("1", 0.5), ("2", 0.5), ("3", 0.5), ("4", 0.5),
    ("5", 0.5), ("6", 0.5), ("7", 0.5), ("i", 1.0),  # 音阶上行
    ("i", 0.5), ("7", 0.5), ("6", 0.5), ("5", 0.5),
    ("4", 0.5), ("3", 0.5), ("2", 0.5), ("1", 1.0),  # 音阶下行
]

# 频率映射 (简化)
FREQS = {
    "1": 262,  # C4
    "2": 294,  # D4
    "3": 330,  # E4
    "4": 349,  # F4
    "5": 392,  # G4
    "6": 440,  # A4
    "7": 494,  # B4
    "i": 523,  # C5
}

SOURCE = %r

def play_tone(freq, duration):
    """播放一个音符 (跨平台简化版)"""
    import math
    import time
    
    try:
        # Windows
        import winsound
        winsound.Beep(freq, int(duration * 1000))
    except ImportError:
        try:
            # Unix/Linux/Mac
            import os
            os.system(f'play -nq -t alsa synth {duration} sine {freq} 2>/dev/null')
        except:
            # 纯 Python 回退（打印音符）
            print(f"♪ {freq}Hz ({duration}s)", end=" ", flush=True)
            time.sleep(duration)

def play_melody():
    """播放旋律"""
    print("Playing melody...")
    for note, duration in MELODY:
        freq = FREQS.get(note, 440)
        play_tone(freq, duration)
    print("\\nDone!")

if __name__ == '__main__':
    if '--play' in sys.argv:
        play_melody()
    else:
        print(SOURCE %% SOURCE)
'''

def play_tone(freq, duration):
    """播放一个音符 (跨平台简化版)"""
    import math
    import time
    
    try:
        # Windows
        import winsound
        winsound.Beep(freq, int(duration * 1000))
    except ImportError:
        try:
            # Unix/Linux/Mac
            import os
            os.system(f'play -nq -t alsa synth {duration} sine {freq} 2>/dev/null')
        except:
            # 纯 Python 回退（打印音符）
            print(f"♪ {freq}Hz ({duration}s)", end=" ", flush=True)
            time.sleep(duration)

def play_melody():
    """播放旋律"""
    print("Playing melody...")
    for note, duration in MELODY:
        freq = FREQS.get(note, 440)
        play_tone(freq, duration)
    print("\nDone!")

if __name__ == '__main__':
    if '--play' in sys.argv:
        play_melody()
    else:
        print(SOURCE % SOURCE)
