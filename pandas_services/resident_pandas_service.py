import pandas as pd
from database import engine


def get_all_resdidents(engine):
    df = pd.read_sql("select * from residents", engine)
    total_number_of_registered_residents = len(df)
    return f"The Total Number Of Registered Residents: {total_number_of_registered_residents}"

def get_all_active_residents(engine):
    df = pd.read_sql("select * from residents where is_active = True", engine)
    total_number_of_active_registered_residents = len(df)
    return f"The Total Number of active Registered Residents: {total_number_of_active_registered_residents}"

def get_the_gender_count(engine):
    df = pd.read_sql("select * from residents where is_active = True", engine)
    gender_count = df.groupby("gender", as_index=False).size()
    return gender_count.to_dict(orient="records")

def get_residents_by_dob(engine):
    df = pd.read_sql("select * from residents where is_active = True", engine)
    df["dob"] = pd.to_datetime(df["dob"])
    df["dob_months"] = df["dob"].dt.month_name
    df["year"] = df["dob"].dt.year
    df_dob_grouped = df[["first_name","last_name","dob", "dob_months","year"]]
    return df_dob_grouped.to_dict(orient="records")

def how_long_residents(engine):
    df = pd.read_sql("select * from residents where is_active = True", engine)
    df["created_at"] = pd.to_datetime(df["created_at"])
    today = pd.Timestamp.today().normalize()
    df["days_since_admission"] = (today - df["created_at"]).dt.day
    df["months_since_admission"] = ((today - df["created_at"]) / 30.4375).astype(int)
    accommodation_period =  df.groupby("first_name", as_index=False)["time_since_admission"].max()
    return accommodation_period.to_dict(orient="records")
