from project import *
# add employees
add_employee("1111111111", "fmanager", "lmanager", "M", "2001-2-21", False, "09121111111", "s1", "a1", 1, "2020-1-1", "2021-1-1",10000000, "Manager", None)
add_employee("2222222222", "fsecretary", "lsecretary", "F", "2005-2-21", False, "09122222222", "s2", "a2", 2, "2021-1-1", "2022-1-1",5000000, "Secratary", None)
add_employee("3333333333", "fdotor", "ldoctor", "M", "2000-2-21", True, "09123333333", "s3", "a3", 3, "2020-1-1", "2023-1-1",9000000, "Dotor", 33333)
add_employee("4444444444", "fexperimenter", "lexperimenter", "F", "1999-2-21", False, "09124444444", "s5", "a5", 4, "2022-1-1", "2024-1-1",7000000, "Experimenter", 44444)

# add patients
add_patient("5555555555","fp1", "lp1", "M", "2001-1-1", True, "09125555555", "s5","a5", 5, "bime1", "2022-2-2", 75, 180)
add_patient("6666666666","fp2", "lp2", "F", "2000-1-1", True, "09126666666", "s6","a6", 6, None, None, 60, 160)
add_patient("7777777777","fp3", "lp3", "M", "1998-1-1", True, "09127777777", "s7","a7", 7, "bime2", "2012-2-2", 75, 190)
add_patient("8888888888","fp4", "lp4", "M", "2001-1-1", False, "09128888888", "s8","a8", 8, "unknown", "2025-2-2", 100, 230)

add_patient("9999999999","fp5", "lp5", "F", "1985-1-1", True, "09129999999", "s9","a9", 9, "bime3", "2022-2-2", 75, 180)
add_patient("1010101010","fp6", "lp6", "M", "1998-1-1", True, "09120000000", "s10","a10", 10, "bime1", "2017-2-2", 75, 180)
add_patient("1212121212","fp7", "lp7", "M", "2001-1-1", True, "09131111111", "s11","a11", 11, "bime1", "2022-2-2", 75, 180)
add_patient("1313131313","fp8", "lp8", "F", "1995-1-1", False,"09132222222", "s12","a12", 12, "unknown", "2012-2-2", 50, 230)

# add insurance company
add_insurance_company("bime1", 80, 500000, "2020-1-1", "2024-1-1")