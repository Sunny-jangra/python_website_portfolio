from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    tech_stack = models.CharField(max_length=250, blank=True)
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)

    # ✅ NEW: video (upload)
    video = models.FileField(upload_to="project_videos/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(",") if t.strip()]

    def __str__(self):
        return self.title
    
from django.contrib.auth.models import User

class Like(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('project', 'user')

    def __str__(self):
        return f"{self.user.username} liked {self.project.title}"


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.project.title}"

from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=80)
    # level = models.PositiveIntegerField(default=50)  # 0-100
    note = models.CharField(max_length=120, default="Learning Phase", blank=True)
    # order = models.PositiveIntegerField(default=0)

class Meta:
    ordering = ["name"]
    
    def __str__(self):
        return f"{self.name} ({self.level}%)"
    

from django.db import models

class Skill(models.Model):
    LEVEL_CHOICES = [
        ("learning", "Learning"),
        ("good", "Good"),
        ("mid", "Intermediate"),
    ]

    name = models.CharField(max_length=50, unique=True)
    percent = models.PositiveIntegerField(default=0)   # 0-100
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default="learning")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

    @property
    def stars(self):
        # ⭐ mapping (choose one)
        # Option A: rounding (50% => 3 stars)
        s = round(self.percent / 20)
        return max(0, min(5, int(s)))



