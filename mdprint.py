from types import ModuleType
from pathlib import Path
import sympy

def expr(*args):
  args = (f'${sympy.latex(a)}$' if isinstance(a, sympy.Expr) else a for a in args)
  print('<markdown>')
  print(*args)
  print('</markdown>\n')

def markdown(s: str):
  print('<markdown>')
  print(s)
  print('</markdown>\n')

def table(data):
  data_iter = iter(data)
  header = next(data_iter)
  print('<markdown>')
  print(' | '.join(header))
  print(' | '.join('---' for h in header))
  for row in data_iter:
    if isinstance(row, str):
      print(row)
    else:
      print(' | '.join(str(v) for v in row))
  print('</markdown>\n')

class PlotPrinter:
  def __init__(self, plt_module: ModuleType, input_file: str):
    self.input_file = Path(input_file)
    self.plt = plt_module
    self.counter = 1

  def __call__(self, format='svg'):
    suffix = '.' + format
    img_name = f'{self.input_file.stem}-{self.counter}'
    img_file = self.input_file.with_name(img_name).with_suffix(suffix)
    self.counter += 1
    self.plt.savefig(img_file)
    self.plt.close()
    print('<markdown>')
    print(f'<img src="{img_file.name}">')
    print('</markdown>\n')