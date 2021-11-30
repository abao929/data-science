SELECT movies.original_title,
CASE
    WHEN EXISTS (SELECT * FROM movies as movies2
    WHERE (movies2.id != movies.id AND movies2.vote_average = movies.vote_average AND movies2.runtime = movies.runtime))
    THEN 1
    ELSE 0
END
FROM movies
ORDER BY movies.original_title