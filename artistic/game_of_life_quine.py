#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生命游戏 Quine

一个可以运行的生命游戏实现，同时也是一个 Quine。

使用方法:
    直接运行查看源代码（Quine 模式）
    python game_of_life_quine.py --play  运行游戏
"""

import sys

# 生命游戏的源代码
SOURCE = '''#!/usr/bin/env python3
"""
生命游戏 Quine

一个可以运行的生命游戏实现，同时也是一个 Quine。

使用方法:
    直接运行查看源代码（Quine 模式）
    python game_of_life_quine.py --play  运行游戏
"""

import sys

# 生命游戏的源代码
SOURCE = %r

# 游戏状态
GRID_SIZE = 20
grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

# 初始化一个滑翔机图案
def init_glider():
    """初始化滑翔机"""
    grid[1][2] = 1
    grid[2][3] = 1
    grid[3][1] = 1
    grid[3][2] = 1
    grid[3][3] = 1

def count_neighbors(x, y):
    """计算邻居数量"""
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = (x + dx) % GRID_SIZE, (y + dy) % GRID_SIZE
            count += grid[nx][ny]
    return count

def next_generation():
    """计算下一代"""
    new_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            neighbors = count_neighbors(x, y)
            if grid[x][y] == 1:
                # 活着的细胞
                if neighbors in [2, 3]:
                    new_grid[x][y] = 1
            else:
                # 死细胞
                if neighbors == 3:
                    new_grid[x][y] = 1
    return new_grid

def display():
    """显示网格"""
    print("\\n" + "=" * (GRID_SIZE * 2 + 2))
    for y in range(GRID_SIZE):
        print("|", end="")
        for x in range(GRID_SIZE):
            print("██" if grid[x][y] else "  ", end="")
        print("|")
    print("=" * (GRID_SIZE * 2 + 2))

def run_game(generations=100):
    """运行游戏"""
    init_glider()
    import time
    import os
    
    for gen in range(generations):
        os.system('clear' if os.name != 'nt' else 'cls')
        print(f"Generation: {gen}")
        display()
        grid[:] = next_generation()
        time.sleep(0.5)

if __name__ == '__main__':
    if '--play' in sys.argv:
        run_game()
    else:
        # Quine 模式: 输出源代码
        print(SOURCE %% SOURCE)
'''

# 游戏状态
GRID_SIZE = 20
grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

# 初始化一个滑翔机图案
def init_glider():
    """初始化滑翔机"""
    grid[1][2] = 1
    grid[2][3] = 1
    grid[3][1] = 1
    grid[3][2] = 1
    grid[3][3] = 1

def count_neighbors(x, y):
    """计算邻居数量"""
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = (x + dx) % GRID_SIZE, (y + dy) % GRID_SIZE
            count += grid[nx][ny]
    return count

def next_generation():
    """计算下一代"""
    new_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            neighbors = count_neighbors(x, y)
            if grid[x][y] == 1:
                # 活着的细胞
                if neighbors in [2, 3]:
                    new_grid[x][y] = 1
            else:
                # 死细胞
                if neighbors == 3:
                    new_grid[x][y] = 1
    return new_grid

def display():
    """显示网格"""
    print("\n" + "=" * (GRID_SIZE * 2 + 2))
    for y in range(GRID_SIZE):
        print("|", end="")
        for x in range(GRID_SIZE):
            print("██" if grid[x][y] else "  ", end="")
        print("|")
    print("=" * (GRID_SIZE * 2 + 2))

def run_game(generations=100):
    """运行游戏"""
    init_glider()
    import time
    import os
    
    for gen in range(generations):
        os.system('clear' if os.name != 'nt' else 'cls')
        print(f"Generation: {gen}")
        display()
        grid[:] = next_generation()
        time.sleep(0.5)

if __name__ == '__main__':
    if '--play' in sys.argv:
        run_game()
    else:
        # Quine 模式: 输出源代码
        print(SOURCE % SOURCE)
