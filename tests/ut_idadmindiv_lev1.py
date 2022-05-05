# 
# ut_idadmindiv_lev1.py
# Test idadmindiv package for province information
# Sparisoma Viridi | https://github.com/dudung
# 
# Execute: python -m tests.idadmindiv_lv1
# 
# 20220505 create this test file and modify __init__.py file
# 

import idadmindiv.ac as ac

vars = dir(ac)
for v in vars:
  if not '__' in v and not 'info' in v:
    print(v, "= ", end='')
    print(getattr(ac, v))
