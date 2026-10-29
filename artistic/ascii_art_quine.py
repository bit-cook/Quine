#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ASCII-art Quine - run with --art to show the banner.
import sys
_s = '#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n# ASCII-art Quine - run with --art to show the banner.\nimport sys\n_s = %r\n_p = %r\nif "--art" in sys.argv:\n    exec(_p)\nelse:\n    print(_s %% (_s, _p))'
_p = 'BANNER = r"""\n +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n |Q|U|I|N|E| |S|E|L|F|-|R|E|P|L|I|C|A|T|I|O|N|\n +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n      .--.     .--.     .--.     .--.\n     |    |   |    |   |    |   |    |\n      \'--\'     \'--\'     \'--\'     \'--\'\n   A program that prints its own source code.\n"""\nprint(BANNER)\nprint("Run without --art to watch this file reproduce itself exactly.")\n'
if "--art" in sys.argv:
    exec(_p)
else:
    print(_s % (_s, _p))
