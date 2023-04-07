class QUERIES:
    total_count = """
    SELECT 
        count(*) as total_count 
    FROM `bigquery-public-data.cms_synthetic_patient_data_omop.procedure_occurrence`;
    """

    def last_n_date(self):
        last_n_date = """
        WITH cte AS (
            SELECT
                max(procedure_dat) as max_date 
            FROM `bigquery-public-data.cms_synthetic_patient_data_omop.procedure_occurrence`
        )
        SELECT 
            procedure_dat as dates,
            COUNT(person_id) as person_count
        FROM `bigquery-public-data.cms_synthetic_patient_data_omop.procedure_occurrence`
        WHERE procedure_dat > (SELECT max_date - @n_date FROM cte)
        GROUP BY dates
        ORDER BY dates DESC;        
        """

        return last_n_date
