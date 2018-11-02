## The challenges!

This challenge uses only SQL queries. Please submit answers in a markdown file.

1. Using the same tennis data, find the number of matches played by
   each player in each tournament. (Remember that a player can be
   present as both player1 or player2).

   ```
   query = '''
   SELECT player, COUNT(player)
   FROM
   (SELECT player1 as player
   FROM us_men_2013
   UNION ALL
   SELECT player2 as player
   FROM us_men_2013) AS t_1
   GROUP BY player
   '''
   
   pd.read_sql_query(query, cnx)
   ```

2. Who has played the most matches total in all of US Open, AUST Open, 
   French Open? Answer this both for men and women.

   ```
   query = '''
   SELECT player, COUNT(player) as count
   FROM
   (SELECT player1 as player
   FROM us_men_2013
   UNION ALL
   SELECT player2 as player
   FROM us_men_2013
   UNION ALL
   SELECT player1 as player
   FROM french_men_2013
   UNION ALL
   select player2 as player
   FROM french_men_2013
   UNION ALL
   SELECT player1 as player
   FROM aus_men_2013
   UNION ALL
   select player2 as player
   FROM aus_men_2013
   UNION ALL
   SELECT player1 as player
   FROM wimbledon_men_2013
   UNION ALL
   select player2 as player
   FROM wimbledon_men_2013) AS t_1
   GROUP BY player
   ORDER BY count DESC
   '''
   
   pd.read_sql_query(query, cnx)
   ```

   **Answer: Rafael Nadal (21), Serena Williams (21)**

3. Who has the highest first serve percentage? (Just the maximum value
   in a single match.)

4. What are the unforced error percentages of the top three players
   with the most wins? (Unforced error percentage is % of points lost
   due to unforced errors. In a match, you have fields for number of
   points won by each player, and number of unforced errors for each
   field.)

*Hint:* `SUM(double_faults)` sums the contents of an entire column. For each row, to add the field values from two columns, the syntax `SELECT name, double_faults + unforced_errors` can be used.

*Special bonus hint:* To be careful about handling possible ties, consider using [rank functions](http://www.sql-tutorial.ru/en/book_rank_dense_rank_functions.html).