WITH subquery AS (
    SELECT DISTINCT ID2
    FROM people_likes
)
SELECT
    people_main.occupation, COUNT(people_main.occupation)
FROM
    subquery LEFT JOIN people_main ON subquery.ID2 = people_main.ID
GROUP BY people_main.occupation
ORDER BY COUNT(subquery.ID2) ASC, people_main.occupation ASC
LIMIT 2;