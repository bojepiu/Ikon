USE ikondb;

DROP PROCEDURE IF EXISTS get_random_cards_from_topic;

DELIMITER $$
CREATE PROCEDURE get_random_cards_from_topic(IN p_topic_id VARCHAR(255))
BEGIN
    select * from cards where topic_id = p_topic_id LIMIT 5; 
END$$
DELIMITER;
