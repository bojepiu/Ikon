use ikondb;

DROP PROCEDURE IF EXISTS insert_module;
DROP PROCEDURE IF EXISTS update_module;
DROP PROCEDURE IF EXISTS delete_module;
DROP PROCEDURE IF EXISTS get_all_modules;
DROP PROCEDURE IF EXISTS get_module_by_id;

-- Procedimiento para insertar una nueva session
DELIMITER $$
CREATE PROCEDURE insert_module (
  IN p_name VARCHAR(255),
  IN p_description TEXT,
  OUT result VARCHAR(255)
)
BEGIN
  -- Validamos que no exista session con el mismo nombre en el mismo modulo
  IF NOT EXISTS (SELECT * FROM modules as s WHERE s.name = p_name) THEN
    INSERT INTO modules (name,description) VALUES (p_name,p_description);
    COMMIT;
    SET result = 'SUCCESS';
  ELSE
    set result = 'DUPLICATED';
  END IF;
END$$
DELIMITER ;


-- Procedimiento para obtener información de todos los topics
DELIMITER $$
CREATE PROCEDURE get_all_modules()
BEGIN
  SELECT * FROM modules;
END$$
DELIMITER ;
