# Bar

## ✨ Tech stack

- 🌍 Docker
- 📦 Docker-compose

## 📦 Install

0. clone the project
1. enter project/directory
    ```
    cd project directory
    ```
2. Build images in docker compose:
    ```
    docker-compose build
    ```
3. Run images:
    ```
    docker-compose up
    ```

4. Migrate DB tables, create super user and load initial data:
      - Enter api container:
        ```
        docker exec -it test-app /bin/bash
        ```
      - Migrarate DB tables:
          ```
          python manage.py migrate
          ```
      - Create a super user:
          ```
          python manage.py createsuperuser
          ```
      - Load initial data for user and bar models
          ```
          python manage.py loaddata initial_data.json

          ```
          that will add some Bar rows in database and
          will create test user with:

            username: user1
            password: P@@ssword@@

## Routes

Server starting at http://0.0.0.0:8000/

* /api/admin/
  * django admin panel
  * login with superuser username and password
* /api/accounts/registration/
  * accepts 'POST' requests
  * body should contain username and password
* /api/login/
  * accepts 'POST' requests
  * body should contain existing user username and password
  * return token
* /api/bars/
  * required token authentication
  * accepts 'GET', 'POST' requests
  * accepts 'rating_gte' query parameter for filtering bars,
        returning only bars that have rating equal or greater than the parameter
  * returns a list of bars in the form of: { id, name, rating }
* /api/bars/{id}
  * required token authentication
  * accepts 'GET', 'DELETE'
  * gets or deletes a single bar by id
