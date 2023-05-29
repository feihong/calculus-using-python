# Section 3: Functions: Power and log

# Imports and helper functions

import random
import itertools
import numpy as np
import sympy as sym
from sympy.abc import x, a, b
import matplotlib.pyplot as plt
import htmlprint

def rand():
  return random.randint(0, 100) / 10.

def compare_expressions(e1, e2, a, b, data):
  htmlprint.expr(e1, 'is equivalent to', e2)

  def generate_data():
    yield 'a', 'b', f'${sym.latex(e1)}$', f'${sym.latex(e2)}$'

    rows = itertools.chain([data], ((rand(), rand()) for _ in range(4)))

    for a_val, b_val in rows:
      sub1 = e1.subs({a: a_val, b: b_val})
      sub2 = e2.subs({a: a_val, b: b_val})
      yield f'{a_val} | {b_val} | ${sym.latex(sub1)}$ | ${sym.latex(sub2)}$'

  htmlprint.table(generate_data())

def compare_using_numpy(a, b, fa, fb, fa_label, fb_label):
  def generate_data():
    yield 'a', 'b', f'◊{fa_label}◊', f'◊{fb_label}◊', 'diff'

    for a_, b_, fa_, fb_ in zip(a[:6], b[:6], fa[:6], fb[:6]):
      yield f'{a_} | {b_} | {fa_:.3f} | {fb_:.3f} | {abs(fa_ - fb_):.5f}'

  htmlprint.markdown(f'◊{fa_label} = {fb_label}◊')
  htmlprint.table(generate_data())
  plt.plot(fa - fb, '.')
  plt.ylim(-1, 1)
  plt.show()

# What is ◊0^0◊?

f"""
It has been a point of contention, but mathematicians hashed it out and decided that ◊0^0 = {0**0}◊.
"""

# Exercise 1: Adding powers

compare_expressions(x**a * x**b, sym.simplify(x**a * x**b), a, b, (3.4, 7.3))

# Exercise 2: Subtracting powers

compare_expressions(x**a / x**b, sym.simplify(x**a / x**b), a, b, (4, 4))

# Exercise 3: Powers upon powers

def use_positive_numbers():
  # This wouldn't work without positive=True
  x, a, b = sym.symbols('x a b', positive=True)
  compare_expressions((x**a)**b, sym.simplify((x**a)**b), a, b, (3, 7))

use_positive_numbers()

e = (x**a)**b

f"""
In general, simplifying ${sym.latex(e)}$ will result in the same expression.

Using `sym.symplify`, you get ${sym.latex(sym.simplify(e))}$.

Using `sym.powsimp`, you get ${sym.latex(sym.powsimp(e))}$.

For ◊x = -2, a = 4.1, b = -0.3◊:

◊(-2^4.1)^{-0.3}◊ = {((-2)**4.1)**(-.3)}

◊-2^(4.1 xx -0.3)◊ = {(-2)**(4.1*(-.3))}
"""

# Exercise 4: The power of log

def ex4():
  a = np.random.randint(1, 20, size=100)
  b = np.random.randint(1, 20, size=100)

  compare_using_numpy(a, b, np.log(a * b), np.log(a) + np.log(b), 'ln(a xx b)', 'ln(a) + ln(b)')
  compare_using_numpy(a, b, np.log(a**b), b*np.log(a), 'ln(a^b)', 'b ln(a)')
  compare_using_numpy(a, b, np.log(a/b), np.log(a) - np.log(b), 'ln(a/b)', 'ln(a)-ln(b)')

ex4()
