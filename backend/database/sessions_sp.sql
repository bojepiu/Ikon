use ikondb;

DROP PROCEDURE IF EXISTS insert_session;
DROP PROCEDURE IF EXISTS update_session;
DROP PROCEDURE IF EXISTS delete_session;
DROP PROCEDURE IF EXISTS get_all_sessions;
DROP PROCEDURE IF EXISTS get_session_by_id;

-- Procedimiento para insertar una nueva session
DELIMITER $$
CREATE PROCEDURE insert_session (
  IN p_name VARCHAR(255),
  IN p_module_id VARCHAR(255),
  OUT result VARCHAR(255)
)
BEGIN
  -- Validamos que no exista session con el mismo nombre en el mismo modulo
  IF NOT EXISTS (SELECT * FROM sessions as s WHERE s.name = p_name and s.module_id = p_module_id) THEN
    INSERT INTO sessions (name,module_id) VALUES (p_name,p_module_id);
    COMMIT;
    SET result = 'SUCCESS';
  ELSE
    set result = 'ERROR';
  END IF;
END$$
DELIMITER ;

-- Procedimiento para obtener información de todos las sessions
DELIMITER $$
CREATE PROCEDURE get_all_sessions()
BEGIN
  SELECT * FROM sessions;
END$$
DELIMITER ;