from django.shortcuts import render, HttpResponse
from django.urls import reverse
from .forms import Event_model, Registration_modle
from .models import Event, Registration
from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.
def event(request):
    if request.method == 'POST':
        titl = request.POST.get('title')
        des = request.POST.get('description')
        dat = request.POST.get('date')
        locat = request.POST.get('location')
        eve = Event(title=titl, description=des, date=dat, locathbion=locat)
        print(titl, des, dat, locat)
        eve.save()

        return HttpResponse('Your Event is registered')
    else:
        request.method == 'GET'
        return render(request, 'portal/eventform.html',)


def registration(request):
    if request.method == 'GET':
        return render(request, 'portal/registration.html',)
    else:
        request.method == 'POST'
        name = request.POST.get('name')
        email = request.POST.get('email')
        event = request.POST.get('event')
        eve = Event.objects.get(title=event)
        reg = Registration(name=name, email=email, event=eve)
        reg.save()
        return HttpResponse('this is registration form')


def event_list(request):
    # if request.method == 'POST':
    list = Event.objects.all()
    return render(request, 'portal/event-list.html', {'list': list})


def event_detail(request, id):
    event = Event.objects.get(id=id)
    return render(request, 'portal/event-details.html', {"event": event})


def modelevent(request):
    if request.method == 'POST':
        form = Event_model(request.POST)
        # if form.is_valid():
        form.save()
        return HttpResponse(f'{form} is your form ')
        # return render(request, 'portal/eventform.html', {'from': form})
    else:
        form = Event_model()
        return render(request, 'portal/eventform.html', {'form': form})


def model_registration(request):
    if request.method == 'POST':
        form = Registration_modle()
        form.save()
    else:
        form = Registration_modle()
        return render(request, 'portal/registrationform.html', {'form': form})


class Class_View(TemplateView):
    template_name = 'portal/classview.html'


class List_View(ListView):
    model = Event
    context_object_name = 'event'
    template_name = 'portal/listview.html'


class Creat_list(CreateView):
    model = Event
    template_name = 'portal/listview.html'
    fields = ['title', 'description', 'location', 'date']
    # success_url = ''

    def get_success_url(self):
        return reverse('create-list')


class Update_list(UpdateView):
    model = Event
    template_name = 'portal/updateform.html'
    fields = ['title', 'description', 'location']

    def get_success_url(self):
        return reverse('create-list')


class Delete_form(DeleteView):
    model = Event
    template_name = 'portal/deleteform.html'

    def get_success_url(self):
        return reverse('create-list')


class List_Registration(ListView):
    model = Registration
    template_name = 'portal/listview.html'
    context_object_name = 'registration'


class Create_Registration(CreateView):
    model = Registration
    template_name = 'portal/create-registration.html'
    fields = ['name', 'email', 'event']

    def get_success_url(self):
        return reverse('reg-list')


class Delete_Registration(DeleteView):
    model = Registration
    template_name = 'portal/delete-registration.html'

    def get_success_url(self):
        return reverse('create-reg')

