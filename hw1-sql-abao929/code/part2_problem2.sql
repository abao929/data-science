SELECT COUNT(original_title)
FROM movies
WHERE original_title LIKE 'The%' OR 
original_title LIKE '%2' OR
original_title LIKE '%shark%'