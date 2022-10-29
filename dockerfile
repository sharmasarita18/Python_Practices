FROM python:3.8-slim-buster
Run mkdir PYTHON_Practices && cd PYTHON_Practices
RUN pip install flask
ADD /app.py /PYTHON_Practices
CMD flask run
