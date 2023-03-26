USE ikondb;
DROP PROCEDURE IF EXISTS insert_user;
DROP PROCEDURE IF EXISTS update_user;
DROP PROCEDURE IF EXISTS delete_user;
DROP PROCEDURE IF EXISTS get_all_users;
DROP PROCEDURE IF EXISTS get_user_by_id;

-- Procedimiento para insertar un nuevo usuario
CREATE PROCEDURE insert_user (
  IN name VARCHAR(255),
  IN email VARCHAR(255),
  IN password VARCHAR(255),
  IN role INT
)
AS
BEGIN
  IF NOT EXISTS (SELECT * FROM users WHERE email = @email)
  BEGIN
    INSERT INTO users (name, email, password, role) VALUES (@name, @email, @password, @role)
  END
  ELSE
  BEGIN
    RAISERROR('Already user exists', 16, 1)
  END
END;

-- Procedimiento para actualizar un usuario existente
CREATE PROCEDURE update_user (
  @id INT,
  @name VARCHAR(255),
  @email VARCHAR(255),
  @password VARCHAR(255) = NULL,
  @role INT
)
AS
BEGIN
  IF (@password is NULL)
  BEGIN
    UPDATE users SET name = @name, email = @email, role = @role WHERE id = @id
  END
  ELSE
  BEGIN
   UPDATE users SET name = @name, email = @email, password = @password WHERE id = @id
  END
END;

-- Procedimiento para eliminar un usuario
CREATE PROCEDURE delete_user (
  @id INT
)
AS
BEGIN
  DELETE FROM users WHERE id = @id AND @id <> 'admin'
END;

-- Procedimiento para obtener información de todos los usuarios menos el password
CREATE PROCEDURE get_all_users
AS
BEGIN
  SELECT id,name,email,role FROM users
END;

-- Procedimiento para obtener información de un usuario específico
CREATE PROCEDURE get_user_by_id (
  @id INT
)
AS
BEGIN
  SELECT * FROM users WHERE id = @id
END;
