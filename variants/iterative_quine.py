#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Iterative Quine (self-contained 2-cycle): A -> B -> A
n = 0
N = 2
s = '#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n# Iterative Quine (self-contained 2-cycle): A -> B -> A\nn = %d\nN = %d\ns = %r\nprint(s %% ((n + 1) %% N, N, s))'
print(s % ((n + 1) % N, N, s))
