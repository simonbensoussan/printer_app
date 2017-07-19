from django.test import TestCase
from .models import Bucketlist
# Create your tests here.

class ModelTestCase(TestCase):
    """This class defines test suite odf bucketlist model"""
    
    def setUp(self):
        """ Define the test clents and other variables"""
        self.bucketlist_name = "Class code"
        self.bucketlist = Bucketlist(name=self.bucketlist_name) #1
    
    def test_model_can_create_a_bucketlist(self):
        """Test the model can create a bucketlist"""
        old_count = Bucketlist.objects.count()
        self.bucketlist.save() #1
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count,new_count)
        
        
        