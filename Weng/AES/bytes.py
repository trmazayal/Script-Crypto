from __future__ import annotations
from typing import Union, Callable


class Byte:
    def __init__(self, bits):
        assert 0 <= bits <= 255
        self.bits = bits

    def __repr__(self):
        return f"{self.bits:02x}"
        # return f"{self.bits:08b}"

    def __xor__(self, other: Byte):
        return Byte(self.bits ^ other.bits)

    def __or__(self, other: Byte):
        return Byte(self.bits | other.bits)

    def __and__(self, other: Byte):
        return Byte(self.bits & other.bits)

    def __eq__(self, other):
        return self.bits == other.bits

    def __add__(self, other: Byte):
        temp = self.bits + other.bits
        return Byte(temp % 256)


    def addWithCarry(self, *other: Byte):
        assert len(other) < 256
        temp = self.bits + sum(map(int, other))
        carry = Byte(temp // 256)
        return carry, Byte(temp % 256)

    def __int__(self):
        return self.bits

    def __invert__(self):
        return Byte((~self.bits) & 0b_1111_1111)

    def __hex__(self):
        return f"{self.bits:02x}"

    def __getitem__(self, index: int):
        ret = self.bits & (1 << index)
        return int(bool(ret))


class MutableByte(Byte):
    def __setitem__(self, index: int, value):
        assert value in (0, 1)
        bit_mask = (1 << index)
        need_negation = value ^ bool(self.bits & bit_mask)
        if not need_negation:
            return
        self.bits ^= bit_mask


class Word:
    def __init__(self, arrOfBytes: list[Byte]):
        self.arr = arrOfBytes

    @staticmethod
    def fromBytes(byte:bytes):
        arr = []
        for c in byte:
            arr.append(Byte(c))
        return Word(arr)

    @staticmethod
    def fromInt(integer: int, numOfBytes=None):
        assert integer >= 0
        if (integer == 0):
            return Word([Byte(0)] * numOfBytes)

        res = []
        while True:
            if (numOfBytes is not None) and numOfBytes <= 0:
                break
            elif (numOfBytes is None) and integer == 0:
                break

            res.append(Byte(integer & 0b_1111_1111))
            integer >>= 8
            if numOfBytes is not None:
                numOfBytes -= 1
        return Word(res[::-1])

    def apply(self, func: Callable[[Byte], Byte]):
        return Word(list(
            map(func, self.arr)
        ))

    def append(self, byte: Byte):
        self.arr.append(byte)

    def extend(self, *words: Word):
        for word in words:
            self.arr.extend(word.arr)

    def __int__(self):
        temp = 0
        for byte in self.arr:
            temp <<= 8
            temp |= byte.bits
        return temp

    def __repr__(self):
        return " ".join(map(repr, self.arr))

    def __xor__(self, other: Word):
        assert len(self.arr) == len(other.arr)
        return Word(list(map(
            lambda x: x[0] ^ x[1], zip(self.arr, other.arr)
        )))

    def __or__(self, other: Word):
        assert len(self.arr) == len(other.arr)
        return Word(list(map(
            lambda x: x[0] | x[1], zip(self.arr, other.arr)
        )))

    def __and__(self, other: Word):
        assert len(self.arr) == len(other.arr)
        return Word(list(map(
            lambda x: x[0] & x[1], zip(self.arr, other.arr)
        )))

    def __invert__(self):
        return Word(list(map(lambda x: ~x, self.arr)))

    def __add__(self, other: Word):
        assert len(self.arr) == len(other.arr)
        n = len(self.arr)
        res: list[Union[None, Byte]] = [None] * n
        carry = Byte(0)
        for i in range(n-1, -1, -1):  # from n-1 to 0 (inclusive)
            carry, result = self[i].addWithCarry(other[i], carry)
            res[i] = result
        return Word(res)

    def __eq__(self, other: Word):
        assert len(self.arr) == len(other.arr)
        return all(map(lambda x: x[0] == x[1], zip(self.arr, other.arr)))

    def __getitem__(self, item):
        ret = self.arr[item]
        if isinstance(ret, list):
            ret = Word(ret)
        return ret

    def __len__(self):
        return len(self.arr)

    def prettyStr(self, sliceWidth=4):
        return "\n".join(map(repr, self.slice(sliceWidth)))

    def slice(self, sliceWidth: int) -> list[Word]:
        i = 0
        ret = []
        while i < len(self):
            temp = self[i: i + sliceWidth]
            ret.append(temp)
            i += sliceWidth
        return ret

    def __lshift__(self, shift_amount):
        n = len(self)
        res = int(self) << shift_amount
        return Word.fromInt(res, n)

    def leftRotate(self, bit_shift_amount):
        n = len(self)
        int_self = int(self)
        res = int_self << bit_shift_amount
        rotated = int_self >> (8 * n - bit_shift_amount)
        return Word.fromInt(res | rotated, n)

    def __hex__(self):
        return " ".join(map(lambda x: x.__hex__(), self.arr))

    def toggleEndian(self):
        return Word(self.arr[::-1])
