# 自包含衔尾蛇链节点 (self-contained Ouroboros node)
n = 2
N = 3
s = '# 自包含衔尾蛇链节点 (self-contained Ouroboros node)\nn = %d\nN = %d\ns = %r\nprint(s %% ((n + 1) %% N, N, s))'
print(s % ((n + 1) % N, N, s))
