from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import meta, engine


users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("email", String(255)),
    Column("password", String(255)),
    Column('has_visual_access', Boolean, default=True),
    Column('has_instrument_access', Boolean, default=True),
    Column('has_app_access', Boolean, default=True),
)



meta.create_all(engine)
