FROM python:3.9

ENV PYTHONPATH="${PYTHONPATH}:."

WORKDIR /code

COPY . /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["python", "/code/src/api.py"]
