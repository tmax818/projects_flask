"""
This is the model
"""

DATABASE = "projects"

class Project:
    pass

    def __init__(self) -> None:
        pass

    #! CREATE
    @classmethod
    def save(cls, data):
        """save an instance of a project to the DB"""
        pass

    #! READ ALL
    @classmethod
    def get_all(cls):
        """retrieve all projects from DB"""
        pass

    #! READ ONE
    @classmethod
    def get_one(cls, id):
        """retrieve one project by the project id"""
        pass


    #! UPDATE
    @classmethod
    def update(cls, data):
        """update a project record in DB"""
        pass

    #! DELETE
    @classmethod
    def destroy(cls, data):
        """remove a project from the database"""
        pass