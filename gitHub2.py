karta='АБВ БГДЕ ВБЖ ГЗ ДИО ЕПР ЖРС ЗТИ ИУ ОИП  ПШХЦ РЦЧ СРЧ ТУ УЪФ ФЪ ШЪ ХШ ЦЫ ЧЫЭ ЪЭ ЫЭ ' #пишем вершины+куда мы можем попасть из них
#print(len(karta.split())) #можем проверить,что все вершины учтены (их должно быть  на 1 меньше (без последней))
slovar={vershina[0]:vershina[1:] for vershina in karta.split()} #создаем словарь ( ключ(вершина):значение(вершины,в которые из нее попадем) )

def f(marshrut,end_marshruta): #создаем рекурсию 
    if marshrut[-1]==end_marshruta: #если последний пункт пути равен концу маршрута,то return...
        return (('Е' not in marshrut) and ('Х' not in marshrut))   #если маршрут не включает лишние вершины (поганки),добавляем его  
    return sum( f(marshrut+ sled_punkt,end_marshruta) for sled_punkt in slovar[marshrut[-1]])
    #перебираем все возможные маршруты и суммируем их



print(f('А','Э')) #запуск рекурсии ( ФУНКЦИЯ("начало маршрута","конец маршрута") )
                  #на "начало маршрута" наслаиваются вершины



