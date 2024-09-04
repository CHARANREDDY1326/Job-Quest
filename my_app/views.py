from django.shortcuts import render, redirect
from job.models import Job
from .user_interface import UserInterface  # Assuming UserInterface is in the same directory
def match_and_display(request):
    ui = UserInterface()
    results = ui.match_candidates_to_jobs(request)
    context = {'jobs': results}
    print(context)
    return render(request, 'my_app/result.html',context)