from django.test import TestCase
from django.urls import reverse
from .models import Note


class NoteModelTest(TestCase):
    def setUp(self):
        # Create a Note object for testing
        Note.objects.create(title="Test Note", content="This is a test note.")

    def test_note_has_title(self):
        # Test that a Note object has the expected title
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, "Test Note")

    def test_note_has_content(self):
        # Test that a Note object has the expected content
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, "This is a test note.")

    def test_note_str_returns_title(self):
        # Test that the __str__ method returns the note's title
        note = Note.objects.get(id=1)
        self.assertEqual(str(note), "Test Note")

    def test_note_created_at_is_set(self):
        # Test that the created_at field is set automatically
        note = Note.objects.get(id=1)
        self.assertIsNotNone(note.created_at)


class NoteViewTest(TestCase):
    def setUp(self):
        # Create a Note object for testing views
        Note.objects.create(title="Test Note", content="This is a test note.")

    def test_note_list_view(self):
        # Test the note-list view
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_note_detail_view(self):
        # Test the note-detail view
        note = Note.objects.get(id=1)
        response = self.client.get(reverse("note_detail", args=[str(note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")
        self.assertContains(response, "This is a test note.")

    def test_note_create_view_get(self):
        # Test that the create form page loads successfully
        response = self.client.get(reverse("note_create"))
        self.assertEqual(response.status_code, 200)

    def test_note_create_view_post(self):
        # Test that submitting the form creates a new note
        response = self.client.post(
            reverse("note_create"),
            {
                "title": "New Note",
                "content": "New note content.",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Note.objects.filter(title="New Note").exists())

    def test_note_update_view(self):
        # Test that submitting the update form changes the note
        note = Note.objects.get(id=1)
        response = self.client.post(
            reverse("note_update", args=[str(note.id)]),
            {
                "title": "Updated Note",
                "content": "Updated content.",
            },
        )
        self.assertEqual(response.status_code, 302)
        note.refresh_from_db()
        self.assertEqual(note.title, "Updated Note")

    def test_note_delete_view(self):
        # Test that the delete view removes the note
        note = Note.objects.get(id=1)
        response = self.client.get(reverse("note_delete", args=[str(note.id)]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(id=note.id).exists())
