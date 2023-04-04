USE ikondb;

DROP PROCEDURE IF EXISTS insert_sentence;
DROP PROCEDURE IF EXISTS update_sentence;
DROP PROCEDURE IF EXISTS delete_sentence;
DROP PROCEDURE IF EXISTS get_all_sentences;
DROP PROCEDURE IF EXISTS get_sentence_by_id;
DROP PROCEDURE IF EXISTS get_sentence_by_session;

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
BEGIN
  DECLARE strLen    INT DEFAULT 0;
  DECLARE SubStrLen    INT DEFAULT 0;
  IF EXISTS(SELECT * FROM  sentences as s WHERE s.session_id = p_session_id and s.sentence_text = p_sentence_text ) THEN
    set result="DUPLICATED";
  ELSE
    do_this:
    LOOP
        SET strLen = LENGTH(p_sentence_order);
        IF NOT EXISTS (SELECT id FROM cards WHERE id = SUBSTRING_INDEX(p_sentence_order, ',', 1)) THEN
            SET result=p_senten_order;
        END IF;
        SET SubStrLen = LENGTH(SUBSTRING_INDEX(p_sentence_order, ',', 1))+1;
        SET p_sentence_order = MID(p_sentence_order, SubStrLen, strLen);
        IF p_sentence_order = NULL THEN
            LEAVE do_this;
        END IF;
    END LOOP do_this;
    IF result <> "CARD_NOT_FOUND" THEN
      INSERT INTO cards (session_id,senten_text,sentence_order,sentence_image,sentence_audio,sentence_video,sentence_aux_image) VALUES (p_session_id,p_senten_text,p_sentence_order,p_sentence_image,p_sentence_audio,p_sentence_video,p_sentence_aux_image);
      COMMIT;
    END IF;
    set result="SUCCESS";
  END IF;
END $$
DELIMITER ;


DELIMITER $$
CREATE PROCEDURE get_all_sentences()
BEGIN
  SELECT * FROM sentences;
END$$
DELIMITER ;
