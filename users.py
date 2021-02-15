import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()


class User(Base):

    __tablename__ = 'user'
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.Float)

def connect_db():

    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()

def request_data():

    print("Привет! Я запешу твои данные!")
    first_name = input("Твое имя: ")
    last_name = input("Твоя фамилия: ")
    gender = input("Твой пол? (варианты: Male, Female) ")
    email = input("Адрес электронной почты: ")
    birthdate = input("Дата рождения в формате ГГГГ-ММ-ДД. Например, 1987-05-05: ")
    height = input("Твой рост в метрах? (Для разделения целой и десятичной части используй точку): ")
    user = User(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=height
    )
    return user

def main():

    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    print("Теперь ты есть в базе!")

if __name__ == "__main__":
    main()