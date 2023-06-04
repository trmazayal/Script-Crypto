from math import gcd

from GF_ops import *
from table_printer import *


ainv = GF(0b10011000)
a = GF(0b101010)
print(ainv.as_pangkat())
print(a.as_pangkat())
print(GF(0b10011).as_pangkat())
print(ainv * a)
