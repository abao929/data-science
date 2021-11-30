SELECT movies.original_title, movies.release_date, revenue
FROM movies
JOIN (SELECT movies2.release_date AS movies2_release_date, AVG(movies2.revenue) AS avg_revenue
    FROM movies AS movies2
    GROUP BY movies2.release_date)
    ON movies2_release_date = movies.release_date
    WHERE revenue > avg_revenue
ORDER BY movies.release_date ASC, revenue DESC;