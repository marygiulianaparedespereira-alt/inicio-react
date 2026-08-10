SELECT  c.FirstName, c.LastName, c.Address, i.InvoiceDate FROM customers c
JOIN invoices i on c.CustomerId = i.CustomerId
ORDER by c.LastName

SELECT * FROM artists
JOIN albums ON artists.ArtistId = albums.ArtistId
JOIN tracks ON albums.AlbumId = tracks.AlbumId
JOIN genres ON tracks.GenreId = genres.GenreId
WHERE UnitPrice = 0.99;



SELECT tracks.name, tracks.Milliseconds, albums.Title, artists.name FROM tracks
JOIN albums ON artists.ArtistId = albums.ArtistId
JOIN artists ON albums.ArtistId = albums.AlbumId
JOIN genres ON tracks.GenreId = genres.GenreId
ORDER BY tracks.Milliseconds ASC
LIMIT 20;


SELECT e.LastName AS "apellido_empleado", j.LastName AS "ape_jefe", e.Title, COUNT(c.CustomerId)  FROM  employees e
JOIN employees j ON e.ReportsTo = j.EmployeeId
JOIN customers c  ON e.EmployeeId = c.SupportRepId
GROUP BY e.EmployeeId

SELECT e.FirstName , e.LastName, c.FirstName, c.LastName FROM employees e
JOIN customers c on e.EmployeeId = c.SupportRepId
ORDER by e.LastName
SELECT c.FirstName, c.LastName, c.Address, i.InvoiceId
FROM customers c
JOIN invoices i
ON c.CustomerId=i.CustomerId;


SELECT g.Name,
COUNT(*) Cantidad
FROM genres g
JOIN tracks t
ON g.GenreId=t.GenreId
GROUP BY g.Name
ORDER BY Cantidad DESC;


SELECT DISTINCT c.FirstName, c.LastName, ar.Name
FROM customers c JOIN invoices i ON c.CustomerId=i.CustomerId
JOIN invoice_items ii ON i.InvoiceId=ii.InvoiceId
JOIN tracks t ON ii.TrackId=t.TrackId
JOIN albums al ON t.AlbumId=al.AlbumId
JOIN artists ar ON al.ArtistId=ar.ArtistId
ORDER BY c.LastName;

SELECT c.FirstName, c.LastName, c.City, t.Name, g.Name FROM customers c
JOIN invoices i ON c.CustomerId=i.CustomerId
JOIN invoice_items ii ON i.InvoiceId=ii.InvoiceId
JOIN tracks t ON ii.TrackId=t.TrackId
JOIN genres g ON t.GenreId=g.GenreId;


SELECT * FROM customers c
JOIN invoices i ON c.CustomerId = i.CustomerId
JOIN invoice_items ii ON i.InvoiceId = ii.InvoiceId
JOIN tracks t ON ii.TrackId = t.TrackId
JOIN albums a ON t.AlbumId = a.AlbumId
JOIN artists ar ON a.ArtistId = ar.ArtistId
JOIN genres g ON t.GenreId = g.GenreId
JOIN media_types mt ON t.MediaTypeId = mt.MediaTypeId
JOIN playlist_track pt ON t.TrackId = pt.TrackId
JOIN playlists p ON pt.PlaylistId = p.PlaylistId
JOIN employees e ON c.SupportRepld=e.EmployeeID



