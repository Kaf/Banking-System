from django.conf.urls.defaults import *



urlpatterns = patterns('',
#url(r'^$', 'bank.view.home'),
url(r'^bank/$', 'bank.views.transfer'),
url(r'^bank/$', 'bank.views.create_account'),
url(r'^bank/', 'bank.views.homepage'),)

