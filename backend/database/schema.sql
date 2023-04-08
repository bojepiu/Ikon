-- db_volume/mysql
-- ikonpwdbd
-- Crear la base de datos
DROP DATABASE IF EXISTS ikondb;
CREATE DATABASE IF NOT EXISTS ikondb;

-- Seleccionar la base de datos
USE ikondb;

-- Crear la tabla users
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  role INT NOT NULL
);

-- Crear la tabla modules
CREATE TABLE modules (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT
);

-- Crear la tabla sessions
CREATE TABLE sessions (
  id INT PRIMARY KEY AUTO_INCREMENT,
  module_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  FOREIGN KEY(module_id) REFERENCES modules(id)
);

-- Crear la tabla topics
CREATE TABLE topics (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL
);

-- Crear la tabla 'cards'
CREATE TABLE cards (
  id INT PRIMARY KEY AUTO_INCREMENT,
  topic_id INT NOT NULL,
  card_text VARCHAR(255) NOT NULL,
  card_image VARCHAR(255) NOT NULL,
  card_audio VARCHAR(255) NOT NULL,
  card_video VARCHAR(255) NOT NULL,
  card_aux_image VARCHAR(255) NOT NULL,
  FOREIGN KEY (topic_id) REFERENCES topics(id)
);

-- Crear la tabla sentences
-- Sentence order es un csv de id's de cards
CREATE TABLE sentences (
  id INT PRIMARY KEY AUTO_INCREMENT,
  session_id INT NOT NULL,
  sentence_text VARCHAR(255) NOT NULL,
  sentence_order VARCHAR(255) NOT NULL,
  sentence_image VARCHAR(255) NOT NULL,
  sentence_audio VARCHAR(255) NOT NULL,
  sentence_video VARCHAR(255) NOT NULL,
  sentence_aux_image VARCHAR(255) NOT NULL,
  FOREIGN KEY (session_id) REFERENCES sessions(id)
);

-- Relacion session-module
CREATE TABLE session_module (
  id INT PRIMARY KEY AUTO_INCREMENT,
  session_id INT NOT NULL,
  module_id INT NOT NULL,
  FOREIGN KEY (session_id) REFERENCES sessions(id),
  FOREIGN KEY (module_id) REFERENCES modules(id)
);

-- Crear la tabla relacion cards-sentences
-- Para obtener el orden correcto de la sentencia el select tiene que ser order by id
CREATE TABLE cards_sentences (
  id INT PRIMARY KEY AUTO_INCREMENT,
  card_id INT NOT NULL,
  sentence_id INT NOT NULL,
  FOREIGN KEY (card_id) REFERENCES cards(id),
  FOREIGN KEY (sentence_id) REFERENCES sentences(id)
);

-- Relacion sentencia session
CREATE TABLE sentence_session (
  id INT PRIMARY KEY AUTO_INCREMENT,
  sentence_id INT NOT NULL,
  session_id INT NOT NULL,
  FOREIGN KEY (sentence_id) REFERENCES sentences(id),
  FOREIGN KEY (session_id) REFERENCES sessions(id)
);


-- Crear la tabla log
CREATE TABLE log (
  id INT PRIMARY KEY,
  user_id INT NOT NULL,
  module_id INT NOT NULL,
  session_id INT NOT NULL,
  duration INT NOT NULL,
  correct BOOLEAN NOT NULL,
  initiated DATETIME NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (module_id) REFERENCES modules(id),
  FOREIGN KEY (session_id) REFERENCES sessions(id)
);

-- Initialized with default user
INSERT INTO users values(null,"admin","admin@ikons.com","adminadmin",1);