from django.shortcuts import render, get_object_or_404, redirect

from .models import Note
from .forms import NoteForm


def note_list(request):
    """Display a list of all sticky notes.

    :param request: HTTP request object.
    :return: Rendered template showing all notes.
    """
    notes = Note.objects.all()
    context = {
        "notes": notes,
        "page_title": "My Sticky Notes",
    }
    return render(request, "notes/note_list.html", context)


def note_detail(request, pk):
    """Display a single sticky note.

    :param request: HTTP request object.
    :param pk: Primary key of the note to display.
    :return: Rendered template showing the note's details.
    """
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


def note_create(request):
    """Create a new sticky note.

    Handles both GET (display blank form) and POST (save submitted form).

    :param request: HTTP request object.
    :return: Rendered form on GET or redirect to list on successful POST.
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm()
    return render(request, "notes/note_form.html", {"form": form})


def note_update(request, pk):
    """Update an existing sticky note.

    Handles both GET (display form pre-filled with the note's data)
    and POST (save the updated data).

    :param request: HTTP request object.
    :param pk: Primary key of the note to update.
    :return: Rendered form on GET or redirect to list on successful POST.
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm(instance=note)
    return render(request, "notes/note_form.html", {"form": form})


def note_delete(request, pk):
    """Delete an existing sticky note.

    :param request: HTTP request object.
    :param pk: Primary key of the note to delete.
    :return: Redirect to the note list.
    """
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect("note_list")
