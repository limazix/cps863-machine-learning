FROM elyra/elyra

COPY requirements.txt .

RUN pip install -r requirements.txt