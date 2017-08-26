import logging

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect


from .models import Drill
from .forms import DrillForm


def intro(request):
    if request.method == "POST":
        form = DrillForm(request.POST)
        if form.is_valid():
            return redirect('drill1_step1')
    else:
        return render(request, 'quiz/intro.html', )


def drill_categories(request):
    categories = Drill.objects.all()  # this is just a placeholder for when we have cats in db
    return render(request, 'quiz/categories.html', {'categories': categories})


# Helper method
def get_current_drill(request):
    # For the current session's drill, save the workstation count estimate
    current = request.session['drill_id']
    current_drill = Drill.objects.get(drill_id=current)
    return current_drill


# Drill: Basic Network Monitoring (BNM)
def drill_bnm_step1(request):
    if request.method == "POST":
        form = DrillForm(request.POST)
        if form.is_valid():
            post = form.save()
            # Save the current drill's uuid in the session object
            request.session['drill_id'] = str(post.drill_id)
            post.save()
            return redirect('drill_bnm_step2')
    else:
        form = DrillForm()
    return render(request, 'quiz/bnm/step1.html', {'form': form})


def drill_bnm_step2(request):
    if request.method == "POST":
        form = DrillForm(request.POST)
        if form.is_valid():
            has_network_monitoring = form.cleaned_data['has_network_monitoring']
            current_drill = get_current_drill(request)
            current_drill.has_network_monitoring = has_network_monitoring
            current_drill.save()

            if has_network_monitoring == '1':
                return redirect('drill_bnm_step3')
            else:
                return redirect('drill_bnm_results')
    else:
        form = DrillForm()
    return render(request, 'quiz/bnm/step2.html', {'form': form})


def drill_bnm_step3(request):
    if request.method == "POST":
        form = DrillForm(request.POST)
        if form.is_valid():
            wannacry_notification_time = form.cleaned_data['wannacry_notification_time']
            current_drill = get_current_drill(request)
            current_drill.wannacry_notification_time = wannacry_notification_time
            current_drill.save()

            return redirect('drill_bnm_results')
    else:
        form = DrillForm()
    return render(request, 'quiz/bnm/step3.html', {'form': form})


def drill_bnm_results(request):
    current_drill = get_current_drill(request)

    # Calculate drill risk results as HIGH (bad), MEDIUM, or LOW (good)
    # noinspection PyBroadException
    try:
        if current_drill.has_network_monitoring == '2' or current_drill.wannacry_notification_time == '':
            current_drill.risk = 'high'
            current_drill.reason = 'no network monitoring'
        elif int(current_drill.wannacry_notification_time) > 10800:
            current_drill.risk = 'high'
            current_drill.reason = 'too long to notify'
        elif 3600 <= int(current_drill.wannacry_notification_time) <= 10800:
            current_drill.risk = 'medium'
            current_drill.reason = 'moderate time to notify'
        else:
            current_drill.risk = 'low'
            current_drill.reason = 'short time to notify'

    except Exception as e:
        logging.error('Something went wrong in calculating risk and reason.')
        logging.error(e)
        current_drill.risk = 'high'
        current_drill.reason = 'error'

    current_drill.save()
    return render(request, 'quiz/bnm/results.html', {'drill': current_drill})


# Drill: Notorious Vulnerabilities
def drill_notorious_vulnerabilities_step1(request):
    if request.method == "POST":
        form = DrillForm(request.POST)
        if form.is_valid():
            post = form.save()
            # Save the current drill's uuid in the session object
            request.session['drill_id'] = str(post.drill_id)
            post.save()
            return redirect('drill_notorious_vulnerabilities_step2')
    else:
        form = DrillForm()
    return render(request, 'quiz/notorious-vulnerabilities/step1.html', {'form': form})


