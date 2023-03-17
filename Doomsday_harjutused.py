
import random
import time
import PySimpleGUI as sg

def random_date_generator():
    
    year=random.randint(1700,2300)
    month=random.randint(1,12)
    long_months=[1,3,5,7,8,10,12]
    if month in long_months:
        day=random.randint(1,31)
    elif month == 2:
        if year%4==0:
            if year%400!=0 and year%100==0:
                day=random.randint(1,28)
            else:
                day=random.randint(1,29)
        else:
            day=random.randint(1,28)
    else:
        day=random.randint(1,30)
    
    return day, month, year
        

def day_calculation(day, month, year):
    month_dic = {'january':0,'february':3, 'march':3, 'april':6, 'may':1, 'june':4, 'july':6,'august':2,'september':5, 'october':0,'november':3, 'december':5}
    weekdays={0:'sunday', 1:'monday', 2:'tuesday', 3:'wednesday', 4:'thursday', 5:'friday', 6:'saturday'}
    month_values=month_dic[month]
    if year in range(1700,1799) or year in range(2100, 2199):
        year_value=4
    elif year in range(1800,1899) or year in range(2200, 2299):
        year_value=2
    elif year in range(1900,1999):
        year_value=0
    elif year in range(2000,2099):
        year_value=6
    last_values = int(str(year)[-2:])
    formula = day + month_values + year_value + last_values + (last_values//4)
    weekday = formula%7
    if month=='january' or month=='february':
        if year%4==0:
            weekday-=1
    return weekdays[weekday]



def game_start():
    sg.theme('LightGrey1')
    layout = [
        [sg.Text('Doomsday calculations game', font='Verdana 16')],
        [sg.Text('Start?', font = 'Verdana 12')],
        [sg.Button('Yes', size=(10, 1),font='Lucida'), sg.Button('No', size=(10, 1), font='Lucida'),
         sg.Button('Ok', visible=False, bind_return_key=True)]
    ]

    wdw = sg.Window('Doomsday', layout, element_justification='centre')
    
    while True:
        event, values = wdw.read()
        if event == 'Yes' or event == 'Ok':
            wdw.close()
            game_window()


        elif event is None or event == 'No':
            wdw.close()
            break

def game_window():
    
    start_time = time.time()
    rdm_date = random_date_generator()
    mths=['january','february','march', 'april', 'may', 'june', 'july','august','september', 'october','november', 'december']
    y=rdm_date[2]
    m=mths[rdm_date[1]-1]
    d=rdm_date[0]
    actual_day=day_calculation(d,m,y)
    
    sg.theme('LightGrey1')
    layout=[
    [sg.Text('What weekday is on ' + str(d)+ '. ' + m + ' '+ str(y)+ '?\n', font='Verdana 16')],
    [sg.Input(key='user_input', text_color='Blue', font='Verdana 14')],
    [sg.Text()],
    [sg.Button('OK', size=(10, 1), font='Lucida'), sg.Button('Cancel', size=(10, 1), font='Lucida'),
     sg.Button('Submit', visible=False, bind_return_key=True)]
    ]
    new_wdw = sg.Window('Doomsday', layout, element_justification='centre')
    
    while True:
        event, values = new_wdw.read()
        if event == 'OK' or event == 'Submit':
            user_input = values['user_input'].strip()
            end_time = time.time()
            guess_time = end_time - start_time
            if user_input==actual_day:
                new_wdw.close()
                result_wdw(guess_time)
            else:
                new_wdw.close()
                wrong_answer(actual_day)
        elif event is None or event == 'Cancel':
            new_wdw.close()
            break
        
def result_wdw(guess_time):
    
    sg.theme('LightGrey1')
    layout=[
    [sg.Text('Correct answer', font='Verdana 16')],
    [sg.Text('Your time was ' + str(round(guess_time,2)) + ' seconds\n', font='Verdana 16')],
    [sg.Button('Again', size=(10, 1),font='Lucida'), sg.Button('Close', size=(10, 1), font='Lucida'),
     sg.Button('Submit', visible=False, bind_return_key=True)]
    ]
    result_wdw = sg.Window('Doomsday', layout, element_justification='centre')
    
    while True:
        event, values = result_wdw.read()
        if event == 'Again' or event == 'Submit':
            result_wdw.close()
            game_window()
            
        elif event is None or event == 'Close':
            result_wdw.close()
            break   
        
def wrong_answer(actual_day):
    sg.theme('LightGrey1')
    layout=[
    [sg.Text('Wrong answer', font='Verdana 16')],
    [sg.Text('Correct answer would have been ' + actual_day, font='Verdana 16')],
    [sg.Button('Again', size=(10, 1), font='Lucida'), sg.Button('Close', size=(10, 1), font='Lucida'),
     sg.Button('Submit', visible=False, bind_return_key=True)]
    ]
    wrong_answer = sg.Window('Doomsday', layout, element_justification='left')
    
    while True:
        event, values = wrong_answer.read()
        if event == 'Again' or event == 'Submit':
            wrong_answer.close()
            game_window()
            
        elif event is None or event == 'Close':
            wrong_answer.close()
            break   

game_window()

    

    






