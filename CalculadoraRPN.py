import collections as col

def prioridad(x: str) -> int:
  if (x == '^'):
    return 3
  if (x == '*' or x == '/'):
    return 2
  if (x == '+' or x == '-'):
    return 1 
  return 0

def getNumber(expr: str) -> tuple:
  index = 0
  length = len(expr)
  while (index < length):
    if (not expr[index].isnumeric()):
      break
    index += 1
  result = (expr[:index], index)
  return result

def toRPN(expr: str) -> list[str]:
  expr = expr.replace(" ", "")
  stack = col.deque()
  result = col.deque()
  while(expr != ""):
    res = getNumber(expr)
    char = res[0]
    if (char != ""):
      result.append(char)
      expr = expr[res[1]:]
      continue
    char = expr[0]
    expr = expr[1:]
    if (char == "("):
      stack.append(char)
    elif (char == ")"):
      while (len(stack) > 0 and stack[-1] != "("):
        result.append(stack.pop())
      stack.pop()
    else:
      while (len(stack) > 0 and prioridad(char) <= prioridad(stack[-1])):
        result.append(stack.pop())
      stack.append(char)

  while (len(stack) != 0):
    result.append(stack.pop())
  return result

def evaluateRPN(expr: col.deque[str]):
  stack = col.deque()
  while (len(expr) != 0):
    char = expr.popleft()
    if (char.isnumeric()):
      stack.append(float(char))
    else:
      n1 = stack.pop()
      n2 = stack.pop()
      stack.append(calcule(n1, n2, char))
  return stack.pop()

def calcule(n1: float, n2: float, oper: str, /) -> float:
  if (oper == "*"):
    return n1 * n2
  if (oper == "/"):
    return n1 / n2
  if (oper == "+"):
    return n1 + n2
  if (oper == "-"):
    return n1 - n2
  if (oper == "^"):
    return n1 ** n2
  
def main() -> None:
  try:
    print("resultado: ", evaluateRPN(toRPN(input("Ingrese una expresión matemática (Válida ps)\n=>"))))
  except:
    print(ValueError("Expresión no soportada"))


if __name__ == "__main__":
  main()