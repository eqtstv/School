#1.
def difference(a, b):
    """return list of elements that exists only in list A but not in B"""
    c = [i for i in a + b if i not in a or i not in b]
    return c

def greeting(list_of_guests):
    """Print greetings for the guests"""
    for i in list_of_guests:     
        print('Witaj ' + i)
        
#create lists
goscie = ["Wojtek", "Marcin", 'Damian', 'Maciek', 'Krzysztof', 'Michau', 'Janusz', 'Dariusz', 'Szymon',
'Jan', 'Patrycja', 'Marta', 'Magda', 'Katy', 'Celia', 'Kristle', 'Rusty', 'Pandora', 'Moon', 'Jaclyn',
'Ruthanne', 'Laine', 'Bobbi', 'Rod', 'Pam', 'Mazie', 'Delana', 'Nova', 'Krystyna', 'Becki', 'Cedrick']

nie_przyjdzie = ["Marcin", 'Damian', 'Wojtek', 'Bartosz']

#update goscie list
goscie = difference(goscie, nie_przyjdzie)

#greet guests
greeting(goscie)

print('\n \n')
#--------------------------------------
#2.
def make_two_dim_list(number_of_lists, number_of_points_in_list):
    """Make x * y two dim list with '' values in it """
    z = [[''] * number_of_points_in_list for i in range(number_of_lists)]
    return z

def merge_lists_apologies(list_of_values, list_to_fill):
    '''Fill two dim list with another list + apologies'''
    counter = 0
    for x in range(len(list_to_fill)):
        for y in range (len(list_to_fill[x])):
            if (counter == len(list_of_values)):
                break
            if (list_to_fill[x][y] == ''):
                list_to_fill[x][y] = list_of_values[counter]
                counter += 1
    #apologize if some didnt fit
    if (len(list_of_values) > counter):
        didnt_fit = len(list_of_values) - counter
        apology = 'Przykro mi, dla ' + str(didnt_fit) + ' gosci zabraklo miejsca \n'
        print(apology)

#declaration of tables
number_of_tables = 5
number_of_seats_at_table = 3

#prepare structure
stoly = make_two_dim_list(number_of_tables, number_of_seats_at_table)

#fill tables, apologize if some didnt fit
merge_lists_apologies(goscie, stoly)

#print tables
print(stoly)