from django.shortcuts import render
from django.conf import settings

from django.core.mail import send_mail

from .forms import contactForm
# Create your views here.
 
def contact (request):
	title = 'Contact'
	form = contactForm(request.POST or None) 
	confirm_message = None

	if form.is_valid():
		coment = form.cleaned_data['coment']
		name = form.cleaned_data['name']
		subject = 'messsage from ECOM.COM'
		message = '%s %s %s' %(coment, '\n --', name)
		emailFrom = form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom,emailTo, fail_silently= True)
		title ='Thanks'
		confirm_message = ' Thanks for the message we will reach you shortly '
		form = None
	
	context ={ 'title': title, 'form': form, 'confirm_message': confirm_message}
	template ='contact.html'
	return render(request, template, context)