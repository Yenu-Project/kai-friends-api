Project Setup
---

### Create & Activate Virtual Environment

Please make sure you are using python 3.8.

```
$ python3 -m venv env
$ source env/bin/activate
```

### Install Requirements

```
$ pip install poetry
$ poetry install
```

### Environment Configuration

Create a `.env` file based on `.env.example`, and fill in your database credentials.

Then, call `source .env`.

### Create and Migrate Database

```
$ make init
```

### Run server

```
$ make run
```