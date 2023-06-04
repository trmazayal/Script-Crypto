from unittest import TestCase

from AES import int_to_list_of_words_big_endian, AesRound, AES, ExpansionKey, AesSBoxTransformer
from bytes import Word, Byte
from table_printer import transpose


class TestAES(TestCase):
    def test_add_round_key(self):
        key =   int_to_list_of_words_big_endian(0x01010101010101010101010101010101)
        plain = int_to_list_of_words_big_endian(0x000102030405060708090A0B0C0D0E0F)

        aes = AES(key)
        round = AesRound(aes.sbox_transformer, aes.irreducible)

        curr_plain = round.add_round_key(plain, aes.expansion_keys[0])
        # telah dicocokkan dengan PR 2
        self.assertEqual("[01 00 03 02, 05 04 07 06, 09 08 0b 0a, 0d 0c 0f 0e]", repr(curr_plain))

    def test_sbox_SubBytes(self):
        key =   int_to_list_of_words_big_endian(0x01010101010101010101010101010101)
        plain = int_to_list_of_words_big_endian(0x000102030405060708090A0B0C0D0E0F)

        aes = AES(key)
        round = AesRound(aes.sbox_transformer, aes.irreducible)

        processed_plain = round.add_round_key(plain, aes.expansion_keys[0])
        resulting_plain = round.sbox_substitution(processed_plain)
        # telah dicocokkan dengan PR 2
        self.assertEqual("[7c 63 7b 77, 6b f2 c5 6f, 01 30 2b 67, d7 fe 76 ab]", repr(resulting_plain))

    def test_shift_row(self):
        key =   int_to_list_of_words_big_endian(0x01010101010101010101010101010101)
        plain = int_to_list_of_words_big_endian(0x000102030405060708090A0B0C0D0E0F)

        aes = AES(key)
        round = AesRound(aes.sbox_transformer, aes.irreducible)

        processed_plain = round.add_round_key(plain, aes.expansion_keys[0])
        processed_plain = round.sbox_substitution(processed_plain)

        curr_no_transpose = round.list_of_words_to_table_of_byte(processed_plain)
        curr_transposed = transpose(curr_no_transpose)
        resulting_plain = round.shift_row(curr_transposed)

        # telah dicocokkan dengan PR 2
        self.assertEqual("[[7c, 6b, 01, d7], [f2, 30, fe, 63], [2b, 76, 7b, c5], [ab, 77, 6f, 67]]", repr(resulting_plain))

    def test_mix_columns(self):
        key =   int_to_list_of_words_big_endian(0x01010101010101010101010101010101)
        plain = int_to_list_of_words_big_endian(0x000102030405060708090A0B0C0D0E0F)

        aes = AES(key)
        round = AesRound(aes.sbox_transformer, aes.irreducible)

        processed_plain = round.add_round_key(plain, aes.expansion_keys[0])
        processed_plain = round.sbox_substitution(processed_plain)

        curr_no_transpose = round.list_of_words_to_table_of_byte(processed_plain)
        curr_transposed = transpose(curr_no_transpose)
        resulting_plain = round.shift_row(curr_transposed)

        # telah dicocokkan dengan PR 2
        self.assertEqual("[[7c, 6b, 01, d7], [f2, 30, fe, 63], [2b, 76, 7b, c5], [ab, 77, 6f, 67]]", repr(resulting_plain))

        key =   int_to_list_of_words_big_endian(0x01010101010101010101010101010101)
        plain = int_to_list_of_words_big_endian(0x000102030405060708090A0B0C0D0E0F)

        aes = AES(key)
        round = AesRound(aes.sbox_transformer, aes.irreducible)

        processed_plain = round.add_round_key(plain, aes.expansion_keys[0])
        processed_plain = round.sbox_substitution(processed_plain)

        curr_no_transpose = round.list_of_words_to_table_of_byte(processed_plain)
        curr_transposed = transpose(curr_no_transpose)
        processed_plain = round.shift_row(curr_transposed)
        resulting_plain = round.mix_columns(processed_plain)

        # telah dicocokkan dengan PR 2
        self.assertEqual("[[<75>, <87>, <0f>, <b2>], [<55>, <e6>, <04>, <22>], [<3e>, <2e>, <b8>, <8c>], [<10>, <15>, <58>, <0a>]]", repr(resulting_plain))

    def test_encrypt(self):  # TODO
        key =   int_to_list_of_words_big_endian(0x01010101010101010101010101010101)
        plain = int_to_list_of_words_big_endian(0x000102030405060708090A0B0C0D0E0F)

        aes = AES(key)
        round = AesRound(aes.sbox_transformer, aes.irreducible)

        processed_plain = round.add_round_key(plain, aes.expansion_keys[0])
        resulting_plain = round.encrypt(processed_plain, aes.expansion_keys[1])
        print(resulting_plain)
        # self.assertEqual("", repr(resulting_plain))  # TODO

