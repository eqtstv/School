def fill_two_dim_list(list_to_fill, number_of_lists, number_of_points_in_list):
    '''Fill empty space of list with '' to make x * y two dim list'''
    for x in range(len(list_to_fill), number_of_lists):
        list_to_fill.append([])
        for y in range(len(list_to_fill)):
            for z in range((len(list_to_fill[y])), number_of_points_in_list):
                list_to_fill[y].append('')

            

def merge_lists(list_of_values, list_to_fill):
    '''Fill two dim list with another list'''
    counter = 0
    for x in range(len(list_to_fill)):
        for y in range (len(list_to_fill[x])):
            if (counter == len(list_of_values)):
                break
            if (list_to_fill[x][y] == ''):
                list_to_fill[x][y] = list_of_values[counter]
                counter += 1

#list of patients enroled to doctors
lekarze = [
['Nowak', 'Kowalski'],
[],
['Grabowski', 'Piotrowski']
] 

#list of waiting patients
pacjenci = [
'Wisniewski',
'Wojcik',
'Kowalczyk',
'Kaminski',
'Lewandowski'
'Nowak',
'Kowalski'
'Wisniewski',
'Wojcik',
'Kowalczyk',
'Kaminski',
'Lewandowski',
'Zielinski',
'Szymanski',
'Wozniak',
'Dabrowski',
'Kozlowski',
'Jankowski',
'Mazur',
'Kwiatkowski',
'Wojciechowski',
'Krawczyk',
'Kaczmarek',
'Piotrowski',
'Piecyk'
]

#clinic
number_of_doctors = 5
number_of_patients_for_one_doctor = 10

#make room for patients
fill_two_dim_list(lekarze, number_of_doctors, number_of_patients_for_one_doctor)
print(lekarze)

#assign patients to doctors
merge_lists(pacjenci, lekarze)
print(lekarze)