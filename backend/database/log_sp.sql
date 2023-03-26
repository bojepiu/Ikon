

-- Procedimiento para insertar una nueva entrada en el log
CREATE PROCEDURE insert_log (
  @message VARCHAR(255),
  @created_at DATETIME
)
AS
BEGIN
  INSERT INTO log (message, created_at) VALUES (@message, @created_at)
END;

-- Procedimiento para actualizar una entrada existente en el log
CREATE PROCEDURE update_log (
  @id INT,
  @message VARCHAR(255),
  @created_at DATETIME
)
AS
BEGIN
  UPDATE log SET message = @message, created_at = @created_at WHERE id = @id
END;

-- Procedimiento para eliminar una entrada del log
CREATE PROCEDURE delete_log (
  @id INT
)
AS
BEGIN
  DELETE FROM log WHERE id = @id
END;

-- Procedimiento para obtener información de todas las entradas del log
CREATE PROCEDURE get_all_logs
AS
BEGIN
  SELECT * FROM log
END;

-- Procedimiento para obtener información de una entrada específica del log
CREATE PROCEDURE get_log_by_id (
  @id INT
)
AS
BEGIN
  SELECT * FROM log WHERE id = @id
END;
