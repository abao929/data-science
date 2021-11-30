SELECT
    people_main.name, COUNT(people_likes.ID2)
FROM
    people_main LEFT JOIN people_likes ON people_likes.ID2 = people_main.ID
GROUP BY people_main.name
ORDER BY COUNT(people_likes.ID2) DESC, people_main.name ASC;