insert into Experiment values('a', 10000), ('b', 20000), ('c', 30000);
insert into InsuranceCompany values(1, 'bime', 10, 10000, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP );

insert into Person values(1, 'asd', 'asd', 'M', CURRENT_TIMESTAMP, true, '09198227902', 'asdas', 'sad', 10 );


insert into Patient values(1, 'bime', CURRENT_TIMESTAMP, 100, 100);

insert into Prescription values(1, 1, 'ad', 0, CURRENT_TIMESTAMP);

insert into RelatedTo values(1, 'a'),(1,'b'),(1,'c');

------------------------------------------
insert into Person values(2, 'asd', 'asd', 'M', CURRENT_TIMESTAMP, true, '09198227902', 'asdas', 'sad', 10 ), (3, 'asd', 'asd', 'M', CURRENT_TIMESTAMP, true, '09198227902', 'asdas', 'sad', 10 );

insert into Patient values(2, 'bime', CURRENT_TIMESTAMP, 100, 100), (3, 'bime', CURRENT_TIMESTAMP, 100, 100);

insert into Prescription values(2, 2, 'ad',0 , CURRENT_TIMESTAMP),(3, 3, 'ad', 0, CURRENT_TIMESTAMP);


insert into RelatedTo values(2, 'a'),(2,'b'),(2,'c'), (3, 'a'),(3,'b'),(3,'c');


---------------------------

insert into Person values(4, 'asd', 'asd', 'M', CURRENT_TIMESTAMP, true, '09198227902', 'asdas', 'sad', 10 ), (5, 'asd', 'asd', 'M', CURRENT_TIMESTAMP, true, '09198227902', 'asdas', 'sad', 10 );
insert into Patient values(4, 'bime2', CURRENT_TIMESTAMP, 100, 100), (5, null, CURRENT_TIMESTAMP, 100, 100);


insert into Prescription values(4, 4, 'ad', 0, CURRENT_TIMESTAMP),(5, 5, 'ad',0 , CURRENT_TIMESTAMP);
insert into RelatedTo values(4, 'a'),(4,'b'),(4,'c'), (5, 'a'),(5,'b'),(5,'c');
-------------------------

insert into Prescription values(6, 2, 'ad',0 , CURRENT_TIMESTAMP),(7, 3, 'ad', 0, CURRENT_TIMESTAMP);
insert into RelatedTo values(6, 'a'),(6,'b'),(6,'c'), (7, 'a'),(7,'b'),(7,'c');
