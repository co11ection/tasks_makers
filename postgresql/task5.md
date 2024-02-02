SELECT title FROM work WHERE totalwords > (SELECT AVG(totalwords) FROM work);
