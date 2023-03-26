-- BEGIN SECTION CARDS

-- Procedimiento para insertar una nueva tarjeta
CREATE PROCEDURE insert_card (
  @topic_id INT,
  @card_text VARCHAR(255),
  @card_image VARCHAR(255),
  @card_audio VARCHAR(255),
  @card_video VARCHAR(255),
  @card_aux_image VARCHAR(255)
)
AS
BEGIN
  IF EXISTS (SELECT * FROM topics as t, cards as c WHERE t.id = @topic_id and c.card_text  = @card_text)
  BEGIN
    RAISERROR('The card already exists', 16, 1)
  END
  ELSE
  BEGIN
   INSERT INTO cards (topic_id,card_text,card_image,card_audio,card_video,card_aux_image) VALUES (@topic_id,@card_text,@card_image,@card_audio,@card_video,@card_aux_image)
  END
END;

-- Procedimiento para actualizar una tarjeta existente
CREATE PROCEDURE update_card (
  @id INT,
  @topic_id INT,
  @card_text VARCHAR(255),
  @card_image VARCHAR(255),
  @card_audio VARCHAR(255),
  @card_video VARCHAR(255),
  @card_aux_image VARCHAR(255)
)
AS
BEGIN
  IF NOT EXISTS (SELECT * FROM topics as t, cards as c WHERE t.id = @topic_id and c.card_text = @card_text and c.id <> @id)
  BEGIN
   UPDATE cards SET topic_id = @topic_id, card_text = @card_text, card_image = @card_image, card_audio = @card_audio, card_video = @card_video, card_aux_image = @card_aux_image WHERE id = @id
  END
  ELSE
  BEGIN
   RAISERROR('The card already exists', 16, 1)
  END
END;

-- Procedimiento para eliminar una tarjeta
CREATE PROCEDURE delete_card (
  @id INT
)
AS
BEGIN
  IF NOT EXISTS (SELECT * FROM cards_sentences WHERE card_id = @id)
  BEGIN
    DELETE FROM cards WHERE id = @id
  END
  ELSE
  BEGIN
    RAISERROR('The card is in use', 16, 1)
  END
END;

-- Procedimiento para obtener información de todas las tarjetas
CREATE PROCEDURE get_all_cards
AS
BEGIN
  SELECT * FROM cards
END;

-- Procedimiento para obtener información de una tarjeta específica
CREATE PROCEDURE get_card_by_id (
  @id INT
)
AS

