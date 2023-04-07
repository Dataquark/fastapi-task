# API for job application task

The Swagger Docs is here: [LINK](http://46.101.199.96:8008/docs)

## API Info

**GET /total**

- returns a record with the total number of rows from the database
- example response: { "data": [ { "total_count": 56139 } ] }

**GET /person-count/{last_n_date}**

- accepts positive integer or zero
- returns a record with the count of persons breakdown for the last N dates
- example response: { "data": [ { "dates": 2010-10-31, "person_count": 56139 } ] }
