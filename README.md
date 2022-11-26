# mpk-api

## Clone repository

```
git clone https://github.com/jedrzej-smok/mpk-api.git
```

## Create virtual environment, activate it and install required packages

```
cd nbp-api
python -m venv ./venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run application

```
uvicorn src.main:app --reload
```

## Open

```
http://127.0.0.1:8000/cities
http://127.0.0.1:8000/routes
```

## Test code

```
pytest
```
