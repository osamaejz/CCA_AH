from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, FileResponse, Http404
from urllib.parse import urlencode
import os
from useraccounts.models import Employee, Student
import mimetypes

import sqlite3
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
from . import plot_functions, Pdf_generation
from PIL import Image
import numpy as np

from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages


from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def index(request):
    return HttpResponse("Hello, Admin!")


@login_required
@staff_member_required
def tables_view(request):
    # Retrieve data from the UserAccounts_Employee model
    employees = Employee.objects.all()

    # Retrieve data from the UserAccounts_Student model
    students = Student.objects.all()
    if request.GET.get('email'):

        user_type = request.GET.get('user_type')
        user_id = request.GET.get('user_id')
        name = request.GET.get('name')
        email = request.GET.get('email')
        file_location = save_report(user_type, user_id, name)
        redirect_url = f'/adminaccounts/email/?{urlencode({"file_location": file_location,"email":email})}'
        return redirect(redirect_url)
    elif request.GET.get('user_type'):

        user_type = request.GET.get('user_type')
        user_id = request.GET.get('user_id')
        name = request.GET.get('name')
        file_location = save_report(user_type, user_id, name)
        redirect_url = f'/adminaccounts/download/?{urlencode({"file_location": file_location})}'
        return redirect(redirect_url)

    # Prepare the data to be rendered in the template
    context = {
        'employees': employees,
        'students': students,
    }

    # Render the template with the provided data
    return render(request, 'accounts/tables.html', context)


def send_email(request):
    pdf_path = request.GET.get('file_location')
    to_email = request.GET.get('email')

    subject = "test email"
    body = "your results"

    email = EmailMessage(
        subject, body, settings.DEFAULT_FROM_EMAIL, [to_email])

    # Attach the PDF file
    with open(pdf_path, 'rb') as file:
        email.attach('result.pdf', file.read(), 'application/pdf')

    email.send(fail_silently=False)
    print("Email sent successfully!")
    messages.success(request, 'Email sent to '+to_email)

    return redirect('adminaccounts:table')


def download_pdf(request):
    # Retrieve the file location parameter
    file_location = request.GET.get('file_location')

    path = open(file_location, 'rb')
    mime_type, _ = mimetypes.guess_type(file_location)
    response = HttpResponse(path, content_type=mime_type)

    st = file_location

    substring = st.split('report')[1]

    filename = substring.replace("+", " ")

    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def pdf_list(request):
    # Replace with the path to your PDF directory

    pdf_directory = os.path.join(settings.BASE_DIR, 'report')

    # Get the search query from the URL parameter
    search_query = request.GET.get('q', '')

    # Get the list of PDF files in the directory
    pdf_files = []
    for filename in os.listdir(pdf_directory):
        if filename.endswith('.pdf') and search_query.lower() in filename.lower():
            pdf_files.append(filename)

    context = {
        'pdf_files': pdf_files,
        'search_query': search_query
    }
    return render(request, 'accounts/pdf_list.html', context)


