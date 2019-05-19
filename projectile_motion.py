# DUISC Advanced Physics Project
# Projectile Motion Simulator
# Yuhao Li 2019
import os
import traceback
import platform
from projectile_object import projectile_object
run_programme = True

try:
    import matplotlib.pyplot as plt
    from prettytable import PrettyTable
except ModuleNotFoundError:
    print(traceback.format_exc())
    input("Press any key to continue")
    run_programme = False

# Check platform
sys_platform = platform.system()

# console clear command
if sys_platform is "Windows":
    sys_clear = "CLS"
else:
    sys_clear = "clear"

# Initialise global prompts
title = "DUISC Advanced Physics Project"
author_copyright = "Yuhao Li 2019"
name = "Projectile Motion Simulator"

def print_head_menu():
    os.system(sys_clear)
    print(title)
    print(author_copyright)
    print(name+"\n")


def print_main_menu():
    # This function is to print the main menu in the console
    print_head_menu()
    print("+-------------------------------------------+")
    print("|{:^43s}|".format("Main menu"))
    print("+-------------------------------------------+")
    print("| {:<42s}|".format("1. Edit objects"))
    print("| {:<42s}|".format("2. Calculate"))
    print("| {:<42s}|".format("3. Plot data"))
    print("| {:<42s}|".format("4. Save to CSV"))
    print("| {:<42s}|".format("5. Open 3-D simulator"))
    print("| {:<42s}|".format("Quit -- q"))
    print("+-------------------------------------------+\n")

def print_object_menu(option_list_callback):
    print_head_menu()
    print("+-------------------------------------------------------------+")
    print("|{:^30s}|{:^30s}|".format("Objects","Calculation Status"))
    print("+-------------------------------------------------------------+")
    index = int(1)

    for ob in projectile_object.object_list:
        name = str(index) + ". " + ob.name
        calculate_status = str(ob.cal_res["is_calculated"])
        print("|{:^30s}|{:^30s}|".format(name, calculate_status))
        index += 1

    if len(projectile_object.object_list) == 0:
        print("|{:^30s}|{:^30s}|".format("",""))
    print("+-------------------------------------------------------------+\n")
    option_list_callback()

def print_plot_menu():
    # This function is to print ploting option menu in the console

    print_head_menu()
    print("+----------------------------------------------------------+")
    print("|{:^58s}|".format("Plot options"))
    print("+----------------------------------------------------------+")
    print("| {:<56s} |".format("1. Print acceleration x"))
    print("| {:<56s} |".format("2. Print acceleration y"))
    print("| {:<56s} |".format("3. Print velocity x"))
    print("| {:<56s} |".format("4. Print velocity y"))
    print("| {:<56s} |".format("5. Print displacement x"))
    print("| {:<56s} |".format("6. Print displacement y"))
    print("| {:<56s} |".format("7. Print resultant displacement"))
    print("| {:<56s} |".format("8. Print angle"))
    print("| {:<56s} |".format("9. Print four summative graphs"))
    print("| {:<56s} |".format("Quit -- q"))
    print("+----------------------------------------------------------+\n")

def case_1_options():
    print("1. Add objects")
    print("2. Edit parameters")
    print("3. Delete an object")
    print("4. Delete all objects")
    print("Quit -- q\n")

def case_2_options():
    print("1. View result table")
    print("2. View summary")
    print("Quit -- q\n")

def case_4():
    print("Quit -- q\n")

def object_has_result():
    for ob in projectile_object.object_list:
        if ob.cal_res["is_calculated"]:
            return True
    
    return False

def case_1():
    print_object_menu(case_1_options)
    user_option = ""

    while user_option is not "q":
        print_object_menu(case_1_options)
        user_option = input("Options: ")

        try:
            if user_option is "1":
                object_names = input("Object name: ").split(",")
                for name in object_names:
                    projectile_object(name, print_head_menu)

            elif user_option is "2":
                object_index = int(input("Object index: ")) - 1
                ob = projectile_object.object_list[object_index]
                ob.set_params()
            
            elif user_option is "3":
                object_index = int(input("Object index: ")) - 1
                ob = projectile_object.object_list[object_index]
                projectile_object.remove_from_list(ob)

            elif user_option is "4":
                projectile_object.remove_all()
        except:
            print(traceback.format_exc())
            input()

def case_2():
    print_object_menu(case_2_options)

    for ob in projectile_object.object_list:
        if not ob.cal_res["is_calculated"]:
            ob.calculate()
        print_object_menu(case_2_options)
    
    if object_has_result():
        user_option = ""

        while user_option is not "q":
            print_object_menu(case_2_options)
            user_option = input("Options: ")

            try:
                if user_option is "1":
                    object_index = int(input("Object index: ")) - 1
                    ob = projectile_object.object_list[object_index]
                    print_head_menu()
                    ob.print_res_table()
                elif user_option is "2":
                    object_index = int(input("Object index: ")) - 1
                    ob = projectile_object.object_list[object_index]
                    print_head_menu()
                    ob.print_summary()
            except:
                pass
    else:
        input("No available result to plot, press any key to continue")

def case_3():
    if object_has_result():
        print_plot_menu()
        user_option = ""

        while user_option is not "q":
            print_plot_menu()
            user_option = input("Options: ")
            projectile_object.plot_graphs(user_option)
    else:
        input("No available result to plot, press any key to continue")

def case_4():
    if object_has_result():
        for ob in projectile_object.object_list:
            ob.save_to_csv()
        input("Saving complete, press any key to continue")
    else:
        input("No available result to save, press any key to continue")

def case_5():
    if object_has_result():
        try:
            projectile_object.run_animation()
        except:
            pass
    else:
        input("No available result to save, press any key to continue")

def main():
    input_options = ""  # Input option variable

    # Main loop starts
    while input_options is not "q":
        try:
            print_main_menu()
            input_options = input("Options: ")

            if input_options is "1":
                case_1()

            elif input_options is "2":
                case_2()

            elif input_options is "3":
                case_3()

            elif input_options is "4":
                case_4()

            elif input_options is "5":
                case_5()

            elif input_options is "q":
                print("Exit the programme...")

        except ValueError:
            print(traceback.format_exc())
            input("Invalid input, press any key to continue")

        except Exception:
            print(traceback.format_exc())
            input("\n Press any key to continue")

if __name__ == "__main__" and run_programme:
    main()
