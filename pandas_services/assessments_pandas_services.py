from database import engine
import pandas as pd

# pandas Services for physio assessments
def get_physio_assessments_by_physio(engine):
    df = pd.read_sql("select * from physio_assessments", engine)
    count_per_physio = df.groupby("physio_id", as_index=False).size()
    return count_per_physio.to_dict(orient="records")

def get_active_physio_assessments(engine):
    df = pd.read_sql("select * from physio_assessments where is_active = True", engine)
    physio_ax_by_resident_id = df.groupby("resident_id", as_index=False)["updated_at"].max()
    return physio_ax_by_resident_id.to_dict(orient="records")

def get_overdue_physio_assessments(engine):
    df = pd.read_sql("select * from physio_assessments where is_active = True", engine)
    df["updated_at"] = pd.to_datetime(df["updated_at"])
    today = pd.Timestamp.today().normalize()
    df["days_since_last_update"] = (today - df["updated_at"]).dt.day
    df["the_months_since_last_update"] = (df["days_since_last_update"] / 30.3475).astype(int)
    df["is_overdue"] = df["the_months_since_last_update"] >= 6
    overdue = df[df["is_overdue"]]
    return overdue.to_dict(orient="records")

#pandas Services for mobility assessments
def get_mobility_assessments_by_physio(engine):
    df = pd.read_sql("select * from mobility_assessments", engine)
    count_per_physio = df.groupby("physio_id", as_index=False).size()
    return count_per_physio.to_dict(orient="records")

def get_active_mobility_assessments(engine):
    df = pd.read_sql("select * from mobility_assessments where is_active = True", engine)
    physio_ax_by_resident_id = df.groupby("resident_id", as_index=False)["updated_at"].max()
    return physio_ax_by_resident_id.to_dict(orient="records")


def get_overdue_mobility_assessments(engine):
    df = pd.read_sql("select * from mobility_assessments where is_active = True", engine)
    df["updated_at"] = pd.to_datetime(df["updated_at"])
    today = pd.Timestamp.today().normalize()
    df["days_since_last_update"] = (today - df["updated_at"]).dt.day
    df["the_months_since_last_update"] = (df["days_since_last_update"] / 30.3475).astype(int)
    df["is_overdue"] = df["the_months_since_last_update"] >= 6
    overdue = df[df["is_overdue"]]
    return overdue.to_dict(orient="records")

