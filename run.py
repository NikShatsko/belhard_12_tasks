import datetime

from db import session_scope
from db import tables

with session_scope() as session:
    person = tables.Person(
        surname="some_surname",
        name="some_name",
        birth_date=datetime.datetime.now()
    )
    session.add(person)
    session.commit()

    user = tables.User(
        login="some_login",
        password="some_password",
        user_type_id="ADMIN",
        person_id=1
    )
