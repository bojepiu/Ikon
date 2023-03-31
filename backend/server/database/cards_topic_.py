import _init_ as DB

CONNECTION=DB.init_connection()


def get_cards_by_topic():
    try:
        return 'OK'
    except Exception as e:
        return 'ERROR'

