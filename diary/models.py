from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class DiaryEntry(models.Model):
    # Link each entry to a user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='diary_entries')
    # Content of the diary entry, text field is suitable for long text
    content = models.TextField()
    # Automatically set the date when the entry is first created
    date_posted = models.DateTimeField(default=timezone.now)
    # Optional: Add a field to track when an entry was last updated
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        # This will display the entry content in admin or shell
        return f'Entry by {self.user.username} on {self.date_posted.strftime("%Y-%m-%d %H:%M:%S")}'

    class Meta:
        # Orders the returned entries by date, newest first
        ordering = ['-date_posted']

