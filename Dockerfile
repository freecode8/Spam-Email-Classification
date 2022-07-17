FROM python:3.7

cmd mkdir /spam

copy . /spam

WORKDIR /spam

EXPOSE 8501


RUN pip3 install -r requirements.txt



CMD streamlit run spam.py
