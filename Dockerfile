FROM python:3.9

ADD bot.py .

RUN pip install requests

CMD [ "python", "./bot.py" ]