from django.http import Http404
from django.shortcuts import render, redirect

from .models import Profile
from .forms import ProfileForm, UserProfileForm, ProfileBasicForm


def profile_update_view(request, *args, **kwargs):
    if not request.user.is_authenticated: # is_authenticated()
        return redirect("/login?next=/profile/update")
    user = request.user
    user_data = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email
    }
    my_profile = user.profile
    form = ProfileBasicForm(request.POST or None, instance=my_profile, initial=user_data)
    if form.is_valid():
        user_obj = form.save(commit=False)
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        user_obj.save()
    context = {
        "form": form,
        "btn_label": "Save",
        "title": "Update Profile"
    }
    return render(request, "profiles/form.html", context)



def profile_detail_view(request, username,*args, **kwargs):
    qs = Profile.objects.filter(user__username=username)
    edit = Profile.objects.filter(user__username="edit")
    if edit.exists():
        profile_update_view(request, *args, **kwargs)
        return render(request, "profiles/form.html", context)
    if not qs.exists():
        raise Http404
    profile_obj = qs.first()
    context = {
        "username": username,
        "profile": profile_obj
        }
    return render(request, "profiles/detail.html", context)