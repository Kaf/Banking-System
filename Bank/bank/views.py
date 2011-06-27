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


