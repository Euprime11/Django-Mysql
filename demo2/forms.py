from django import forms
from . models import Patients


#creating a form
class PatientForm(forms.ModelForm):
	class Meta:
		model = Patients
		fields = [
			"name",
			"description"
		]