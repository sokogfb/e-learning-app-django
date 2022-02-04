from re import sub

from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from _elms_core.settings import EMAIL_HOST_USER
from courses.models import Course
from home.contact import ContactForm
from home.subscribe import Subscribe


def index(request):
    return render(request, 'index.html', {})


class HomeListView(ListView):
    model = Course
    template_name = 'index.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_courses'] = self.model.objects.all().order_by('?')
        return context


class SearchView(ListView):
    model = Course
    template_name = 'search.html'
    context_object_name = 'courses'
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(title__contains=self.request.GET['q'])


# DataFlair #Send Email
def subscribe(request):
    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        subject = 'Welcome to Smart Learning'
        message = 'Hope you are enjoying your smart learning'
        recepient = str(sub['Email'].value())
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)

        return render(request, 'contact/success.html', {'recepient': recepient})
    return render(request, 'contact/index.html', {'form': sub})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            # message = "\n".join(body.values())
            message = form.cleaned_data['message']

            try:
                send_mail(subject, message, EMAIL_HOST_USER, [EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("home:home")

    form = ContactForm()
    return render(request, "contact/contact.html", {'form': form})
