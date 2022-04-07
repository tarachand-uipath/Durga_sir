from django import forms
from testapp.models import Employee


class EmployeeForm(forms.ModelForm):
	def clean_esalary(self):
		inputsal =  self.cleaned_data['esalary']
		if inputsal < 5000:
			raise forms.ValidationError('The minimum salary should be 6000 ')
		return inputsal

	

	class Meta:
		model = Employee
		fields = '__all__'
