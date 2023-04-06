from fastapi import FastAPI
from fastapi.responses import JSONResponse
from google.cloud import bigquery

from app.bq.queries.queries import QUERIES
from app.bq.queryExecutor import QueryExecutor

app = FastAPI()
client = bigquery.Client()
queries = QUERIES()
queryExecutor = QueryExecutor()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/total")
async def total_users():
    """
    Returns a record with the total number of rows

    Example response:
    {
        "data": [
            {
                "total_count": 56139
            }
        ]
    }
    """
    rows = await queryExecutor.get_total(client, queries.total_count)
    records = [dict(row) for row in rows]
    data = {"data": records}

    return data


@app.get("/person-count/{last_n_date}")
async def person_count(last_n_date: int):
    """
    Returns a record with the count of persons
    breakdown for the last N dates

    Example response:
    {
        "data": [
            {
                "dates": 2010-10-31,
                "person_count": 56139
            }
        ]
    }
    """

    if last_n_date < 0:
        return JSONResponse(
            status_code=501,  # possibly 422
            content={"message": "Parameter must a positive integer or 0"},
        )

    query = queries.last_n_date()
    rows = await queryExecutor.get_last_n_date(client, query, last_n_date)
    records = [dict(row) for row in rows]
    data = {"data": records}

    return data
