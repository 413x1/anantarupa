# Test Anantarupa

## Database installation
### requirement
- Database mariadb or mysql

to install database you should have ready empty database. then run all `sql command` in `answers_database_schema_modified.sql` inside your empty database or simply import the sql file.


## Project Installation from github
### requirement
- python3.6 or higher

```bash
# 1. Clone the Repository
git clone https://github.com/413x1/anantarupa.git

# 2. Navigate to the Project Directory
cd anantarupa

# 3. Create a Virtual Environment
python -m venv venv

# On Windows, use:
# python -m venv venv

# 4. Activate the Virtual Environment
# On Linux/Mac:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate

# 5. Install Dependencies
pip install -r requirements.txt

# 6. copy .env.exaple and rename to .env
cp .env.example .env

# 7. configure database
# modified database configuration variable inside the .env file such as DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

# 6. run server
python manage.py runserver

# 7. visit localhost:8000
```
