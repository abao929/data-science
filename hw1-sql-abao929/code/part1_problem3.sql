SELECT
    people_main.name, people_main.occupation
FROM
    people_friends LEFT JOIN people_main ON people_friends.ID2 = people_main.ID
GROUP BY people_main.name
HAVING COUNT(people_friends.ID2) > 3
ORDER BY people_main.name ASC;