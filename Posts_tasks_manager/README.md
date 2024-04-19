```mermaid
sequenceDiagram
    participant t as terminal
    participant app as Main program (in app.py)
    participant ar as AlbumRepository class <br /> (in lib/album_repository.py)
    participant db_conn as DatabaseConnection class in (in lib/database_connection.py)
    participant db as Postgres database

    Note left of t: Flow of time <br />⬇ <br /> ⬇ <br /> ⬇ 

    t->>app: Runs `python app.py`
    app->>db_conn: Opens connection to database by calling "connect" method on DatabaseConnection
    db_conn->>db_conn: Opens database connection using PG and stores the connection
    app->>ar: Calls "all" method on AlbumRepository
    ar->>db_conn: Sends SQL query by calling 'execute' method on DataConnection
    db_conn->>db: Sends query to database via the open database connection
    db->>db_conn: Returns a list of dictionaries, one for each row of the album table

    db_conn->>ar: Returns an list of dictionaries, one for each row of the album table
    loop 
        ar->>ar: Loops through the list and creates a Album object for every row
    end
    ar->>app: Returns a list of Album objects
    app->>t: Prints list of app.py to terminal
```

<!-- 
A sequence diagram for a database-backed program helps us to explain and communicate two important things:

The interaction between the different components of the program and the database
The order in which the different parts interact together -->