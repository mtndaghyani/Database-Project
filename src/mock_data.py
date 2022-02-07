# from src.project import *
from project import *

# add employees

add_employee(
    "2222222222",
    "pass2",
    SECRETARY,
    "fsecretary",
    "lsecretary",
    "F",
    "2005-2-21",
    False,
    "09122222222",
    "s2",
    "a2",
    2,
    "2021-1-1",
    "2022-1-1",
    5000000,
    SECRETARY,
    None,
)

add_employee(
    "3333333333",
    "pass3",
    DOCTOR,
    "fdoctor",
    "ldoctor",
    "M",
    "2000-2-21",
    True,
    "09123333333",
    "s3",
    "a3",
    3,
    "2020-1-1",
    "2023-1-1",
    9000000,
    DOCTOR,
    33333,
)

add_employee(
    "1515151515",
    "pass15",
    DOCTOR,
    "farid",
    "faridi",
    "M",
    "2000-2-21",
    False,
    "09122112222",
    "s222",
    "a2222",
    2,
    "2021-1-1",
    "2022-1-1",
    1200000,
    DOCTOR,
    45312,
)

add_employee(
    "4444444444",
    "pass4",
    EXPERIMENTER,
    "fexperimenter",
    "lexperimenter",
    "F",
    "1999-2-21",
    False,
    "09124444444",
    "s5",
    "a5",
    4,
    "2022-1-1",
    "2024-1-1",
    7000000,
    EXPERIMENTER,
    44444,
)

add_employee(
    "1234567890",
    "pass5",
    EXPERIMENTER,
    "fexperimenter2",
    "lexperimenter2",
    "M",
    "2000-2-21",
    False,
    "09124444444",
    "s101",
    "a501",
    111,
    "2022-1-1",
    "2024-1-1",
    6500000,
    EXPERIMENTER,
    43211,
)

add_employee(
    "5151515151",
    "pass6",
    SAMPLER,
    "kambiz",
    "kambizian",
    "M",
    "2000-12-20",
    False,
    "09013337725",
    "felan",
    "felamnaki",
    10,
    "2021-01-11",
    "2027-01-11",
    98000000,
    SAMPLER,
    98980,
)
add_employee(
    "0909090909",
    "pass7",
    SAMPLER,
    "folan",
    "folanaki",
    "F",
    "2001-01-11",
    True,
    "09090902345",
    "pipi",
    "popo",
    8,
    "2009-01-11",
    "2029-01-11",
    98000,
    SAMPLER,
    66666,
)


# add patients
add_patient(
    "5555555555",
    "pass8",
    PATIENT,
    "fp1",
    "lp1",
    "M",
    "2001-1-1",
    True,
    "09125555555",
    "s5",
    "a5",
    5,
    "bime1",
    "2022-2-2",
    75,
    180,
)
add_patient(
    "6666666666",
    "pass9",
    PATIENT,
    "fp2",
    "lp2",
    "F",
    "2000-1-1",
    True,
    "09126666666",
    "s6",
    "a6",
    6,
    None,
    None,
    60,
    160,
)
add_patient(
    "7777777777",
    "pass10",
    PATIENT,
    "fp3",
    "lp3",
    "M",
    "1998-1-1",
    True,
    "09127777777",
    "s7",
    "a7",
    7,
    "bime2",
    "2012-2-2",
    75,
    190,
)
add_patient(
    "8888888888",
    "pass11",
    PATIENT,
    "fp4",
    "lp4",
    "M",
    "2001-1-1",
    False,
    "09128888888",
    "s8",
    "a8",
    8,
    "unknown",
    "2025-2-2",
    100,
    230,
)

add_patient(
    "9999999999",
    "pass12",
    PATIENT,
    "fp5",
    "lp5",
    "F",
    "1985-1-1",
    True,
    "09129999999",
    "s9",
    "a9",
    9,
    "bime3",
    "2022-2-2",
    75,
    180,
)
add_patient(
    "1010101010",
    "pass13",
    PATIENT,
    "fp6",
    "lp6",
    "M",
    "1998-1-1",
    True,
    "09120000000",
    "s10",
    "a10",
    10,
    "bime1",
    "2017-2-2",
    75,
    180,
)
add_patient(
    "1212121212",
    "pass14",
    PATIENT,
    "fp7",
    "lp7",
    "M",
    "2001-1-1",
    True,
    "09131111111",
    "s11",
    "a11",
    11,
    "bime1",
    "2022-2-2",
    75,
    180,
)
add_patient(
    "1313131313",
    "pass15",
    PATIENT,
    "fp8",
    "lp8",
    "F",
    "1995-1-1",
    False,
    "09132222222",
    "s12",
    "a12",
    12,
    "unknown",
    "2012-2-2",
    50,
    230,
)

