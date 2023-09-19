from django import forms


class Form_Profile(forms.Form):
    name = forms.CharField(label='Имя')
    img = forms.ImageField()
    age = (('школьник', 'школьник'), ('студент', 'студент'), ('молодой сотрудник', 'молодой сотрудник'),
           ('сотрудник со стажем', 'сотрудник со стажем'), ('пенсионер', 'пенсионер'))
    age_status = forms.TypedChoiceField(label='Возраст',choices=age)
    nation = (('Россия', 'rus'), ('США', 'en'), ('Германия', 'gmn'),
           ('Франция', 'fr'), ('ОАЭ', 'uae'))
    nation_status = forms.TypedChoiceField(label='Национальность',choices=nation)
    city = forms.CharField(label='Город проживания')
    prof = forms.CharField(label='Профессия')
    language = (('русский', 'rus'), ('английский', 'en'), ('немецкий', 'gmn'),
           ('французский', 'fr'), ('арабский', 'uae'))
    lang_status = forms.TypedChoiceField(label='Язык',choices=language)
    mail = forms.EmailField(label='Эл.почта')
    family_status = forms.NullBooleanField(label='Семейное положение')
    bad_habits = forms.BooleanField(label='Вредные привычки',required=False)

