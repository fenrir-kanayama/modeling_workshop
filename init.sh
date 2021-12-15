# データ削除
rm -rf example_app/company/__pycache__
rm -rf example_app/company/migrations
rm -rf example_app/example_app/__pycache__
rm -f example_app/db.sqlite3

# データベース作成
python example_app/manage.py makemigrations company
python example_app/manage.py migrate

# create superuser
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python example_app/manage.py shell

python example_app/manage.py runserver 0.0.0.0:8000