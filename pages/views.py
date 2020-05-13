from django.shortcuts import render
from students.models import Student
from marks.models import Mark

def index(request):
    students = Student.objects.all()
    marks = Mark.objects.all()
    table_tuple = ()
    avgMark, rating, temp_rating, temp_count, temp_ex_mark, temp_count_ex_mark = 0, 0, 0, 0, 0, 0
    for student in students:
        for mark in marks:
            if mark.student == student:
                temp_rating = temp_rating + int(mark.mark)
                temp_count = temp_count + 1
                if mark.mark_type == 'Экзамен':
                    temp_ex_mark = temp_ex_mark + int(mark.mark)
                    temp_count_ex_mark = temp_count_ex_mark + 1
        if temp_count != 0:  
            rating = round(temp_rating / temp_count,1) * 10
            temp_rating, temp_count = 0, 0   
        if temp_ex_mark != 0:
            avgMark = temp_ex_mark / temp_count_ex_mark
            temp_ex_mark, temp_count_ex_mark = 0, 0
        textSNP = student.surname + ' ' + student.name + ' ' + student.patronymic
        table_tuple += (textSNP, str(student.group), round(avgMark,2), int(rating)),
    
    table_content = list(table_tuple)
    table_content.sort(key=lambda i: i[3], reverse=True)
    print(table_content)

    context = {
        'table_content': table_content,
    }

    return render(request, 'pages/main.html', context)