use ikondb;

DROP PROCEDURE IF EXISTS insert_topic;
DROP PROCEDURE IF EXISTS update_topic;
DROP PROCEDURE IF EXISTS delete_topic;
DROP PROCEDURE IF EXISTS get_all_topics;
DROP PROCEDURE IF EXISTS get_topic_by_id;

-- Procedimiento para insertar un nuevo topic
DELIMITER $$
CREATE PROCEDURE insert_topic (
  IN p_name VARCHAR(255),
  OUT result VARCHAR(255)
)
BEGIN
  -- Validamos que no exista un topic con el mismo nombre
  IF NOT EXISTS (SELECT * FROM topics WHERE name = p_name) THEN
    INSERT INTO topics (name) VALUES (p_name);
    COMMIT;
    SET result = 'SUCCESS';
  ELSE
    set result = 'DUPLICATED';
  END IF;
END$$
DELIMITER ;


-- Procedimiento para actualizar un topic existente
DELIMITER $$
CREATE PROCEDURE update_topic (
  IN p_id INT,
  IN p_name VARCHAR(255),
  OUT result VARCHAR(255)
)
BEGIN
  IF NOT EXISTS (SELECT * FROM topics WHERE name = p_name and id <> p_id) THEN
    UPDATE topics SET name = p_name WHERE id = p_id;
    COMMIT;
    SET result = "SUCCESS";
  ELSE
    set result = "DUPLICATED";
  END IF;
END$$
DELIMITER ;

-- Procedimiento para eliminar un topic siempre y cuando este no se use en ningun lugar
DELIMITER $$
CREATE PROCEDURE delete_topic (
  IN p_id INT,
  OUT result VARCHAR(255) 
)
BEGIN
    -- Validamos que no este asociado alguna card
  IF NOT EXISTS (SELECT * FROM cards WHERE topic_id = p_id) THEN
    DELETE FROM topics WHERE id = p_id;
    COMMIT;
    SET result = "SUCCESS";
  ELSE
    SET result = "USED_TOPIC";
  END IF;
END$$
DELIMITER ;

-- Procedimiento para obtener información de todos los topics
DELIMITER $$
CREATE PROCEDURE get_all_topics()
BEGIN
  SELECT * FROM topics;
END$$
DELIMITER ;

-- Procedimiento para obtener información de un topic específico
DELIMITER $$
CREATE PROCEDURE get_topic_by_id (
  p_id INT
)
BEGIN
  SELECT * FROM topics WHERE id = p_id;
END$$
DELIMITER ;

