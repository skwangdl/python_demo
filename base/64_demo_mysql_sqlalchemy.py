from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
DBSession = sessionmaker(bind=engine)
session = DBSession()
new_user = User(id='5', name='kepler')
session.add(new_user)
session.commit()
session.close()

# 创建Query查询， filter是where条件， 最后调用one()返回唯一行，调用all()返回所有行
user = session.query(User).filter(User.id =='5').one()
print(user)
session.close()