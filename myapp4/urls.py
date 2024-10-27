from django.urls import path
from .views import user_form, many_fields_form
from .views import add_use
from .views import upload_image

urlpatterns = [
    path('user/add/', user_form, name='user_form'),
    path('forms/', many_fields_form, name='many_fields_form'),
    path('user/', add_use, name='add_use'),
    path('upload/', upload_image, name='upload_image'),
]
