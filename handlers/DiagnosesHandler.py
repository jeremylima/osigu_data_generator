from infrastructure.ElasticSearchClient import ElasticSearchClient
from handlers.DatabaseHandler import DatabaseHandler
from config.Sequences import Sequences

elasticSearchClient = ElasticSearchClient
databaseHandler = DatabaseHandler
sequences = Sequences


class DiagnosesHandler:
    def __init__(self):
        self.diagnosis_sequence = sequences.DIAGNOSES
        self.diagnoses_statement = ""
        self.diagnosis_code = ""
        self.diagnosis_name = ""

    def populate_diagnoses_in_database(self):

        statement = "insert into public.diagnoses (id, code, name, created_by, enabled, updated_by) values " \
                    "({id}, '{code}', '{name}', 'test', true, 'test');" \
            .format(id=self.diagnosis_sequence, code=self.diagnosis_code, name=self.diagnosis_name)

        self.diagnoses_statement += statement

    def populate_diagnoses_in_elasticsearch(self):
        body = {
            "id": self.diagnosis_sequence,
            "code": self.diagnosis_code,
            "name": self.diagnosis_name
        }

        elasticSearchClient.post(index='diagnoses', doc_id=self.diagnosis_sequence, body=body)

    def populate(self):
        for i in range(10):
            self.diagnosis_code = "CODE_" + str(self.diagnosis_sequence)
            self.diagnosis_name = "DIAGNOSES " + str(self.diagnosis_sequence) + " QA TESTING"
            self.populate_diagnoses_in_database()
            self.populate_diagnoses_in_elasticsearch()
            self.diagnosis_sequence += 1

        databaseHandler.execute_non_query(self.diagnoses_statement)

        print('Diagnoses populated successfully')
