import datetime

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from _elms_core.settings import EMAIL_HOST_USER
from courses.models import Course
from home.contact import ContactForm
from home.models import Event, Blog
from home.subscribe import Subscribe


class HomeListView(ListView):
    model = Course
    template_name = 'lms/index.html'
    context_object_name = 'courses'
    date_today = datetime.datetime.now().date()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_courses'] = self.model.objects.all().order_by('?')
        context['recent_news'] = Blog.objects.all().order_by('-created_at')[:10]
        context['upcoming_events'] = Event.objects.all().order_by('-created_at').filter(
            event_date__gte=datetime.datetime.now())
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


# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = "Website Inquiry"
#             body = {
#                 'first_name': form.cleaned_data['first_name'],
#                 'last_name': form.cleaned_data['last_name'],
#                 'email': form.cleaned_data['email_address'],
#                 'message': form.cleaned_data['message'],
#             }
#             message = "\n".join(body.values())
#             # message = form.cleaned_data['message']
#
#             try:
#                 send_mail(subject, message, EMAIL_HOST_USER, [EMAIL_HOST_USER])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect("home:home")
#
#     form = ContactForm()
#     return render(request, "lms/contact-1.html", {'form': form})


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
            message = "\n".join(body.values())

            try:
                # send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
                send_mail(subject, message, EMAIL_HOST_USER, [EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("home:home")

    form = ContactForm()
    return render(request, "lms/contact-1.html", {'form': form})


def about(request):
    return render(request, "lms/about-2.html")


class blogList(ListView):
    paginate_by = 6
    model = Blog
    template_name = 'lms/blog-classic-grid.html'
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all().order_by('-created_at')[:3]
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'lms/blog-details.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        slug = self.kwargs.get(self.slug_url_kwarg)
        slug_field = self.get_slug_field()
        queryset = queryset.filter(**{slug_field: slug})

        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404("No %(verbose_name)s found matching the query" %
                          {'verbose_name': self.model._meta.verbose_name})
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_blogs'] = Blog.objects.all().order_by('-created_at')[:3]
        return context


def eventList(request):
    all_events = Event.objects.all().order_by('created_at')
    happening_events = Event.objects.all().order_by('created_at').filter(event_date=datetime.datetime.now())
    upcoming_events = Event.objects.all().order_by('created_at').filter(
        event_date__gt=datetime.datetime.now() + datetime.timedelta(days=1))
    expired_events = Event.objects.all().order_by('created_at').filter(event_date__lte=datetime.datetime.now())
    template_name = 'lms/event.html'
    return render(request, template_name,
                  {'all': all_events, 'hp': happening_events, 'up': upcoming_events, 'ep': expired_events})


class EventDetailView(DetailView):
    model = Event
    template_name = 'lms/events-details.html'
    context_object_name = 'event'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        slug = self.kwargs.get(self.slug_url_kwarg)
        slug_field = self.get_slug_field()
        queryset = queryset.filter(**{slug_field: slug})

        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404("No %(verbose_name)s found matching the query" %
                          {'verbose_name': self.model._meta.verbose_name})
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_events'] = Event.objects.all().order_by('-created_at')[:3]
        return context
