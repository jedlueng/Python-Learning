#Jedsada Luengaramsuk jedsada-io
#3 February 2021

import re

namesRegex = re.compile(r'Agent \w+')

namesRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob.')
#'CENSORED gave the secret documents to CENSORED.'


agentNamsRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agnt Carol that Agent Eve knew Agent Bob was a double agent.')
#A**** told C**** that E**** knew B**** was a double agent.'
