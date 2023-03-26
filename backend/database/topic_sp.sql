-- TOPIC SECTION
-- Procedimiento para insertar un nuevo topic
CREATE PROCEDURE insert_topic (
  @name VARCHAR(255)
)
AS
BEGIN
  -- Validamos que no exista un topic con el mismo nombre
  IF NOT EXISTS (SELECT * FROM topics WHERE name = @name)
  BEGIN
    INSERT INTO topics (name) VALUES (@name)
  END
  ELSE
  BEGIN
    RAISERROR('Already exists', 16, 1)
  END
END;

-- Procedimiento para actualizar un topic existente
CREATE PROCEDURE update_topic (
  @id INT,
  @name VARCHAR(255)
)
AS
BEGIN
  IF NOT EXISTS (SELECT * FROM topics WHERE name = @name)
  BEGIN
    UPDATE topics SET name = @name WHERE id = @id
  END
  ELSE
  BEGIN
    RAISERROR('Already exists', 16, 1)
  END
END;

-- Procedimiento para eliminar un topic siempre y cuando este no se use en ningun lugar
CREATE PROCEDURE delete_topic (
  @id INT
)
AS
BEGIN
    -- Validamos que no este asociado alguna card
  IF NOT EXISTS (SELECT * FROM cards WHERE topic_id = @id)
  BEGIN
    DELETE FROM topics WHERE id = @id
  END
  ELSE
  BEGIN
    RAISERROR('Topic is going used', 16, 1)
  END
END;

-- Procedimiento para obtener información de todos los topics
CREATE PROCEDURE get_all_topics
AS
BEGIN
  SELECT * FROM topics
END;

-- Procedimiento para obtener información de un topic específico
CREATE PROCEDURE get_topic_by_id (
  @id INT
)
AS
BEGIN
  SELECT * FROM topics WHERE id = @id
END;
--END TOPIC SECTION
