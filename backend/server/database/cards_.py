import _init_ as DB

CONNECTION = DB.init_connection()

def get_all_cards():
    try:
        return 'OK'
    except Exception as e:
        return 'ERROR'

def insert_card():
    try:
        return 'OK'
    except Exception as e:
        return 'ERROR'

def update_card():
    try:
        return 'OK'
    except Exception as e:
        return 'ERROR'

def delete_card():
    try:
        return 'OK'
    except Exception as e:
        return 'ERROR'
