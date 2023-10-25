
# Python-Jenkins


This project is a simple REST API built with FastAPI and Docker, designed for testing and learning purposes. It demonstrates how to create a Python-based web service using FastAPI, containerize it with Docker for easy deployment and scalability, and integrate it into Jenkins for continuous integration. You can use this project as a hands-on example to explore FastAPI, Docker, and Jenkins for your development and automation needs.


## Authors

- [@Leonel Gareis](https://www.github.com/gareisdev)



## Run Locally

Clone the project

```bash
  git clone https://github.com/gareisdev/python-jenkins
```

Go to the project directory

```bash
  cd python-jenkins
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  uvicorn src.main:app --port 8000
```

Or you can use Docker

```bash
  docker-compose up api
```

## Running Tests

To run tests, run the following command

```bash
  pip install -r requirements.txt
  pytest tests/test.py
```

