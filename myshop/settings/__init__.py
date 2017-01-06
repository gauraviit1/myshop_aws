
from .base import *
live = False

try:
	from .local import *
except:
	live = True

if live:
	try:
		from .production import *
	except:
		pass