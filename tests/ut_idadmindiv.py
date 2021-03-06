# 
# ut_idadmindiv.py
# Test idadmindiv package for country information
# Sparisoma Viridi | https://github.com/dudung
# 
# Execute: python -m tests.idadmindiv
# 
# 20220505 create this test file and modify __init__.py file
# 

import idadmindiv as id

vars = dir(id)
for v in vars:
  if not '__' in v and not 'info' in v:
    print(v, "= ", end='')
    print(getattr(id, v))
