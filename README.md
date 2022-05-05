# id-admin-div
administrative division of id


## how to use
Import 1st level information using

```python
import idadmindiv.ac as ac

vars = dir(ac)
for v in vars:
  if not '__' in v and not 'info' in v:
    print(v, "= ", end='')
    print(getattr(ac, v))

print()

import idadmindiv.pb as pb

vars = dir(pb)
for v in vars:
  if not '__' in v and not 'info' in v:
    print(v, "= ", end='')
    print(getattr(pb, v))
```

to produce

```
area = 57956
capital = Banda Aceh
code = 11
iso = id-ac
level = 1
name = Aceh

area = 102955.15
capital = Manokwari
code = 92
iso = id-pb
level = 1
name = Papua Barat
```

and there are another 32 1st level information.