class TestExpansionKey(TestCase):
    def test_get_g__first_step_is_correct(self):
        empty_word = lambda: Word([Byte(0), Byte(0), Byte(0), Byte(0)])
        NOT_NEEDED_FOR_THIS_METHOD = [empty_word(), empty_word(), empty_word(), empty_word()]
        irreducible = 0b100011011
        expansion_key = ExpansionKey(NOT_NEEDED_FOR_THIS_METHOD, irreducible=irreducible,
                                     sbox_transformer=AesSBoxTransformer(irreducible=irreducible))
        detail1, result_g = expansion_key.get_g_detailed(curr_key=Word.fromInt(0x7f8d292f), curr_round=9)
        self.assertEqual("5d a5 15 d2", repr(detail1))  # sudah dicocokkan dengan slide

    def test_get_g__second_step_is_correct(self):
        empty_word = lambda: Word([Byte(0), Byte(0), Byte(0), Byte(0)])
        NOT_NEEDED_FOR_THIS_METHOD = [empty_word(), empty_word(), empty_word(), empty_word()]
        irreducible = 0b100011011
        expansion_key = ExpansionKey(NOT_NEEDED_FOR_THIS_METHOD, irreducible=irreducible,
                                     sbox_transformer=AesSBoxTransformer(irreducible=irreducible))
        _, result_g = expansion_key.get_g_detailed(curr_key=Word.fromInt(0x7f8d292f), curr_round=9)  # from 8 to 9
        self.assertEqual(Word.fromInt(0x46_A5_15_D2, 4), result_g)  # sudah dicocokkan dengan slide

    def test_generate_round_keys__first_item_is_correct(self):
        empty_word = lambda: Word([Byte(0), Byte(0), Byte(0), Byte(0)])
        NOT_NEEDED_FOR_THIS_METHOD = [empty_word(), empty_word(), empty_word(), empty_word()]
        irreducible = 0b100011011
        expansion_key = ExpansionKey(NOT_NEEDED_FOR_THIS_METHOD, irreducible=irreducible,
                                     sbox_transformer=AesSBoxTransformer(irreducible=irreducible))
        results = expansion_key._generate_round_key_helper([
            Word.fromInt(0xead27321, 4),
            Word.fromInt(0xb58dbad2, 4),
            Word.fromInt(0x312bf560, 4),
            Word.fromInt(0x7f8d292f, 4),
        ], 9)
        self.assertEqual(Word.fromInt(0xAC7766F3, 4), results[0])  # sudah dicocokkan dengan slide

    def test_generate_round_keys__all_resulting_key_is_correct(self):
        empty_word = lambda: Word([Byte(0), Byte(0), Byte(0), Byte(0)])
        NOT_NEEDED_FOR_THIS_METHOD = [empty_word(), empty_word(), empty_word(), empty_word()]
        irreducible = 0b100011011
        expansion_key = ExpansionKey(NOT_NEEDED_FOR_THIS_METHOD, irreducible=irreducible,
                                     sbox_transformer=AesSBoxTransformer(irreducible=irreducible))
        results = expansion_key._generate_round_key_helper([
            Word.fromInt(0xa0a0a0a0, 4),
            Word.fromInt(0xb1b1b1b1, 4),
            Word.fromInt(0xc2c2c2c2, 4),
            Word.fromInt(0xd3d3d3d3, 4),
        ], 3)
        self.assertEqual(Word.fromInt(0xc2_c6_c6_c6, 4), results[0])  # sudah dicocokkan dengan hasil worksheet
        self.assertEqual(Word.fromInt(0x73_77_77_77, 4), results[1])  # sudah dicocokkan dengan hasil worksheet
        self.assertEqual(Word.fromInt(0xb1_b5_b5_b5, 4), results[2])  # sudah dicocokkan dengan hasil worksheet
        self.assertEqual(Word.fromInt(0x62_66_66_66, 4), results[3])  # sudah dicocokkan dengan hasil worksheet

