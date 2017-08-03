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
        print('before validation')

        if form.is_valid():
            print('passed validation')

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
    return render(request, 'quiz/drill1/step4.html',)


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
    return render(request, 'quiz/drill1/results.html', {'drill': get_current_drill(request)})
