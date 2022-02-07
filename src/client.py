from project import *
from termcolor import colored

user_state = {"is_authenticated": False, "national_id": None, "role": None}

MENUS = {
    MANAGER: "",
    SAMPLER: "",
    EXPERIMENTER: "",
    DOCTOR: "",
    SECRETARY: "",
    PATIENT: "",
}

while True:
    if user_state["is_authenticated"] is False:
        print("Please Login To Access Menu OR Exit")
        print(colored("1.Login\n0.Exit", "yellow"))
        option = input("Please Enter ONE OF The Options: ")
        if option == "0":
            break
        elif option == "1":
            national_id = input("Enter Your National Id: ")
            password = input("Enter Your Password: ")
            user_state = login(national_id, password)
            if user_state["is_authenticated"] == True:
                print(colored("You Have Logged In Successfully.", "green"))
            else:
                print(
                    colored(
                        "User with This National Id and Password Does Not Exists!!!",
                        "red",
                    )
                )

        else:
            print(colored("Wrong Input!!!","red"))
    else:
        print(user_state["role"])
        pass
