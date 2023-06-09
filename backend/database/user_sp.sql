USE ikondb;
DROP PROCEDURE IF EXISTS insert_user;
DROP PROCEDURE IF EXISTS update_user;
DROP PROCEDURE IF EXISTS delete_user;
DROP PROCEDURE IF EXISTS get_all_users;
DROP PROCEDURE IF EXISTS get_user_by_id;
DROP PROCEDURE IF EXISTS validate_user;


-- Procedimiento para insertar un nuevo usuario
DELIMITER $$
CREATE PROCEDURE insert_user (IN p_name VARCHAR(255),IN p_email VARCHAR(255),IN p_password VARCHAR(255),IN p_role INT,OUT result VARCHAR(255))
BEGIN
  IF NOT EXISTS (SELECT * FROM users WHERE email = p_email or name = p_name) THEN
    INSERT INTO users (name, email, password, role) VALUES (p_name, p_email, p_password, p_role);
    COMMIT;
    set result ='SUCCESS';
  ELSE
    set result = 'ALREADY_EXISTS';
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
  OUT result VARCHAR(255)
)
BEGIN
  IF NOT EXISTS (SELECT * FROM users WHERE (email = p_email or name = p_name) and id <> p_id ) THEN
    IF (p_password = "" ) THEN
      UPDATE users SET name = p_name, email = p_email, role = p_role WHERE id = p_id;
      COMMIT;
      set result ='SUCCESS';
    ELSE
      UPDATE users SET name = p_name, email = p_email, password = p_password,  role = p_role WHERE id = p_id;
      COMMIT;
      set result ='SUCCESS';
    END IF;
  ELSE
    set result = 'ALREADY_EXISTS';
  END IF;
END$$
DELIMITER ;


-- Procedimiento para eliminar un usuario
DELIMITER $$
CREATE PROCEDURE delete_user (
  IN p_id INT,
  OUT result VARCHAR(255)
)
BEGIN
  DELETE FROM users WHERE id = p_id AND name <> 'admin';
  COMMIT;
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

-- Procedimiento para obtener información de un usuario específico
DELIMITER $$
CREATE PROCEDURE validate_user (
  IN p_name VARCHAR(255),
  IN p_password VARCHAR(255)
)
BEGIN
  SELECT name,email,role FROM users WHERE name = p_name and password=p_password;
END$$
DELIMITER ; 