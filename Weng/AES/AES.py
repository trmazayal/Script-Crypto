from pprint import pprint
from typing import Union

from GCD_table import matrix_mult
from GF_ops import mod, get_multiplicative_inverse, get_generator_span, is_generator, GaloisFieldOfTwo
from bytes import Word, Byte, MutableByte
from table_printer import print_table, transpose


class AES:
    def __init__(self, master_key: list[Word]):
        self.irreducible = 0b100011011
        self.generator = 0b11
        assert is_generator(self.generator, list(range(2**8)), self.irreducible)

        self.master_key = master_key
        self.sbox_transformer = AesSBoxTransformer(self.generator, self.irreducible)
        self.expansion_keys = ExpansionKey(self.master_key, self.irreducible,
                                           self.sbox_transformer).generate_round_keys()



class AesSBoxTransformer:
    def __init__(self, generator: int=0b11, irreducible:int=0b100011011):
        self.generator = generator
        self.irreducible = irreducible

        self.mult_inv = self._initialize_multiplicative_inverse_dict()
        self.sbox = self._generate_sbox_table()


    def _initialize_multiplicative_inverse_dict(self):
        span = get_generator_span(self.generator, self.irreducible)
        dct = get_multiplicative_inverse(self.generator, span, self.irreducible, include_zero=True)
        return dct

    def map_to_sbox(self, value: int) -> Byte:
        row = value >> 4
        col = value & 0b1111
        return self.sbox[row][col]

    def _generate_sbox_table(self) -> list[list[int]]:
        table = []
        for row in range(16):
            table.append([])
            for col in range(16):
                value = row << 4 | col
                value = self.mult_inv[value]
                value = self._sbox_construction_byte_transformation(Byte(value))
                table[-1].append(value)
        return table

    def _sbox_construction_byte_transformation(self, byte: Byte):
        bits = MutableByte(0)
        for i in range(8):
            bits[i] = self._sbox_construction_bit_transformation(i, byte)
        return bits


    def _sbox_construction_bit_transformation(self, nth_bit, byte: Byte):
        c = Byte(0x63)
        bi = byte[nth_bit]
        bi4 = byte[(nth_bit + 4) % 8]
        bi5 = byte[(nth_bit + 5) % 8]
        bi6 = byte[(nth_bit + 6) % 8]
        bi7 = byte[(nth_bit + 7) % 8]
        ci = c[nth_bit]
        ret = bi ^ bi4 ^ bi5 ^ bi6 ^ bi7 ^ ci
        return ret



class AesRound:
    # def __init__(self, aes: AES):
    def __init__(self, sbox_transformer: AesSBoxTransformer, irreducible):
        self.sbox_transformer = sbox_transformer
        self.irreducible = irreducible

    def encrypt(self, not_transposed_plaintext: Union[int, list[Word]], curr_key: list[Word]):
        if isinstance(not_transposed_plaintext, int):
            not_transposed_plaintext = int_to_list_of_words_big_endian(not_transposed_plaintext)
        curr_no_transpose = self.sbox_substitution(not_transposed_plaintext)

        curr_no_transpose = self.list_of_words_to_table_of_byte(curr_no_transpose)
        curr_transposed = transpose(curr_no_transpose)
        curr_transposed = self.shift_row(curr_transposed)

        curr_transposed = self.mix_columns(curr_transposed)
        curr_transposed = table_of_gf_to_table_of_bytes(curr_transposed)
        curr_no_transpose = transpose(curr_transposed)
        curr_no_transpose = self.table_of_byte_to_list_of_words(curr_no_transpose)
        curr_no_transpose = self.add_round_key(curr_no_transpose, curr_key)
        return curr_no_transpose


    def sbox_substitution(self, not_transposed_plaintext: list[Word]):
        transformer = self.sbox_transformer
        # transformer = self.aes.sbox_transformer
        ret = []
        for row in not_transposed_plaintext:
            curr_new_row = []
            for cell_byte in row.arr:
                transformed_cell = transformer.map_to_sbox(cell_byte.bits)
                curr_new_row.append(transformed_cell)
            ret.append(Word(curr_new_row))
        return ret

    def shift_row(self, transposed_plaintext_state: list[list[Byte]]):
        """
        :param transposed_plaintext_state: plaintext dalam keadaan normal (direction dari kiri ke kanan). nanti akan ditranspose
        :return:
        """
        ret = []
        for index, arr_of_int in enumerate(transposed_plaintext_state):
            left_rotated = Word(arr_of_int).leftRotate(8 * index).arr
            ret.append(left_rotated)
        return ret

    def mix_columns(self, transposed_plaintext_state: list[list[Byte]]):
        multiplication_matrix = self._2d_ints_to_2d_gf([
            [2, 3, 1, 1],
            [1, 2, 3, 1],
            [1, 1, 2, 3],
            [3, 1, 1, 2],
        ])
        res = matrix_mult(multiplication_matrix, transposed_plaintext_state)
        return res

    def add_round_key(self, not_transposed_plaintext: list[Word], keys: list[Word]):
        """Perform add round key stage in AES"""
        ret: list[Word] = []
        for (not_transposed_plaintext, key) in zip(not_transposed_plaintext, keys):
            ret.append(not_transposed_plaintext ^ key)
        return ret

    def table_of_byte_to_list_of_words(self, table_of_bytes: list[list[Byte]]):
        return [Word(row_byte) for row_byte in table_of_bytes]

    def list_of_words_to_table_of_byte(self, list_of_words: list[Word]):
        return [word.arr for word in list_of_words]

    def _2d_ints_to_2d_gf(self, table_of_ints):
        return [
            self.list_of_ints_to_list_of_gf(lst) for lst in table_of_ints
        ]

    def list_of_ints_to_list_of_gf(self, list_of_ints: list[int]) -> list[GaloisFieldOfTwo]:
        return [
            GaloisFieldOfTwo(integer, 8, self.irreducible) for integer in list_of_ints
            # GaloisFieldOfTwo(integer, 8, self.aes.irreducible) for integer in list_of_ints
        ]