def view_pdf(request, file_path):
    # Construct the absolute path to the PDF file
    pdf_file_path = os.path.join(settings.BASE_DIR, 'report')

    # Check if the file exists
    if os.path.exists(pdf_file_path):
        # Open the PDF file in binary mode
        with open(pdf_file_path, 'rb') as pdf_file:
            response = HttpResponse(
                pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'inline; filename="{file_path}"'
            return response
    else:
        # Return a 404 response if the file does not exist

        raise Http404("PDF file does not exist.")


def save_report(user_type, user_id, name):

    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()

    User = name
    user_type = user_type
    user_id = user_id
    res_id = ""

    if user_type == "e":
        # to get specific value from a table based on condition
        cur.execute(
            "SELECT result_id FROM useraccounts_employee WHERE name = ? AND employee_id = ?",
            (User, user_id))
        res_id = cur.fetchall()
        # converting the value into tuple for input in below query
        res_id = res_id[0]

        # cur.execute("select organization from useraccounts_employee where name = ?", User,)
        # organization = cur.fetchall()
        # organization = organization[0]

        cur.execute(
            "select qualification FROM useraccounts_employee WHERE name = ? AND employee_id = ?",
            (User, user_id))
        qualification = cur.fetchall()
        qualification = qualification[0]

        # cur.execute("select designation from useraccounts_employee where name = ?", User,)
        # designation = cur.fetchall()
        # designation = designation[0]

        cur.execute(
            "select year_of_birth FROM useraccounts_employee WHERE name = ? AND employee_id = ?",
            (User, user_id))
        year_of_birth = cur.fetchall()
        year_of_birth = year_of_birth[0]

        cur.execute(
            "select email FROM useraccounts_employee WHERE name = ? AND employee_id = ?",
            (User, user_id))
        email = cur.fetchall()
        email = email[0]

        cur.execute(
            "select date_created FROM useraccounts_employee WHERE name = ? AND employee_id = ?",
            (User, user_id))
        date_created = cur.fetchall()
        date_created = date_created[0]

    elif user_type == "s":
        # to get specific value from a table based on condition
        cur.execute(
            "SELECT result_id FROM useraccounts_student WHERE name = ? AND student_id = ?",
            (User, user_id))
        res_id = cur.fetchall()
        # converting the value into tuple for input in below query
        res_id = res_id[0]

        # cur.execute("select organization from useraccounts_student where name = ?", User,)
        # organization = cur.fetchall()
        # organization = organization[0]

        # cur.execute("select qualification from useraccounts_student where name = ?", User,)
        # qualification = cur.fetchall()
        # qualification = qualification[0]
        qualification = 'Student'

        # cur.execute("select designation from useraccounts_student where name = ?", User,)
        # designation = cur.fetchall()
        # designation = designation[0]

        cur.execute(
            "select year_of_birth FROM useraccounts_student WHERE name = ? AND student_id = ?",
            (User, user_id))
        year_of_birth = cur.fetchall()
        year_of_birth = year_of_birth[0]

        cur.execute(
            "select email FROM useraccounts_student WHERE name = ? AND student_id = ?",
            (User, user_id))
        email = cur.fetchall()
        email = email[0]

        cur.execute(
            "select date_created FROM useraccounts_student WHERE name = ? AND student_id = ?",
            (User, user_id))
        date_created = cur.fetchall()
        date_created = date_created[0]

    # #to get records of a table
    # sql_select_query = """select * from useraccounts_results """
    # result_records = cur.execute(sql_select_query)
    # #to get column names
    # res_col_names = list(map(lambda x: x[0], result_records.description))

    # to get specific value from a table based on condition
    cur.execute(
        "select anxiety from useraccounts_results where result_id = ?", res_id,)
    anx = cur.fetchall()
    anx = anx[0]
    anx = anx[0]

    cur.execute(
        "select depression from useraccounts_results where result_id = ?", res_id,)
    dep = cur.fetchall()
    dep = dep[0]
    dep = dep[0]

    cur.execute(
        "select lifeSatisfaction from useraccounts_results where result_id = ?", res_id,)
    ls = cur.fetchall()
    ls = ls[0]
    ls = ls[0]

    cur.execute(
        "select stress from useraccounts_results where result_id = ?", res_id,)
    stress = cur.fetchall()
    stress = stress[0]
    stress = stress[0]

    energy = int(ls) / (int(anx) + int(dep) + int(stress))

    # For Digit Span Task
    # to get records of a table
    sql_select_query = """select * from useraccounts_digitspantestresult """
    ds_records = cur.execute(sql_select_query)
    # to get column names
    ds_col_names = list(map(lambda x: x[0], ds_records.description))

    # to get accuracy of digit span from a table based on result ID
    cur.execute(
        "select accuracy from useraccounts_digitspantestresult where result_id = ?", res_id,)
    ds_acc = cur.fetchall()

    # to get reaction time of digit span from a table based on result ID
    cur.execute(
        "select rt from useraccounts_digitspantestresult where result_id = ?", res_id,)
    ds_rt = cur.fetchall()

    ds_score = np.zeros((10, 1), dtype=np.double)
    ds_rtime = np.zeros((10, 1), dtype=np.double)

    for i in range(10):
        ds_score[i] = ds_acc[i][0]
        ds_rtime[i] = ds_rt[i][0]

    ds_scr = np.sum(ds_score)
    ds_scr_percent = (ds_scr/10)*100

    ds_rt_per_avg = ds_rtime / np.mean(ds_rtime)
    mem_perf = ds_scr_percent/ds_rt_per_avg

    # For Visual Array Task
    # to get records of a table
    sql_select_query = """select * from useraccounts_visualarraytestresult """
    va_records = cur.execute(sql_select_query)
    # to get column names
    va_col_names = list(map(lambda x: x[0], va_records.description))

    # to get accuracy of Visual Array Task from a table based on result ID
    cur.execute(
        "select key_press from useraccounts_visualarraytestresult where result_id = ?", res_id,)
    va_rt = cur.fetchall()

    # to get reaction time of Visual Array Task from a table based on result ID
    cur.execute(
        "select rt from useraccounts_visualarraytestresult where result_id = ?", res_id,)
    va_acc = cur.fetchall()  # as accurate responses are named as rt in VA table in DB

    va_score = np.zeros((12, 1), dtype=np.double)
    va_rtime = np.zeros((12, 1), dtype=np.double)

    index = 0
    for correct in range(len(va_acc)):
        if va_acc[correct][0] == 'true':
            va_score[index] = 1
            va_rtime[index] = va_rt[correct][0]
            index += 1

        elif va_acc[correct][0] == 'false':
            va_score[index] = 0
            va_rtime[index] = va_rt[correct][0]
            index += 1

    va_scr = np.sum(va_score)
    va_scr_percent = (va_scr/12)*100

    va_rt_per_avg = va_rtime / np.mean(va_rtime)

    visual_perf = va_scr_percent/va_rt_per_avg

    # for competency calculation
    competency = (ds_scr + va_scr) / (np.mean(ds_rtime) + np.mean(va_rtime))

    if (competency >= 0.001701 and competency <= 0.002658):
        x = 2

    elif (competency < 0.001701):
        x = 1

    else:
        x = 3

    if (energy >= 0.190578866 and energy <= 0.755238762):
        y = 2

    elif (energy < 0.190578866):
        y = 1

    else:
        y = 3

    matrix = str(x) + str(y)
    print(matrix)

    # for memory performance graph
    xm = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    mem_X_Y_Spline = make_interp_spline(xm, mem_perf)
    mem_X_ = np.linspace(xm.min(), xm.max(), 500)
    mem_Y_ = mem_X_Y_Spline(mem_X_)
    plt.figure()
    plt.plot(mem_X_, mem_Y_)
    plt.title("Memory Processing Task")
    plt.xlabel("Tasks")
    plt.ylabel("Performance")

    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.right'] = False
    
    plt.savefig('mem.png',
                transparent=False,
                facecolor='white',
                bbox_inches="tight")
    #plt.show()

    # for visual performance graph
    xv = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    visual_X_Y_Spline = make_interp_spline(xv, visual_perf)
    visual_X_ = np.linspace(xv.min(), xv.max(), 500)
    visual_Y_ = visual_X_Y_Spline(visual_X_)
    plt.figure()
    plt.plot(visual_X_, visual_Y_)
    plt.title("Visual Processing Task")
    plt.xlabel("Tasks")
    plt.ylabel("Performance")
    
    # plt.rcParams['axes.spines.top'] = False
    # plt.rcParams['axes.spines.right'] = False

    plt.savefig('visual.png',
                transparent=False,
                facecolor='white',
                bbox_inches="tight")

    anxiety = (float(int(anx)/42) * 100)
    anxiety = float("{:.2f}".format(anxiety))

    if anxiety <= (float(7/42) * 100):
        anx_arrow = 1

    elif anxiety <= (float(9/42) * 100):
        anx_arrow = 2

    elif anxiety <= (float(14/42) * 100):
        anx_arrow = 3

    elif anxiety <= (float(19/42) * 100):
        anx_arrow = 4

    else:
        anx_arrow = 5

    depression = (float(int(dep)/42) * 100)
    depression = float("{:.2f}".format(depression))

    if depression <= (float(9/42) * 100):
        dep_arrow = 1

    elif depression <= (float(13/42) * 100):
        dep_arrow = 2

    elif depression <= (float(20/42) * 100):
        dep_arrow = 3

    elif depression <= (float(27/42) * 100):
        dep_arrow = 4

    else:
        dep_arrow = 5

    work_stress = (float(int(stress)/40) * 100)
    work_stress = float("{:.2f}".format(work_stress))

    if work_stress <= (float(15/40) * 100):
        ws_arrow = 1

    elif work_stress <= (float(20/40) * 100):
        ws_arrow = 2

    elif work_stress <= (float(25/40) * 100):
        ws_arrow = 3

    elif work_stress <= (float(30/40) * 100):
        ws_arrow = 4

    else:
        ws_arrow = 5

    lifesatis = (float(int(ls)/35) * 100)
    lifesatis = float("{:.2f}".format(lifesatis))

    if lifesatis <= (float(9/35) * 100):
        ls_arrow = 5

    elif lifesatis <= (float(19/35) * 100):
        ls_arrow = 4

    elif lifesatis <= (float(20/35) * 100):
        ls_arrow = 3

    elif lifesatis <= (float(30/35) * 100):
        ls_arrow = 2

    else:
        ls_arrow = 1

    dep_anx_labels = ['Normal', 'Mild', 'Moderate', 'Severe', 'Extr. Severe']

    ws_labels = ['Chilled', 'Fairly Low', 'Moderate', 'Severe', 'Dangerous']

    ls_labels = ['Extr. Satisfy', 'Satisfy',
                 'Neutral', 'dissatisfy', 'Extr. disatisfy']

    plot_functions.gauge(dep_anx_labels, title=(
        "Depression"), arrow=dep_arrow, fname="dep")
    plot_functions.gauge(dep_anx_labels, title=(
        "Anxiety"), arrow=anx_arrow, fname="anx")
    plot_functions.gauge(ws_labels, title=("Work Sress"),
                         arrow=ws_arrow, fname="ws")
    plot_functions.gauge(ls_labels, title=(
        "Life Satisfaction"), arrow=ls_arrow, fname="ls")

    image1 = Image.open('anx.png')
    image2 = Image.open('dep.png')
    image3 = Image.open('ws.png')
    image4 = Image.open('ls.png')

    concatenated_image = plot_functions.concatenate_images(
        [image1, image2, image3, image4], direction='horizontal')
    concatenated_image.save('mental_health.png')

    prompt = Pdf_generation.report(matrix, User, qualification, str(res_id[0]),
                                   year_of_birth, date_created[0:10], email)
    return prompt
