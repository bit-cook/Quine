#!/bin/bash
# Shell Quine - classic self-reproducing program.
# Verify: bash quine.sh | diff - quine.sh

s='#!/bin/bash
# Shell Quine - classic self-reproducing program.
# Verify: bash quine.sh | diff - quine.sh

s=\47%s\47
printf "$s" "$s"
'
printf "$s" "$s"
