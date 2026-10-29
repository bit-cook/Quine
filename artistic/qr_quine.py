#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# QR Quine - pipe its output into --generate to make a QR of itself.
import sys
_s = '#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n# QR Quine - pipe its output into --generate to make a QR of itself.\nimport sys\n_s = %r\n_p = %r\nif "--generate" in sys.argv:\n    exec(_p)\nelse:\n    print(_s %% (_s, _p))'
_p = 'import sys\ndata = sys.stdin.read()\nif not data:\n    print("Usage: python qr_quine.py | python qr_quine.py --generate")\n    sys.exit(0)\ntry:\n    import qrcode\nexcept ImportError:\n    print("Install the encoder: pip install qrcode[pil]")\n    sys.exit(1)\nqr = qrcode.QRCode(border=2)\nqr.add_data(data)\nqr.make(fit=True)\nqr.make_image().save("quine_qr.png")\nprint("Saved quine_qr.png - scan it to recover this program\'s own source!")\n'
if "--generate" in sys.argv:
    exec(_p)
else:
    print(_s % (_s, _p))
