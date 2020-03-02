from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestlist_concat_bytes_136(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_list_concat_bytes_136(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/list_concat_bytes.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN { 0xcd ; 0xef ; 0x00 } 0x00ab')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('0x00abcdef00')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)
