from django.test import TestCase
import os
# Create your tests here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dir = os.path.join(BASE_DIR,'webapps\dist')
print(dir)