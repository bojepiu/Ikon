-- BEGIN SECTION CARDS
USE ikondb;
DROP PROCEDURE IF EXISTS insert_card;
DROP PROCEDURE IF EXISTS update_card;
DROP PROCEDURE IF EXISTS delete_card;
DROP PROCEDURE IF EXISTS get_all_cards;
DROP PROCEDURE IF EXISTS get_card_by_id;
DROP PROCEDURE IF EXISTS get_cards_by_topic;



-- Procedimiento para insertar una nueva tarjeta
DELIMITER $$
CREATE PROCEDURE insert_card (
  IN p_topic_id INT,
  IN p_card_text VARCHAR(255),
  IN p_card_image VARCHAR(255),
  IN p_card_audio VARCHAR(255),
  IN p_card_video VARCHAR(255),
  IN p_card_aux_image VARCHAR(255),
  OUT result VARCHAR(255)
)
BEGIN
  IF EXISTS(SELECT * FROM  cards as c WHERE c.topic_id = p_topic_id and c.card_text = p_card_text ) THEN
    set result="DUPLICATED";
  ELSE
   INSERT INTO cards (topic_id,card_text,card_image,card_audio,card_video,card_aux_image) VALUES (p_topic_id,p_card_text,p_card_image,p_card_audio,p_card_video,p_card_aux_image);
   COMMIT;
   set result="SUCCESS";
  END IF;
END $$
DELIMITER ;

-- Procedimiento para actualizar una tarjeta existente
DELIMITER $$
CREATE PROCEDURE update_card (
  IN p_id INT,
  IN p_topic_id INT,
  IN p_card_text VARCHAR(255),
  IN p_card_image VARCHAR(255),
  IN p_card_audio VARCHAR(255),
  IN p_card_video VARCHAR(255),
  IN p_card_aux_image VARCHAR(255),
  OUT result VARCHAR(255)
)
BEGIN
  IF NOT EXISTS (SELECT * FROM cards WHERE topic_id = p_topic_id and card_text = p_card_text and id <> p_id) THEN
    UPDATE cards SET topic_id = p_topic_id, card_text = p_card_text, card_image = p_card_image, card_audio = p_card_audio, card_video = p_card_video, card_aux_image = p_card_aux_image WHERE id = p_id;
    COMMIT;
    SET result="SUCCESS";
  ELSE
    SET result="DUPLICATED";
  END IF;
END $$
DELIMITER ;

-- Procedimiento para eliminar una tarjeta
DELIMITER $$
CREATE PROCEDURE delete_card (
  IN p_id INT,
  OUT result VARCHAR(255)
)
BEGIN
  IF NOT EXISTS (SELECT * FROM cards_sentences WHERE card_id = p_id) THEN
    DELETE FROM cards WHERE id = p_id;
    COMMIT;
    SET result= "SUCCESS";
  ELSE
    SET result="USED";
  END IF;
END $$
DELIMITER ;

-- Procedimiento para obtener información de todas las tarjetas
DELIMITER $$
CREATE PROCEDURE get_all_cards()
BEGIN
  SELECT * FROM cards;
END $$
DELIMITER ;

-- Procedimiento para obtener información de una tarjeta específica
DELIMITER $$
CREATE PROCEDURE get_card_by_id (
  IN p_id INT
)
BEGIN
  SELECT * FROM cards WHERE id=p_id;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE get_cards_by_topic (
  IN p_topic_id INT
)
BEGIN
  SELECT * FROM cards WHERE topic_id=p_topic_id;
END $$
DELIMITER ;
