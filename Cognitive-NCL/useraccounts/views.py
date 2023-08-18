# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect 
from django import forms
from django.http import HttpResponse
from .models import Student,Employee,Results, DigitSpanTestResult, VisualArrayTestResult
from .forms import CreateUserForm
from datetime import datetime
import simplejson as json

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class DetailsForm(forms.Form):
    name = forms.CharField(label="Name")
    birthyear = forms.IntegerField(label="Year of birth", min_value=1920, max_value=2025)
    organization = forms.CharField(label="Organization")
    position = forms.CharField(label="Position")
     
def registerPage(request):
	# if request.user.is_authenticated:
	return redirect('useraccounts:dashboard')
	# else:
		
	# 	if request.method == 'POST':
            
	# 		form = CreateUserForm(request.POST)
	# 		p_form = ProfileForm(request.POST);print("pfrom status");print(p_form);print(p_form.is_valid())
	# 		if(form.is_valid() and p_form.is_valid()):
	# 			print(p_form.is_valid())
	# 			user1 = form.save()
	# 			user = form.cleaned_data.get('username')
	# 			password = form.cleaned_data.get('password1')
	# 			p_form = p_form.save(commit=False)
	# 			p_form.user = user1
	# 			p_form.save()
	# 		else:
	# 			print("abc")
				
	# 	return HttpResponse(json.dumps(form.errors))
    
def loginAPI(request):
    if request.user.is_authenticated:
        return HttpResponse(json.dumps({}))
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse(json.dumps({}))
            else:
                print(json.dumps({"error": "Username or password is incorrect."}))
                return HttpResponse(json.dumps({"error": "Username or password is incorrect."}))

def loginPage(request):
	# if request.user.is_authenticated:
	return redirect('useraccounts:dashboard') 
	# else:
	# 	if request.method == 'POST':
	# 		username = request.POST.get('username')
	# 		password =request.POST.get('password')

	# 		user = authenticate(request, username=username, password=password)

	# 		if user is not None:
	# 			login(request, user)
	# 			return redirect('useraccounts:dashboard')
	# 		else:
	# 			return redirect('useraccounts:assessment')

def logoutUser(request):
	# logout(request)
	return redirect('index')

def employee(request):
    return render(request, 'accounts/employee.html')

def student(request):
    return render(request, 'accounts/student.html')

# #@login_required(login_url='useraccounts:login')         
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

# #@login_required(login_url='useraccounts:login')         
def assessment(request):
    if request.method == 'GET':
        #CHECK STUDENT OR CORPORATE
        # detail = request.GET
        # print(detail)
        request.session['detail'] = request.GET
        return render(request, 'accounts/assessment.html', {'error': 'Success.'})
    else:
        print("Some error occured")
    #return HttpResponse('Visual Array Processed')
    
    # if request.method == 'GET':
    #    if OTP.objects.filter(otp = request.GET.get('OTP')).exists():
    #       validity = OTP.objects.filter(otp = request.GET.get('OTP')).values('valid')[0]['valid']
    #       print("CODE:", validity)
    #       if(validity==1):
    #           #OTP.objects.filter(otp=request.GET.get('OTP')).update(valid=0)
    #           #return render(request, 'accounts/assessment.html')
    #           return render(request, 'accounts/assessment.html', {'error': 'Success.'})
    #       else:
    #           return render(request, 'accounts/dashboard.html', {'error': 'This code is already used.'})
    #    else:
    #       return render(request, 'accounts/dashboard.html', {'error': 'You entered the wrong OTP.'})
       
# #@login_required(login_url='useraccounts:login')         
def processDigitSpan(request):
    if request.method == 'POST':
        print(request.POST.get('filename'))
        print(request.POST.get('filedata'))
        request.session['digitspan'] = request.POST.get('filedata')
    else:
        print("Some error occured")
    return HttpResponse('Digit Span Processed')

# #@login_required(login_url='useraccounts:login')         
def processSymmetrySpan(request):
    if request.method == 'POST':
        print(request.POST.get('filename'))
        print(request.POST.get('filedata'))
        request.session['symmetryspan'] = request.POST.get('filedata')
    else:
        print("Some error occured")
    return HttpResponse('Symmetry Span Processed')