# add insurance company
add_insurance_company("bime1", 80, 500000, "2020-1-1", "2024-1-1")
add_insurance_company("bime2", 30, 40000, "2013-1-1", "2019-1-1")
add_insurance_company("bime3", 70, 10000, "2020-1-1", "2022-1-1")
add_insurance_company("bime4", 10, 8000000, "2020-1-1", "2024-1-1")

# disease background
add_disease_background("hiv", "5555555555", "2013-1-1", "2019-1-1")
add_disease_background("Migraine", "5555555555", "2015-1-1", "2018-1-1")
add_disease_background("HeartAttack", "6666666666", "2012-1-1", "2014-1-1")
add_disease_background("Covid-19", "6666666666", "2020-1-1", "2021-1-1")
add_disease_background("Diabetes", "7777777777", "2010-1-1", "2021-1-1")
add_disease_background("Diabetes", "8888888888", "2015-1-1", "2019-1-1")
add_disease_background("Cancer", "9999999999", "2011-1-1", "2013-1-1")
add_disease_background("HeartAttack", "9999999999", "2009-1-1", "2010-1-1")
add_disease_background("hiv", "1010101010", "2017-1-1", "2018-1-1")
add_disease_background("Covid-19", "1212121212", "2012-1-1", "2015-1-1")


# education degree
add_education_degree("4444444444", "ampolzani", "tehran", "2013-1-1", "2019-1-1")
add_education_degree("3333333333", "maqz", "beheshti", "2013-1-1", "2019-1-1")
add_education_degree("5151515151", "az", "tehran", "2010-1-1", "2018-1-1")
add_education_degree("0909090909", "az", "Azad", "2013-1-1", "2021-1-1")
add_education_degree("5151515151", "maqz", "beheshti", "2013-1-1", "2019-1-1")
add_education_degree("1515151515", "ghalb", "tehran", "2000-1-1", "2006-1-1")


# experiments
add_experiment("edrar", 100000)
add_experiment("madfo", 200000)
add_experiment("khon", 80000)
add_experiment("checkUP", 200000)
add_experiment("Pregnancy", 7000)

# prescription
add_prescription("5555555555", "noskhe", "2021-01-11", "2021-01-15", ["edrar", "madfo"])
add_prescription("6666666666", "hi", "2021-01-11", "2021-02-15", ["khon", "Pregnancy"])
add_prescription(
    "7777777777", "hehe", "2021-01-21", "2021-03-15", ["khon", "checkUP", "madfo"]
)
add_prescription(
    "5555555555", "noskhe2", "2021-01-01", "2021-01-05", ["madfo", "khon", "edrar"]
)
add_prescription(
    "9999999999", "noskhe3", "2020-01-01", "2022-01-10", ["madfo", "khon", "checkUP"]
)
add_prescription("1010101010", "noskhe4", "2019-01-01", "2019-01-05", ["edrar"])
add_prescription("1010101010", "noskhe5", "2019-03-01", "2019-03-15", ["Pregnancy"])
add_prescription(
    "1212121212",
    "noskhe6",
    "2021-03-02",
    "2021-04-01",
    ["madfo", "khon", "checkUP", "Pregnancy"],
)
add_prescription("1212121212", "noskhe7", "2021-02-10", "2021-02-16", ["madfo"])
add_prescription(
    "1313131313", "noskhe8", "2021-09-02", "2021-09-10", ["checkUP", "edrar"]
)
add_prescription("6666666666", "noskhe9", "2019-01-02", "2021-01-09", ["madfo", "khon"])


