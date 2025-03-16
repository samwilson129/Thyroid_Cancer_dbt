USE DBT25_A1_PES2UG22CS506_Sanket;

SELECT * FROM patient;
SELECT * FROM medical_history;
SELECT * FROM nodule_details;
SELECT * FROM diagnosis;
SELECT * FROM thyroid_test_results;

SELECT COUNT(*) as patient_count FROM patient;
SELECT COUNT(*) as medical_history_count FROM medical_history;
SELECT COUNT(*) as nodule_details_count FROM nodule_details;
SELECT COUNT(*) as diagnosis_count FROM diagnosis;
SELECT COUNT(*) as result_count FROM thyroid_test_results;

EXPLAIN ANALYZE SELECT * FROM patient;
EXPLAIN ANALYZE SELECT * FROM medical_history;
EXPLAIN ANALYZE SELECT * FROM nodule_details;
EXPLAIN ANALYZE SELECT * FROM diagnosis;
EXPLAIN ANALYZE SELECT * FROM thyroid_test_results;

EXPLAIN ANALYZE  
SELECT p.ethnicity, COUNT(*) AS cancer_cases  
FROM patient p  
INNER JOIN diagnosis d ON p.id = d.id  
WHERE d.diagnosis = 'malignant'  
GROUP BY p.ethnicity;

EXPLAIN ANALYZE  
SELECT p.ethnicity, COUNT(*) AS cancer_cases  
FROM diagnosis d  
INNER JOIN patient p ON p.id = d.id  
WHERE d.diagnosis = 'malignant'  
GROUP BY p.ethnicity;

EXPLAIN ANALYZE 
SELECT p.id, n.thyroid_cancer_risk, d.diagnosis 
FROM patient p
INNER JOIN nodule_details n ON p.id = n.id
INNER JOIN diagnosis d ON d.id = n.id
WHERE d.diagnosis = 'malignant';

EXPLAIN ANALYZE 
SELECT p.id, n.thyroid_cancer_risk, d.diagnosis 
FROM diagnosis d
INNER JOIN nodule_details n ON d.id = n.id
INNER JOIN patient p ON p.id = n.id
WHERE d.diagnosis = 'malignant';


CREATE INDEX idx_patient_id ON patient(id);
CREATE INDEX idx_medical_history_id ON medical_history(id);
CREATE INDEX idx_nodule_details_id ON nodule_details(id);
CREATE INDEX idx_diagnosis_id ON diagnosis(id);
CREATE INDEX idx_thyroid_test_results_id ON thyroid_test_results(id);

CREATE INDEX idx_patient_ethnicity ON patient(id, ethnicity);
CREATE INDEX idx_diagnosis_type ON diagnosis(id, diagnosis);

EXPLAIN ANALYZE SELECT * FROM patient;
EXPLAIN ANALYZE SELECT * FROM medical_history;
EXPLAIN ANALYZE SELECT * FROM nodule_details;
EXPLAIN ANALYZE SELECT * FROM diagnosis;
EXPLAIN ANALYZE SELECT * FROM thyroid_test_results;

EXPLAIN ANALYZE  
SELECT ethnicity, COUNT(*) as count FROM patient GROUP BY ethnicity;

CREATE INDEX idx_ethnicity ON patient(ethnicity);

EXPLAIN ANALYZE  
SELECT ethnicity, COUNT(*) as count FROM patient GROUP BY ethnicity;

DROP INDEX idx_ethnicity ON patient;

DROP INDEX idx_patient_id ON patient;
DROP INDEX idx_medical_history_id ON medical_history;
DROP INDEX idx_nodule_details_id ON nodule_details;
DROP INDEX idx_diagnosis_id ON diagnosis;
DROP INDEX idx_thyroid_test_results_id ON thyroid_test_results;

EXPLAIN ANALYZE
SELECT p.id, p.age, p.gender, d.diagnosis, mh.family_history, mh.smoking
FROM patient p
JOIN diagnosis d ON p.id = d.id
JOIN medical_history mh ON p.id = mh.id
WHERE p.id IN (
    SELECT id FROM patient WHERE age > 40
) 
AND mh.smoking = 'yes';

EXPLAIN ANALYZE
SELECT p.id, p.age, p.gender, d.diagnosis, mh.family_history, mh.smoking
FROM patient p
JOIN diagnosis d ON p.id = d.id
JOIN medical_history mh ON p.id = mh.id
WHERE p.age > 40 AND mh.smoking = 'yes';

CREATE INDEX idx_patient_age ON patient(age);
CREATE INDEX idx_patient_id ON patient(id);
CREATE INDEX idx_diagnosis_id ON diagnosis(id);
CREATE INDEX idx_medical_history_id ON medical_history(id);
CREATE INDEX idx_smoking ON medical_history(smoking);

EXPLAIN ANALYZE
SELECT p.id, p.age, p.gender, d.diagnosis, mh.family_history, mh.smoking
FROM patient p
JOIN diagnosis d ON p.id = d.id
JOIN medical_history mh ON p.id = mh.id
WHERE p.age > 40 AND mh.smoking = 'yes';

DROP INDEX idx_patient_age ON patient;
DROP INDEX idx_patient_id ON patient;
DROP INDEX idx_diagnosis_id ON diagnosis;
DROP INDEX idx_medical_history_id ON medical_history;
DROP INDEX idx_smoking ON medical_history;
