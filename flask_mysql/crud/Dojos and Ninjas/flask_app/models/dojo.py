from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def show_dojo(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL("dojos_and_ninjas").query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_dojos_ninjas(cls):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id"
        all_dojos_ninjas = connectToMySQL("dojos_and_ninjas").query_db(query)
        dojos_ninjas = []

        for dojosninjas in all_dojos_ninjas:
            dojo_instance = Dojo(dojosninjas)

            ninja_data = {
                "id" : dojosninjas["ninjas.id"],
                "first_name" : dojosninjas["first_name"],
                "last_name" : dojosninjas["last_name"],
                "age" : dojosninjas["age"],
                "dojo_id" : dojosninjas["dojo_id"],
                "created_at" : dojosninjas["created_at"],
                "updated_at" : dojosninjas["updated_at"],
            }
            dojo_instance.ninja = ninja.Ninja(ninja_data)

            dojos_ninjas.append(dojo_instance)
        
        return dojos_ninjas

    @classmethod
    def get_dojo_ninjas(cls,data):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE ninjas.dojo_id = %(id)s"
        all_dojo_ninjas = connectToMySQL("dojos_and_ninjas").query_db(query,data)
        dojo = Dojo(all_dojo_ninjas[0])

        for dojosninjas in all_dojo_ninjas:
            ninja_data = {
                "id" : dojosninjas["ninjas.id"],
                "first_name" : dojosninjas["first_name"],
                "last_name" : dojosninjas["last_name"],
                "age" : dojosninjas["age"],
                "dojo_id" : dojosninjas["dojo_id"],
                "created_at" : dojosninjas["created_at"],
                "updated_at" : dojosninjas["updated_at"]
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))

        return dojo

    @classmethod
    def create_dojo(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        return connectToMySQL("dojos_and_ninjas").query_db(query,data)

    @classmethod
    def create_ninja(cls,data):
        query = "INSERT INTO ninjas (dojo_id,first_name,last_name,age) VALUES (%(dojo_id)s,%(first_name)s,%(last_name)s,%(age)s)"
        return connectToMySQL("dojos_and_ninjas").query_db(query,data)






