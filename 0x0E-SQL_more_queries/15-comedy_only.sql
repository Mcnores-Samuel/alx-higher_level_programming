SELECT  show.title FROM tv_shows AS show
INNER JOIN tv_show_genres ON show.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genres_id
WHERE tv_genres.name = 'Comedy'
ORDER BY show.title;
