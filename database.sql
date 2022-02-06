-- CREATE DATABASE laboratory;

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


CREATE TABLE Person(
    NationalId NationalIdType NOT NULL PRIMARY KEY,
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

CREATE TABLE Secretory(
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
    Expenses CurrencyType NOT NULL DEFAULT 0,
    "Date" DateType NOT NULL,
    FOREIGN KEY(PatientId) REFERENCES Patient(NationalId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE RelatedTo(
    PrescriptionId INTEGER NOT NULL,
    ExperimentName VARCHAR(128) NOT NULL,
    PRIMARY KEY(PrescriptionId, ExperimentName),
    FOREIGN KEY(PrescriptionId) REFERENCES Prescription(PrescriptionId) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(ExperimentName) REFERENCES Experiment(ExperimentName) ON DELETE CASCADE ON UPDATE CASCADE

);

CREATE TABLE Receipt(
    ReceiptId SERIAL NOT NULL PRIMARY KEY,
    PrescriptionId INTEGER NOT NULL,
    PatientId NationalIdType NOT NULL,
    TotalCost CurrencyType NOT NULL,
    PreparationDate DateType NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(PatientId) REFERENCES Patient(NationalId) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(PrescriptionId) REFERENCES Prescription(PrescriptionId) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE OR REPLACE FUNCTION create_receipt() RETURNS trigger AS $create_receipt$
    BEGIN
        INSERT INTO Receipt(PatientId, TotalCost, PrescriptionId) VALUES (NEW.PatientId, NEW.Expenses, NEW.PrescriptionId);
	    RETURN NEW;
    END;
$create_receipt$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER create_receipt AFTER INSERT ON Prescription 
    FOR EACH ROW EXECUTE FUNCTION create_receipt();


CREATE OR REPLACE FUNCTION calculate_total_cost() RETURNS trigger AS $calculate_total_cost$
    BEGIN

        IF (SELECT Count(*) FROM InsuranceCompany WHERE InsuranceName = (SELECT Patient.InsuranceName FROM Patient WHERE NationalId = NEW.PatientId)) = 0 THEN
            UPDATE Receipt SET
                TotalCost = NEW.Expenses 
                WHERE NEW.PrescriptionId=Receipt.PrescriptionId;
        END IF;
        IF (SELECT Count(*) FROM InsuranceCompany WHERE InsuranceName = (SELECT Patient.InsuranceName FROM Patient WHERE NationalId = NEW.PatientId)) > 0 THEN
            UPDATE Receipt SET
                TotalCost = NEW.Expenses * (
                    100 - (SELECT "Percentage" FROM InsuranceCompany  WHERE InsuranceName = (SELECT Patient.InsuranceName FROM Patient WHERE NationalId=NEW.PatientId))
                    ) / 100
                    
                WHERE NEW.PrescriptionId=Receipt.PrescriptionId;
        END IF;
        RETURN NEW;
    END;
$calculate_total_cost$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER calculate_total_cost AFTER UPDATE OF Expenses ON Prescription 
    FOR EACH ROW EXECUTE FUNCTION calculate_total_cost();


CREATE OR REPLACE FUNCTION calculate_expenses() RETURNS trigger AS $calculate_expenses$
    BEGIN
        UPDATE Prescription SET 
        Expenses = Prescription.Expenses + (SELECT ExperimentCost FROM Experiment 
        WHERE ExperimentName = NEW.ExperimentName)
        WHERE Prescription.PrescriptionId = NEW.PrescriptionId;

	    RETURN NEW;
    END;
$calculate_expenses$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER expenses_trigger AFTER INSERT ON RelatedTo 
    FOR EACH ROW EXECUTE FUNCTION calculate_expenses(); 

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
    ReceiptId INTEGER NOT NULL,
    PrescriptionId INTEGER NOT NULL UNIQUE,
    SampleId INTEGER NOT NULL,
    ExperimentDate DateType NOT NULL,
    "Description" VARCHAR(256),
    "Comment" VARCHAR(256),
    PRIMARY KEY(ExperimenterId, ReceiptId),
    FOREIGN KEY(ReceiptId) REFERENCES Receipt(ReceiptId),
    FOREIGN KEY(ExperimenterId) REFERENCES Experimenter(NationalId)
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