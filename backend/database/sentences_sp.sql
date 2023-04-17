USE ikondb;

DROP PROCEDURE IF EXISTS insert_sentence;
DROP PROCEDURE IF EXISTS insert_cards_sentences;
DROP PROCEDURE IF EXISTS update_sentence;
DROP PROCEDURE IF EXISTS delete_sentence;
DROP PROCEDURE IF EXISTS get_all_sentences;
DROP PROCEDURE IF EXISTS get_sentence_by_id;
DROP PROCEDURE IF EXISTS get_sentences_by_session;

-- Procedimiento para insertar una nueva tarjeta
-- p_sentence_order es un array separado por comas de los ids de las tarjetas
DELIMITER $$
CREATE PROCEDURE insert_sentence (
  IN p_session_id INT,
  IN p_sentence_text VARCHAR(255),
  IN p_sentence_order VARCHAR(255),
  IN p_sentence_image VARCHAR(255),
  IN p_sentence_audio VARCHAR(255),
  IN p_sentence_video VARCHAR(255),
  IN p_sentence_aux_image VARCHAR(255),
  OUT result VARCHAR(255)
)
proc_insert:
BEGIN
  DECLARE p_sentence_id INT DEFAULT 0;
  SET result = 'init';
  IF NOT EXISTS (select id from sessions where id=p_session_id) THEN
    set result="SESSION_NOT_FOUND";
    LEAVE proc_insert;
  END IF;
  IF EXISTS(SELECT * FROM  sentences as s WHERE s.session_id = p_session_id and s.sentence_text = p_sentence_text ) THEN
    set result="DUPLICATED";
    LEAVE proc_insert;
  ELSE
    INSERT INTO sentences (session_id,sentence_text,sentence_order,sentence_image,sentence_audio,sentence_video,sentence_aux_image) VALUES (p_session_id,p_sentence_text,p_sentence_order,p_sentence_image,p_sentence_audio,p_sentence_video,p_sentence_aux_image);
    COMMIT;
    set p_sentence_id= (select id from sentences where session_id=p_session_id and sentence_text=p_sentence_text and sentence_order=p_sentence_order and sentence_image=p_sentence_image);
    set result=p_sentence_id;
  END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE insert_cards_sentences (
  IN p_card_id INT,
  IN p_sentence_id INT,
  OUT result VARCHAR(255)
)
insert_this:BEGIN
  SET result = 'init';
  IF NOT EXISTS(select id from cards where id=p_card_id)THEN
    set result="CARD_NOT_FOUND";
    LEAVE insert_this;
  END IF;
  IF NOT EXISTS(select id from sentences where id=p_sentence_id)THEN
    set result="SENTENCE_NOT_FOUND";
    LEAVE insert_this;
  END IF;
  IF EXISTS(SELECT id FROM  cards_sentences as s WHERE s.card_id_s = p_card_id and s.sentence_id = p_sentence_id ) THEN
    set result="DUPLICATED";
  ELSE
    INSERT INTO cards_sentences (card_id_s,sentence_id) VALUES (p_card_id,p_sentence_id);
    COMMIT;
    set result="SUCCESS";
  END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE update_sentence (
  IN p_sentence_id INT,
  IN p_session_id INT,
  IN p_sentence_text VARCHAR(255),
  IN p_sentence_order VARCHAR(255),
  IN p_sentence_image VARCHAR(255),
  IN p_sentence_audio VARCHAR(255),
  IN p_sentence_video VARCHAR(255),
  IN p_sentence_aux_image VARCHAR(255),
  OUT result VARCHAR(255)
)
proc_update:BEGIN
  SET result = 'init';

  IF NOT EXISTS (SELECT id FROM sentences WHERE id = p_sentence_id) THEN
    SET result='BAD_ID';
    LEAVE proc_update;
  END IF;
  IF EXISTS(SELECT * FROM  sentences as s WHERE s.session_id = p_session_id and s.sentence_text = p_sentence_text and p_sentence_id <> id ) THEN
    set result="DUPLICATED";
    LEAVE proc_update;
  ELSE
    UPDATE sentences SET session_id=p_session_id, sentence_text=p_sentence_text, sentence_order=p_sentence_order, sentence_image=p_sentence_image, sentence_audio=p_sentence_audio, sentence_video=p_sentence_video, sentence_aux_image=p_sentence_aux_image where id=p_sentence_id;
    COMMIT;
    set result="SUCCESS";
  END IF;
END $$
DELIMITER ;

-- Procedimiento para eliminar una sentencia de una session
DELIMITER $$
CREATE PROCEDURE delete_sentence (
  IN p_id INT,
  OUT result VARCHAR(255)
)
BEGIN
    DELETE FROM cards_sentences where sentence_id=p_id;
    DELETE FROM sentences WHERE id = p_id;
    COMMIT;
    SET result = "SUCCESS";
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE get_sentences_by_session(IN p_session_id INT)
BEGIN
  SELECT * FROM sentences where session_id=p_session_id;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE get_all_sentences()
BEGIN
  SELECT * FROM sentences;
END$$
DELIMITER ;
