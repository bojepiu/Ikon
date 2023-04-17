use ikondb;

DROP PROCEDURE IF EXISTS insert_session;
DROP PROCEDURE IF EXISTS update_session;
DROP PROCEDURE IF EXISTS delete_session;
DROP PROCEDURE IF EXISTS get_all_sessions;
DROP PROCEDURE IF EXISTS get_sessions_by_module;
DROP PROCEDURE IF EXISTS get_session_by_id;


-- Procedimiento para insertar una nueva session
DELIMITER $$
CREATE PROCEDURE insert_session (
  IN p_name VARCHAR(255),
  IN p_module_id INT,
  OUT result VARCHAR(255)
)
BEGIN
  -- Validamos que no exista session con el mismo nombre en el mismo modulo
  IF NOT EXISTS (SELECT * FROM sessions as s WHERE s.name = p_name and s.module_id = p_module_id) THEN
    INSERT INTO sessions (name,module_id) VALUES (p_name,p_module_id);
    COMMIT;
    SET result = 'SUCCESS';
  ELSE
    set result = 'DUPLICATED';
  END IF;
END$$
DELIMITER ;

-- Procedimiento para obtener información de todos las sessions
DELIMITER $$
CREATE PROCEDURE update_session(
  IN p_id INT,
  IN p_module_id INT,
  IN p_name VARCHAR(255),
  OUT result VARCHAR(255)
)
update_this:BEGIN
  -- Validamos que no exista session con el mismo nombre en el mismo modulo
  IF NOT EXISTS (SELECT id from sessions where id=p_id) THEN
    set result = "ID_NOT_FOUND";
    leave update_this;
  END IF;
  IF NOT EXISTS (SELECT id from modules where id=p_module_id) THEN
    set result = "MODULE_ID_NOT_FOUND";
    leave update_this;
  END IF;
  IF NOT EXISTS (SELECT * FROM sessions as s WHERE s.name = p_name and s.module_id = p_module_id and s.id <> p_id) THEN
    UPDATE sessions SET name=p_name, module_id=p_module_id WHERE id=p_id;
    COMMIT;
    SET result = 'SUCCESS';
  ELSE
    set result = 'DUPLICATED';
  END IF;
END$$
DELIMITER ;


-- Procedimiento para eliminar la session esto elimina todas las sentencias asociadas
DELIMITER $$
CREATE PROCEDURE delete_session (
  IN p_id INT,
  OUT result VARCHAR(255) 
)
BEGIN
    -- Validamos que no este asociado a alguna sentencia
  IF NOT EXISTS (SELECT * FROM sentences WHERE session_id = p_id) THEN
    DELETE FROM sessions WHERE id = p_id;
    COMMIT;
    SET result = "SUCCESS";
  ELSE
    SET result = "USED_SESSION";
  END IF;
END$$
DELIMITER ;

-- Procedimiento para obtener información de todos las sessions por module
DELIMITER $$
CREATE PROCEDURE get_sessions_by_module(IN p_module_id INT)
BEGIN
  SELECT * FROM sessions where module_id=p_module_id;
END$$
DELIMITER ;

-- Procedimiento para obtener información de todos las sessions
DELIMITER $$
CREATE PROCEDURE get_all_sessions()
BEGIN
  SELECT * FROM sessions;
END$$
DELIMITER ;