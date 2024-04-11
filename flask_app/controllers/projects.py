"""
This is my controller.
"""

from flask_app import app, render_template



#! CREATE
@app.get("/projects/new")
def new_project():
    """route that displays a new project form"""
    pass

@app.post("/projects/create")
def add_project():
    """post route to handle new project"""
    pass


#! READ ALL
@app.get("/")
@app.get("/projects")
def projects():
    """Main route"""
    return render_template("index.html")

#! READ ONE
@app.get("/projects/<int:id>")
def show_project(id):
    """show one project by id"""
    pass

#! UPDATE
@app.get("/projects/edit/<int:id>")
def edit_project(id):
    """display the edit form"""
    pass

@app.post("/projects/update")
def update_project():
    """post route to update project record"""
    pass



#! DELETE

@app.get("/projects/delete/<int:id>")
def destroy_project(id):
    """delete project by id"""
    pass