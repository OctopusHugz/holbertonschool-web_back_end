-- This file counts fans from different countries
-- Fans are rank-ordered by country
SELECT origin,
	SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
