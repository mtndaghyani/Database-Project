import psycopg2
import psycopg2.extras

connection = psycopg2.connect(
    dbname="laboratory",
    password="1234",
    user="mohamadamin",
    host="localhost",
    port=5432,
)
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


def __convert_to_dict(selected_rows):
    rows = []
    for row in selected_rows:
        dict_row = {}
        for key in row:
            dict_row[key] = row[key]
        rows.append(dict_row)
    return rows


def __add_person(
    national_id,
    fname,
    lname,
    gender,
    bithday,
    is_married,
    phonenumber,
    street,
    alley,
    no,
):
    cursor.execute(
        "INSERT INTO Person VALUES(%(national_id)s, %(fname)s, %(lname)s, %(gender)s, %(birthday)s, %(is_married)s, %(phonenumber)s, %(street)s, %(alley)s, %(no)s);",
        {
            "national_id": national_id,
            "fname": fname,
            "lname": lname,
            "gender": gender,
            "birthday": bithday,
            "is_married": is_married,
            "phonenumber": phonenumber,
            "street": street,
            "alley": alley,
            "no": no,
        },
    )


def __add_employee(
    national_id,
    fname,
    lname,
    gender,
    bithday,
    is_married,
    phonenumber,
    street,
    alley,
    no,
    contract_start_date,
    contract_end_date,
    salary,
):
    __add_person(
        national_id,
        fname,
        lname,
        gender,
        bithday,
        is_married,
        phonenumber,
        street,
        alley,
        no,
    )

    cursor.execute(
        "INSERT INTO Employee VALUES(%(national_id)s, %(contract_start_date)s, %(contract_end_date)s , %(salary)s)",
        {
            "contract_start_date": contract_start_date,
            "contract_end_date": contract_end_date,
            "salary": salary,
        },
    )


def add_patient(
    national_id,
    fname,
    lname,
    gender,
    bithday,
    is_married,
    phonenumber,
    street,
    alley,
    no,
    insurance_name,
    insurance_exp_date,
    weight,
    height,
):
    __add_person(
        national_id,
        fname,
        lname,
        gender,
        bithday,
        is_married,
        phonenumber,
        street,
        alley,
        no,
    )

    cursor.execute(
        "INSERT INTO Patient VALUES(%(national_id)s, %(insurance_name)s, %(insurance_exp_date)s , %(weight)s, %(height)s)",
        {
            "national_id": national_id,
            "insurance_name": insurance_name,
            "insurance_exp_date": insurance_exp_date,
            "weight": weight,
            "height": height,
        },
    )

    connection.commit()


def add_employee(
    national_id,
    fname,
    lname,
    gender,
    bithday,
    is_married,
    phonenumber,
    street,
    alley,
    no,
    contract_start_date,
    contract_end_date,
    salary,
    table_name,
    gmc_number,
):
    __add_employee(
        national_id,
        fname,
        lname,
        gender,
        bithday,
        is_married,
        phonenumber,
        street,
        alley,
        no,
        contract_start_date,
        contract_end_date,
        salary,
    )

    cursor.execute(
        "INSERT INTO {%(table_name)s} VALUES(%(national_id)s" + ")"
        if table_name in ["Manager", "Secratary"]
        else ",%(gmc_number)s)",
        {"table_name": table_name, "gmc_number": gmc_number},
    )
    connection.commit()


def add_insurance_company(insurance_name, percentage, limit, start_date, end_date):
    cursor.execute(
        "INSERT INTO InsuranceCompany VALUES(%(insurance_name)s, %(percentage)s, %(limit)s, %(start_date)s, %(end_date)s)",
        {
            "insurance_name": insurance_name,
            "percentage": percentage,
            "limit": limit,
            "start_date": start_date,
            "end_date": end_date,
        },
    )
    connection.commit()


def add_education_degree(employee_id, title, university, start_date, end_date):
    cursor.execute(
        "INSERT INTO EducationDegree VALUES(%(employee_id)s, %(title)s, %(university)s, %(start_date)s, %(end_date)s)",
        {
            "employee_id": employee_id,
            "title": title,
            "university": university,
            "start_date": start_date,
            "end_date": end_date,
        },
    )

    connection.commit()


def add_disease_background(disease_name, patient_id, start_date, end_date):
    cursor.execute(
        "INSERT INTO DiseaseBackground VALUES(%(disease_name)s, %(patient_id)s, %(start_date)s, %(end_date)s)",
        {
            "disease_name": disease_name,
            "patient_id": patient_id,
            "start_date": start_date,
            "end_date": end_date,
        },
    )
    connection.commit()


def add_experiment(exp_name, exp_cost):
    cursor.execute(
        "INSERT INTO Experiment VALUES(%(exp_name)s, %(exp_const)s)",
        {"exp_name": exp_name, "exp_cost": exp_cost},
    )
    connection.commit()


def update_experiment(exp_name, exp_cost):
    cursor.execute(
        "UPDATE EXPERIMENT "
        + "SET ExperimentCost= %(exp_name)s"
        + "WHERE ExperimentName= %(exp_cost)s",
        {"exp_name": exp_name, "exp_cost": exp_cost},
    )
    connection.commit()


def delete_experiment(exp_name):
    cursor.execute(
        "DELETE FROM EXPERIMENT WHERE ExperimentName= %(exp_name)s",
        {"exp_name": exp_name},
    )
    connection.commit()


def add_prescription(patient_id, refer_doctor, date, experimnets):
    cursor.execute(
        'INSERT INTO Prescription(PatientId, ReferDoctor,"Date") VALUES(%(patient_id)s, %(refer_doctor)s, %(date)s)',
        {"patient_id": patient_id, "refer_doctor": refer_doctor, "date": date},
    )

    connection.commit()


