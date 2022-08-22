
import harperdb
import os
from dotenv import load_dotenv

load_dotenv()

def create_db():
    db = harperdb.HarperDB(
        url=os.getenv("HARPER_URL"),
        username=os.getenv("HARPER_USERNAME"),
        password=os.getenv("HARPER_PASSWORD")
    )
    return db