# -*- coding: utf-8 -*-

import subprocess


cmd = "sed -i 's/render_to_response(/render(request, /g' `grep 'render_to_response' -rl  ./*`"
subprocess.call([""], shell=True)
