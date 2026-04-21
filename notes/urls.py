from django.urls import path

from .views import (
    note_list,
    note_detail,
    note_create,
    note_update,
    note_delete,
)


urlpatterns = [
    # URl for displaying a list of all notes
    path("", note_list, name="note_list"),
    # URL for displaying details of a specfic note
    path("note/<int:pk>/", note_detail, name="note_detail"),
    # URL for creating a new note
    path("note/new/", note_create, name="note_create"),
    # URL for updating an existing note
    path("note/<int:pk>/edit/", note_update, name="note_update"),
    # URL pattern for deleting a existing note
    path("note/<int:pk>/delete/", note_delete, name="note_delete"),
]
