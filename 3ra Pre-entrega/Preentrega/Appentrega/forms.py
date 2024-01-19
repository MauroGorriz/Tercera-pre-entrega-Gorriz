from django import forms

class form_bcen(forms.Form):
    modelo = forms.CharField(max_length=40)
    materiales_carcaza = forms.CharField(max_length=40)
    materiales_voluta = forms.CharField(max_length=40)
    presion = forms.IntegerField()
    caudal = forms.IntegerField()
    altura = forms.IntegerField()
    temp = forms.IntegerField()

class form_btor(forms.Form):
    modelo = forms.CharField(max_length=40)
    materiales_carcaza = forms.CharField(max_length=40)
    materiales_tornillo = forms.CharField(max_length=40)
    presion = forms.IntegerField()
    caudal = forms.IntegerField()
    altura = forms.IntegerField()
    temp = forms.IntegerField()

class form_beng(forms.Form):
    modelo = forms.CharField(max_length=40)
    materiales_carcaza = forms.CharField(max_length=40)
    materiales_engranajes = forms.CharField(max_length=40)
    presion = forms.IntegerField()
    caudal = forms.IntegerField()
    altura = forms.IntegerField()
    temp = forms.IntegerField()