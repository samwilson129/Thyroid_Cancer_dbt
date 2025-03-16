use DBT25_A1_PES2UG22CS506_Sanket;
alter table diagnosis add constraint foreign key(id) references patient(id);
alter table medical_history add constraint foreign key(id) references patient(id);
alter table nodule_details add constraint foreign key(id) references patient(id);
alter table thyroid_test_results add constraint foreign key(id) references patient(id);