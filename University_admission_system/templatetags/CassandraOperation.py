from cassandra import cluster, query
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
class CassandraManagement:
    def __init__(self):
        try:
        #     cloud_config= {
        #             'secure_connect_bundle': 'E:\INeuron\secure-connect-university-db.zip'
        #     }
        #     auth_provider = PlainTextAuthProvider('ROZWCgfeXRDSbMRLywDItvbn', '.xO3__vFQMdj3vv18b_h4cmoBBeB4ZJn8j7OoEmhu0_n8344QmmvdnDva.7ZA3wvFvoILmwyjWa3ZPRC.AaQd4ptwxklaroLGO_+17XHofD+dGkA35Il-RebSCRZZS6R')
        #     cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            self.session = Cluster.connect('university')

            self.session.execute("select release_version from system.local").one()
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
            cluster = Cluster()
            session = cluster.connect()
            query = "insert into university.faculty_info(id,fullname,email,password)values({},'{}','{}','{}')".format(id,fullname,email,password)
            print(query)
            new = session.execute(query)
            
            return new
        except Exception as e:
            return e
    
    def student_registration(self,id,fullname,email,password):
        try:
            cluster = Cluster()
            session = cluster.connect()
            query = "insert into university.student_info(id,fullname,email,password)values({},'{}','{}','{}')".format(id,fullname,email,password)
            print(query)
            new = session.execute(query)
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
            cluster = Cluster()
            session = cluster.connect("university")
            query = "select * from faculty_info where email='{}' and password='{}' ALLOW FILTERING ;".format(email,password)
            result = session.execute(query)
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