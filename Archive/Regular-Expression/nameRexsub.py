#Jedsada Luengaramsuk jedsada-io
#2 Febuary 2021

import re

namesRegex = re.compile(r'Agent \w+'')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
#'CENSORED gave the secret documents to CENSORED.
#Change Alice to CENSORED
