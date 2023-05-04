FROM python:3.8

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "chatBot.py"]

# docker build -t chatbot .
