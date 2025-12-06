def AND(a: bool, b: bool) -> bool:
  if a:
    return b
  return False

def OR(a: bool, b: bool) -> bool:
  if a:
    return True
  return b