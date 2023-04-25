activate_this = '/home/ubuntu/mc-1-19-4/app.py'
with open(activate_this) as f:
	exec(f.read(), dict(__file__=activate_this))

import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/html/mc-1-19-4/")

from app import app as application