# Guido van Rossum <guido@python.org>

def step1():
    print(
        'Утка-маляр 🦆 решила пойти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

def step2_umbrella(): 
     print(
        'Ура! Теперь ее аутфит не будет испорчен непогодой!\n'
        'Утка-маляр уже собралась, но не знает, куда пойти.\n'
        'Что ей сделать?'
        )
     option = ''
     options = {'Прочекать афишу': 1, 'Позвонить утке-монтажнику': 2}
     while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
     if options[option] == 1:
         return step3_event()
     else:
       return step4_party_1()

def step4_party_1():
    print('-Привет! Тусишь где-то сегодня? - спросила утка.\n'
          '-Да, залетай к нам в Ровесник, пока не начался дождь - ответила утка-монтажник.\n'
          )
    return step4_rovesnik()

def step4_rovesnik(): 
    print('В Ровеснике утка-маляр классно отдохнула - новое барное меню не разочаровало.\n'
          'В тот вечер там также выступал Диджей-Кряк - биты были что надо!\n'
          'Чудесный был вечер!\n'
          )
    print('Поменять планы утки-маляра?')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
        
    if options[option]:
        return step1()
    else:
        print('Приключения утки закончились!')

def step2_no_umbrella(): 
    print(
        'Ну и правда, зачем зонт? Прогноз на вечер был отличный.\n'
        'Куда же можно пойти выпить?'
        )
    option = ''
    options = {'Зинзивер': 1, 'Ровесник': 2}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option] == 1:
      return step4_over_zinziver()
    else:
      return step4_rovesnik()

def step3_event(): 
    print(
        'Утка открыла заметки Московкой щуки.\n'
        'Там как раз был список классных баров.\n'
        'Утка решила пойти в:'
        )
    option = ''
    options = {'Бар Маляр': 1, 'Зинзивер': 2, 'Столовая №2':3}
    while option not in options:
        print('Выберите: {}/{}/{}'.format(*options))
        option = input()
    
    if options[option] == 1:
      return step4_over_bar()
    elif options[option] == 2:
      return step4_over_zinziver()
    else:
      return step4_over_stolovaya()

def step4_over_bar(): 
    print('Хо-хо-хо! Афиша не подвела - в баре проходил фестиваль бельгийского пива!\n'
          'Утка классно провела время и поехала домой.\n'
          'Жаль, что зонт так и не понадобился.\n'
          )
    print('Поменять планы утки-маляра?')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step1()
    else:
        print('Приключения утки закончились!')

def step4_over_zinziver(): 
    print('Вот беда! На улице начался ливень,а в Зинзивере как обычно не было мест.\n'
          'Утке пришлось поехать домой.\n'
          )
    print('Поменять планы утки-маляра?')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step1()
    else:
        print('Приключения утки закончились!')

def step4_over_stolovaya(): 
    print('Несмотря на много сомнений, в Столовой №2 было не так плохо.\n'
          'Утка заценила новую краску на стенах и все настойки в барном меню.\n'
          'Вечер прошел идеально!\n'
          )
    print('Поменять планы утки-маляра?')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step1()
    else:
        print('Приключения утки закончились!')

if __name__ == '__main__':
    step1()

