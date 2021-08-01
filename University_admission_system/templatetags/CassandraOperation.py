from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
class CassandraManagement:
    def __init__(self):
        try:
            cloud_config= {
                    'secure_connect_bundle': 'E:\INeuron\secure-connect-university-db.zip'
            }
            auth_provider = PlainTextAuthProvider('ROZWCgfeXRDSbMRLywDItvbn', '.xO3__vFQMdj3vv18b_h4cmoBBeB4ZJn8j7OoEmhu0_n8344QmmvdnDva.7ZA3wvFvoILmwyjWa3ZPRC.AaQd4ptwxklaroLGO_+17XHofD+dGkA35Il-RebSCRZZS6R')
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            self.session = cluster.connect()

            self.session.execute("select release_version from system.local").one()
        except Exception as e:
            return e
    def createKeyspace(self,KeyspaceName):
        try:
            self.session.execute("CREATE KEYSPACE javatpoint WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3}; ")
        except Exception as e:
            pass