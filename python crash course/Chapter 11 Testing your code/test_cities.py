import unittest
from city_functions import formatted_city_country


class TestCity(unittest.TestCase):
    """Test for 'city_functions.py' """

    def test_formatted_city(self):
        """Do city name formatted 'City, Country' work?"""
        formatted_city = formatted_city_country('mexico city', 'mexico')
        self.assertEqual(formatted_city, 'Mexico City, Mexico')

    def test_formatted_city_population(self):
        """Do city name formatted (City, Country - population xxxx) work?"""
        formatted_city = formatted_city_country(
            'mexico city', 'mexico', 5000000)
        self.assertEqual(
            formatted_city, 'Mexico City, Mexico - population 5000000')


if __name__ == '__main__':
    unittest.main()
