from __future__ import annotations

from typing import Union

from bytes import Byte


class GaloisFieldOfTwo:
    def __init__(self, represented_value, n=8, irreducible: int=0b100011011):
        """Representing operations of GF(2**n)"""
        assert 0 <= represented_value < 2**n
        self.val = represented_value
        self.n = n
        self.irreducible = irreducible

    def __rmul__(self, other):
        return self * other

    def __radd__(self, other):
        return self + other

    def __rxor__(self, other):
        return self ^ other

    def __xor__(self, other):
        return self + other

    def __mul__(self, other: Union[int, GaloisFieldOfTwo]):
        other = self.convert_to_int(other)
        res = mult(self.val, other)
        res = mod(res, self.irreducible)
        return GaloisFieldOfTwo(res, self.n, self.irreducible)

    def __rsub__(self, other):
        other = self.convert_to_GaloisFieldOfTwo(other)
        return other + self  # - is same as +

    def __sub__(self, other):
        other = self.convert_to_GaloisFieldOfTwo(other)
        return self + other  # - is same as +

    def __add__(self, other: Union[int, GaloisFieldOfTwo]):
        other = self.convert_to_int(other)
        res = self.val ^ other
        return GaloisFieldOfTwo(res, self.n, self.irreducible)

    def convert_to_GaloisFieldOfTwo(self, other: Union[int, GaloisFieldOfTwo]):
        if isinstance(other, int):
            other = GaloisFieldOfTwo(other, self.n, self.irreducible)
        assert isinstance(other, GaloisFieldOfTwo)
        return other

    def convert_to_int(self, other: Union[int, GaloisFieldOfTwo]):
        if isinstance(other, GaloisFieldOfTwo):
            assert other.irreducible == self.irreducible
            assert other.n == self.n
            other = other.val
        if isinstance(other, Byte):
            other = other.bits
        return other

    def __repr__(self):
        ret =  f"<{self.val:02x}>"
        return ret

    def as_bin(self):
        return f"<{self.val:08b}>"

    def as_pangkat(self):
        if self.val == 0:
            return "0"
        ret = []
        curr = self.val
        i = 0
        while curr != 0:
            if curr % 2 == 1:
                ret.append("1" if i==0 else f"x^{i}")
            i += 1
            curr >>= 1
        return " + ".join(ret[::-1])

    def __int__(self):
        return self.val
GF = GaloisFieldOfTwo

def mult(x, y):
    res = 0
    while y > 0:
        if y%2 == 1:
            res = res ^ x
        x <<= 1
        y >>= 1
    return res

def get_msb_left_shift_cnt(binary):
    assert binary >= 0
    ret = 0
    while binary > 0:
        binary >>= 1
        ret += 1
    return ret - 1

def mod(x, m):
    while True:
        x_lshift = get_msb_left_shift_cnt(x)
        m_lshift = get_msb_left_shift_cnt(m)
        if x_lshift < m_lshift:
            break
        diff = x_lshift - m_lshift
        m_shifted = m << diff
        x = x ^ m_shifted
        
    return x

def is_irreducible(x):
    for i in range(0b10, x):
        if mod(x, i) == 0:
            return False
    return True

def find_mult_in_gf(x, y, irreducible):
    multiplied = mult(x, y)
    return mod(multiplied, irreducible)

def get_gf_table(ordo, irreducible):
    assert ordo == (1 << get_msb_left_shift_cnt(ordo))
    
    table = []
    for row in range(0, ordo):
        table.append([])
        for col in range(0, ordo):
            res = find_mult_in_gf(row, col, irreducible)
            table[-1].append(res)
        
    return table

def get_gf_elements(ordo):
    return [i for i in range(ordo)]

def is_generator(generator, gf_elements, irreducible, mult_op=mult, mod_op=mod):
    gf_elements = set(gf_elements)
    gf_elements = gf_elements - {0}
    generated = get_generator_span(generator, irreducible, mult_op=mult_op, mod_op=mod_op)
    generated = set(map(lambda x: x[1], generated))
    return generated == gf_elements

def get_generator_span(generator: int, irreducible: int, mult_op=mult, mod_op=mod) -> list[tuple[int, int]]:
    """
    misal g = `generator`, maka fungsi ini akan mengembalikan list of tuple (X, Y) di mana g**X == Y
    :param generator:
    :param irreducible:
    :return:
    """
    assert is_irreducible(irreducible)
    initial_value = 1
    ret_elements = []
    elements = set()

    exponentiation = 0
    value = initial_value
    while value not in elements:
        elements.add(value)
        ret_elements.append((exponentiation, value))
        value = mult_op(value, generator)
        value = mod_op(value, irreducible)
        exponentiation += 1
    return ret_elements


def is_power_of_two(value):
    left_shift = get_msb_left_shift_cnt(value)
    power_of_two = 1 << left_shift
    return value == power_of_two


def get_multiplicative_inverse(generator: int, span: list[tuple[int, int]], irreducible: int, include_zero=True):
    """
    misal g = `generator`
    :param span: list of tuple (X, Y), di mana g**X == y
    :param irreducible:
    :return:
    """
    assert is_irreducible(irreducible)
    assert is_power_of_two(len(span) + 1)
    span = sorted(span, key=lambda x: x[0])  # sort by its power
    num_of_generator_exponentiation = len(span)

    ret = {1: 1}
    if include_zero:
        ret[0] = 0

    for i in range(len(span)):
        generator1, value1 = span[i]
        generator2 = num_of_generator_exponentiation - generator1
        generator2 %= num_of_generator_exponentiation

        # if we multiply them, we got g**0 which is 1
        assert (generator1 + generator2) % num_of_generator_exponentiation == 0

        value2 = span[generator2][1]
        assert mod(mult(value1, value2), irreducible) == 1
        ret[value1] = value2
        ret[value2] = value1
    return ret


    
