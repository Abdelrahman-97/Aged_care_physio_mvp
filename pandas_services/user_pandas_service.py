import pandas as pd
from database import engine



def get_all_users(engine):
    df = pd.read_sql("select * from users", engine)
    total_number_of_registered_users = len(df)
    
    return f" THe total number of Registered Physios: {total_number_of_registered_users}"

def get_active_users(engine):
    df = pd.read_sql("select * from users where is_active = True", engine)
    total_number_of_active_registerd_users = len(df)
    return f" The number of Active Registered Physios: {total_number_of_active_registerd_users}"


def physio_roles(engine):
    df = pd.read_sql("select * from users where is_active = True", engine)
    physio_roles_count = df["role"].value_counts()
    return physio_roles_count.to_dict(orient="records")

def started_work_since(engine):
    df = pd.read_sql("select * from users where is_active =True", engine)
    df["created_at"] = pd.to_datetime(df["created_at"])
    worked_since = df.groupby("name", as_index=False)["created_at"].min()
    today = pd.Timestamp.today().normalize()
    delta_time = (today - worked_since["created_at"]).dt.days
    worked_since["months_since_wroking"] = (delta_time / 30.4375).astype(int)
    return worked_since.to_dict(orient="records")