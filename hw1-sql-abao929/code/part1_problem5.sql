SELECT people_main1.ID, people_main1.name, people_main2.ID, people_main2.name
FROM
    people_likes LEFT JOIN people_main as people_main1 ON people_likes.ID1 = people_main1.ID
    LEFT JOIN people_main as people_main2 on people_likes.ID2 = people_main2.ID
WHERE NOT EXISTS(
    SELECT *
    FROM people_friends
    WHERE people_friends.ID1 = people_main1.ID
    AND people_friends.ID2 = people_main2.ID
)
GROUP BY people_main2.name
ORDER BY people_main1.ID ASC, people_main2.ID ASC;