def drill_notorious_vulnerabilities_step2(request):
    if request.method == "POST":
        form = DrillForm(request.POST)
        if form.is_valid():
            current_drill = get_current_drill(request)
            current_drill.wannacry_count = form.cleaned_data['wannacry_count']
            current_drill.save()
            return redirect('drill_notorious_vulnerabilities_step3')
    else:
        form = DrillForm()
    return render(request, 'quiz/notorious-vulnerabilities/step2.html', {'form': form})


def drill_notorious_vulnerabilities_step3(request):
    if request.method == "POST":
        form = DrillForm(request.POST)
        if form.is_valid():
            current_drill = get_current_drill(request)
            current_drill.doublepulsar_count = form.cleaned_data['doublepulsar_count']
            current_drill.save()
            return redirect('drill_notorious_vulnerabilities_step4')
    else:
        form = DrillForm()
    return render(request, 'quiz/notorious-vulnerabilities/step3.html', {'form': form})


def drill_notorious_vulnerabilities_step4(request):
    if request.method == "POST":
        form = DrillForm(request.POST)
        if form.is_valid():
            current_drill = get_current_drill(request)
            current_drill.heartbleed_count = form.cleaned_data['heartbleed_count']
            current_drill.save()
            return redirect('drill_notorious_vulnerabilities_step5')
    else:
        form = DrillForm()
    return render(request, 'quiz/notorious-vulnerabilities/step4.html', {'form': form})


def drill_notorious_vulnerabilities_step5(request):
    if request.method == "POST":
        form = DrillForm(request.POST)
        if form.is_valid():
            current_drill = get_current_drill(request)
            current_drill.shellshock_count = form.cleaned_data['shellshock_count']
            current_drill.save()
            return redirect('drill_notorious_vulnerabilities_step6')
    else:
        form = DrillForm()
    return render(request, 'quiz/notorious-vulnerabilities/step5.html', {'form': form})


def drill_notorious_vulnerabilities_step6(request):
    if request.method == "POST":
        form = DrillForm(request.POST)
        if form.is_valid():
            current_drill = get_current_drill(request)
            current_drill.mirai_count = form.cleaned_data['mirai_count']
            current_drill.save()
            return redirect('drill_notorious_vulnerabilities_results')
    else:
        form = DrillForm()
    return render(request, 'quiz/notorious-vulnerabilities/step6.html', {'form': form})


def drill_notorious_vulnerabilities_results(request):
    current_drill = get_current_drill(request)

    # Calculate drill risk results as HIGH (bad), MEDIUM, or LOW (good)
    # noinspection PyBroadException
    try:
        count = 0

        if current_drill.wannacry_count is not "0":
            count += 1
        if current_drill.doublepulsar_count is not "0":
            count += 1
        if current_drill.heartbleed_count is not "0":
            count += 1
        if current_drill.shellshock_count is not "0":
            count += 1
        if current_drill.mirai_count is not "0":
            count += 1

        if count > 1:
            current_drill.risk = 'high'
            current_drill.reason = 'multiple cases'
        elif count == 1:
            current_drill.risk = 'medium'
            current_drill.reason = 'single case'
        else:
            current_drill.risk = 'low'
            current_drill.reason = 'no cases'

    except:
        logging.error('Something went wrong in calculating risk and reason.')
        current_drill.reason = 'error'
        current_drill.risk = 'high'

    print('debug', current_drill.risk, current_drill.reason)
    current_drill.save()
    return render(request, 'quiz/notorious-vulnerabilities/results.html', {'drill': current_drill})


# Drill: Workstation Inventory
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
                # this used to be step 4, now go directly to results
                current_drill.risk = 'high'
                current_drill.reason = 'no report'
                current_drill.save()
                return redirect('drill1_results')
    else:
        form = DrillForm()
    return render(request, 'quiz/drill1/step3.html', {'form': form})


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
        if current_drill.risk == 'high':
            # we already set risk earlier, probably they didn't have a report
            pass
        elif current_drill.workstation_count_estimate is "0" or current_drill.workstation_count_active is "0":
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
