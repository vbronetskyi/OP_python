"""Test flower.py"""
import unittest
import flower
class TestFlower(unittest.TestCase):
    """Class for tests from module square_preceding"""
    def setUp(self):
        """init objects to test"""
        # self.try_eror1 = flower.Flower("blue", 12, -1)
        # self.try_eror2 = flower.Flower("blue", -5, 40)
        # self.try_eror3 = flower.Flower(7, 12, 40)
        # self.try_eror4 = flower.Flower("red", "five", 40)
        # self.try_eror5 = flower.Flower("blue", 12, 'ten')
        self.A = flower.Flower("blue", 12, 40)
        self.B = flower.Tulip(12, 50)
        self.C = flower.Rose(9, 80)
        self.D = flower.Chamomile(15, 30)
        self.flowers1 = flower.FlowerSet()
        self.flowers1.add_flower(self.A)
        self.flowers1.add_flower(self.B)
        self.flowers2 = flower.FlowerSet()
        self.flowers2.add_flower(self.C)
        self.flowers2.add_flower(self.D)
        self.bucket = flower.Bucket()
        self.bucket.add_set(self.flowers1)
        self.bucket.add_set(self.flowers2)

    def test_flower_classes(self):
        """test flower"""
        self.assertEqual(self.A.get_price(), 40,\
            f"Функція повертає не правильну ціну {self.A.get_price()}")
        self.assertEqual(self.C.color, "red",\
            f"Функція повертає не правельний колір {self.C.color}")
        self.assertTrue(flower.Flower("blue", -12, 1),\
            "Кількість пелюсток не може бути відємною")
        self.assertTrue(flower.Flower("blue", 12, -1),\
            "Ціна не може бути відємною")
        self.assertTrue(flower.Flower(7, 12, 40),\
            "Колір повинен бути типу str")
        self.assertTrue(flower.Flower("blue", 12, "five"),\
            "Ціна повинна бути типу int")
        self.assertTrue(flower.Flower("blue", "yes", 1),\
            "Кількість пелюсток повинна бути типу int")
        self.assertFalse(flower.Tulip(12, 50).check_attributes(),\
            "Не правильно задані атрибути")
    def test_bucket_classes(self):
        """test bucket classes"""
        self.assertEqual(len(self.flowers1.flowerset),2,\
            "Не правильно розроблено flowerset")
        self.assertEqual(len(self.flowers2.flowerset),2,\
            "Не правильно розроблено flowerset")
        self.assertEqual(len(self.bucket.bucket),4,\
            "Не правильно розроблено bucket")
        self.assertEqual(self.bucket.total_price(), 200)

# if __name__ == '__main__':
#     unittest.main()
