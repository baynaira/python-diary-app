from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from .models import DiaryEntry
from .forms import DiaryEntryForm
from django.http import HttpResponse
from django.contrib import messages


def home(request):
    if request.user.is_authenticated:
        return redirect('diary:entry_list')  # Assuming you have an 'entry_list' view for logged in users
    return redirect('diary:register')  # Redirect unauthenticated users to register


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("diary:entry_list")  # Adjust redirect to an appropriate view
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()
    return render(request, "diary/register.html", {"form": form})  # Ensure this template path is correct


@login_required
def entry_list(request):
    entries = DiaryEntry.objects.filter(user=request.user).order_by('-date_posted')
    return render(request, 'diary/entry_list.html', {'entries': entries})

@login_required
def entry_detail(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)
    return render(request, 'diary/entry_detail.html', {'entry': entry})

@login_required
def entry_create(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('diary:entry_detail', pk=entry.pk)
    else:
        form = DiaryEntryForm()
    return render(request, 'diary/entry_form.html', {'form': form})

@login_required
def entry_edit(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('diary:entry_detail', pk=entry.pk)
    else:
        form = DiaryEntryForm(instance=entry)
    return render(request, 'diary/entry_form.html', {'form': form})

@login_required
def entry_delete(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        entry.delete()
        return redirect('diary:entry_list')
    return render(request, 'diary/entry_confirm_delete.html', {'entry': entry})
