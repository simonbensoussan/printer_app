from django.test import TestCase
from .models import Bucketlist
# Create your tests here.

class ModelTestCase(TestCase):
    """This class defines test suite odf bucketlist model"""
    
    def setUp(self):
        """ Define the test clents and other variables"""
        self.bucketlist_name = "Class code"
        self.bucketlist_obj = Bucketlist(name=self.bucketlist_name) #1
    
    def test_model_can_create_a_bucketlist(self):
        """Test the model can create a bucketlist"""
        old_count = Bucketlist.objects.count()
        self.bucketlist_obj.save() #1
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count,new_count)
    
    def test_string_model_representation_work(self):
        """Test bucketlist entry's string is equal to the name __str__()"""
        self.bucketlist_name = Bucketlist(name="Entry test")
        self.assertEqual(str(self.bucketlist_name), self.bucketlist_name.name) 
        
        
    def test_verbose_name_plural_of_ours_model(self):
        """test if we have more than one record the instance call bucketlists"""
        self.assertEqual(str(Bucketlist._meta.verbose_name_plural), "Ma list de courses")
