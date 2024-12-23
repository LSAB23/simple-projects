import sqlite3

'''
A todo cli app that can add, edit, mark as done and delete programs 
'''


def create_connection() -> tuple:
    db_connection = sqlite3.connect('db.sqlite3')
    cursor = db_connection.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Todo(id  INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT, status boolean DEFAULT 0);
        '''
    )
    return cursor, db_connection


def write_todo(*args: object, text: str) -> str:
    cursor, connection = args
    cursor.execute('''
        INSERT INTO Todo(content) values(?);
        ''',
                   (str(text),)
                   )
    connection.commit()
    return f'Todo has been added'


def edit_todo(id: int, replace_with: str, cursor, connection):
    cursor.execute(
        '''
        UPDATE Todo
        SET content = ?
        WHERE id = ?;
        ''',
        (replace_with, id)
    )
    connection.commit()
    return f'It has been changed to  "{replace_with}" '


def mark_as_done(id: int, cursor, connection) -> str:
    cursor.execute(
        '''
            UPDATE Todo
            SET status = 1
            WHERE id = ?;
            ''',
        (id,)
    )
    connection.commit()
    return 'Done'


def get_todos(cursor):
    cursor.execute(
        '''
        SELECT id,content 
        FROM 
        Todo
        WHERE status = 0
        '''
    )
    return cursor.fetchall()


def get_display():
    for todo in get_todos(cur):
        print(f'|//////||   {todo[0]}. {todo[1]}')

def delete(id,cur, conn):
    cur.execute(
        f'''
        DELETE
        FROM Todo
        WHERE id = '{id}'
        '''
    )
    conn.commit()
    return 'Delete done'

def help_display():
    print(
        '''
    Display -> To get all todos
    Add -> To create a todo
    Edit -> To edit a todo
    Done -> To mark something as done
    delete -> To delete a todo
    exit -> close
    Also all the inputs are case insensitive
        '''
    )
# def search(cur, what_to_search):
#     results = cur.execute(
#         f'''
#         SELECT id, content
#         FROM Todo
#         WHERE content LIKE '%{what_to_search}%'
#         '''
#     )
#     return results


if __name__ == '__main__':
    while True:
        cur, conn = create_connection()

        what_to_do: str = str(input('Enter Operation or help >> ')).lower()

        if what_to_do == 'help':
            help_display()
            continue
        elif what_to_do == 'display':
            get_display()

        elif what_to_do == 'add':
            todo = str(input('Enter to do >>'))
            print(write_todo(cur, conn, text=todo))

        elif what_to_do == 'edit':
            print('which one to edit just type the number')
            get_display()
            which_one = str(input('Enter number>> '))

            replace_with = input('enter the edited version >> ')
            print(
                f'''
            {edit_todo(id=which_one, replace_with=replace_with, cursor=cur, connection=conn)}

            ''')

        elif what_to_do == 'done':
            get_display()
            search_or_id = int(input('enter the number>> '))
            print(mark_as_done(search_or_id, cur, conn))
            break

        elif what_to_do == 'delete':
            get_display()
            what_to_delete = int(input('Number of what to delete >> '))
            print(delete(what_to_delete,cur,conn))

        elif what_to_do == 'exit':
            break
        else:
            help_display()
