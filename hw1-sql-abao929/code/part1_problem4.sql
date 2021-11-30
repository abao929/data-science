SELECT DISTINCT people_main2.name, people_main2.age
FROM
    people_likes LEFT JOIN people_main AS people_main1 ON people_likes.ID1 = people_main1.ID
    LEFT JOIN people_main AS people_main2 ON people_likes.ID2 = people_main2.ID
GROUP BY people_main2.name
HAVING people_main2.age > people_main1.age
ORDER BY people_main2.name ASC;
