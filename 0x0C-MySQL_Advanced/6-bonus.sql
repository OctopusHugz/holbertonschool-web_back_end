-- This script creates an AddBonus stored procedure
-- AddBonus adds a new correction for a student
DELIMITER $$

CREATE PROCEDURE AddBonus(
	IN user_id VARCHAR(255),
	IN project_name VARCHAR(255),
	IN score INT
)
BEGIN
	IF NOT EXISTS(SELECT 1 FROM projects WHERE name = project_name) THEN
		INSERT INTO projects (name) VALUES (project_name);
	END IF;
END $$

DELIMITER ;
