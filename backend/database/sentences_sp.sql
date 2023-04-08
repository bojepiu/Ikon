USE ikondb;

DROP PROCEDURE IF EXISTS insert_sentence;
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
proc_insert:BEGIN
  DECLARE strLen    INT DEFAULT 0;
  DECLARE SubStrLen    INT DEFAULT 0;
  DECLARE aux_sentence_order VARCHAR(255) DEFAULT p_sentence_order;
  SET result = 'init';
  SET p_sentence_order=CONCAT(p_sentence_order,",");

  IF EXISTS(SELECT * FROM  sentences as s WHERE s.session_id = p_session_id and s.sentence_text = p_sentence_text ) THEN
    set result="DUPLICATED";
  ELSE
    do_this:
    LOOP
        SET strLen = LENGTH(p_sentence_order);
        IF NOT EXISTS (SELECT id FROM cards WHERE id = SUBSTRING_INDEX(p_sentence_order, ',', 1)) THEN
          SET result=p_sentence_order;
          LEAVE proc_insert;
        END IF;
        SET SubStrLen = LENGTH(SUBSTRING_INDEX(p_sentence_order, ',', 1));
        SET p_sentence_order = MID(p_sentence_order, SubStrLen+2, strLen);
        IF LENGTH(p_sentence_order) = 0 THEN
            LEAVE do_this;
        END IF;
    END LOOP do_this;
    IF result = "init" THEN
      INSERT INTO sentences (session_id,sentence_text,sentence_order,sentence_image,sentence_audio,sentence_video,sentence_aux_image) VALUES (p_session_id,p_sentence_text,aux_sentence_order,p_sentence_image,p_sentence_audio,p_sentence_video,p_sentence_aux_image);
      COMMIT;
       set result="SUCCESS";
    ELSE
      set result=CONCAT("CARD_NOT_FOUND,",LENGTH(p_sentence_order));
    END IF;
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
  DECLARE strLen    INT DEFAULT 0;
  DECLARE SubStrLen    INT DEFAULT 0;
  SET result = 'init';
  SET p_sentence_order=CONCAT(p_sentence_order,",");
  IF EXISTS(SELECT * FROM  sentences as s WHERE s.session_id = p_session_id and s.sentence_text = p_sentence_text and p_sentence_id <> id ) THEN
    set result="DUPLICATED";
  ELSE
    do_this:
    LOOP
        SET strLen = LENGTH(p_sentence_order);
        IF NOT EXISTS (SELECT id FROM cards WHERE id = SUBSTRING_INDEX(p_sentence_order, ',', 1)) THEN
          SET result=p_sentence_order;
          LEAVE proc_update;
        END IF;
        SET SubStrLen = LENGTH(SUBSTRING_INDEX(p_sentence_order, ',', 1));
        SET p_sentence_order = MID(p_sentence_order, SubStrLen+2, strLen);
        IF LENGTH(p_sentence_order) = 0 THEN
            LEAVE do_this;
        END IF;
    END LOOP do_this;
    IF result = "init" THEN
      UPDATE sentences SET session_id=p_session_id, sentence_text=p_sentence_text, sentence_order=p_sentence_order, sentence_image=p_sentence_image, sentence_audio=p_sentence_audio, sentence_video=p_sentence_video, sentence_aux_image=p_sentence_aux_image where id=p_sentence_id;
      COMMIT;
       set result="SUCCESS";
    ELSE
      set result=CONCAT("CARD_NOT_FOUND,",LENGTH(p_sentence_order));
    END IF;
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
