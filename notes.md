py -m venv ./venv
pip freeze > requirements.txt
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt

uvicorn src.main:app --reload
