from django.contrib import admin
from django.urls import path

from Blog_application.views import editor, delete_document

urlpatterns = [
    path('', editor, name='editor'),
    path('delete_document/<int:docid>/', delete_document, name='delete_document'),
    path('admin/', admin.site.urls),
]