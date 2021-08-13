import datetime
from db import session_scope
from db import tables

with session_scope() as session:

    # Вставка

    person = tables.Person(
        surname="some_surname2",
        name="some_name2",
        birth_date=datetime.datetime.now()
    )
    session.add(person)
    session.commit()

    # Удаление

    some_person = session.query(tables.Person).filter_by(id=9).one()
    print(some_person)
    session.delete(some_person)
    session.commit()

    # Обновление

    new_user_id = session.query(tables.UserType).filter(tables.UserType.id == "ADMIN").one()
    new_user_id.name = "Администратор"
    session.commit()

    # Сортировка
    result = (
        session.query(tables.User)
        .join(tables.UserType, tables.User.user_type_id == tables.UserType.id)
        .filter(tables.UserType.name == "User").all()
    )

    result2 = session.query(tables.Genre).order_by(tables.Genre.id.desc()).all()

    result3 = (
        session.query(tables.Person)
        .join(tables.Film, tables.Person.id == tables.Film.director_id)
        .order_by(tables.Film.release_date.asc()).all()
    )

    print(result)
    print(result2)
    print(result3)
