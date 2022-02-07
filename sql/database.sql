-- CREATE DATABASE laboratory;

CREATE EXTENSION pgcrypto;

CREATE DOMAIN NationalIdType AS CHAR(10) CHECK (LENGTH(VALUE) = 10);

CREATE DOMAIN DateType AS TIMESTAMP WITH TIME ZONE;

CREATE DOMAIN TimeType AS TIME WITH TIME ZONE;

CREATE DOMAIN PhoneNumberType AS CHAR(11) CHECK (LENGTH(VALUE) = 11);

CREATE DOMAIN CurrencyType AS BIGINT;

CREATE DOMAIN GenderType AS CHAR(1) CHECK(VALUE IN('M', 'F'));


CREATE DOMAIN DayType AS VARCHAR(10) CHECK(
    VALUE IN (
        'Saturday',
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday'
    )
);

CREATE DOMAIN RoleType AS VARCHAR(12) CHECK(
    VALUE IN (
        'Manager',
        'Doctor',
        'Sampler',
        'Experimenter',
        'Patient',
        'Secretary'
    )
);

CREATE TABLE Person(
    NationalId NationalIdType NOT NULL PRIMARY KEY,
    "Password" TEXT NOT NULL,
    "Role" RoleType NOT NULL,
    FName VARCHAR(512) NOT NULL,
    LName VARCHAR(512) NOT NULL,
    Gender GenderType NOT NULL,
    BirthDay DateType NOT NULL,
    IsMarried BOOLEAN NOT NULL,
    PhoneNumber PhoneNumberType NOT NULL,
    Street VARCHAR(128) NOT NULL,
    Alley VARCHAR(128) NOT NULL,
    "No" INTEGER NOT NULL
);

