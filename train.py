import re
import os
from subprocess import call
from random import shuffle


files = [f for f in os.listdir('.') if re.match(r'\d\d\.md', f)]
shuffle(files)

call(['vim', *files])
