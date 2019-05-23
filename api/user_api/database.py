from sqlalchemy import create_engine

e = create_engine('sqlite:///user.db')

class Users_data():
    def all_data(self, id, first_name, last_name, gender, age, email):
        # Connect to databse
        conn = e.connect()
        # Perform query and return JSON data
        if id:
            query = conn.execute("select * from users where id='{}' order by id".format(id))
        elif first_name:
            query = conn.execute("select * from users where first_name=='{}' order by id".format(first_name))
        elif last_name:
            query = conn.execute("select * from users where last_name='{}' order by id".format(last_name))
        elif gender:
            query = conn.execute("select * from users where gender == '{}' order by id".format(gender))
        elif age:
            query = conn.execute("select * from users where age='{}' order by id".format(age))
        elif email:
            query = conn.execute("select * from users where email== '{}' order by id".format(email))
        else:
            query = conn.execute("select * from users order by id")
        result = {
            'data': [
                {
                    'identify': row[0],
                    'first_name': row[1],
                    'last_name': row[2],
                    'email': row[3],
                    'gender': row[4],
                    'age': row[5]
                }
                for row in query.cursor.fetchall()
            ]
        }
        return result


    def delete_data(self, id):
        conn = e.connect()
        conn.execute("DELETE FROM users WHERE id=?", (id,))
        result = {'data': [
                {
                    'identify': row[0],
                    'first_name': row[1],
                    'last_name': row[2],
                    'email': row[3],
                    'gender': row[4],
                    'age': row[5]
                }
                for row in conn.execute("select * from users").fetchall()
            ]
        }
        return result


    def insert_data(self, id, first_name, last_name, gender, age, email):
        conn = e.connect()
        conn.execute("INSERT INTO users values (?,?,?,?,?,?)", (id, first_name, last_name,
                                                                         email, gender, age))
        result = {'data': [
            {
                'identify': row[0],
                'first_name': row[1],
                'last_name': row[2],
                'email': row[3],
                'gender': row[4],
                'age': row[5]
            }
            for row in conn.execute("select * from users ORDER by id").fetchall()
        ]
        }
        return result


    def update_data(self, id, first_name, last_name, gender, age, email):
        conn = e.connect()
        conn.execute("UPDATE users SET first_name=?, last_name=?, "
                     "email=?, gender=?, age=? where id = ?", (first_name, last_name, email, gender, age, id))

        result = {'data': [
            {
                'identify': row[0],
                'first_name': row[1],
                'last_name': row[2],
                'email': row[3],
                'gender': row[4],
                'age': row[5]
            }
            for row in conn.execute("select * from users ORDER by id").fetchall()
        ]
        }
        return result





