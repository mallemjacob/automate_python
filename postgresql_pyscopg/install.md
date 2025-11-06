pip install "psycopg[binary]"

"host=localhost dbname=postgres user=postgres password=mysecretpassword port=5432"

create new group role
General - python_application
Definition - password
Privileges - Can login? Yes

Permission denied:
1.Go to database that we're accessing
2.Properties
3.Default Privileges --> select user (under Grantee)
                     --> grant queries (under Privileges)

4.Schemas --> Tables (table we created)  --> security --> select Grantee and Privileges.

# Docker
----------

docker run --name my-postgres-new -p 5432:5432 \
-e POSTGRES_PASSWORD=mysecretpassword \
-d postgres

docker exec -it my-postgres-new \               
psql -h localhost -U postgres postgres
