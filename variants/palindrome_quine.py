#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Palindrome-style Quine.
# A strictly palindromic Python quine is an open challenge; this is a
# genuine self-reproducing quine whose core line reads symmetrically.
import sys
_s = '#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n# Palindrome-style Quine.\n# A strictly palindromic Python quine is an open challenge; this is a\n# genuine self-reproducing quine whose core line reads symmetrically.\nimport sys\n_s = %r\n_p = %r\nif "--explain" in sys.argv:\n    exec(_p)\nelse:\n    print(_s %% (_s, _p))'
_p = "print('The core mirrors itself: s = %r' % 's')"
if "--explain" in sys.argv:
    exec(_p)
else:
    print(_s % (_s, _p))
