# Flask with pyalchemy

A simple rest-api using flask and pyalchemy.

## Running with dev-containers

This project uses vs-code with dev-containers, install the extension. To get started open command pallet (`Ctrl + Shift + p`) and
choose `Dev Containers: Rebuild and Reopen in Container`.

Inside the dev-container run `flask --app app run` to start the server.

## Requests

### Get employees

List all employees:

```sh
curl http://localhost:5000/api/v1/employees
```

Get a single employee:

```sh
curl http://localhost:5000/api/v1/employees/1
```

### Create employee

```sh
curl -H "Content-Type: application/json" -d '{"username":"foo","email":"foo@bar.com"}' http://localhost:5000/api/v1/employees
```

### Delete employee

```sh
curl --request "DELETE" http://localhost:5000/api/v1/employees/2
```
