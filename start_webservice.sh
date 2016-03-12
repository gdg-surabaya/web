cd /root/web/gdg_webservice/
gunicorn app:app -b 0.0.0.0:8000 &