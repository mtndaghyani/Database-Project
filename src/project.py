import psycopg2
import psycopg2.extras
from psycopg2.extensions import AsIs

MANAGER = "Manager"
SAMPLER = "Sampler"
EXPERIMENTER = "Experimenter"
DOCTOR = "Doctor"
SECRETARY = "Secretary"
PATIENT = "Patient"

connection = psycopg2.connect(
    dbname="laboratory",
    user="mohamadamin",
    password="1234",
    host="localhost",
    port=5432,
)
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


def login(national_id, password):

    cursor.execute(
        'SELECT NationalId, "Role" FROM Person WHERE NationalId=%(national_id)s AND "Password"=crypt(%(password)s, "Password")',
        {"national_id": national_id, "password": password},
    ),

    user = cursor.fetchone()
    if user:
        return {
            "is_authenticated": True,
            "national_id": user["nationalid"],
            "role": user["Role"],
        }

    else:
        return {"is_authenticated": False, "national_id": None, "role": None}


def logout():
    return {"is_authenticated": False, "national_id": None, "role": None}


# ok
def __convert_to_dict(selected_rows):
    rows = []
    for row in selected_rows:
        dict_row = {}
        for key in row:
            dict_row[key] = row[key]
        rows.append(dict_row)
    return rows


# ok
def __add_person(
    national_id,
    password,
    role,
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
        "INSERT INTO Person VALUES(%(national_id)s, crypt(%(password)s, gen_salt('bf')),(%(role)s), %(fname)s, %(lname)s, %(gender)s, %(birthday)s, %(is_married)s, %(phonenumber)s, %(street)s, %(alley)s, %(no)s);",
        {
            "national_id": national_id,
            "password": password,
            "role": role,
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


# ok
def __add_employee(
    national_id,
    password,
    role,
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
        password,
        role,
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
            "national_id": national_id,
            "contract_start_date": contract_start_date,
            "contract_end_date": contract_end_date,
            "salary": salary,
        },
    )


# ok
def add_patient(
    national_id,
    password,
    role,
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
        password,
        role,
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


def get_employees():
    cursor.execute(
        "SELECT * FROM Employee INNER JOIN Person ON Employee.NationalId=Person.NationalId"
    )

    return __convert_to_dict(cursor.fetchall())


def get_insurances():
    cursor.execute("SELECT * FROM InsuranceCompany")
    return __convert_to_dict(cursor.fetchall())


# ok
def add_employee(
    national_id,
    password,
    role,
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
        password,
        role,
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
        "INSERT INTO %(table_name)s VALUES(%(national_id)s"
        + (")" if table_name in [MANAGER, SECRETARY] else ",%(gmc_number)s)"),
        {
            "table_name": AsIs(table_name),
            "national_id": national_id,
            "gmc_number": gmc_number,
        },
    )
    connection.commit()


# ok
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


# ok
def delete_insurance_company(insurance_name):
    cursor.execute(
        "DELETE FROM InsuranceCompany WHERE InsuranceName=%(insurance_name)s",
        {"insurance_name": insurance_name},
    )
    connection.commit()


# ok
def update_insurance_company(insurance_name, updates):
    query = __convert_updates_to_query(updates)
    cursor.execute(
        "UPDATE InsuranceCompany SET "
        + query
        + "WHERE InsuranceName = %(insurance_name)s",
        {"insurance_name": insurance_name},
    )
    connection.commit()


def get_samplers_samples(sampler_id):
    cursor.execute(
        'SELECT * FROM "Sample" WHERE SamplerId=%(sampler_id)s',
        {"sampler_id": sampler_id},
    )

    return __convert_to_dict(cursor.fetchall())


# ok
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


# ok
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


# ok
def add_experiment(exp_name, exp_cost):
    cursor.execute(
        "INSERT INTO Experiment VALUES(%(exp_name)s, %(exp_cost)s)",
        {"exp_name": exp_name, "exp_cost": exp_cost},
    )
    connection.commit()


# ok
def update_experiment(exp_name, updates):
    query = __convert_updates_to_query(updates)
    cursor.execute(
        "UPDATE EXPERIMENT SET " + query + " WHERE ExperimentName= %(exp_name)s",
        {"exp_name": exp_name},
    )
    connection.commit()


# ok
def delete_experiment(exp_name):
    cursor.execute(
        "DELETE FROM EXPERIMENT WHERE ExperimentName=%(exp_name)s",
        {"exp_name": exp_name},
    )
    connection.commit()


# ok
def add_prescription(patient_id, refer_doctor, date, prepration_date, experiments):
    cursor.execute(
        'INSERT INTO Prescription(PatientId, ReferDoctor,"Date", PreparationDate) VALUES(%(patient_id)s, %(refer_doctor)s, %(date)s, %(prepration_date)s) RETURNING PrescriptionId',
        {
            "patient_id": patient_id,
            "refer_doctor": refer_doctor,
            "date": date,
            "prepration_date": prepration_date,
        },
    )
    prescription_id = cursor.fetchone()["prescriptionid"]

    values = [(prescription_id, exp) for exp in experiments]
    args = ",".join(cursor.mogrify("(%s,%s)", i).decode("utf-8") for i in values)
    cursor.execute("INSERT INTO RelatedTo VALUES " + (args))
    connection.commit()


# ok
def add_sample(patient_id, exp_name, sampler_id):
    cursor.execute(
        'INSERT INTO "Sample"(PatientId, ExperimentName, SamplerId) VALUES(%(patient_id)s, %(exp_name)s, %(sampler_id)s)',
        {"patient_id": patient_id, "exp_name": exp_name, "sampler_id": sampler_id},
    )
    connection.commit()


# ok
def add_result(
    experimenter_id,
    prescription_id,
    sample_id,
    experiment_date,
    description,
    comment,
):
    cursor.execute(
        "INSERT INTO Result VALUES(%(experimenter_id)s, %(prescription_id)s, %(sample_id)s, %(experiment_date)s, %(description)s, %(comment)s)",
        {
            "experimenter_id": experimenter_id,
            "prescription_id": prescription_id,
            "sample_id": sample_id,
            "experiment_date": experiment_date,
            "description": description,
            "comment": comment,
        },
    )
    connection.commit()


# ok
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


# ok
def add_pay_check(employee_id, date, amount):
    cursor.execute(
        'INSERT INTO Paycheck(EmployeeId, "Date", Amount) VALUES(%(employee_id)s, %(date)s, %(amount)s)',
        {"employee_id": employee_id, "date": date, "amount": amount},
    )
    connection.commit()


# queries ---------------------------------------------------------------------------------------------------------------------------

# ok
def get_patient_prescriptions(patient_id, start_date, end_date):
    cursor.execute(
        'SELECT ReferDoctor, "Date", Expenses, TotalCost, PreparationDate FROM Prescription WHERE PatientId=(%(patient_id)s) AND PreparationDate > (%(start_date)s) AND PreparationDate < (%(end_date)s)',
        {"patient_id": patient_id, "start_date": start_date, "end_date": end_date},
    )

    return __convert_to_dict(cursor.fetchall())


def __convert_updates_to_query(updates):
    query = ""
    case_sensitive_cols = [
        "Password",
        "Role",
        "No",
        "Weight",
        "Percentage",
        "Limit",
        "Date",
        "Description",
        "Comment",
        "Day",
        "Start",
        "End",
    ]
    for update in updates:
        if type(updates[update]) == str:
            if update in case_sensitive_cols:
                if update == "Password":
                    query += (
                        f"\"{update}\"=crypt('{updates[update]}',  gen_salt('bf')),"
                    )
                else:
                    query += f"\"{update}\"='{updates[update]}',"
            else:
                query += f"{update}='{updates[update]}',"
        else:
            if update in case_sensitive_cols:
                query += f'"{update}"={updates[update]} ,'
            else:
                query += f"{update}={updates[update]} ,"
    return query[:-1]


# ok
def update_person_info(national_id, updates):
    query = __convert_updates_to_query(updates)

    cursor.execute(
        "UPDATE Person SET " + query + " WHERE NationalId = %(national_id)s",
        {"national_id": national_id},
    )

    connection.commit()


def update_patient_info(national_id, updates):
    query = __convert_updates_to_query(updates)

    cursor.execute(
        "UPDATE Patient SET " + query + "WHERE NationalId = %(national_id)s",
        {"national_id": national_id},
    )

    connection.commit()


def get_experiments():
    cursor.execute("SELECT * FROM Experiment")
    return __convert_to_dict(cursor.fetchall())


def get_person_info(national_id):
    cursor.execute(
        "SELECT * FROM Person WHERE NationalId=%(national_id)s",
        {"national_id": national_id},
    )

    return __convert_to_dict(cursor.fetchall())


# ok
def get_experimenter_results(experimenter_id, start_date, end_date):
    cursor.execute(
        "SELECT * FROM Result WHERE ExperimenterId=(%(experimenter_id)s) AND ExperimentDate >= (%(start_date)s) AND ExperimentDate < (%(end_date)s)",
        {
            "experimenter_id": experimenter_id,
            "start_date": start_date,
            "end_date": end_date,
        },
    )

    return __convert_to_dict(cursor.fetchall())


def get_patients():
    cursor.execute(
        "SELECT * FROM Patient INNER JOIN Person ON Patient.NationalId=Person.NationalId",
    )
    return __convert_to_dict(cursor.fetchall())


# ok
def get_experimenters_patients(experimenter_id, start_date, end_date):
    cursor.execute(
        "SELECT * FROM Patient INNER JOIN Person ON Patient.NationalId=Person.NationalId WHERE Patient.NationalId IN "
        + "(SELECT PatientId FROM Prescription WHERE PrescriptionId IN "
        + "(SELECT PrescriptionId FROM Result WHERE ExperimenterId=(%(experimenter_id)s) AND ExperimentDate >= (%(start_date)s) AND ExperimentDate < (%(end_date)s)))",
        {
            "experimenter_id": experimenter_id,
            "start_date": start_date,
            "end_date": end_date,
        },
    )

    return __convert_to_dict(cursor.fetchall())


# ok
def calculate_income(start_date, end_date):
    cursor.execute(
        "SELECT SUM(Expenses) AS Expenses, SUM(TotalCost) AS TotalCosts FROM Prescription WHERE PreparationDate >= (%(start_date)s) AND PreparationDate < (%(end_date)s)",
        {
            "start_date": start_date,
            "end_date": end_date,
        },
    )

    return __convert_to_dict(cursor.fetchall())


# ok
def calculate_paid_salaries(start_date, end_date):
    cursor.execute(
        'SELECT SUM(Amount) AS Amount FROM Paycheck WHERE "Date" >= (%(start_date)s) AND "Date"< (%(end_date)s)',
        {
            "start_date": start_date,
            "end_date": end_date,
        },
    )

    return __convert_to_dict(cursor.fetchall())


def get_patients_Results(patient_id, start_date, end_date, order_by_date):
    cursor.execute(
        "SELECT * FROM Result WHERE ExperimentDate >= (%(start_date)s) AND ExperimentDate < (%(end_date)s) AND "
        + "Result.PrescriptionId IN (SELECT Prescription.PrescriptionId FROM Prescription WHERE PatientId=(%(patient_id)s))"
        + (" ORDER BY ExperimentDate" if order_by_date else ""),
        {"start_date": start_date, "end_date": end_date, "patient_id": patient_id},
    )
    return __convert_to_dict(cursor.fetchall())


# ok
def calculate_work_hours():
    cursor.execute(
        'SELECT EmployeeId, SUM(EXTRACT(HOUR FROM "End") - EXTRACT(HOUR FROM "Start")) AS workHoursInWeek FROM WorkDay GROUP BY EmployeeId'
    )
    return __convert_to_dict(cursor.fetchall())


def get_patient_info(national_id):
    cursor.execute(
        "SELECT * FROM Patient INNER JOIN Person ON Patient.NationalId=Person.NationalId WHERE Patient.NationalId=%(national_id)s",
        {"national_id": national_id},
    )
    return __convert_to_dict(cursor.fetchall())


# -----------------------------------

# ok
def delete_person(national_id):
    cursor.execute(
        "DELETE FROM Person WHERE NationalId=%(national_id)s",
        {"national_id": national_id},
    )
    connection.commit()


def delete_sample(sample_id, sampler_id):
    cursor.execute(
        'DELETE FROM "Sample" WHERE SampleId=%(sample_id)s AND SamplerId=%(sampler_id)s',
        {"sample_id": sample_id, "sampler_id": sampler_id},
    )
    connection.commit()


# Manager Is needed To start The Project
if __name__ == "__main__":
    add_employee(
        "1111111111",
        "pass1",
        MANAGER,
        "fmanager",
        "lmanager",
        "M",
        "2001-2-21",
        False,
        "09121111111",
        "s1",
        "a1",
        1,
        "2020-1-1",
        "2021-1-1",
        10000000,
        MANAGER,
        None,
    )
