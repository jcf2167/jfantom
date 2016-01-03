#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")

from FlaskApp import app as application
application.secret_key = '\xdaJ\xe0A\x1c\xa0\x8c\xdd\xf0\t\x0e\x19{\x01\x89\xf9a\xc3\rA\x0csw1'
