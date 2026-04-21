from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    """Form for creating and updating Note objects.

    Uses ModelForm to auto-generate fields from the Note model. Only
    title and content are editable; created_at is set automatically.
    """

    class Meta:
        model = Note
        fields = ["title", "content"]
