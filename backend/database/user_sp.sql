USE ikondb;
DROP PROCEDURE IF EXISTS insert_user;
DROP PROCEDURE IF EXISTS update_user;
DROP PROCEDURE IF EXISTS delete_user;
DROP PROCEDURE IF EXISTS get_all_users;
DROP PROCEDURE IF EXISTS get_user_by_id;

-- Procedimiento para insertar un nuevo usuario
DELIMITER $$
CREATE PROCEDURE insert_user (IN p_name VARCHAR(255),IN p_email VARCHAR(255),IN p_password VARCHAR(255),IN p_role INT,OUT result VARCHAR(255))
BEGIN
  IF NOT EXISTS (SELECT * FROM users WHERE email = p_email) THEN
    INSERT INTO users (name, email, password, role) VALUES (p_name, p_email, p_password, p_role);
    set result ='SUCCESS';
  ELSE
    set result = 'ERROR';
  END IF;
END$$
DELIMITER ;

-- Procedimiento para actualizar un usuario existente
DELIMITER $$
CREATE PROCEDURE update_user (
  IN p_id INT,
  IN p_name VARCHAR(255),
  IN p_email VARCHAR(255),
  IN p_password VARCHAR(255),
  IN p_role INT,
  result VARCHAR(255)
)
BEGIN
  IF (p_password = NULL ) THEN
    UPDATE users SET name = p_name, email = p_email, role = p_role WHERE id = p_id;
    set result ='SUCCESS';
  ELSE
    UPDATE users SET name = p_name, email = p_email, password = p_password WHERE id = p_id;
    set result ='ERROR';
  END IF;
END$$
DELIMITER ;


-- Procedimiento para eliminar un usuario
DELIMITER $$
CREATE PROCEDURE delete_user (
  IN p_id INT,
  result VARCHAR(255)
)
BEGIN
  DELETE FROM users WHERE id = p_id AND p_id <> 'admin';
  set result ='SUCCESS';
END$$
DELIMITER ;

-- Procedimiento para obtener información de todos los usuarios menos el password
DELIMITER $$
CREATE PROCEDURE get_all_users()
BEGIN
  SELECT id,name,email,role FROM users;
END$$
DELIMITER ;

-- Procedimiento para obtener información de un usuario específico
DELIMITER $$
CREATE PROCEDURE get_user_by_id (
  IN p_id INT
)
BEGIN
  SELECT * FROM users WHERE id = p_id;
END$$
DELIMITER ;