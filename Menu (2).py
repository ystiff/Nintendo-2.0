import os
import csv
import pwinput
import time
from login import login


is_exit = False
main_menu_input = ''
                                                                                                              
def main():
    clear()
    print( '')
    print( '')
    print( '')
    print( '')
    print( '')
    print( '                                         ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗   ')  
    print( '                                         ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗  ')  
    print( '                                         ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║  ')  
    print( '                                         ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║  ') 
    print( '                                          ███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝  ') 
    print( '                                          ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝   ')

    print( '                           ███████╗ █████╗ ██╗   ██╗ ██████╗  ██████╗ ██╗   ██╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗███████╗    ')
    print( '                           ██╔════╝██╔══██╗██║   ██║██╔═══██╗██╔════╝ ██║   ██║██╔════╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝██╔════╝    ')
    print( '                           ███████╗███████║██║   ██║██║   ██║██║  ███╗██║   ██║█████╗      ██║  ███╗███████║██╔████╔██║█████╗  ███████╗    ')
    print( '                           ╚════██║██╔══██║╚██╗ ██╔╝██║   ██║██║   ██║██║   ██║██╔══╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ╚════██║    ')
    print( '                           ███████║██║  ██║ ╚████╔╝ ╚██████╔╝╚██████╔╝╚██████╔╝███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗███████║    ')
    print( '                           ╚══════╝╚═╝  ╚═╝  ╚═══╝   ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝    ')    
   
    print( '')
    print( '')
    print( '')
    print( '')
    print( '')
    #clear()
    print( '')
    print( '')
    print( '')
    print('                                                                           [1] Register')
    print('                                                                           [2] Login')
    print('                                                                           [3] Logout')
    print('                                                                           [4] Reset Password')
    print('                                                                           [0] Exit')
    print( '')
    print( '')
    global main_menu_input
    main_menu_input = input( 'Choice: ')
    is_exit = False

    while is_exit == False:
        if main_menu_input == '1':                                                                                              
            print( '                   ███████╗ █████╗ ██╗   ██╗ ██████╗  ██████╗ ██╗   ██╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗███████╗    ')
            print( '                   ██╔════╝██╔══██╗██║   ██║██╔═══██╗██╔════╝ ██║   ██║██╔════╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝██╔════╝    ')
            print( '                   ███████╗███████║██║   ██║██║   ██║██║  ███╗██║   ██║█████╗      ██║  ███╗███████║██╔████╔██║█████╗  ███████╗    ')
            print( '                   ╚════██║██╔══██║╚██╗ ██╔╝██║   ██║██║   ██║██║   ██║██╔══╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ╚════██║    ')
            print( '                   ███████║██║  ██║ ╚████╔╝ ╚██████╔╝╚██████╔╝╚██████╔╝███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗███████║    ')
            print( '                   ╚══════╝╚═╝  ╚═╝  ╚═══╝   ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝    ')
            print('')
            print( '                                         ____ ____ ____ _ ____ ___ ____ ____    ____ _ ____ ____ ___    ')
            print( '                                         |__/ |___ | __ | [__   |  |___ |__/    |___ | |__/ [__   |     ')
            print( '                                         |  \ |___ |__] | ___]  |  |___ |  \    |    | |  \ ___]  |     ')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            clear()
            register()
            main()
            return True
            
            
        if main_menu_input == '2':
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '                                                         ██       ██████   ██████      ██ ███    ██            ')
            print( '                                                         ██      ██    ██ ██           ██ ████   ██            ')
            print( '                                                         ██      ██    ██ ██   ███     ██ ██ ██  ██            ')
            print( '                                                         ██      ██    ██ ██    ██     ██ ██  ██ ██            ')
            print( '                                                         ███████  ██████   ██████      ██ ██   ████            ')
            print( '                                                                                                               ')
                                                                          
            print('')
            print( '                                                 ╦ ╦┌─┐┬┌┬┐  ┌─┐┌─┐┬─┐  ┌─┐┬ ┬┌┬┐┬ ┬┌─┐┌┐┌┌┬┐┬┌─┐┌─┐┌┬┐┬┌─┐┌┐┌   ')
            print( '                                                 ║║║├─┤│ │   ├┤ │ │├┬┘  ├─┤│ │ │ ├─┤├┤ │││ │ ││  ├─┤ │ ││ ││││   ')
            print( '                                                 ╚╩╝┴ ┴┴ ┴   └  └─┘┴└─  ┴ ┴└─┘ ┴ ┴ ┴└─┘┘└┘ ┴ ┴└─┘┴ ┴ ┴ ┴└─┘┘└┘   ')
            
            print('')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            #clear()
            login()
            main()
            return True
            
            
        if main_menu_input == '3':
            print('')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '                          ███████╗ █████╗ ██╗   ██╗ ██████╗  ██████╗ ██╗   ██╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗███████╗    ')
            print( '                          ██╔════╝██╔══██╗██║   ██║██╔═══██╗██╔════╝ ██║   ██║██╔════╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝██╔════╝    ')
            print( '                          ███████╗███████║██║   ██║██║   ██║██║  ███╗██║   ██║█████╗      ██║  ███╗███████║██╔████╔██║█████╗  ███████╗    ')
            print( '                          ╚════██║██╔══██║╚██╗ ██╔╝██║   ██║██║   ██║██║   ██║██╔══╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ╚════██║    ')
            print( '                          ███████║██║  ██║ ╚████╔╝ ╚██████╔╝╚██████╔╝╚██████╔╝███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗███████║    ')
            print( '                          ╚══════╝╚═╝  ╚═╝  ╚═══╝   ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝    ')
            print('')                           
            print( '                                                                   __   __      __       ___       ')
            print( '                                                             |    /  \ / _`    /  \ |  |  |        ')
            print('                                                              |___ \__/ \__>    \__/ \__/  |        ')
                                                     

            #clear
            logout()
            return True
            
        if main_menu_input == '4':
            print('')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print('')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '                          ███████╗ █████╗ ██╗   ██╗ ██████╗  ██████╗ ██╗   ██╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗███████╗    ')
            print( '                          ██╔════╝██╔══██╗██║   ██║██╔═══██╗██╔════╝ ██║   ██║██╔════╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝██╔════╝    ')
            print( '                          ███████╗███████║██║   ██║██║   ██║██║  ███╗██║   ██║█████╗      ██║  ███╗███████║██╔████╔██║█████╗  ███████╗    ')
            print( '                          ╚════██║██╔══██║╚██╗ ██╔╝██║   ██║██║   ██║██║   ██║██╔══╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ╚════██║    ')
            print( '                          ███████║██║  ██║ ╚████╔╝ ╚██████╔╝╚██████╔╝╚██████╔╝███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗███████║    ')
            print( '                          ╚══════╝╚═╝  ╚═╝  ╚═══╝   ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝    ')
            print("                                          ___   ____  __   ____ _____      ___    __    __   __   _       ___   ___   ___  ")
            print("                                          | |_) | |_  ( (` | |_   | |      | |_)  / /\  ( (` ( (` \ \    // / \ | |_) | | \ ")
            print("                                          |_| \ |_|__ _)_) |_|__  |_|      |_|   /_/--\ _)_) _)_)  \_\/\/ \_\_/ |_| \ |_|_/ ")
            print('')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            reset_password()
            main()
            return True
        
        if  main_menu_input == '0':
            is_exit = True
            return True
            
            
def register():
    print('Registration Form')
    username = input('Enter your username: ')
    password = pwinput.pwinput(prompt='Enter your password: ', mask='*')
    with open('database.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([username, password])
    return True

def logout():
    return True

def reset_password():
    print('Reset Password Form')
    print('Login First')
    username = input('Username: ')
    password = pwinput.pwinput(prompt='Password: ', mask='*')
    with open('database.csv') as csv_file:
        reader = csv.reader(csv_file)
        is_success = False
        counter = 0
        index = None
        new_list = []
        for row in reader:
            new_list.append(row)
            if len(row) > 1:
                if row[0] == username and row[1] == password:
                    is_success = True
                    index = counter
            counter += 1
        
        if is_success:
            new_password = input('Input New Password: ')
            for i in range(len(new_list)):
                if i == index:
                    new_list[i][1] = new_password
                    main()
            with open('database.csv', 'w+') as csv_file:
                writer = csv.writer(csv_file)
                for i in range(len(new_list)):
                    writer.writerow(new_list[i])
            time.sleep(20)
        else:
            print('Login Failed')
        global is_exit
        global main_menu_input
        is_exit = True
        main_menu_input = ''
        # time.sleep(10)

def clear():
    os.system('clear||cls')

main()