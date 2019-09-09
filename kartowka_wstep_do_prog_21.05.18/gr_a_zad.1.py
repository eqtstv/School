def keyboard_input(list, dictionary):
    '''Append input to list until an empty input'''
    while True:
        x = input('Podaj wojewodztwo: ')
        if (x != ""):
            if (x in dictionary):
                if (x in list):
                    print('To wojewodztwo jest juz na liscie')
                else:
                    list.append(x)
            else:
                print('Nieprawidlowa nazwa wojewodztwa')
        else:
            break

def show_values(list, dictionary, count):
    '''Return dictionary value of 'count' element in list'''
    name = list[count]
    return dictionary[name]


#list of wojewodztwa
wojewodztwa = [
'wielkopolskie',
'kujawskopomorskie',
'malopolskie',
'lodzkie'
]

#dictionary of areas
rozmiar_wojewodztwa = {
'dolnoslaskie': 19947,
'kujawskopomorskie': 17972,
'lubelskie':25122,
'lubuskie': 13988,
'lodzkie': 18219,
'malopolskie': 15183,
'mazowieckie': 35558,
'opolskie': 9412,
'podkarpackie': 17846,
'podlaskie': 20187,
'pomorskie': 18310,
'slaskie': 12333,
'świetokrzyskie': 11711,
'warminsko-mazurskie': 24173,
'wielkopolskie': 29826,
'zachodniopomorskie': 2892,
}

#append values to wojewodztwa from keyboard until empty input
keyboard_input(wojewodztwa, rozmiar_wojewodztwa)

#print areas of wojewodztwa
count = 0
for count in range (0, len(wojewodztwa)):
    area = show_values(wojewodztwa, rozmiar_wojewodztwa, count)
    print(str(wojewodztwa[count]) + ': to wojewodztwo ma rozmiar: ' + str(area) + ' km^2')


#sum the total area of values in wojewodztwa
i = 0
total_area = 0
for i in range(0, len(wojewodztwa)):
    append_area = show_values(wojewodztwa, rozmiar_wojewodztwa, i)
    total_area = total_area + append_area

print('\n Suma rozmiarow wojewodztw z listy wojewodztwa wynosi: ' + str(total_area) + '\n')


#append to duze_wojewodztwa only if area > 10000
duze_wojewodztwa = []
j = 0
for j in range(0, len(wojewodztwa)):
    append_area = show_values(wojewodztwa, rozmiar_wojewodztwa, j)
    if (append_area > 10000):
        duze_wojewodztwa.append(wojewodztwa[j])

print('Duze wojewodztwa: (rozmiar powyzej 10000)')
print(duze_wojewodztwa)