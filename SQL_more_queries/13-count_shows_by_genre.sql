-- 13th
SELECT g.name AS genre,COUNT(sg.genre_id) AS number_of_shows
FROM tv_show_genres AS sg INNER JOIN tv_genres AS g ON genre_id = id
GROUP BY genre_id
ORDER BY number_of_shows DESC;
