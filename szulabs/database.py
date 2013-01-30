

def init_database(db):
	db.create_all()


def tear_database(db):
	db.drop_all()
