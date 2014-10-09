# Create your views here.
from django.shortcuts import render_to_response, HttpResponseRedirect
from mysite.contact.forms import ContactForm
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                    cd['subject'],
                    cd['message'],
                    cd.get('email', '57259644@qq.com'),
                    ['wangzhaojiang2013@gmail.com'],
                    )
            return HttpResponseRedirect('/contact/thanks')

    else:
        form = ContactForm(
                initial = {'subject': 'I Love Your Site!'} #初始值
    return render_to_response('contact_form.html', {'form': form})
