from time import timezone
import psycopg

cursor = psycopg.connect(
    dbname="laboratory",
    password="1234",
    user="mohamadamin",
    host="localhost",
    port=5432,
).cursor()


def get_patient_receipt(patient_id, start_date, end_date):

    cursor.execute(
        "SELECT * FROM receipt WHERE PatientId=(%(patient_id)s) AND PreparationDate > (%(start_date)s) AND PreparationDate < (%(end_date)s)",
        {"patient_id": patient_id, "start_date": start_date, "end_date": end_date},
    )

    query = []

    for q in cursor.fetchall():
        query.append(
            {
                "Repceip_id": q[0],
                "Prescription_id": q[1],
                "patient_id": q[2],
                "total_cost": q[3],
                "prepration_date": q[4],
            }
        )

    return query


def get_experimenter_results(experimenter_id, start_date, end_date):
    cursor.execute(
        "SELECT * FROM Result WHERE ExperimenterId=(%(experimenter_id)s) AND ExperimentDate > (%(start_date)s) AND ExperimentDate < (%(end_date)s)",
        {
            "experimenter_id": experimenter_id,
            "start_date": start_date,
            "end_date": end_date,
        },
    )

    query = []

    for q in cursor.fetchall():
        query.append(
            {
                "ExperimenterId": q[0],
                "ReceiptId": q[1],
                "PrescriptionId": q[2],
                "SampleId": q[3],
                "ExperimentDate": q[4],
                "Description": q[5],
                "Comment": q[6],
            }
        )

    return query


print(get_patient_receipt("1", "2021-2-2", "2023-2-2"))
