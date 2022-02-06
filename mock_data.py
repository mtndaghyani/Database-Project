from project import *

# add employees
add_employee("1111111111", "fmanager", "lmanager", "M", "2001-2-21", False, "09121111111", "s1", "a1", 1, "2020-1-1",
             "2021-1-1", 10000000, "Manager", None)
add_employee("2222222222", "fsecretary", "lsecretary", "F", "2005-2-21", False, "09122222222", "s2", "a2", 2,
             "2021-1-1", "2022-1-1", 5000000, "Secratary", None)
add_employee("3333333333", "fdotor", "ldoctor", "M", "2000-2-21", True, "09123333333", "s3", "a3", 3, "2020-1-1",
             "2023-1-1", 9000000, "Dotor", 33333)
add_employee("4444444444", "fexperimenter", "lexperimenter", "F", "1999-2-21", False, "09124444444", "s5", "a5", 4,
             "2022-1-1", "2024-1-1", 7000000, "Experimenter", 44444)
add_employee("5151515151", "kambiz", "kambizian", "M", "2000-12-20", False, "09013337725", "felan", "felamnaki", 10,
             "2021-01-11", "2027-01-11", 98000000, "Sampler", 98980)
add_employee("0909090909", "folan", "folanaki", "F", "2001-01-11", True, "09090902345", "pipi", "popo", 8, "2009-01-11",
             "2029-01-11", 98000, "Sampler", 66666)
# add patients
add_patient("5555555555", "fp1", "lp1", "M", "2001-1-1", True, "09125555555", "s5", "a5", 5, "bime1", "2022-2-2", 75,
            180)
add_patient("6666666666", "fp2", "lp2", "F", "2000-1-1", True, "09126666666", "s6", "a6", 6, None, None, 60, 160)
add_patient("7777777777", "fp3", "lp3", "M", "1998-1-1", True, "09127777777", "s7", "a7", 7, "bime2", "2012-2-2", 75,
            190)
add_patient("8888888888", "fp4", "lp4", "M", "2001-1-1", False, "09128888888", "s8", "a8", 8, "unknown", "2025-2-2",
            100, 230)

add_patient("9999999999", "fp5", "lp5", "F", "1985-1-1", True, "09129999999", "s9", "a9", 9, "bime3", "2022-2-2", 75,
            180)
add_patient("1010101010", "fp6", "lp6", "M", "1998-1-1", True, "09120000000", "s10", "a10", 10, "bime1", "2017-2-2", 75,
            180)
add_patient("1212121212", "fp7", "lp7", "M", "2001-1-1", True, "09131111111", "s11", "a11", 11, "bime1", "2022-2-2", 75,
            180)
add_patient("1313131313", "fp8", "lp8", "F", "1995-1-1", False, "09132222222", "s12", "a12", 12, "unknown", "2012-2-2",
            50, 230)

# add insurance company
add_insurance_company("bime1", 80, 500000, "2020-1-1", "2024-1-1")
add_insurance_company("unknown", 0, 0, None, None)
add_insurance_company("bime2", 30, 40000, "2013-1-1", "2019-1-1")
add_insurance_company("bime4", 10, 8000000, "2020-1-1", "2024-1-1")

# disease background
add_disease_background("hiv", "5555555555", "2013-1-1", "2019-1-1")
add_disease_background("Migraine", "8888888888", "2013-1-1", "2019-1-1")

# education degree
add_education_degree("4444444444", "ampolzani", "tehran", "2013-1-1", "2019-1-1")
add_education_degree("3333333333", "maqz", "beheshti", "2013-1-1", "2019-1-1")

# experiments
add_experiment("edrar", "100000")
add_experiment("madfo", "200000")
add_experiment("khon", "80000")
add_experiment("checkUP", "200000")
add_experiment("Pregnancy", "7000")

# prescription
add_prescription("5555555555", "noskhe", "2021-01-11", ["edrar", "madfo"])
add_prescription("6666666666", "hi", "2021-01-11", ["khon", "Pregnancy"])
add_prescription("7777777777", "hehe", "2021-01-21", ["khon", "checkUP", "madfo"])
add_prescription("5555555555", "noskhe2", "2021-06-01", ["madfo", "khon", "edrar"])

# Sample
add_sample("5555555555", "madfo", "5151515151")
add_sample("5555555555", "edrar", "0909090909")
add_sample("6666666666", "khon", "0909090909")
add_sample("7777777777", "khon", "5151515151")

# work day
add_work_day("2222222222", "monday", "08:00:00", "22:00:00", 9, "09125363104")
add_work_day("1111111111", "friday", "09:00:00", "10:00:00", 1, "09123836309")
add_work_day("3333333333", "saturday", "08:00:00", "11:00:00", 3, "09123836308")
add_work_day("4444444444", "monday", "09:00:09", "18:00:00", 4, "09125363109")
add_work_day("0909090909","sunday","08:00:00", "11:00:00","09013337725")

#pay check

