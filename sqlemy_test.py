from sqlalchemy import create_engine,Column ,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
engine = create_engine(f'''sqlite:///.//sqlite.db''',echo=True)
class Person(Base):
	__tablename__ = "person"

	id = Column('id',Integer,primary_key=True)
	username = Column('username',String,unique=True)


Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
person = "person"
# 223.__table__.drop(engine)
session = Session()
rs = session.execute(f"DROP TABLE IF EXISTS {person}")
# rs.fetchone()
# print(rs)
# for m in rs:
# 	print(rs.username)
# session = Session()
# s = session.query(Person).filter(Person.username == "alice1")
# t = [x for x in session.query(Person).filter(Person.username == "alice1").limit(1)]
# print(t[0].username)
# # for m in s:
# # 	x = m
# # 	print(m.username)
# # user = Person()
# # user.id = 1
# # user.username = "alice1"
# # session.add(user)
# session.delete(t[0])
session.commit()
session.close()