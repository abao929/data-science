WITH subquery as (
  SELECT
    movies.original_title, movies.budget, movies.release_date
  FROM
    movies
  WHERE (movies.original_title = 'John Carter')
)
SELECT
  original_title, budget, release_date
FROM
  subquery
UNION
SELECT
  movies.original_title, movies.budget, movies.release_date
FROM  subquery, movies
WHERE date(subquery.release_date, '+9 days') = movies.release_date;