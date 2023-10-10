from sqlalchemy import create_engine, MetaData
#alexchangrojas123#

engine = create_engine("mysql+pymysql://root:alexchangrojas123#@localhost:3306/fastapi_pvvc2")

meta = MetaData()

conn = engine.connect()

