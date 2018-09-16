from pymongo import MongoClient


class DbWorker:
    def __init__(self):
        client = MongoClient()
        self.db = client.test_database
        self.applications = self.db.applications

    def add(self, app):
        if self.applications.find_one({'id': app.get('id')}):
            self.applications.update({'id': app.get('id')}, app)
        else:
            self.applications.save(app)

    def get_item(self, id):
        return self.applications.find_one({'id': id})

    def list(self):
        return self.applications.find()