def table_of_gf_to_table_of_bytes(table: list[list[GaloisFieldOfTwo]]):
    ret = []
    for row in table:
        ret.append([])
        for col in row:
            ret[-1].append(Byte(col.val))
    return ret

def int_to_list_of_words_big_endian(long_int: Union, word_size=4):
    reversed_ret = []
    for _ in range(word_size):
        curr_int = 0x_ff_ff_ff_ff & long_int
        long_int >>= word_size * 8
        reversed_ret.append(Word.fromInt(curr_int, word_size))
    ret = reversed_ret[::-1]
    return ret



class ExpansionKey:
    def __init__(self, master_key: list[Word], irreducible: int, sbox_transformer: AesSBoxTransformer):
        assert len(master_key) == 4
        for i in range(4):
            assert len(master_key[i]) == 4

        self.master_key = master_key
        self.irreducible = irreducible
        self.sbox_transformer = sbox_transformer
        self.rc_j = self._get_rcj()

    def generate_round_keys(self):
        ret = []
        curr_key = self.master_key
        ret.append(curr_key)

        for nth_round in range(1, 10+1):
            # g = self.get_g(curr_key[3], nth_round)
            # curr_key = self._generate_round_key(curr_key, g)

            curr_key = self._generate_round_key_helper(curr_key, nth_round)

            ret.append(curr_key)
        return ret

    def _generate_round_key_helper(self, curr_key: list[Word], nth_round: int):
        g = self.get_g(curr_key[3], nth_round)
        return self._generate_round_key(curr_key, g)

    def _generate_round_key(self, prev_key: list[Word], curr_g: Word):
        w0, w1, w2, w3 = prev_key
        w0 = w0 ^ curr_g
        w1 = w1 ^ w0
        w2 = w2 ^ w1
        w3 = w3 ^ w2
        return [w0, w1, w2, w3]

    def _get_rcj(self):
        rc_j_temp = [GaloisFieldOfTwo(1, 8, self.irreducible)]
        for i in range(2, 10+1):
            rc_j_temp.append(2 * rc_j_temp[-1])
        rc_j_temp = list(map(lambda x: Byte(int(x)), rc_j_temp))
        rc_j = [None] + rc_j_temp  # one-based index
        return rc_j

    def get_g_detailed(self, curr_key: Word, curr_round: int):
        """ curr_round should start from 1 up to 10 (inclusive) """
        curr_key = curr_key.leftRotate(8 * 1)

        sbox_transform = self.sbox_transformer.map_to_sbox
        curr_key = curr_key.apply(lambda x: sbox_transform(
            int(x)
        ))
        curr_key_1 = curr_key
        curr_key = curr_key ^ Word([
            self.rc_j[curr_round], Byte(0), Byte(0), Byte(0)
        ])
        curr_key_2 = curr_key
        return curr_key_1, curr_key_2

    def get_g(self, curr_key: Word, curr_round: int):
        return self.get_g_detailed(curr_key, curr_round)[1]








