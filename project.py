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


def calculate_work_hours():
    cursor.execute(
        'SELECT EmployeeId, SUM(EXTRACT(HOUR FROM "End") - EXTRACT(HOUR FROM "Start")) AS workHoursInWeek FROM WorkDay GROUP BY EmployeeId'
    )
    return __convert_to_dict(cursor.fetchall())


def create_patient(
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
    cursor.execute(
        "INSERT INTO Person VALUES(%(national_id)s, %(fname)s, %(lname)s, %(gender)s, %(birthday)s, %(is_married)s, %(phonenumber)s, %(street)s, %(alley)s, %(no)s);"
        + "INSERT INTO Patient VALUES(%(national_id)s, %(insurance_name)s, %(insurance_exp_date)s , %(weight)s, %(height)s);",
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
            "insurance_name": insurance_name,
            "insurance_exp_date": insurance_exp_date,
            "weight": weight,
            "height": height,
        },
    )

    connection.commit()


def update_person(national_id, updates):
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
