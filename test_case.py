import unittest
import desafio_02


class CapegeminiTest(unittest.TestCase):
    def test_questao1(self):
        q1 = desafio_02.questao1([9, 2, 1, 4, 6])
        self.assertEqual(q1,4)

    def test_questao2(self):
        q2 = desafio_02.questao2([1, 5, 3, 4, 2], 2)
        self.assertEqual(q2, 3)
    
    def test_questao3(self):
        q3 = desafio_02.questao3('tenha um bom dia')
        self.assertEqual(q3, 'taoa eum nmd hbi')

if __name__ == '__main__':
    unittest.main()
