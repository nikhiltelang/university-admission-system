from cassandra import cluster, query
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
class CassandraManagement:
    def __init__(self):
        try:
            self.cloud_config= {
                    'secure_connect_bundle': 'D:\secure-connect-university-db.zip'
            }
            self.auth_provider = PlainTextAuthProvider('ROZWCgfeXRDSbMRLywDItvbn', '.xO3__vFQMdj3vv18b_h4cmoBBeB4ZJn8j7OoEmhu0_n8344QmmvdnDva.7ZA3wvFvoILmwyjWa3ZPRC.AaQd4ptwxklaroLGO_+17XHofD+dGkA35Il-RebSCRZZS6R')
            self.cluster = Cluster(cloud=self.cloud_config, auth_provider=self.auth_provider)
            self.session = self.cluster.connect('university')
        except Exception as e:
            pass
        #     return e
    def createKeyspace(self,KeyspaceName):
        try:
            self.session.execute("CREATE KEYSPACE javatpoint WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3}; ")
        except Exception as e:
            pass
    
    def select_student_info(self):
        try:
            cluster = Cluster()
            session = cluster.connect()
            personal_details = session.execute("select * from university.personal_details")
            religion_details = session.execute("select * from university.religion_details")
            caste_details = session.execute("select * from university.caste_details")
            income_details = session.execute("select * from university.income_details")
            domicile_details = session.execute("select * from university.domicile_details")
            permanent_address_details = session.execute("SELECT * FROM university.permanent_address_details ;")
            correspondence_address_details = session.execute("SELECT * FROM university.correspondence_address_details ;")
            past_qualification_details = session.execute("SELECT * FROM university.past_qualification_details ;")
            applying_details = session.execute("SELECT * FROM university.applying_details ;")
            return personal_details, religion_details, caste_details, income_details, domicile_details,permanent_address_details,correspondence_address_details,past_qualification_details,applying_details
        except Exception as e:
            return e

    def select_admission_summery(self):
        try:
            cluster = Cluster()
            session = cluster.connect()
            personal_details = session.execute("select id,name from university.personal_details")
            return personal_details
        except Exception as e:
            return e
    def faculty_registration(self,id,fullname,email,password):
        try:
            # cluster = Cluster()
            # session = cluster.connect()
            query = "insert into university.faculty_info(id,fullname,email,password)values({},'{}','{}','{}')".format(id,fullname,email,password)
            new = self.session.execute(query)
            
            return new
        except Exception as e:
            return e
    
    def student_registration(self,id,fullname,email,password):
        try:
            # cluster = Cluster()
            # session = cluster.connect()
            query = "insert into university.student_info(id,fullname,email,password)values({},'{}','{}','{}')".format(id,fullname,email,password)
            print(query)
            new = self.session.execute(query)
            return new
        except Exception as e:
            return e

    def student_signin(self,email,password):
        try:
            cluster = Cluster()
            session = cluster.connect("university")
            query = "select * from student_info where email='{}' and password='{}' ALLOW FILTERING ;".format(email,password)
            result = session.execute(query)
            for i in result:
                if i is None:
                    return "No"
                else:
                    return "Yes"

        except Exception as e:
            return e
    
    def faculty_signin(self,email,password):
        try:
            # cluster = Cluster()
            # session = cluster.connect("university")
            query = "select * from faculty_info where email='{}' and password='{}' ALLOW FILTERING ;".format(email,password)
            result = self.session.execute(query)
            return result
        except Exception as e:
            return e

    def faculty_profile_data(self):
        try:
            cluster = Cluster()
            session = cluster.connect("university")
            query1 = "select * from faculty_info  ;"
            query2 = "select * from faculty_profile"
            query3 = "select * from faculty_connections"
            result1 = session.execute(query1)
            result2 = session.execute(query2)
            result3 = session.execute(query3)
            return result1, result2, result3
        except Exception as e:
            pass
    def insert_personal_details(self,id,Aadhar_card_no,fullname,email,mobile,dateofbirth,age,gender,Applicant_Full_Name_As_Per_SSC_Marksheet,Guardian_Mobile_No,Marital_Status):
        try:
            query = """insert into personal_details(id, aadhar_card_no,name,email, mobile_no,date_of_birth,age, gender, applicant_fullname,
                    parent_mobile_no,marital_status)values({},{},'{}','{}',{},'{}',{},'{}','{}',{},'{}')""".format(id, Aadhar_card_no,fullname,email, mobile,dateofbirth, age, gender,
                    Applicant_Full_Name_As_Per_SSC_Marksheet,Guardian_Mobile_No,Marital_Status)

            # cluster = Cluster()
            # session = cluster.connect("university")
            result = self.session.execute(query)
            print(query)
            return result
        except Exception as e:
            return e

    def insert_religion_details(self,id,religion):
        try:
            query = """insert into religion_details(id, religion)values({},'{}')""".format(id,religion)

            # cluster = Cluster()
            # session = cluster.connect("university")
            result = self.session.execute(query)
            print(query)
            return result
        except Exception as e:
            return e


    def insert_caste_details(self,id,Caste_Category,caste,Do_you_have_Caste_Certificate,Caste_Certificate_Number,Issuing_District,Applicant_Name,Issuing_Authority,Caste_Certificate,Caste_Issuing_Date):
        try:
            query = """insert into caste_details(id, category, caste, do_you_have_caste_certificate, caste_certificate_no,
             issuing_district, applicant_name, issuing_athority, caste_document, issuing_date)values({},'{}','{}','{}',{},'{}','{}','{}',
            '{}','{}')""".format(id, Caste_Category, caste, Do_you_have_Caste_Certificate, Caste_Certificate_Number, Issuing_District, Applicant_Name,
                            Issuing_Authority, Caste_Certificate, Caste_Issuing_Date)

            # cluster = Cluster()
            # session = cluster.connect("university")
            cloud_config = {
                'secure_connect_bundle': 'D:\secure-connect-university-db.zip'
            }
            auth_provider = PlainTextAuthProvider('ROZWCgfeXRDSbMRLywDItvbn',
                                                  '.xO3__vFQMdj3vv18b_h4cmoBBeB4ZJn8j7OoEmhu0_n8344QmmvdnDva.7ZA3wvFvoILmwyjWa3ZPRC.AaQd4ptwxklaroLGO_+17XHofD+dGkA35Il-RebSCRZZS6R')
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            self.session = cluster.connect('university')
            result = self.session.execute(query)
            print(query)
            return result
        except Exception as e:
            return e


    def insert_income_details(self,id,Family_Annual_Income, Do_you_have_Income_Certificate, Income_Certificate_No, Income_Issuing_Authority, Income_Certificate, Income_Issuing_Date):
        try:
            query = """insert into income_details(id, income, do_you_have_income_certificate, income_certificate_no, issuing_authority,
             income_document, issuing_date)values({},{},'{}',{},'{}','{}','{}')""".format(id, Family_Annual_Income, Do_you_have_Income_Certificate, Income_Certificate_No, Income_Issuing_Authority, Income_Certificate, Income_Issuing_Date,)

            # cluster = Cluster()
            # session = cluster.connect("university")
            cloud_config = {
                'secure_connect_bundle': 'D:\secure-connect-university-db.zip'
            }
            auth_provider = PlainTextAuthProvider('ROZWCgfeXRDSbMRLywDItvbn',
                                                  '.xO3__vFQMdj3vv18b_h4cmoBBeB4ZJn8j7OoEmhu0_n8344QmmvdnDva.7ZA3wvFvoILmwyjWa3ZPRC.AaQd4ptwxklaroLGO_+17XHofD+dGkA35Il-RebSCRZZS6R')
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            self.session = cluster.connect('university')
            result = self.session.execute(query)
            print(query)
            return result
        except Exception as e:
            return e

    def insert_domicile_details(self,id,Are_you_Domicile_of_Maharashtra, Do_you_have_Domicile_Certificate, Relationship_Type,Domicile_Certificate_No, Applicant_Name, Issuing_Authority, domicile_Issuing_Date, Domicile_Certificate):
        try:
            query = """insert into domicile_details(id,are_you_domicile_of_maharashtra,do_you_have_domicile_certificate,relationship_type, domicile_certificate_no, applicant_name,
             issuing_authority, issuing_date,domicile_document)values({},'{}','{}','{}',{},'{}','{}','{}','{}')""".format(id,Are_you_Domicile_of_Maharashtra,Do_you_have_Domicile_Certificate, Relationship_Type ,Domicile_Certificate_No, Applicant_Name, Issuing_Authority, domicile_Issuing_Date,Domicile_Certificate)

            # cluster = Cluster()
            # session = cluster.connect("university")
            cloud_config = {
                'secure_connect_bundle': 'D:\secure-connect-university-db.zip'
            }
            auth_provider = PlainTextAuthProvider('ROZWCgfeXRDSbMRLywDItvbn',
                                                  '.xO3__vFQMdj3vv18b_h4cmoBBeB4ZJn8j7OoEmhu0_n8344QmmvdnDva.7ZA3wvFvoILmwyjWa3ZPRC.AaQd4ptwxklaroLGO_+17XHofD+dGkA35Il-RebSCRZZS6R')
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            self.session = cluster.connect('university')
            result = self.session.execute(query)
            print(query)
            return result
        except Exception as e:
            return e

    def insert_address_details(self,id,paddress,pstate,pdistrict,ptaluka,pvillage,ppincode,caddress,cstate,cdistrict,ctaluka,cvillage,cpincode):
        try:
            query1 = """insert into permanent_address_details(id, address,state,district,taluka,village,
            pincode)values({},'{}','{}','{}','{}','{}',{})""".format(id, paddress,pstate,pdistrict,ptaluka,pvillage,ppincode)

            query2 = """insert into correspondence_address_details(id, address,state,district,taluka,village,
                        pincode)values({},'{}','{}','{}','{}','{}',{})""".format(id,caddress,cstate,cdistrict,ctaluka,cvillage,cpincode)

            # cluster = Cluster()
            # session = cluster.connect("university")
            cloud_config = {
                'secure_connect_bundle': 'D:\secure-connect-university-db.zip'
            }
            auth_provider = PlainTextAuthProvider('ROZWCgfeXRDSbMRLywDItvbn',
                                                  '.xO3__vFQMdj3vv18b_h4cmoBBeB4ZJn8j7OoEmhu0_n8344QmmvdnDva.7ZA3wvFvoILmwyjWa3ZPRC.AaQd4ptwxklaroLGO_+17XHofD+dGkA35Il-RebSCRZZS6R')
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)

            self.session = cluster.connect('university')
            result1 = self.session.execute(query1)
            result2 = self.session.execute(query2)
            print(query)
            return result1, result2
        except Exception as e:
            return e

    def insert_past_edu_details(self,id,qualification_level,stream,completed,institute_state,institute_district,institute_taluka,college_school_name,course,
                                             board_university,mode,Admission_Year,passing_year,result,percentage,Attempts,Upload_Marksheet):
        try:
            query = """insert into past_qualification_details(id, qualification_level,stream,completed,institute_state, institute_district,
             institute_taluka,school_college_name,board_university_name,mode,admission_year,passing_year,result,percentage,attempts,
             marksheet_doc)values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}',{},
             '{}')""".format(id, qualification_level,stream,completed,institute_state,institute_district,institute_taluka,college_school_name,course,
                            board_university,mode,Admission_Year,passing_year,result,percentage,Attempts,Upload_Marksheet)

            print(query)
            result = self.session.execute(query)

            return result
        except Exception as e:
            return e

    def insert_applying_details(self,id,apply_course_name, apply_Admission_Type, apply_cet_percentage, apply_cap_id,apply_admission_through,apply_gap_year,apply_mode):
        try:
            query = """insert into applying_details(id, course_name, admission_type, cet_percentage, cap_id_no,
             reserved_category, gap_year,mode)values({},'{}','{}',{},{},'{}',{},'{}')""".format(id,apply_course_name, apply_Admission_Type, apply_cet_percentage,
                                                                                                apply_cap_id,apply_admission_through,apply_gap_year,apply_mode)

            cluster = Cluster()
            session = cluster.connect('university')
            result = session.execute(query)
            return result
        except Exception as e:
            return e