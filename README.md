# Vyaguta Leave Visualization

## Description
It is a sample project on creating a dashboard using the Streamlit and Postgresql.

## Installation

1. Flask and Postgresql Setup
- Create a `.env` file using `.env.example` file

Inside app folder:
```
docker compose up
```

- Locally

```
pip install -r requirements.txt
python main.py
```

This will create a flask server and postgres database

2. ETL

Inside etl folder
```
docker compose up
```

- Locally

```
pip install -r requirements.txt
python main.py
```

3. Streamlit

- Inside streamlit folder 

```
docker build -t my-streamlit-app .
docker run -p 8501:8501 my-streamlit-app
```
- Locally

```
pip install -r requirements.txt
streamlit run Home.py --server.runOnSave True
```

