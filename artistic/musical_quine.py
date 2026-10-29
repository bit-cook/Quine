#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Musical Quine - run with --play to hear the melody.
import sys
_s = '#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n# Musical Quine - run with --play to hear the melody.\nimport sys\n_s = %r\n_p = %r\nif "--play" in sys.argv:\n    exec(_p)\nelse:\n    print(_s %% (_s, _p))'
_p = 'import time\nMELODY = [("1", .4), ("2", .4), ("3", .4), ("4", .4), ("5", .4), ("6", .4),\n          ("7", .4), ("i", .8), ("i", .4), ("7", .4), ("6", .4), ("5", .4),\n          ("4", .4), ("3", .4), ("2", .4), ("1", .8)]\nFREQS = {"1": 262, "2": 294, "3": 330, "4": 349, "5": 392, "6": 440, "7": 494, "i": 523}\n\n\ndef tone(freq, dur):\n    try:\n        import winsound\n        winsound.Beep(freq, int(dur * 1000))\n        return\n    except ImportError:\n        pass\n    try:\n        import os\n        os.system(f"play -nq -t alsa synth {dur} sine {freq} 2>/dev/null")\n        return\n    except Exception:\n        pass\n    print(f"\\u266a {freq}Hz", end=" ", flush=True)\n    time.sleep(dur)\n\n\nprint("Playing melody...")\nfor note, dur in MELODY:\n    tone(FREQS.get(note, 440), dur)\nprint("\\nDone!")\n'
if "--play" in sys.argv:
    exec(_p)
else:
    print(_s % (_s, _p))
