from django.urls import path
from .import views
from portal.views import (Creat_list, Update_list, Delete_form, List_Registration, Create_Registration,
                          Delete_Registration, )


urlpatterns = [
    path('event/', views.event, name='event'),
    path('reg/', views.registration, name='registration'),
    path('list/', views.event_list, name='event_list'),
    path('details/<int:id>/', views.event_detail, name='event_detail'),

    path('model-event/', views.modelevent, name='model-event'),
    path('model-registration/', views.Registration_modle, name='model-registration'),

    path('class-view/', views.Class_View.as_view(), name='class-view'),
    path('list-view/', views.List_View.as_view(), name='list-view'),
    path('create-list/', Creat_list.as_view(), name='create-list'),
    path('update-form/<int:pk>/', Update_list.as_view(), name='update-list'),
    path('delete-form/<int:pk>/', Delete_form.as_view(), name='delete-form'),
    path('reg-list/', List_Registration.as_view(), name='reg-list'),
    path('create-reg/', Create_Registration.as_view(), name='create-reg'),
    path('delete-reg/<int:pk>/', Delete_Registration.as_view(), name='delete-reg')

]
