from django.shortcuts import render
from prof_person.form import *


# Create your views here.
def index(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        # загружаем изображение (3 строчки)
        img = req.FILES.get('img').read()
        file = open('prof_person/static/img/{0}.jpg'.format(name), 'wb')
        file.write(img)
        # выводим загруженный файл (2 строчки)
        fpath = 'img/{0}.jpg'.format(name)
        age_status = req.POST.get('age_status')
        nation_status = req.POST.get('nation_status')
        city = req.POST.get('city')
        prof = req.POST.get('prof')
        lang_status = req.POST.get('lang_status')
        mail = req.POST.get('mail')
        family_status = req.POST.get('family_status')
        bad_habits = req.POST.get('bad_habits')
        info = {'k1': name, 'k2': fpath, 'k3': age_status, 'k4': nation_status, 'k5': city, 'k6': prof,
                'k7': lang_status, 'k8': mail, 'k9': family_status, 'k10': bad_habits}
        return render(req, 'person_page.html', context=info)

    else:
        person = Form_Profile()
        data = {'form': person}
        return render(req, 'index.html', context=data)