##@login_required(login_url='useraccounts:login')         
def processVisualArray(request):
    if request.method == 'POST':
        print(request.POST.get('filename'))
        print(request.POST.get('filedata'))
        request.session['visualarray'] = request.POST.get('filedata')
    else:
        print("Some error occured")
    return HttpResponse('Visual Array Processed')

##@login_required(login_url='useraccounts:login')         
def tmt(request):
    return render(request, 'accounts/tmt.html')

##@login_required(login_url='useraccounts:login')         
def nback(request):
    return render(request, 'accounts/nback.html')

#@login_required(login_url='useraccounts:login')         
def results(request):
    if request.method == 'POST':

        startTime = int(request.POST.get('startTime') if 'startTime' in request.POST else "0")
        import time
        endTime = round(time.time())
        duration = endTime - startTime
        # print(duration)
        #Depression
       
        d1 = int(request.POST.get('d1') if 'd1' in request.POST else "0") 
        d2 = int(request.POST.get('d2') if 'd2' in request.POST else "0")
        d3 = int(request.POST.get('d3') if 'd3' in request.POST else "0")
        d4 = int(request.POST.get('d4') if 'd4' in request.POST else "0")
        d5 = int(request.POST.get('d5') if 'd5' in request.POST else "0")
        d6 = int(request.POST.get('d6') if 'd6' in request.POST else "0")
        d7 = int(request.POST.get('d7') if 'd7' in request.POST else "0")
        
        depression = (d1 + d2 + d3 + d4 + d5 + d6 + d7)*2
        checkDepression(depression)
        print("Depression: " , checkDepression(depression))
        
        #Anxiety
        a1 = int(request.POST.get('a1') if 'a1' in request.POST else "0")
        a2 = int(request.POST.get('a2') if 'a2' in request.POST else "0")
        a3 = int(request.POST.get('a3') if 'a3' in request.POST else "0")
        a4 = int(request.POST.get('a4') if 'a4' in request.POST else "0")
        a5 = int(request.POST.get('a5') if 'a5' in request.POST else "0")
        a6 = int(request.POST.get('a6') if 'a6' in request.POST else "0")
        a7 = int(request.POST.get('a7') if 'a7' in request.POST else "0")
        
        anxiety = (a1 + a2 + a3 + a4 + a5 + a6 + a7)*2
        print("Anxiety: ", checkAnxiety(anxiety))
        
        #Work Satisfaction
        w1 = int(request.POST.get('w1') if 'w1' in request.POST else "0")
        w2 = int(request.POST.get('w2') if 'w2' in request.POST else "0")
        w3 = int(request.POST.get('w3') if 'w3' in request.POST else "0")
        w4 = int(request.POST.get('w4') if 'w4' in request.POST else "0")
        w5 = int(request.POST.get('w5') if 'w5' in request.POST else "0")
        w6 = int(request.POST.get('w6') if 'w6' in request.POST else "0")
        w7 = int(request.POST.get('w7') if 'w7' in request.POST else "0")
        w8 = int(request.POST.get('w8') if 'w8' in request.POST else "0")
        
        workStress = (w1 + w2 + w3 + w4 + w5 + w6 + w7 + w8)
        print("Work Stress: " , checkStress(workStress))
        
        #Life Satisfaction
        l1 = int(request.POST.get('l1') if 'l1' in request.POST else "0")
        l2 = int(request.POST.get('l2') if 'l2' in request.POST else "0")
        l3 = int(request.POST.get('l3') if 'l3' in request.POST else "0")
        l4 = int(request.POST.get('l4') if 'l4' in request.POST else "0")
        l5 = int(request.POST.get('l5') if 'l5' in request.POST else "0")
        
        lifeSatisfaction = (l1 + l2 + l3 + l4 + l5)
        print("Life Satisfaction: " , checkLifeSatisfaction(lifeSatisfaction))
        
        #Sleep
        
        #Bedtime
        '''s1 = request.POST.get('s1') if 's1' in request.POST else ""
        
        s2 = int(request.POST.get('s2') if 's2' in request.POST else "0")
        #Getting up time
        s3 = request.POST.get('s3') if 's3' in request.POST else ""

        sleeptime = datetime.strptime(s1, "%H:%M")
        uptime = datetime.strptime(s3, "%H:%M")
        duration = sleeptime-uptime
        hoursInBed = int(abs(int(duration.total_seconds()))/3600)
     
        #Number of hours spent 
        s4 = int(request.POST.get('s4') if 's4' in request.POST else "0")
        sleepEfficiency = (hoursInBed/s4)*100
        
        if(sleepEfficiency<65):
            c4 = 3
        elif(sleepEfficiency>=65 and sleepEfficiency<=74):
            c4 = 2
        elif(sleepEfficiency>=75 and sleepEfficiency<=84):
            c4 = 1
        elif(sleepEfficiency>84):
            c4 = 0
        
        s6 = int(request.POST.get('s6') if 's6' in request.POST else "0")
        s7 = int(request.POST.get('s7') if 's7' in request.POST else "0")
        s8 = int(request.POST.get('s8') if 's8' in request.POST else "0")
        s9 = int(request.POST.get('s9') if 's9' in request.POST else "0")
        
        s51 = int(request.POST.get('s51') if 's51' in request.POST else "0") #5a
        s52 = int(request.POST.get('s52') if 's52' in request.POST else "0") #5b
        s53 = int(request.POST.get('s53') if 's53' in request.POST else "0") #5c
        s54 = int(request.POST.get('s54') if 's54' in request.POST else "0") #5d
        s55 = int(request.POST.get('s55') if 's55' in request.POST else "0") #5e
        s56 = int(request.POST.get('s56') if 's56' in request.POST else "0") #5f
        s57 = int(request.POST.get('s57') if 's57' in request.POST else "0") #5g
        s58 = int(request.POST.get('s58') if 's58' in request.POST else "0") #5h
        s59 = int(request.POST.get('s59') if 's59' in request.POST else "0") #5i
        s510 = int(request.POST.get('s510') if 's510' in request.POST else "0") #5j
        
        #Component 5: Sleep Disturbances 
        sum5bto5j = s52 + s53 + s54 + s55 + s56 + s57 + s58 + s59 + s510
        
        if(sum5bto5j==0):
            c5 = 0
        elif(sum5bto5j>=1 and sum5bto5j<=9):
            c5 = 1
        elif(sum5bto5j>=10 and sum5bto5j<=18):
            c5 = 2
        elif(sum5bto5j>=19 and sum5bto5j<=27):
            c5 = 3
        
        c1 = s6
        c2 = s2 + s51
        
        if(c2!=0 and c2%2==0):
            c2 = c2/2
        elif(c2!=0 and c2%2!=0):
            c2 = (c2+1)/2
            
        c3 = s4
        c6 = s7
        
        #Component 7: Daytime Dysfunction
        c7 = s8 + s9
        if(c7!=0 and c7%2==0):
            c7 = c2/2
        elif(c7!=0 and c7%2!=0):
            c7 = (c7+1)/2
        
        psqiScore = c1 + c2 + c3 + c4 + c5 + c6 + c7
        print(psqiScore)
        
        if(psqiScore <=5):
            sleep = "Good Quality Sleep"
        else:
            sleep = "Poor Quality Sleep"
        '''
        
        if 'detail' in request.session:
            participant = request.session['detail']
            print(participant)
        else:
            print("participant not found")
        
  
        if 'visualarray' in request.session:
            visualarray = request.session['visualarray']
        else:
            visualarray = ""
        
        if 'symmetryspan' in request.session:
            symmetryspan = request.session['symmetryspan']
        else:
            symmetryspan = ""
            
        if 'digitspan' in request.session:
            digitspan = request.session['digitspan']
        else:
            digitspan = ""
        
        # print(visualarray)
        # obj = ast.literal_eval(digitspan)
        # print(obj)

        if participant['detail-of']=='student':
            student = Student.objects.create(name=participant['name'],roll_no=participant['roll_no'],batch=participant['batch'],semester=participant['semester'],department=participant['department'],year_of_birth=participant['year_of_birth'],email=participant['email'])
            last_student_id = student.student_id
        elif participant['detail-of']=='employee':
            employee = Employee.objects.create(name=participant['name'],organization=participant['org_name'],qualification=participant['qualification'],designation=participant['designation'],year_of_birth=participant['year_of_birth'],email=participant['email'])
            last_employee_id = employee.employee_id

        result = Results.objects.create(anxiety=str(anxiety), depression=str(depression),
                               stress=str(workStress),lifeSatisfaction=str(lifeSatisfaction),
                               visualarray=visualarray,digitspantest=digitspan,test2=symmetryspan,d1=d1,d2=d2,d3=d3,d4=d4,d5=d5,
                               d6=d6,d7=d7,a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,w1=w1,w2=w2,w3=w3,
                               w4=w4,w5=w5,w6=w6,w7=w7,w8=w8,l1=l1,l2=l2,l3=l3,l4=l4,l5=l5,assessment_duration=duration)
        last_result_id = result.result_id

        if participant['detail-of']=='student':
            s = Student.objects.get(student_id=last_student_id)
            s.result_id = last_result_id
            s.save()
        elif participant['detail-of']=='employee':
            e = Employee.objects.get(employee_id=last_employee_id)
            e.result_id = last_result_id
            e.save()

        #last_result_id = Results.objects.latest('id').result_id
        #print(last_result_id)
        #DigitSpan.objects.create(result_id=last_result_id,)
        #print('digitspan = ')
        linesplitDS = digitspan.splitlines()
        for i in linesplitDS[1:]: 
            temp = i.strip('"')
            new_row = temp.split('","')
            DigitSpanTestResult.objects.create(result_id=last_result_id, rt=new_row[0], recall = new_row[1], stimuli = new_row[2], accuracy = new_row[3], trial_type = new_row[4], trial_index = new_row[5], time_elapsed = new_row[6], internal_node_id= new_row[7])

        linesplitVA = visualarray.splitlines()
        # print(linesplitVA)
        for j in linesplitVA[1:]: 
            temp2 = j[1:-1]
            new_row_VA = temp2.split('","')
            # print("new_row_VA = ")
            # print(new_row_VA)
            VisualArrayTestResult.objects.create(result_id=last_result_id, trial_type=new_row_VA[0], trial_index=new_row_VA[1], time_elapsed=new_row_VA[2], set_size=new_row_VA[3],	locations=new_row_VA[4], colours=new_row_VA[5], correct=new_row_VA[6], rt=new_row_VA[7], key_press=new_row_VA[8], target_different=new_row_VA[9])
        
        context = {'depression': checkDepression(depression),
                   'anxiety':checkAnxiety(anxiety),
                   'lifeSatisfaction': checkLifeSatisfaction(lifeSatisfaction),
                   'workStress':checkStress(workStress)
                   }
        
        return render(request, 'accounts/results.html', context)

