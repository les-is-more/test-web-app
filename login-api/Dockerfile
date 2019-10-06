FROM python:3-onbuild
ADD /models /models
COPY . /usr/src/login-api
CMD ["python","config.py"]
RUN pip install -r requirements.txt
EXPOSE 5000