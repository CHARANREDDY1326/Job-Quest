from django.shortcuts import render,redirect
from django.contrib import messages

def render_analytics(request):
    is_applicant = request.user.is_applicant
    print(is_applicant)
    context = {'is_applicant': is_applicant}
    return render(request,'analytics/analytics.html',context)