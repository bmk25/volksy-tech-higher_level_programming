-- 14th
SELECT g.name
FROM tv_show_genres AS sg INNER JOIN tv_genres AS g ON genre_id = id
WHERE sg.show_id = (SELECT id FROM tv_shows WHERE title ="Dexter");
