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


def print_menu(options):
    print(colored(options, "yellow"))


def print_success_message(message):
    print(colored(message, "green"))


def print_error_message(message):
    print(colored(message, "red"))


def print_title(title):
    print(colored(title, "blue"))


def print_description(description):
    print(colored(description, "cyan"))


def input_with_description(description):
    return input(colored(description, "cyan"))


def get_option_input():
    return int(input(colored("Please Enter ONE OF The Options: ", "cyan")))


def show_wrong_option_number_message():
    print_error_message("Wrong Option Number!!!")


def get_role():
    return input_with_description(
        f"Role ({MANAGER}, {SAMPLER}, {DOCTOR}, {EXPERIMENTER}, {SECRETARY}): "
    )


def __get_start_and_end_date():
    start_date = input_with_description("Start Date: ")
    end_date = input_with_description("End Date: ")
    return [start_date, end_date]


def __get_fixed_update_fields(updates):
    fields = {}
    for k in updates:
        if updates[k] != None or updates[k] != "":
            fields[k] = updates[k]
    return fields


def __get_employee_info_from_input(role):
    con_start_date = input_with_description("Contract Start Date: ")
    con_end_date = input_with_description("Contract End Date: ")
    salary = int(input_with_description("Salary: "))
    gmc_number = (
        int(input_with_description("GMC Number: "))
        if role not in [MANAGER, SECRETARY]
        else None
    )
    return [con_start_date, con_end_date, salary, gmc_number]


def __get_experiment_info_from_input():
    exp_name = input_with_description("Experiment Name: ")
    exp_cost = int(input_with_description("Experiment Cost: "))
    return [exp_name, exp_cost]


def __get_person_info_from_input(ask_role):
    national_id = input_with_description("National Id: ")
    password = input_with_description("Password: ")
    role = get_role() if ask_role else None
    fname = input_with_description("First Name: ")
    lname = input_with_description("Last Name: ")
    gender = input_with_description("Gender (M, F): ")
    birthday = input_with_description("Birthday (2000-1-1): ")
    is_married = input_with_description("Married (Y, N): ") == "Y"
    phonenumber = input_with_description("Phone Number(09121111111): ")
    street = input_with_description("Street: ")
    alley = input_with_description("Alley: ")
    no = input_with_description("No.: ")

    return [
        national_id,
        password,
        role,
        fname,
        lname,
        gender,
        birthday,
        is_married,
        phonenumber,
        street,
        alley,
        no,
    ]


def __get_patient_info_from_input():
    insurance_name = input_with_description("Insurance Name: ")
    insurance_exp_date = input_with_description("Insurance Expiration Date: ")
    weight = float(input_with_description("Weigth: "))
    height = float(input_with_description("height: "))
    return [insurance_name, insurance_exp_date, weight, height]


def __get_insurance_info_from_input():
    insurance_name = input_with_description("Insurance Name: ")
    percentage = float(input_with_description("Percentage: "))
    limit = int(input_with_description("Limit: "))
    start_date = input_with_description("Contract Start Date: ")
    end_date = input_with_description("Contract End Date: ")
    return [insurance_name, percentage, limit, start_date, end_date]


