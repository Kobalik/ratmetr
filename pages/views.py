from django.shortcuts import render, redirect
from students.models import Student
from marks.models import Mark
from groups.models import Group
from subjects.models import Subject
from django.contrib import messages, auth

def index(request):
    students = Student.objects.all()
    marks = Mark.objects.all()
    groups = Group.objects.all()
    table_tuple = ()
    avgExMark, rating, temp_rating, temp_count, temp_ex_mark, temp_count_ex_mark = 0, 0, 0, 0, 0, 0
    for student in students:
        for mark in marks:
            if mark.student == student:
                if mark.mark_type == 'Семестр':
                    temp_rating = temp_rating + int(mark.mark)
                    temp_count = temp_count + 1
                elif mark.mark_type == 'Экзамен':
                    temp_ex_mark = temp_ex_mark + int(mark.mark)
                    temp_count_ex_mark = temp_count_ex_mark + 1
        if temp_count != 0:  
            rating = (temp_rating / temp_count + temp_ex_mark / temp_count_ex_mark) * 5
            temp_rating, temp_count = 0, 0   
        if temp_ex_mark != 0:
            avgExMark = temp_ex_mark / temp_count_ex_mark
            temp_ex_mark, temp_count_ex_mark = 0, 0
        textSNP = student.surname + ' ' + student.name + ' ' + student.patronymic
        table_tuple += (textSNP, str(student.group), round(avgExMark,2), int(rating)),
    
    table_content = list(table_tuple)
    table_content.sort(key=lambda i: i[3], reverse=True)

    context = {
        'table_content': table_content,
        'groups': groups,
    }

    return render(request, 'pages/main.html', context)

def addMarks(request):
    groups = Group.objects.all()
    subjects = Subject.objects.all() 
    students = '    '
    

    try:
        selected_group = request.GET['group']
        selected_subject = request.GET['subject']
        students_on_group = []
        if selected_group != '':
            students = Student.objects.all()
            for student in students:
                if str(student.group) == selected_group:
                    students_on_group.append(student)
    except Exception:
        selected_group = ''
        students = Student.objects.all()
        students_on_group = []
        students_on_group = students

    context = {
        'groups': groups,
        'subjects': subjects,
        'students': students_on_group,
        'values': request.GET,
        'selected_group': selected_group,
    }
    
    return render(request, 'pages/addmarks.html', context)

def addsubjects(request):
    groups = Group.objects.all()
    
    context = {
        'groups': groups,
    }

    return render(request, 'pages/addsubjects.html', context)

def printdoc(request):
    groups = Group.objects.all()

    context = {
        'groups': groups,
    }
    return render(request, 'pages/vedom.html', context)

def printPDF(request):
    import pdfcrowd
    import sys

    group = request.POST['group']
    type_vedom = request.POST['typeVedom']
    
    if type_vedom == 'Экзаменационная ведомость':
        try:
            # create the API client instance
            client = pdfcrowd.HtmlToPdfClient('RazValik', '2179080295fed93f1c1d97f96dd72818')
            path_to_html_file = 'D:/University/Диплом/ratmetr/templates/groups/{}.html'.format(group)
            path_to_pdf_file = 'D:/University/Диплом/Материалы для диплома/vedom.pdf'

            # run the conversion and write the result to a file
            client.convertFileToFile(path_to_html_file, path_to_pdf_file)
        except pdfcrowd.Error as why:
            # report the error
            sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))

            # rethrow or handle the exception
            raise
        return redirect('index')
    elif type_vedom == 'Контроль текущей успеваемости':
        count_point = request.POST['countPoint']
        try:
            # create the API client instance
            client = pdfcrowd.HtmlToPdfClient('RazValik', '2179080295fed93f1c1d97f96dd72818')
            path_to_html_file = 'D:/University/Диплом/ratmetr/templates/groups/{}({}).html'.format(group, count_point)
            path_to_pdf_file = 'D:/University/Диплом/Материалы для диплома/vedom.pdf'

            # run the conversion and write the result to a file
            client.convertFileToFile(path_to_html_file, path_to_pdf_file)
        except pdfcrowd.Error as why:
            # report the error
            sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))

            # rethrow or handle the exception
            raise
        return redirect('index')
        
    
def search(request):
    selected_group = request.POST['selected_group']

    students = Student.objects.all()
    marks = Mark.objects.all()
    groups = Group.objects.all()
    table_tuple = ()
    avgExMark, rating, temp_rating, temp_count, temp_ex_mark, temp_count_ex_mark = 0, 0, 0, 0, 0, 0
    for student in students:
        if str(student.group) == selected_group:
            for mark in marks:
                if mark.student == student:
                    if mark.mark_type == 'Семестр':
                        temp_rating = temp_rating + int(mark.mark)
                        temp_count = temp_count + 1
                    elif mark.mark_type == 'Экзамен':
                        temp_ex_mark = temp_ex_mark + int(mark.mark)
                        temp_count_ex_mark = temp_count_ex_mark + 1
            if temp_count != 0:  
                rating = (round(temp_rating / temp_count,1) + round(temp_ex_mark / temp_count_ex_mark)) * 5
                temp_rating, temp_count = 0, 0   
            if temp_ex_mark != 0:
                avgExMark = temp_ex_mark / temp_count_ex_mark
                temp_ex_mark, temp_count_ex_mark = 0, 0
            textSNP = student.surname + ' ' + student.name + ' ' + student.patronymic
            table_tuple += (textSNP, str(student.group), round(avgExMark,2), int(rating)),
    
    table_content = list(table_tuple)
    table_content.sort(key=lambda i: i[3], reverse=True)

    context = {
        'table_content': table_content,
        'groups': groups,
        'selected_group': selected_group,
    }

    return render(request, 'pages/search.html', context)

def searchStudent(request):
    groups = Group.objects.all()
    text = request.POST['selected_text']
    students = Student.objects.filter(surname__contains=text)
    
    context = {
        'students': students,
        'text': text,
        'groups': groups,
    }


    return render(request,'pages/searchStudent.html', context)

def dashboard(request):
    groups = Group.objects.all()
    snp = request.GET['snp']
    surname, name, patr = snp.split(' ')

    student = Student.objects.get(name=name, surname=surname, patronymic=patr)
    marks = Mark.objects.filter(student=student.id)

    subject_tuple = ()
    subject_dict = {}
    table_content = ()
    table_tuple = ()

    for mark in marks:
        if str(mark.subject) not in subject_tuple:
            subject_tuple += (str(mark.subject),)

    for subject in subject_tuple:
        all_marks = ''
        ex_marks = ''
        for mark in marks:
            if subject == str(mark.subject):   
                if mark.mark_type == 'Экзамен':
                    ex_marks += str(mark.mark) + ' '
                else: 
                    all_marks += str(mark.mark) + ' '
        table_content += ((subject, all_marks, ex_marks),)            

    context = {
        'marks':marks,
        'student': student, 
        'groups': groups,
        'table_content': table_content,
    }

    return render (request, 'pages/dashboard.html', context)