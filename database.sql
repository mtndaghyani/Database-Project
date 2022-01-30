CREATE DATABASE laboratory;

CREATE DOMAIN NationalIdType AS CHAR(10);

CREATE DOMAIN DateType AS DateType;

CREATE DOMAIN TimeType AS TIME WITH TIME ZONE;

CREATE DOMAIN PhoneNumberType AS CHAR(11);

CREATE DOMAIN CurrencyType AS BIGINT;

CREATE DOMAIN GenderType AS CHAR(1) CHECK(VALUE IN("M", "F"));

CREATE DOMAIN DayType AS VARCHAR(10) CHECK(
    VALUE IN (
        "Saturday",
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
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
    'No' INTEGER NOT NULL,
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
    'Weight' DECIMAL(3, 2),
    Height DECIMAL(3, 2),
    FOREIGN KEY (NationalId) REFERENCES Person(NationalId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Doctor(
    NationalId NationalIdType NOT NULL PRIMARY KEY,
    GMCNumber INTEGER NOT NULL,
    FOREIGN KEY (NationalId) REFERENCES Employee(NationalId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Experimenter(
    NationalId NationalIdType NOT NULL PRIMARY KEY,
    GMCNumber INTEGER NOT NULL,
    FOREIGN KEY (NationalId) REFERENCES Employee(NationalId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Sampler(
    NationalId NationalIdType NOT NULL PRIMARY KEY,
    GMCNumber INTEGER NOT NULL,
    FOREIGN KEY (NationalId) REFERENCES Employee(NationalId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Manager(
    NationalId NationalIdType NOT NULL PRIMARY KEY,
    FOREIGN KEY (NationalId) REFERENCES Employee(NationalId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Secratary(
    NationalId NationalIdType NOT NULL PRIMARY KEY,
    FOREIGN KEY (NationalId) REFERENCES Employee(NationalId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE InsuranceCompany(
    InsuranceId SERIAL NOT NULL PRIMARY KEY,
    InsuranceName VARCHAR(128) NOT NULL UNIQUE,
    'Percentage' DECIMAL(3, 2) NOT NULL,
    'Limit' CurrencyType NOT NULL,
    StartDate DateType NOT NULL,
    EndDate DateType NOT NULL,
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
    ExperimentCost CurrencyType NOT NULL,
);

CREATE TABLE Prescription(
    PrescriptionId SERIAL NOT NULL PRIMARY KEY,
    PatientId NationalIdType NOT NULL,
    ReferDoctor VARCHAR(128) NOT NULL,
    Expenses CurrencyType NOT NULL DEFAULT 0,
    'Date' DateType NOT NULL,
    FOREIGN KEY(PatientId) REFERENCES Patient(NationalId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE RelatedTo(
    PrescriptionId INTEGER NOT NULL,
    ExperimentName VARCHAR(128) NOT NULL,
    PRIMARY KEY(PrescriptionId, ExperimentName)
);

CREATE TABLE Receipt(
    ReceiptId SERIAL NOT NULL PRIMARY KEY,
    PatientId NationalIdType NOT NULL,
    TotalCost CurrencyType NOT NULL,
    PreparationDate DateType NOT NULL,
    FOREIGN KEY(PatientId) REFERENCES Patient(NationalId) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE 'Sample'(
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
    'Description' VARCHAR(256),
    'Comment' VARCHAR(256) PRIMARY KEY(ExperimenterId, ReceiptId),
    FOREIGN KEY(ReceiptId) REFERENCES Receipt(ReceiptId),
    FOREIGN KEY(ExperimenterId) REFERENCES Experimenter(NationalId),
);

CREATE TABLE WorkDay(
    EmployeeId NationalIdType NOT NULL,
    'Day' DayType NOT NULL,
    'Start' TimeType NOT NULL,
    'End' TimeType NOT NULL,
    roomNo INTEGER NOT NULL,
    roomPhoneNumber PhoneNumberType,
    PRIMARY KEY(EmployeeId, 'Day')
);

CREATE TABLE PayCheck(
    Id SERIAL NOT NULL PRIMARY KEY,
    EmployeeId NationalIdType NOT NULL,
    'Date' DateType NOT NULL,
    Amount CurrencyType NOT NULL,
);