from google.cloud import bigquery


class QueryExecutor:
    async def get_total(self, client, query):
        query_job = client.query(query)
        rows = query_job.result()

        return rows

    async def get_last_n_date(self, client, query, n_date):
        job_config = bigquery.QueryJobConfig(
            query_parameters=[bigquery.ScalarQueryParameter("n_date", "INT64", n_date)]
        )
        query_job = client.query(query, job_config=job_config)
        rows = query_job.result()

        return rows
