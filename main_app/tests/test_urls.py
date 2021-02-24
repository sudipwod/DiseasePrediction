from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from main_app.views import patient_ui, home, covid, consult_a_doctor

class TestUrls(SimpleTestCase):

    def test_patient_ui_url_is_resolved(self):
        url = reverse('patient_ui')
        self.assertEquals(resolve(url).func, patient_ui)

    
    def test_doctor_ui_url_is_resolved(self):
        url = reverse('covid')
        self.assertEquals(resolve(url).func, covid)    

    def test_checkdisease_url_is_resolved(self):
        url = reverse('consult_a_doctor')
        self.assertEquals(resolve(url).func, consult_a_doctor)    