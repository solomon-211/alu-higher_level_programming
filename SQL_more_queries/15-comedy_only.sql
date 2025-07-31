-- Lists all Comedy shows alphabetically
SELECT s.title
FROM tv_shows s
INNER JOIN tv_show_genres sg ON s.id = sg.show_id
INNER JOIN tv_genres g ON g.id = sg.genre_id
WHERE g.name = 'Comedy'
ORDER BY s.title;
