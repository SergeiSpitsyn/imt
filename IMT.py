# -*- coding: UTF-8 -*-
height = int(input('Введите свой рост в см: '))
weight = int(input('Введите массу тела в кг: '))

def calc_imt(h, m):
    IMT = m / ((h / 100) ** 2)
    return IMT

def verdict_imt(IMT = calc_imt(height, weight)):
    print('Индекc массы тела:', IMT)
    if IMT <= 16:
        result = 'У Вас сильный дефицит массы тела'
    elif (IMT > 16 and IMT <= 18.5):
        result = 'У Вас дефицит массы тела'

    elif (IMT > 18.5 and IMT <= 25):
        result = 'Ваша масса тела в норме'

    elif (IMT > 25 and IMT <= 30):
        result = 'У Вас предожирение'

    elif (IMT > 30 and IMT <=35):
        result = 'У Вас ожирение'

    elif (IMT > 35 and IMT <= 40):
        result = 'У Вас резкое ожирение'

    else:
        result = 'У Вас очень резкое ожирение'

    print(result)
    return IMT, result

IMT, result = verdict_imt()
