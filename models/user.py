from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

users = Table("test_users", meta,
            Column("id", Integer(), primary_key=True),
            Column("name", String(255)),
            Column("email", String(255)),
            Column("password", String(255))
        )


""" user = Table("user", meta,
            Column("id", Integer, primary_key=True),
            Column("name", String),
            Column("user", String),    
            Column("password", String),
            Column("id", Integer),
            Column("email", String),
            Column("status", Integer),
        )

locatarios = Table("cat_locatario", meta,
            Column("cat_locatario_id", Integer, primary_key=True),
            Column("cat_local_id", Integer),
            Column("cat_puesto_id", Integer),
            Column("nombre_locatario", String(64)),
            Column("apellidos_locatario", String(128))
) """

meta.create_all(engine)