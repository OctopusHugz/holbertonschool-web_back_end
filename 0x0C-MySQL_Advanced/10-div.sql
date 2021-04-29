-- This script creates a function SafeDiv
-- The SafeDiv function divides and returns quotient of a / b or 0 if b == 0
DELIMITER $$

CREATE FUNCTION SafeDiv(
    a INT,
    b INT
)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    END IF;
    RETURN a / b;
END $$

DELIMITER ;