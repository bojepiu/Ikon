import _init_ as DB

CONNECTION=DB.init_connection()

def get_all_modules():
    try:
        cursor=CONNECTION.cursor()
        cursor.callproc('get_all_modules')
        for i in cursor.stored_results():
            result=i.fetchall()
            print(result)
            return result
        return []
    except Exception as e:
        return 'ERROR'
    
def insert_module(name,description):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('insert_module',(name,description,''))
        print(output)
        return 'OK'
    except Exception as e:
        print(str(e))
        return 'ERROR'

def update_module(module_id,name,description):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('update_module',(module_id,name,description,''))
        print(output)
        return 'OK'
    except Exception as e:
        print(str(e))
        return 'ERROR'

def delete_module(module_id):
    try:
        cursor=CONNECTION.cursor()
        output=cursor.callproc('delete_module',(module_id,''))
        print(output)
        return 'OK'
    except Exception as e:
        print(str(e))
        return 'ERROR'
    

    

# insert_module('Modulo1','Modulo para eliminar y una breve descripcion')
# update_module(1,'Modulo2','Modulo para eliminar y modificado')
delete_module(3)
get_all_modules()