def checkDepression(depression):
    if depression >=0 and depression <=9:
        return "Normal."
    elif depression >=10 and depression <=13:
        return "Mild."
    elif depression >=14 and depression <=20:
        return "Moderate."
    elif depression >=21 and depression <=27:
        return "Severe."
    elif depression >28:
        return "Extremely Severe."
    
def checkStress(stress):
    if stress<=15:
        return "Chilled out and relatively calm."
    elif stress >=16 and stress <=20:
        return "Fairly low."
    elif stress >=20 and stress <=25:
        return "Moderate stress."
    elif stress >=26 and stress <=30:
        return "Severe."
    elif stress >=31 and stress <=40:
        return "Stress level is potentially dangerous."

def checkLifeSatisfaction(lifeSatisfaction):
    if lifeSatisfaction >=5 and lifeSatisfaction <=9:
        return "Extremely dissatisfied."
    elif lifeSatisfaction >=10 and lifeSatisfaction <=14:
        return "Dissatisfied."
    elif lifeSatisfaction >=15 and lifeSatisfaction <=19:
        return "Slightly dissatisfied."
    elif lifeSatisfaction ==20:
        return "Neutral."
    elif lifeSatisfaction >=21 and lifeSatisfaction <=25:
        return "Slightly satisfied."
    elif lifeSatisfaction >=26 and lifeSatisfaction <=30:
        return "Satisfied."
    elif lifeSatisfaction >=31 and lifeSatisfaction <=35:
        return "Extremely Satisfied."

def checkAnxiety(anxiety):
    if anxiety >=0 and anxiety <=7:
        return "Normal."
    elif anxiety >=8 and anxiety <=9:
        return "Mild."
    elif anxiety >=10 and anxiety <=14:
        return "Moderate."
    elif anxiety >=15 and anxiety <=19:
        return "Severe."
    elif anxiety > 20:
        return "Extremely Severe."
    

def checkSleep(sleep):
    pass
    
#python manage.py runserver