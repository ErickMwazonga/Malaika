import os
import sys
from .base import *  # noqa

# Load development settings based on DJANGO_MODE environment variable
if os.environ.get('DJANGO_MODE', 'PRODUCTION') == 'DEVELOPMENT':
    from .development import *
else:
    from .production import *


if 'test' in sys.argv:
	try:
		from testing import *
	except ImportError:
		pass
