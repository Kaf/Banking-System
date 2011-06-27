# Create your views here.

class transferForm(forms.Form):
	From = forms.PositiveIntegerField()
	To = forms.PositiveIntegerField()
	Amount = forms.FloatField()
	def __unicode__(self):
		return self.From

def transfer(request):
	transfer = transferForm.objects.all()
	t = loader.get_template('bank/transfer.html')
	c = Context({'transfer':transfer})
	return HttpResponse(t.render(c))
