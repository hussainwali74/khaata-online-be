1. create an app
    - first dockercompose sh into the service
    - create product app using django command below
2. add to admin/settings.py/INSTALLED_APP, 
    'rest-framework'
    'corsheaders'
    'products'
3. add cors middleware to admin/settings.py/MIDDLEWARE
    'corsheaders.middleware.CorsMiddleware'
4. add new constant to admin/settings.py end
    'CORS_ORIGIN_ALLOW_ALL=True'
5. connect to sql, in admin/settings.py/DATABASES
    default->ENGINE-> sqlite to mysql
    default->ENGINE-> NAME  to 'admin'
    default->ENGINE-> USER  to 'root'
    default->ENGINE-> PASSWORD  to 'root'
    default->ENGINE-> HOST  to 'db'
    default->ENGINE-> PORT  to '3306'


------ 
# docker compose exec bash in backend container service:
`docker-compose exec backend sh`
# django commands
create products 
`python manage.py startapp products`
