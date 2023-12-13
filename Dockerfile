FROM python:3.8
WORKDIR /usr/src/app
RUN mkdir /output
COPY requirements.txt plot.py ./
RUN pip install -r requirements.txt
CMD python plot.py