# Sample
add_sample("5555555555", "madfo", "5151515151")
add_sample("5555555555", "edrar", "0909090909")
add_sample("5555555555", "madfo", "5151515151")
add_sample("5555555555", "edrar", "5151515151")
add_sample("5555555555", "madfo", "0909090909")
add_sample("5555555555", "khon", "0909090909")
add_sample("6666666666", "khon", "0909090909")
add_sample("6666666666", "khon", "5151515151")
add_sample("6666666666", "Pregnancy", "5151515151")
add_sample("6666666666", "madfo", "0909090909")
add_sample("7777777777", "khon", "5151515151")
add_sample("7777777777", "checkUP", "0909090909")
add_sample("7777777777", "madfo", "5151515151")
add_sample("9999999999", "madfo", "0909090909")
add_sample("9999999999", "khon", "5151515151")
add_sample("9999999999", "checkUP", "5151515151")
add_sample("1010101010", "Pregnancy", "0909090909")
add_sample("1010101010", "edrar", "5151515151")
add_sample("1212121212", "madfo", "5151515151")
add_sample("1212121212", "madfo", "0909090909")
add_sample("1212121212", "khon", "5151515151")
add_sample("1212121212", "checkUP", "5151515151")
add_sample("1212121212", "Pregnancy", "0909090909")
add_sample("1313131313", "edrar", "5151515151")
add_sample("1313131313", "checkUP", "0909090909")


# work day
add_work_day("2222222222", "Monday", "08:00:00", "22:00:00", 9, "09125363104")
add_work_day("1111111111", "Friday", "09:00:00", "10:00:00", 1, "09123836309")
add_work_day("3333333333", "Saturday", "08:00:00", "11:00:00", 3, "09123836308")
add_work_day("4444444444", "Monday", "09:00:09", "18:00:00", 4, "09125363109")
add_work_day("0909090909", "Sunday", "08:00:00", "11:00:00", 10, "09013337725")


# pay check
add_pay_check("1111111111", "2021-2-02", 10000000)
add_pay_check("1111111111", "2021-3-10", 10000000)
add_pay_check("2222222222", "2021-2-11", 5000000)
add_pay_check("2222222222", "2021-3-09", 5000000)
add_pay_check("3333333333", "2021-2-07", 9000000)
add_pay_check("3333333333", "2021-3-08", 9000000)
add_pay_check("1515151515", "2021-2-09", 1200000)
add_pay_check("1515151515", "2021-3-10", 1200000)
add_pay_check("4444444444", "2021-2-11", 7000000)
add_pay_check("4444444444", "2021-3-14", 7000000)
add_pay_check("1234567890", "2021-2-09", 6500000)
add_pay_check("1234567890", "2021-3-11", 6500000)
add_pay_check("5151515151", "2021-2-12", 98000000)
add_pay_check("5151515151", "2021-3-11", 98000000)
add_pay_check("0909090909", "2021-2-13", 98000)
add_pay_check("0909090909", "2021-3-10", 98000)


# results
add_result("4444444444", 1, 1, "2021-1-11", "des", "comm1")
add_result("1234567890", 1, 2, "2021-1-12", "des", "comm2")
add_result("4444444444", 2, 7, "2021-1-20", "asdf", "comm3")
add_result("1234567890", 2, 9, "2021-2-2", "hhhh", "comm4")
add_result("4444444444", 3, 11, "2021-2-3", "eqtr", "comm5")
add_result("1234567890", 3, 12, "2021-3-10", "des", "comm6")
add_result("4444444444", 3, 13, "2021-2-26", "cc", "comm7")
add_result("1234567890", 4, 4, "2021-1-2", "af", "comm8")
add_result("4444444444", 4, 5, "2021-1-4", "qrawer", "comm9")
add_result("1234567890", 4, 6, "2021-1-3", "asdfasdf", "comm11")
add_result("4444444444", 5, 14, "2021-1-2", "aarehserh", "comm12")
add_result("1234567890", 5, 15, "2021-1-9", "gawr", "comm13")
add_result("4444444444", 5, 16, "2021-1-8", "asdf", "comm14")
add_result("1234567890", 6, 17, "2021-1-4", "ytdu", "comm15")
add_result("4444444444", 7, 18, "2021-3-14", "rtyusery", "comm16")
add_result("1234567890", 8, 19, "2021-3-12", "adsfaw", "comm17")
add_result("4444444444", 8, 20, "2021-3-14", "xcgart", "com18")
add_result("1234567890", 8, 21, "2021-3-20", "aeraedsf", "com19")
add_result("4444444444", 8, 22, "2021-3-2", "asgeaet", "com20")
add_result("1234567890", 9, 23, "2021-2-28", "aefadsf", "comm22")
add_result("4444444444", 10, 24, "2021-9-5", "aeqwr", "comm23")
add_result("1234567890", 10, 25, "2021-9-9", "adsgare", "comm24")
add_result("1234567890", 11, 10, "2021-1-5", "asd", "comm234")
add_result("1234567890", 11, 8, "2021-1-8", "asdfsadf", "comm44")



