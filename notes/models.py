from django.db import models


# Create your models here.
class Note(models.Model):
    """Model representing a single sticky note.

        Flieds:
            title: Short heading for the note, max 200 characters.
            content: The body text of the note.
            created_at: Timestamp set automatically when the note is created.

        Methods:
            __str__: Returns a string representation of the notes, showing the
    title.
    """

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
