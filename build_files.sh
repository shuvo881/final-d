echo "BUILD START"
python3.9 -m pip install -r requirements.txt
python manager.py syncdb
python3.9 manage.py collectstatic
echo "END BUILD"