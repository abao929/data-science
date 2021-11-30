WITH languages AS (
    SELECT DISTINCT original_language
    FROM movies
    GROUP BY original_language
    HAVING COUNT(original_language) > 2
),
poor_good AS (
    SELECT languages.original_language,
    CASE WHEN scores.review = 'poor' THEN 1 ELSE 0 END AS poor,
    CASE WHEN scores.review = 'good' THEN 1 ELSE 0 END AS good
    FROM languages
    LEFT JOIN movies ON languages.original_language = movies.original_language
    LEFT JOIN scores ON movies.vote_average BETWEEN scores.min_score AND scores.max_score)

SELECT poor_good.original_language,
 SUM(poor_good.poor) AS num_poor,
 SUM(poor_good.good) AS num_good
FROM poor_good
GROUP BY poor_good.original_language
ORDER BY num_good DESC, num_poor ASC