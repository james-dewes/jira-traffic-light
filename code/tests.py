import unittest
from light import Light

class LightTestCase(unittest.TestCase):
    def setUp(self):
        self.test_light = Light()

    def test_on(self):
        self.test_light.on()
        self.assertEqual(self.test_light.getState(),1)

    def test_off(self):
        self.test_light.off()
        self.assertEqual(self.test_light.getState(),0)


if __name__ == '__main__':
    unittest.main()