from django.urls import path
from . import views


urlpatterns = [
    path('contact/',views.view_contact,name='view_contact'),
    path('contact_delete/<int:idC>',views.delete_contact,name='delete_contact'),
    # path('contact/',views.post_contact,name='post_contact')
]