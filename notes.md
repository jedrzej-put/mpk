py -m venv ./venv
pip freeze > requirements.txt
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt

uvicorn src.main:app --reload

{
"lat": "51.13382609",
"lon": "16.95673511",
"count": 2
}
