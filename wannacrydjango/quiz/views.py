import logging

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect


from .models import Drill
from .forms import DrillForm


def index(request):
    template = loader.get_template('quiz/index.html')
    context = {
        'latest_question_list': "1",
    }
    return HttpResponse(template.render(context, request))


def post_list(request):
    posts = Drill.objects.all()
    return render(request, 'quiz/post_list.html', {'posts': posts})


def get_current_drill(request):
    # For the current session's drill, save the workstation count estimate
    current = request.session['drill_id']
    current_drill = Drill.objects.get(drill_id=current)
    return current_drill


# STEP 1: Get email
def drill1_step1(request):
    if request.method == "POST":
        form = DrillForm(request.POST)
        if form.is_valid():
            post = form.save()
            # Save the current drill's uuid in the session object
            request.session['drill_id'] = str(post.drill_id)
            post.save()
            return redirect('drill1_step2')
    else:
        form = DrillForm()
    return render(request, 'quiz/drill1/step1.html', {'form': form})


# STEP 2: Get estimated workstation count
def drill1_step2(request):
    if request.method == "POST":
        form = DrillForm(request.POST)
        if form.is_valid():
            current_drill = get_current_drill(request)
            current_drill.workstation_count_estimate = form.cleaned_data['workstation_count_estimate']
            current_drill.save()
            return redirect('drill1_step3')
    else:
        form = DrillForm()
    return render(request, 'quiz/drill1/step2.html', {'form': form})


# STEP 3: Does the user have a report to review?
def drill1_step3(request):
    if request.method == "POST":
        form = DrillForm(request.POST)
        if form.is_valid():
            has_report = form.cleaned_data['has_report']
            current_drill = get_current_drill(request)
            current_drill.has_report = has_report
            current_drill.save()

            if has_report == '1':
                return redirect('drill1_step5')
            else:
                return redirect('drill1_step4')
    else:
        form = DrillForm()
    return render(request, 'quiz/drill1/step3.html', {'form': form})


# STEP 4: User doesn't have a report to review, they fail the drill
def drill1_step4(request):
    current_drill = get_current_drill(request)

    current_drill.risk = 'high'
    current_drill.reason = 'no report'
    current_drill.save()
    return render(request, 'quiz/drill1/results.html', {'drill': current_drill})


# STEP 5: Get active workstation count
def drill1_step5(request):
    if request.method == "POST":
        form = DrillForm(request.POST)
        if form.is_valid():
            current_drill = get_current_drill(request)
            current_drill.workstation_count_active = form.cleaned_data['workstation_count_active']
            current_drill.save()
            return redirect('drill1_step6')
    else:
        form = DrillForm()
    return render(request, 'quiz/drill1/step5.html', {'form': form})


# STEP 6: Get authentication success count
def drill1_step6(request):
    if request.method == "POST":
        form = DrillForm(request.POST)
        if form.is_valid():
            current_drill = get_current_drill(request)
            current_drill.workstation_count_auth = form.cleaned_data['workstation_count_auth']
            current_drill.save()
            return redirect('drill1_results')
    else:
        form = DrillForm()
    return render(request, 'quiz/drill1/step6.html', {'form': form})


# RESULTS
def drill1_results(request):
    current_drill = get_current_drill(request)

    # Calculate drill risk results as HIGH (bad), MEDIUM, or LOW (good)
    # Of the estimated total workstations, how many were active?
    # noinspection PyBroadException
    try:
        if current_drill.workstation_count_estimate is "0" or current_drill.workstation_count_active is "0":
            # We don't want to divide by zero
            current_drill.risk = 'high'
            current_drill.reason = 'bad active'
        else:
            current_drill.active_percent = \
                float(current_drill.workstation_count_active) / float(current_drill.workstation_count_estimate)
            # Of the total active workstations, how many were successfully authenticated during the scan?
            current_drill.auth_percent = \
                float(current_drill.workstation_count_auth) / float(current_drill.workstation_count_active)
            if float(current_drill.active_percent) > 0.9:
                if float(current_drill.auth_percent) > 0.8:
                    current_drill.risk = 'low'
                    current_drill.reason = 'good active and good auth'
                elif float(current_drill.auth_percent) > 0.6:
                    current_drill.risk = 'medium'
                    current_drill.reason = 'good active and decent auth'
                else:
                    current_drill.risk = 'high'
                    current_drill.reason = 'good active and bad auth'
            elif float(current_drill.active_percent) > 0.7:
                if float(current_drill.auth_percent) > 0.8:
                    current_drill.risk = 'medium'
                    current_drill.reason = 'decent active and auth'
                else:
                    current_drill.risk = 'high'
                    current_drill.reason = 'decent active and bad auth'
            else:
                current_drill.risk = 'high'
                current_drill.reason = 'bad active'
    except:
        logging.error('Something went wrong in calculating risk and reason.')
        current_drill.risk = 'high'
        current_drill.reason = 'bad active'

    current_drill.save()
    return render(request, 'quiz/drill1/results.html', {'drill': current_drill})
