from django.conf.urls.defaults import *



urlpatterns = patterns('',
#url(r'^$', 'bank.view.home'),
url(r'^bank/transfer/$', 'bank.views.transfer'),
url(r'^bank/view/$', 'bank.views.viewMoney'),
url(r'^bank/create/$', 'bank.views.create_account'),
url(r'^bank/$', 'bank.views.homepage'),)