# TODO implement RelatedTo

# Receipt will be created when a prescription added.


def add_sample(patient_id, exp_name, sampler_id):
    cursor.execute(
        'INSERT INTO "Sample"(PatientId, ExperimentName, SamplerId) VALUES(%(patient_id)s, %(exp_name)s, %(sampler_id)s)',
        {"patient_id": patient_id, "exp_name": exp_name, "sampler_id": sampler_id},
    )
    connection.commit()


def add_result(
    experimenter_id,
    receipt_id,
    prescription_id,
    sample_id,
    experiment_date,
    description,
    comment,
):
    cursor.execute(
        "INSERT INTO Result VALUES(%(experimenter_id)s, %(receipt_id)s, %(prescription_id)s, %(sample_id)s, %(experiment_date)s, %(description)s, %(comment)s)",
        {
            "experimenter_id": experimenter_id,
            "receipt_id": receipt_id,
            "prescription_id": prescription_id,
            "sample_id": sample_id,
            "experiment_date": experiment_date,
            "description": description,
            "comment": comment,
        },
    )
    connection.commit()


def add_work_day(employee_id, day, start, end, roomno, room_phonenumber):
    cursor.execute(
        "INSERT INTO WorkDay VALUES(%(employee_id)s, %(day)s, %(start)s, %(end)s, %(roomno)s, %(room_phonenumber)s)",
        {
            "employee_id": employee_id,
            "day": day,
            "start": start,
            "end": end,
            "roomno": roomno,
            "room_phonenumber": room_phonenumber,
        },
    )
    connection.commit()


def add_pay_check(employee_id, date, amount):
    cursor.execute(
        'INSERT INTO Paycheck(EmployeeId, "Date", Amount) VALUES(%(employee_id)s, %(date)s, %(amount)s)',
        {"employee_id": employee_id, "date": date, "amount": amount},
    )
    connection.commit()


# ---------------------------------------------------------------------------------------------------------------------------


def update_person_info(national_id, updates):
    s = ""
    for update in updates:
        if type(updates[update]) == str:
            s += f"{update}='{updates[update]}',"
        else:
            s += f"{update}={updates[update]},"

    cursor.execute(
        "UPDATE Person SET " + s[:-1] + "WHERE NationalId = %(national_id)s",
        {"national_id": national_id},
    )

    connection.commit()


def get_person_info(national_id):

    cursor.execute(
        "SELECT * FROM Person WHERE NationalId=%(national_id)s",
        {"national_id": national_id},
    )

    return __convert_to_dict(cursor.fetchall())


def get_patient_receipt(patient_id, start_date, end_date):

    cursor.execute(
        "SELECT * FROM Receipt WHERE PatientId=(%(patient_id)s) AND PreparationDate > (%(start_date)s) AND PreparationDate < (%(end_date)s)",
        {"patient_id": patient_id, "start_date": start_date, "end_date": end_date},
    )

    return __convert_to_dict(cursor.fetchall())


def get_experimenter_results(experimenter_id, start_date, end_date):
    cursor.execute(
        "SELECT * FROM Result WHERE ExperimenterId=(%(experimenter_id)s) AND ExperimentDate > (%(start_date)s) AND ExperimentDate < (%(end_date)s)",
        {
            "experimenter_id": experimenter_id,
            "start_date": start_date,
            "end_date": end_date,
        },
    )

    return __convert_to_dict(cursor.fetchall())


def get_experimenters_patients(experimenter_id, start_date, end_date):

    cursor.execute(
        "SELECT * FROM Patient INNER JOIN Person ON Patient.NationalId=Person.NationalId WHERE NationalId IN "
        + "(SELECT PatientId FROM Prescription WHERE PrescriptionId IN "
        + "(SELECT PrescriptionId FROM Result WHERE ExperimenterId=(%(experimenter_id)s) AND ExperimentDate > (%(start_date)s) AND ExperimentDate < (%(end_date)s)))",
        {
            "experimenter_id": experimenter_id,
            "start_date": start_date,
            "end_date": end_date,
        },
    )

    return __convert_to_dict(cursor.fetchall())


def get_patients_Results(patient_id, start_date, end_date, order_by_date):
    cursor.execute(
        "SELECT * FROM Result WHERE ExperimentDate > (%(start_date)s) AND ExperimentDate < (%(end_date)s) AND "
        + "Result.ReceiptId IN (SELECT Receipt.ReceiptId FROM Receipt WHERE PatientId=(%(patient_id)s))"
        + " ORDER BY ExperimentDate"
        if order_by_date
        else "",
        {"start_date": start_date, "end_date": end_date, "patient_id": patient_id},
    )
    return __convert_to_dict(cursor.fetchall())


def calculate_work_hours():
    cursor.execute(
        'SELECT EmployeeId, SUM(EXTRACT(HOUR FROM "End") - EXTRACT(HOUR FROM "Start")) AS workHoursInWeek FROM WorkDay GROUP BY EmployeeId'
    )
    return __convert_to_dict(cursor.fetchall())


# -----------------------------------


def delete_person(national_id):
    cursor.execute(
        "DELETE FROM Person WHERE national_id=%(national_id)s",
        {"national_id": national_id},
    )
    connection.commit()


def delete_sample(sample_id):
    cursor.execute(
        "DELETE FROM SAMPLE WHERE SampleId=%(sample_id)s", {"sample_id": sample_id}
    )
    connection.commit()
