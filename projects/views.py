from django.shortcuts import render, get_object_or_404
from .models import Project
from .models import Project, Skill

def home(request):
    latest_projects = Project.objects.order_by('-created_at')[:3]
    return render(request, 'projects/home.html', {'latest_projects': latest_projects})

def project_list(request):
    projects = Project.objects.order_by('-created_at')
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

def about(request):
    return render(request, 'projects/about.html')

def contact(request):
    return render(request, 'projects/contact.html')

def home(request):
    skills = Skill.objects.all()
    return render(request, "projects/home.html", {"skills": skills})

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Project, Like, Comment

@require_POST
@login_required
def toggle_like(request, pk):
    project = get_object_or_404(Project, pk=pk)

    like = Like.objects.filter(project=project, user=request.user).first()
    if like:
        like.delete()
    else:
        Like.objects.create(project=project, user=request.user)

    # ✅ SAME PAGE pe wapas
    return redirect(request.META.get("HTTP_REFERER", "projects"))


@require_POST
@login_required
def add_comment(request, pk):
    project = get_object_or_404(Project, pk=pk)
    text = request.POST.get("comment", "").strip()

    if text:
        Comment.objects.create(project=project, user=request.user, text=text)

    # ✅ SAME PAGE pe wapas
    return redirect(request.META.get("HTTP_REFERER", "projects"))

from django.shortcuts import render

def contact(request):
    if request.method == "POST":
        # yaha future me email send / db save kar sakte ho
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        return render(request, "projects/contact.html", {"success": True})

    return render(request, "projects/contact.html")

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"Portfolio Contact Message from {name}"
        body = f"""
Name: {name}
Email: {email}

Message:
{message}
"""

        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        # ⭐ SUCCESS MESSAGE
        messages.success(request, "Message sent successfully! I will contact you soon 😊")

        return redirect("contact")   # reload page

    return render(request, "projects/contact.html")

from django.shortcuts import render
from .models import Skill

def about(request):
    skills = Skill.objects.all()
    return render(request, "projects/about.html", {"skills": skills})