while True:
    if user_state["is_authenticated"] is False:
        print_description("Please Login To Access Menu OR Exit")
        print_menu("1.Login\n0.Exit")
        option = get_option_input()
        if option == 0:
            break
        elif option == 1:
            national_id = input_with_description("Enter Your National Id: ")
            password = input_with_description("Enter Your Password: ")
            user_state = login(national_id, password)
            if user_state["is_authenticated"] == True:
                print_success_message("You Have Logged In Successfully.")
            else:
                print_error_message(
                    "User with This National Id and Password Does Not Exists!!!"
                )

        else:
            show_wrong_option_number_message()

    else:
        role = user_state["role"]
        user_id = user_state["national_id"]
        print_title(f"{role} Menu")

        if role == MANAGER:
            print_menu(
                "1.Employees\n2.Insurances\n3.Experiments\n4.Income And Paid Salary\n0.Logout",
            )
            option = get_option_input()
            if option == 0:
                user_state = logout()
                pass

            elif option == 1:
                while True:
                    print_menu(
                        "1.Add Employee\n2.Remove Employee\n3.Show Work Hours Of Employees\n0.Back"
                    )
                    opt = get_option_input()
                    if opt == 0:
                        break

                    elif opt == 1:
                        [
                            national_id,
                            password,
                            role,
                            fname,
                            lname,
                            gender,
                            birthday,
                            is_married,
                            phonenumber,
                            street,
                            alley,
                            no,
                        ] = __get_person_info_from_input(True)

                        [
                            con_start_date,
                            con_end_date,
                            salary,
                            gmc_number,
                        ] = __get_employee_info_from_input(role)

                        add_employee(
                            national_id,
                            password,
                            role,
                            fname,
                            lname,
                            gender,
                            birthday,
                            is_married,
                            phonenumber,
                            street,
                            alley,
                            no,
                            con_start_date,
                            con_end_date,
                            salary,
                            role,
                            gmc_number,
                        )
                        print_success_message("Employee Created Succesfully.")

                    elif opt == 2:
                        national_id = input_with_description("Employee's National Id: ")
                        delete_person(national_id)
                        print_success_message(
                            f"Employee With National Id {national_id} Deleted Succesfully."
                        )

                    elif opt == 3:
                        print(calculate_work_hours())

                    else:
                        show_wrong_option_number_message()
                pass

            elif option == 2:
                while True:
                    print_menu(
                        "1.Add Insurance\n2.Change Insurance's Information\n3.Delete Insurance\n0.Back"
                    )
                    opt = get_option_input()
                    if opt == 0:
                        break
                    elif opt == 1:
                        [
                            insurance_name,
                            percentage,
                            limit,
                            start_date,
                            end_date,
                        ] = __get_insurance_info_from_input()
                        add_insurance_company(
                            insurance_name, percentage, limit, start_date, end_date
                        )

                        print_success_message("Insurance Has Been Added Successfully.")

                    elif opt == 2:
                        name = input_with_description("ّInsurance Name: ")
                        print_description(
                            "Only Fill In Fields You Need To Change (Leave Others Blank)"
                        )

                        insurance_updates = __get_fixed_update_fields(
                            __get_insurance_info_from_input()
                        )
                        update_insurance_company(name, insurance_updates)
                        print_success_message(
                            "Insurance Has Benn Changed Successfully."
                        )
                    elif opt == 3:
                        name = input_with_description("ّInsurance Name: ")
                        delete_insurance_company(name)
                        print_success_message(
                            "Experiment Has Been Deleted Successfully."
                        )
                    else:
                        show_wrong_option_number_message()

            elif option == 3:
                while True:
                    print_menu(
                        "1.Add Experiment\n2.Change Experiment's Information\n3.Delete Experiment\n0.Back"
                    )
                    opt = get_option_input()
                    if opt == 0:
                        break
                    elif opt == 1:
                        [exp_name, exp_cost] = __get_experiment_info_from_input()
                        add_experiment(exp_name, exp_cost)
                        print_success_message("Experiment Has Been Added Successfully.")
                    elif opt == 2:
                        name = input_with_description("Experiment Name: ")
                        print_description(
                            "Only Fill In Fields You Need To Change (Leave Others Blank)"
                        )
                        exp_updates = __get_fixed_update_fields(
                            __get_experiment_info_from_input()
                        )
                        update_experiment(name, exp_updates)
                        print_success_message(
                            "Experiment Has Benn Changeg Successfully."
                        )
                    elif opt == 3:
                        exp_name = input_with_description("Experiment Name: ")
                        delete_experiment(exp_name)
                        print_success_message(
                            "Experiment Has Been Deleted Successfully."
                        )
                    else:
                        show_wrong_option_number_message()

            elif option == 4:
                while True:
                    print_menu("1.Income\n2.Paid Salary\n0.back")
                    opt = get_option_input()
                    if opt == 0:
                        break
                    elif opt == 1:
                        [start_date, end_date] = __get_start_and_end_date()
                        calculate_income(start_date, end_date)

                    elif opt == 2:
                        [start_date, end_date] = __get_start_and_end_date()
                        calculate_paid_salaries(start_date, end_date)
                    else:
                        show_wrong_option_number_message()

            else:
                show_wrong_option_number_message()

        elif role == SAMPLER:
            print_menu("1.Show Taken Samples\n2.Add Sample\n3.Delete Sample\n0.Logout")

            option = get_option_input()
            if option == 0:
                user_state = logout()

            elif option == 1:
                print(get_samplers_samples(user_id))

            elif option == 2:
                patient_id = input_with_description("Patient's National Id: ")
                exp_name = input_with_description("Experiment Name: ")
                add_sample(patient_id, exp_name, user_id)
                print_success_message("Sample Has Been Added Successfully.")

            elif option == 3:
                id = input_with_description("Sample Id: ")
                delete_sample(id)
                print_success_message("Sample Has Been Deleted Succussfully.")

            else:
                show_wrong_option_number_message()

        elif role == EXPERIMENTER:
            print_menu("1.List Of Results\n2.List Of Information Of Patients\n0.Logout")

            option = get_option_input()
            if option == 0:
                user_state = logout()
                pass
            elif option == 1:
                [start_date, end_date] = __get_start_and_end_date()

                print(get_experimenter_results(user_id, start_date, end_date))

            elif option == 2:
                [start_date, end_date] = __get_start_and_end_date()
                get_experimenters_patients(user_id, start_date, end_date)
            else:
                show_wrong_option_number_message()

        elif role == SECRETARY:
            print_menu(
                "1.Get Patient's Information\n2.Add New Patient\n3.Change Patient's Information\n4.Delete A Patient\n0.Logout"
            )
            option = get_option_input()

            if option == 0:
                user_state = logout()
                pass

            elif option == 1:
                id = input_with_description("Patient's National Id: ")
                print(get_patient_info(id)[0])
                pass

            elif option == 2:
                [
                    national_id,
                    password,
                    role,
                    fname,
                    lname,
                    gender,
                    birthday,
                    is_married,
                    phonenumber,
                    street,
                    alley,
                    no,
                ] = __get_person_info_from_input(False)

                [
                    insurance_name,
                    insurance_exp_date,
                    weight,
                    height,
                ] = __get_patient_info_from_input()

                add_patient(
                    national_id,
                    password,
                    PATIENT,
                    fname,
                    lname,
                    gender,
                    birthday,
                    is_married,
                    phonenumber,
                    street,
                    alley,
                    no,
                    insurance_name,
                    insurance_exp_date,
                    weight,
                    height,
                )
                print_success_message("Patient Has Been Added Succussfully.")
                pass

            elif option == 3:
                id = input_with_description("Patient's National Id: ")
                print_description(
                    "Only Fill In Fields You Need To Change (Leave Others Blank)"
                )
                persons_updates = __get_fixed_update_fields(
                    __get_person_info_from_input(False)
                )

                update_person_info(id, persons_updates)

                patient_updates = __get_fixed_update_fields(
                    __get_patient_info_from_input()
                )

                update_patient_info(id, patient_updates)

            elif option == 4:
                id = input_with_description("Patient's National Id")
                delete_person(id)
                print_success_message("Patient Has Been Deleted Succussfully.")

            else:
                show_wrong_option_number_message()

        elif role == PATIENT:
            print_menu(
                "1.Get Prescriptions\n2.Change Information\n3.Get Results\n0.Logout"
            )
            option = get_option_input()
            if option == 0:
                user_state = logout()
            elif option == 1:
                [start_date, end_date] = __get_start_and_end_date()
                print(get_patient_prescriptions(user_id, start_date, end_date))
            elif option == 2:
                update_person_info(user_id, {})
                print_success_message("Information Has Been Changed Successfully.")
            elif option == 3:
                [start_date, end_date] = __get_start_and_end_date()
                order_by = (
                    input_with_description("Order By Experiment Date?(Y, N)") == "Y"
                )
                print(get_patients_Results(user_id, start_date, end_date, order_by))
            else:
                show_wrong_option_number_message()
            pass
