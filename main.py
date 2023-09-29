name = input('Введите Ваше имя: ')
age = int(input('Введите возраст: '))
place = input('Введите место проживания: ')
country = input('Введите страну проживания: ')
birth_year = 2023 - age

print(
    f'Уважаемый {name}!\n\nНа сегодняшний день Вы проживаете в стране {country},'
    f'\nв городе {place}, '
    f'\nи вы родились в {birth_year} году. '
)
