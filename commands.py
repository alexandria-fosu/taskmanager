import db

def save_task(task):
    #save task to database
    db.tasks.insert_one(task)
    #return response
    return True

def delete_task(id):
    #dellete task from database
    db.tasks.delete_one({"_id":id})
    #return response
    return True

def get_tasks():
    #get all task from data base
    all_task = db.tasks.find()
    #return response
    return all_task

def update_task( task, update):
    #update task in database
    #return response
    return True

