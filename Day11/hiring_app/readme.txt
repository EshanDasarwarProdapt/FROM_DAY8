To create a virtual environment
python -m venv venv

to activate the virtual environment
venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload