"""
Document models for the Django application.

This module defines the Document model used for storing user documents
with automatic timestamping and activation status tracking.
"""
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

User = settings.AUTH_USER_MODEL # -> "auth.User"

# ORM
class Document(models.Model):
    """
    User document storage model.
    
    Attributes:
        owner: Foreign key to the user who owns the document
        title: Document title (default: "Title")
        content: Document content/body
        active: Whether the document is active
        active_at: Timestamp when the document was activated
        created_at: Auto-set timestamp for document creation
        updated_at: Auto-updated timestamp for document modifications
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # owner_id = models.IntegerField() -> user.id
    title = models.CharField(default="Title")
    content = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    active_at = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # db auto update this field to when it's created
    updated_at  = models.DateTimeField(auto_now=True) # db auto update this field to when it's updated

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        """
        Override save to automatically set active_at timestamp.
        
        Sets active_at to current time when document is activated,
        clears it when deactivated.
        """
        if self.active and self.active_at is None:
            self.active_at = timezone.now()
        else:
            self.active_at = None
        super().save(*args, **kwargs)
