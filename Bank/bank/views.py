# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from models import Person

class PersonForm(ModelForm):
	class meta:
	model = Person

def create_account(request):
	account = bank.object.all()
#start form code
	if request.method == 'POST':
		form =PersonForm(request.Post)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(request.path)
	else:
		form = PersonForm()
    		t=loader.get_template('bank/home.html')
    		c= Context({'homeform':homeform.as_p()})
    		return HttpResponse(t.render(c))


# Create your views here.

class transferForm(forms.Form):
	From = forms.PositiveIntegerField()
	To = forms.PositiveIntegerField()
	Amount = forms.FloatField()
	def __unicode__(self):
		return self.From

def transfer(request):
	transfer = transferForm.objects.all()
	for Person.accnum == transfer.From:
		Person.amount= Person.amount -transfer.amount
	for Person.accnum == transfer.To:
		Person.amount = Person.amount + transer.amount
	print 'Transfer Successful'
	t = loader.get_template('bank/transfer.html')
	c = Context({'transfer':transfer})
	return HttpResponse(t.render(c))
