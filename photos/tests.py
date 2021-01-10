from django.test import TestCase
from .models import Location,Image,Category

# Create your tests here.

class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.location = Location(id=1,name = 'Nairobi')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))
        