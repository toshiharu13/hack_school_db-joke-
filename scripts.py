import random

from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from models import Chastisement, Commendation, Lesson, Mark, Schoolkid

COMMENDATIONS = ('Молодец!', 'Отлично!', 'Хорошо!',
                 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!',
                 'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!',
                 'Именно этого я давно ждал от тебя!',
                 'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!',
                 'Очень хороший ответ!', 'Талантливо!',
                 'Ты сегодня прыгнул выше головы!',
                 'Я поражен!', 'Уже существенно лучше!', 'Потрясающе!',
                 'Замечательно!', 'Прекрасное начало!', 'Так держать!',
                 'Ты на верном пути!', 'Здорово!',
                 'Это как раз то, что нужно!', 'Я тобой горжусь!',
                 'С каждым разом у тебя получается всё лучше!',
                 'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!',
                 'Ты растешь над собой!', 'Ты многое сделал, я это вижу!',
                 'Теперь у тебя точно все получится!'
                 )


def create_commendation(name, subject):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
        lessons_fetch = Lesson.objects.filter(
            year_of_study__contains=schoolkid.year_of_study,
            group_letter__contains=schoolkid.group_letter,
            subject__title__contains=subject).order_by(
            '-date', '-timeslot'
        ).first()
        commendation = random.choice(COMMENDATIONS)
        Commendation.objects.create(
            text=commendation, created=lessons_fetch.date, schoolkid=schoolkid,
            subject=lessons_fetch.subject, teacher=lessons_fetch.teacher)
    except MultipleObjectsReturned:
        print(f'Найдено несколько совпадений с  {name}, задайте поиск точнее')
    except ObjectDoesNotExist:
        print(f'Не найдено ни одного ученика с имени {name}')


def fix_marks(schoolkid):
    all_bad_marks = Mark.objects.filter(
        points__lte=3,
        schoolkid__full_name__contains=schoolkid
    )
    for subject in all_bad_marks:
        subject.points += 2
        subject.save()


def remove_chastisements(schoolkid):
    all_chastisement = Chastisement.objects.filter(
        schoolkid__full_name__contains=schoolkid
    )
    all_chastisement.delete()