CREATE TABLE Employee(
    NationalId NationalIdType NOT NULL PRIMARY KEY,
    ContractStartDate DateType NOT NULL,
    ContractEndDate DateType NOT NULL,
    Salary CurrencyType NOT NULL,
    FOREIGN KEY (NationalId) REFERENCES Person(NationalId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Patient(
    NationalId NationalIdType NOT NULL PRIMARY KEY,
    InsuranceName VARCHAR(64),
    InsuranceExpirationDate DateType,
    "Weight" DECIMAL(5, 2),
    Height DECIMAL(5, 2),
    FOREIGN KEY (NationalId) REFERENCES Person(NationalId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Doctor(
    NationalId NationalIdType NOT NULL PRIMARY KEY,
    GMCNumber INTEGER UNIQUE NOT NULL,
    FOREIGN KEY (NationalId) REFERENCES Employee(NationalId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Experimenter(
    NationalId NationalIdType NOT NULL PRIMARY KEY,
    GMCNumber INTEGER UNIQUE NOT NULL,
    FOREIGN KEY (NationalId) REFERENCES Employee(NationalId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Sampler(
    NationalId NationalIdType NOT NULL PRIMARY KEY,
    GMCNumber INTEGER UNIQUE NOT NULL,
    FOREIGN KEY (NationalId) REFERENCES Employee(NationalId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Manager(
    NationalId NationalIdType NOT NULL PRIMARY KEY,
    FOREIGN KEY (NationalId) REFERENCES Employee(NationalId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Secretary(
    NationalId NationalIdType NOT NULL PRIMARY KEY,
    FOREIGN KEY (NationalId) REFERENCES Employee(NationalId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE InsuranceCompany(
    InsuranceName VARCHAR(128) NOT NULL PRIMARY KEY,
    "Percentage" DECIMAL(4, 2) NOT NULL ,
    "Limit" CurrencyType NOT NULL,
    StartDate DateType NOT NULL,
    EndDate DateType NOT NULL,
    CHECK("Percentage" <= 100 AND "Percentage" >= 0)
);

CREATE TABLE EducationDegree(
    EmployeeId NationalIdType NOT NULL,
    Title VARCHAR(128) NOT NULL,
    University VARCHAR(128) NOT NULL,
    StartDate DateType NOT NULL,
    EndDate DateType NOT NULL,
    PRIMARY KEY(EmployeeId, Title),
    FOREIGN KEY(EmployeeId) REFERENCES Employee(NationalId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE DiseaseBackground(
    DiseaseName VARCHAR(128) NOT NULL,
    PatientId NationalIdType NOT NULL,
    StartDate DateType,
    EndDate DateType,
    PRIMARY KEY(DiseaseName, PatientId),
    FOREIGN KEY(PatientId) REFERENCES Patient(NationalId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Experiment(
    ExperimentName VARCHAR(128) NOT NULL PRIMARY KEY,
    ExperimentCost CurrencyType NOT NULL
);

CREATE TABLE Prescription(
    PrescriptionId SERIAL NOT NULL PRIMARY KEY,
    PatientId NationalIdType NOT NULL,
    ReferDoctor VARCHAR(128) NOT NULL,
    "Date" DateType NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Expenses CurrencyType NOT NULL DEFAULT 0,
    TotalCost CurrencyType NOT NULL DEFAULT 0,
    PreparationDate DateType NOT NULL,
    FOREIGN KEY(PatientId) REFERENCES Patient(NationalId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE RelatedTo(
    PrescriptionId INTEGER NOT NULL,
    ExperimentName VARCHAR(128) NOT NULL,
    PRIMARY KEY(PrescriptionId, ExperimentName),
    FOREIGN KEY(PrescriptionId) REFERENCES Prescription(PrescriptionId) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(ExperimentName) REFERENCES Experiment(ExperimentName) ON DELETE CASCADE ON UPDATE CASCADE

);


CREATE OR REPLACE FUNCTION calculate_costs() RETURNS trigger AS $calculate_costs$
    DECLARE diff_expenses CurrencyType;
    DECLARE prescription_row Prescription%ROWTYPE;
    DECLARE valid_insurance InsuranceCompany%ROWTYPE;
    BEGIN
        diff_expenses := (SELECT ExperimentCost FROM Experiment WHERE ExperimentName = NEW.ExperimentName);
        SELECT * INTO prescription_row FROM Prescription WHERE Prescription.PrescriptionId = NEW.PrescriptionId;
        SELECT * INTO valid_insurance FROM InsuranceCompany WHERE InsuranceCompany.InsuranceName = (SELECT Patient.InsuranceName FROM Patient WHERE Patient.NationalId = prescription_row.PatientId AND Patient.InsuranceExpirationDate >= InsuranceCompany.StartDate AND Patient.InsuranceExpirationDate <= InsuranceCompany.EndDate AND prescription_row."Date" >= InsuranceCompany.StartDate AND prescription_row."Date" <= Patient.InsuranceExpirationDate);
        -- calculate Expenses in Prescription
        UPDATE Prescription 
        SET Expenses = Prescription.Expenses + diff_expenses,

        -- calculate TotalCost in Prescription
        TotalCost = 
        CASE
            WHEN valid_insurance IS NOT NULL THEN
                CASE 
                    WHEN ((diff_expenses * (valid_insurance."Percentage") / 100) + Expenses - TotalCost > valid_insurance."Limit") THEN 
                    TotalCost + (diff_expenses * (100 - valid_insurance."Percentage") / 100 ) + (diff_expenses * (valid_insurance."Percentage") / 100 ) + Expenses - TotalCost - valid_insurance."Limit"
                    ELSE TotalCost + ( diff_expenses * (100 - valid_insurance."Percentage") / 100 )
                END
            ELSE TotalCost + diff_expenses
        END
        WHERE Prescription.PrescriptionId = NEW.PrescriptionId;

	    RETURN NEW;
    END;
$calculate_costs$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER prescription_trigger AFTER INSERT ON RelatedTo 
    FOR EACH ROW EXECUTE FUNCTION calculate_costs(); 

CREATE TABLE "Sample"(
    SampleId SERIAL NOT NULL PRIMARY KEY,
    PatientId NationalIdType NOT NULL,
    ExperimentName VARCHAR(128) NOT NULL,
    SamplerId NationalIdType NOT NULL,
    FOREIGN KEY(PatientId) REFERENCES Patient(NationalId) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(ExperimentName) REFERENCES Experiment(ExperimentName) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(SamplerId) REFERENCES Sampler(NationalId) ON DELETE
    SET
        NULL ON UPDATE CASCADE
);

CREATE TABLE Result(
    ExperimenterId NationalIdType NOT NULL,
    PrescriptionId INTEGER NOT NULL,
    SampleId INTEGER NOT NULL,
    ExperimentDate DateType NOT NULL,
    "Description" VARCHAR(256),
    "Comment" VARCHAR(256),
    PRIMARY KEY(ExperimenterId, PrescriptionId),
    FOREIGN KEY(ExperimenterId) REFERENCES Experimenter(NationalId),
    FOREIGN KEY(PrescriptionId) REFERENCES Prescription(PrescriptionId)
);

CREATE TABLE WorkDay(
    EmployeeId NationalIdType NOT NULL,
    "Day" DayType NOT NULL,
    "Start" TimeType NOT NULL,
    "End" TimeType NOT NULL,
    roomNo INTEGER NOT NULL,
    roomPhoneNumber PhoneNumberType,
    PRIMARY KEY(EmployeeId, "Day")
);

CREATE TABLE PayCheck(
    Id SERIAL NOT NULL PRIMARY KEY,
    EmployeeId NationalIdType NOT NULL,
    "Date" DateType NOT NULL,
    Amount CurrencyType NOT NULL
);



CREATE FUNCTION check_paycheck_amount() RETURNS trigger AS $check_paycheck_amount$
    BEGIN
        IF NEW.Amount <> (SELECT Salary from Employee WHERE NationalId = NEW.EmployeeId) THEN
            RAISE EXCEPTION 'pay check amount should be equal to Employee Salary';
        END IF;
        RETURN NEW;
    END;
$check_paycheck_amount$ LANGUAGE plpgsql;

CREATE TRIGGER check_paycheck_amount BEFORE INSERT ON PayCheck
    FOR EACH ROW EXECUTE FUNCTION check_paycheck_amount();