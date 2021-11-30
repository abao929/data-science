SELECT 
CASE WHEN
    scores.review = 'poor' OR scores.review = 'awful'
    THEN 'do not watch'
    ELSE movies.original_title
END, movies.vote_average, scores.review
FROM movies
LEFT JOIN scores ON movies.vote_average BETWEEN scores.min_score AND scores.max_score
ORDER BY movies.id ASC