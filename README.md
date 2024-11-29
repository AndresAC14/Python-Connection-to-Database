# conn

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Run PostgreSQL

```sh
docker run --name some-postgres -e POSTGRES_DB=recipes -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres
```