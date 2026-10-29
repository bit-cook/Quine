#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ouroboros: a self-contained 2-cycle that is valid under both
# Python 2 and Python 3 (A -> B -> A). Run it twice to return to start.
from __future__ import print_function
n = 0
N = 2
s = '#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n# Ouroboros: a self-contained 2-cycle that is valid under both\n# Python 2 and Python 3 (A -> B -> A). Run it twice to return to start.\nfrom __future__ import print_function\nn = %d\nN = %d\ns = %r\nprint(s %% ((n + 1) %% N, N, s))'
print(s % ((n + 1) % N, N, s))
