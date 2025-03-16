import subprocess
import mysql.connector

def initialize():
    subprocess.run(["python","executor.py"])
    
def final_result(id):
      con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="DBT25_A1_PES2UG22CS506_Sanket"
      )
      cursor=con.cursor()
      print("\nFINAL RESULT->")
      tsh_level=float(input("\nEnter tsh level : "))
      t3_level=float(input("\nEnter t3 level : "))
      t4_level=float(input("\nEnter t4 level : "))
      cursor.execute("insert into thyroid_test_results(id,tsh_level,t3_level,t4_level) values(%s,%s,%s,%s);",(id,tsh_level,t3_level,t4_level))
      con.commit()
      cursor.close()
      main()

def nodule_classifier(id):
      con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="DBT25_A1_PES2UG22CS506_Sanket"
      )
      cursor=con.cursor()
      cursor.execute("select min(nodule_size) from nodule_details where thyroid_cancer_risk='low';")
      low_min=cursor.fetchone()[0]
      cursor.execute("select max(nodule_size) from nodule_details where thyroid_cancer_risk='low';")
      low_max=cursor.fetchone()[0]
      cursor.execute("select min(nodule_size) from nodule_details where thyroid_cancer_risk='medium';")
      medium_min=cursor.fetchone()[0]
      cursor.execute("select max(nodule_size) from nodule_details where thyroid_cancer_risk='medium';")
      medium_max=cursor.fetchone()[0]
      cursor.execute("select min(nodule_size) from nodule_details where thyroid_cancer_risk='high';")
      high_min=cursor.fetchone()[0]
      cursor.execute("select max(nodule_size) from nodule_details where thyroid_cancer_risk='high';")
      high_max=cursor.fetchone()[0]
      nodule_size=float(input("\nEnter the size of nodule : "))
      if nodule_size<=low_max :
            thyroid_cancer_risk="low"
      elif medium_min<=nodule_size<=medium_max:
            thyroid_cancer_risk="medium"
      elif high_min<=nodule_size:
            thyroid_cancer_risk="high"
      cursor.execute("insert into nodule_details(id,nodule_size,thyroid_cancer_risk) values(%s,%s,%s);",(id,nodule_size,thyroid_cancer_risk))      
      con.commit()
      cursor.close()
      final_result(id)

def doctor_diagnosis(id):
      con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="DBT25_A1_PES2UG22CS506_Sanket"
      )
      cursor=con.cursor()
      print("\nDOCTOR'S DIAGNOSIS-> ")
      diagnosis=input("\nEnter the doctor's diagnosis (benign/malignant) : ").strip().lower()
      cursor.execute("insert into diagnosis(id,diagnosis) values(%s,%s);",(id,diagnosis))
      con.commit()
      cursor.close()
      nodule_classifier(id)

def patient_registration():
        con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="DBT25_A1_PES2UG22CS506_Sanket"
        )
        cursor=con.cursor()
        print("\nPATIENT REGISTRAION->")
        cursor.execute("select max(id) from patient")
        last_id=cursor.fetchone()[0]
        id=last_id+1
        age=int(input("\nEnter patient age : "))
        gender=input("\nEnter patient gender (male/female) : ").strip().lower()
        country=input("\nEnter patient country : ").strip().lower()
        ethnicity=input("\nEnter patient ethnicity : ").strip().lower()
        cursor.execute("insert into patient(id,age,gender,country,ethnicity) values(%s,%s,%s,%s,%s);",(id,age,gender,country,ethnicity) )
        con.commit()
        print("\nMEDICAL HISTORY->")
        family_history=input("\ndo you have a family history of thyroid cancer ? (yes/no) : ").strip().lower()
        radiation_exposure=input("\nhave you been exposed to radiation ? (yes/no) : ").strip().lower()
        iodine_deficiency=input("\ndo you have iodine deficiency ? (yes/no) ").strip().lower()
        smoking=input("\ndo you smoke ? (yes/no) : ").strip().lower()
        obesity=input("\ndo you suffer from obesity ? (yes/no) : ").strip().lower()
        diabetes=input("\ndo you suffer from diabetes ? (yes/no) : ").strip().lower()
        cursor.execute("insert into medical_history(id,family_history,radiation_exposure,iodine_deficiency,smoking,obesity,diabetes) values(%s,%s,%s,%s,%s,%s,%s);",(id,family_history,radiation_exposure,iodine_deficiency,smoking,obesity,diabetes))
        con.commit()
        cursor.close()
        con.close()
        doctor_diagnosis(id)

