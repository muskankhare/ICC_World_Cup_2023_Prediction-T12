# ICC World Cup 2023 predictions

In this course project, we strive to employ advanced data mining methods to provide valuable insights for decision-making during the ODI Cricket World Cup 2023. The project focuses on three crucial aspects: assessing the individual performance of players, predicting match scores, and anticipating outcomes for both finals and semifinals. Additionally, our endeavor extends to offering strategic recommendations by predicting the playing XI for teams in the finals, contributing to a comprehensive analysis of the tournament.

## Team 12-Gold Diggers

### Individual Contributions:
| Student ID  |   Name   |     Task      |
|-------------|----------|---------------|
| 202218003 | Rahul Upadhyay   | Row 1, Col 3 |
| 202218037 | Muskan Khare     | Row 2, Col 3 |
| 202218061 | Jatan Sahu       | Row 3, Col 3 |
| 202218063 | Bhoomi Prajapati | Row 3, Col 3 |
| 202101201 | Bhargav Vidja    | Row 3, Col 3 |

## DATASETS:

The dataset comprises files from kaggle. 

Dataset 1: [ICC Mens World Cup 2023](https://www.kaggle.com/datasets/pardeep19singh/icc-mens-world-cup-2023)

Dataset2: [ODI Men's Cricket Match Data (2002-2023)](https://www.kaggle.com/datasets/utkarshtomar736/odi-mens-cricket-match-data-2002-2023)

### Dataset Description:

* **ODI_Match_Data.csv**

| Column Name           | Description                                                              |
|------------------------|--------------------------------------------------------------------------|
| match_id               | A unique identifier for each ODI cricket match.                          |
| season                 | The season in which the match took place.                                 |
| start_date             | The date on which the match started.                                      |
| venue                  | The stadium or venue where the match was played.                          |
| innings                | The innings number (1st innings or 2nd innings).                          |
| ball                   | A numeric representation of the ball number bowled in the innings.       |
| batting_team           | The name of the batting team for the current innings.                     |
| bowling_team           | The name of the bowling team for the current innings.                     |
| striker                | The batsman who is currently facing the ball.                             |
| non_striker            | The batsman at the non-striker's end.                                     |
| bowler                 | The bowler who is delivering the ball.                                    |
| runs_off_bat           | The number of runs scored off the bat (excluding extras).                |
| extras                | The total number of extra runs (wides, no-balls, byes, leg-byes, penalty) in the current ball. |
| wides                  | The number of wide deliveries bowled in the current ball.                 |
| noballs               | The number of no-ball deliveries bowled in the current ball.              |
| byes                   | The number of byes scored in the current ball.                            |
| legbyes               | The number of leg-byes scored in the current ball.                        |
| penalty               | The number of penalty runs awarded in the current ball.                   |
| wicket_type           | The type of wicket taken in the current ball (e.g., caught, bowled, run out). |
| player_dismissed      | The player who was dismissed in the current ball.                         |
| other_wicket_type     | Additional information about the wicket (if any) in the current ball.    |
| other_player_dismissed| Additional player information related to the wicket (if any) in the current ball. |
| cricsheet_id          | A unique identifier for the match from Cricsheet.                         |




* **ODI_Match_info.csv**

| Column Name      | Description                                                           |
|-------------------------|-----------------------------------------------------------------|
| id                | A unique identifier for each cricket match.                           |
| season            | The season or year in which the match took place.                      |
| city              | The city where the match was held.                                    |
| date              | The date on which the match was played.                               |
| team1             | The name of the first cricket team participating in the match.        |
| team2             | The name of the second cricket team participating in the match.       |
| toss_winner       | The team that won the toss.                                           |
| toss_decision     | The decision made by the toss-winning team (bat or field).            |
| result            | The result of the match (e.g., "normal," "tie," "no result").         |
| dl_applied        | An indicator of whether the Duckworth-Lewis method was applied (1 for applied, 0 for not applied). |
| winner            | The winning team of the match.                                        |
| win_by_runs       | The margin of victory in runs (0 for wickets, if not applicable).    |
| win_by_wickets    | The margin of victory in wickets (0 for runs, if not applicable).    |
| player_of_match   | The player awarded the "Man of the Match" title.                      |
| venue             | The stadium or venue where the match was played.                      |
| umpire1           | The name of the first on-field umpire.                                |
| umpire2           | The name of the second on-field umpire.                               |
| umpire3           | The name of the third umpire (TV umpire).                             |



* **deliveries.csv**

| Column Name          | Description                                               |
|-----------------------|-----------------------------------------------------------|
| match_id              | Unique identifier for each cricket match.                 |
| season                | The specific season in which the cricket match took place.|
| start_date            | The date when the match started.                           |
| venue                 | The location where the cricket match was held.             |
| innings               | The inning number during which the event occurred.        |
| ball                  | The ball number within the inning.                         |
| batting_team          | The team currently batting.                                |
| bowling_team          | The team currently bowling.                                |
| striker               | The batsman facing the current ball.                       |
| non_striker           | The batsman at the non-striker's end.                      |
| bowler                | The player bowling the current ball.                       |
| runs_off_bat          | Runs scored off the bat on the current ball.               |
| extras                | Additional runs scored, not from the bat (e.g., wides, no-balls). |
| wides                 | The number of wide deliveries bowled.                     |
| noballs               | The number of no-ball deliveries bowled.                  |
| byes                  | Runs scored as byes on the current ball.                  |
| legbyes               | Runs scored as leg-byes on the current ball.              |
| penalty               | Penalty runs awarded on the current ball.                 |
| wicket_type           | Type of dismissal if a wicket fell on the current ball.   |
| player_dismissed      | Batsman dismissed on the current ball.                    |
| other_wicket_type     | Additional information about the type of dismissal.       |
| other_player_dismissed| Additional player dismissed on the current ball.          |




* **matches.csv**
  
| Column Name      | Description                                                   |
|-------------------|---------------------------------------------------------------|
| season            | The cricket season in which the match occurred.                |
| team1             | The first team participating in the match.                      |
| team2             | The second team participating in the match.                     |
| date              | The date on which the match took place.                         |
| match_number      | Unique identifier for the match in the season.                  |
| venue             | The stadium or ground where the match was held.                 |
| city              | The city where the match was played.                            |
| toss_winner       | The team winning the toss.                                      |
| toss_decision     | Decision taken by the toss-winning team (batting or bowling).  |
| player_of_match   | The outstanding player of the match.                            |
| umpire1           | The first on-field umpire for the match.                        |
| umpire2           | The second on-field umpire for the match.                       |
| reserve_umpire    | The reserve umpire designated for the match.                    |
| match_referee     | The official responsible for overseeing the match.              |
| winner            | The team that emerged victorious in the match.                 |
| winner_runs       | The margin of victory in terms of runs.                         |
| winner_wickets    | The number of wickets by which the winning team achieved victory.|
| match_type        | The type of cricket match (e.g., Test, One Day International, T20).|




* **points_table.csv**
  
| Column Name | Description                                                     |
|-------------|-----------------------------------------------------------------|
| Ranking     | The position or order of the team in the current standings.     |
| Team        | The name of the cricket team.                                    |
| Matches     | Total number of matches played by the team.                     |
| Won         | Number of matches won by the team.                              |
| Lost        | Number of matches lost by the team.                             |
| Tie         | Number of matches that ended in a tie for the team.             |
| No Results  | Number of matches with no result for the team.                  |
| Points      | Total points accumulated by the team in the ranking.            |
| Net Run Rate| The net run rate calculated for the team.                       |
| Series Form | Performance trend of the team in recent series.                 |
| Next Match  | Details of the team's upcoming match.                           |
| For         | Total runs scored by the team in all matches.                   |
| Against     | Total runs conceded by the team in all matches.                 |




