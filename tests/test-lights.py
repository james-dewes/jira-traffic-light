import unittest

class TestLight(unittest.TestCase):
    light = new light
    def test_on(self):
        light.on()
        self.assertEqual(light.status,1)
        self.assertFalse(light.status,0)


if __name__ == '__main__':
    unittest.main()