def view_patient():
      id=int(input("\nEnter id of patient : "))
      con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="DBT25_A1_PES2UG22CS506_Sanket"
      )
      cursor=con.cursor()
      print("\nPATIENT DETAILS->")
      cursor.execute("select * from patient left join medical_history on medical_history.id=patient.id where patient.id=%s;",(id,))
      patient_details=cursor.fetchmany()
      patient_columns=[desc[0] for desc in cursor.description]
      patient_dict={}
      i=0
      for x in patient_columns:
            for y in patient_details:
                  patient_dict.update({x:y[i]})
                  i+=1
      print(patient_dict)
      print("\nDOCTOR'S DIAGNOSIS->")
      cursor.execute("""
      select * from diagnosis 
      left join thyroid_test_results on diagnosis.id = thyroid_test_results.id 
      left join nodule_details on diagnosis.id = nodule_details.id 
      where diagnosis.id = %s;
      """, (id,))
      doctors_diagnosis=cursor.fetchmany()
      doctors_diagnosis_columns=[desc[0] for desc in cursor.description]
      dd_dict={}
      j=0
      for x in doctors_diagnosis_columns:
            for y in doctors_diagnosis:
                  dd_dict.update({x:y[j]})
                  j+=1
      print("\n",dd_dict)
      con.close()
      main()




def advanced_stats():
      con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="DBT25_A1_PES2UG22CS506_Sanket"
      )
      cursor=con.cursor()
      cursor.execute("select count(*) from patient;")
      total_count=cursor.fetchone()[0]
      print("\n total number of patients are ",total_count)
      cursor.execute("select ethnicity,count(*) as count from patient group by ethnicity;")
      ethnicity_count=cursor.fetchall()
      print("\n the total number of patients of various ethnicities are : ",ethnicity_count)
      cursor.execute("select ethnicity,count(*) as cancer_cases from patient inner join diagnosis on patient.id=diagnosis.id where diagnosis='malignant'  group by ethnicity;")
      cancer_count=cursor.fetchall()
      print("\n the total number of cancer patients of various ethnicities are : ",cancer_count)
      cursor.execute("select ethnicity,count(*) as non_cancer_cases from patient inner join diagnosis on patient.id=diagnosis.id where diagnosis='benign' group by ethnicity;")
      non_cancer_count=cursor.fetchall()
      print("\n the total number of non cancerous patients of various ethnicities are : ",non_cancer_count)
      cursor.execute("select patient.id,thyroid_cancer_risk from patient inner join nodule_details on patient.id=nodule_details.id inner join diagnosis on diagnosis.id=nodule_details.id where diagnosis.diagnosis='malignant';")
      cancer_count_risk=cursor.fetchall()
      print("\n cancer risk for each patient",cancer_count_risk)





def main():
      while True:
            print("\nSTART MENU->")
            print("\nEnter 1 to register patient")
            print("\nEnter 2 to see registered patient details")
            print("\nEnter 3 to view some advanced stats")
            print("\nEnter 4 to populate database")
            print("\nEnter 5 to exit ")
            inp=int(input("\nInput : "))
            if inp==1:
                  patient_registration()
                  break
            elif inp==2:
                  view_patient()
                  break
            elif inp==3:
                  advanced_stats()
                  break
            elif inp==4:
                  initialize()
                  break
            elif inp==5:
                  print("\nExiting system")
                  break
            
main()


        

