import idadmindiv.info as iad

vars = dir(iad)
for v in vars:
  if not '__' in v:
    print(v)
