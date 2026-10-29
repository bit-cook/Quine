#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Game of Life Quine - run with --play to animate.
import sys
_s = '#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n# Game of Life Quine - run with --play to animate.\nimport sys\n_s = %r\n_p = %r\nif "--play" in sys.argv:\n    exec(_p)\nelse:\n    print(_s %% (_s, _p))'
_p = 'import os, time\nGRID_SIZE = 20\ngrid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]\n\n\ndef init_glider():\n    grid[1][2] = 1\n    grid[2][3] = 1\n    grid[3][1] = 1\n    grid[3][2] = 1\n    grid[3][3] = 1\n\n\ndef count_neighbors(x, y):\n    c = 0\n    for dx in (-1, 0, 1):\n        for dy in (-1, 0, 1):\n            if dx == 0 and dy == 0:\n                continue\n            nx, ny = (x + dx) % GRID_SIZE, (y + dy) % GRID_SIZE\n            c += grid[nx][ny]\n    return c\n\n\ndef next_gen():\n    ng = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]\n    for x in range(GRID_SIZE):\n        for y in range(GRID_SIZE):\n            n = count_neighbors(x, y)\n            if grid[x][y] == 1:\n                ng[x][y] = 1 if n in (2, 3) else 0\n            else:\n                ng[x][y] = 1 if n == 3 else 0\n    return ng\n\n\ndef display():\n    print("\\n" + "=" * (GRID_SIZE * 2 + 2))\n    for y in range(GRID_SIZE):\n        print("|", end="")\n        for x in range(GRID_SIZE):\n            print("\\u2588\\u2588" if grid[x][y] else "  ", end="")\n        print("|")\n    print("=" * (GRID_SIZE * 2 + 2))\n\n\ninit_glider()\nfor gen in range(100):\n    os.system("clear" if os.name != "nt" else "cls")\n    print(f"Generation: {gen}")\n    display()\n    grid[:] = next_gen()\n    time.sleep(0.3)\n'
if "--play" in sys.argv:
    exec(_p)
else:
    print(_s % (_s, _p))
