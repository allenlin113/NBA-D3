import pandas as pd
import csv

stats = pd.read_html('http://www.basketball-reference.com/leagues/NBA_2016_per_game.html')
stats = stats[0]

#Remove Rank (indexing) and TOT from Team
stats = stats[stats.Rk != 'Rk']
stats = stats[stats.Tm != 'TOT']

#Drop categories
stats.drop(['Rk', 'Age', 'GS', 'eFG%',  'ORB', 'DRB', 'PF', 'Tm',
            'FG%', '3P%', '2P%', 'FT%'], axis=1, inplace=True)

stats[['G', 'MP', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PS/G', 'FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA']] = stats[['G', 'MP', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PS/G', 'FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA']].apply(pd.to_numeric)

#Calculate Season Total for stats
stats['MP'] = stats['MP'] * stats['G']
stats['TRB'] = stats['TRB'] * stats['G']
stats['AST'] = stats['AST'] * stats['G']
stats['STL'] = stats['STL'] * stats['G']
stats['BLK'] = stats['BLK'] * stats['G']
stats['TOV'] = stats['TOV'] * stats['G']
stats['PS/G'] = stats['PS/G'] * stats['G']
stats['FG'] = stats['FG'] * stats['G']
stats['FGA'] = stats['FGA'] * stats['G']
stats['3P'] = stats['3P'] * stats['G']
stats['3PA'] = stats['3PA'] * stats['G']
stats['2P'] = stats['2P'] * stats['G']
stats['2PA'] = stats['2PA'] * stats['G']
stats['FT'] = stats['FT'] * stats['G']
stats['FTA'] = stats['FTA'] * stats['G']


#Sort players by position
stats = stats.sort_values(['Pos'], ascending=True)

#Drop Player names category
stats.drop(['G', 'Player'], axis=1, inplace=True)

#Group stats by team
stats = stats.groupby('Pos').sum().reset_index()


#Calculate Per 36 Minutes Averages for Player Per Position
stats['TRB'] = stats['TRB'] / stats['MP'] * 36
stats['AST'] = stats['AST'] / stats['MP'] * 36
stats['STL'] = stats['STL'] / stats['MP'] * 36
stats['BLK'] = stats['BLK'] / stats['MP'] * 36
stats['TOV'] = stats['TOV'] / stats['MP'] * 36
stats['PS/G'] = stats['PS/G'] / stats['MP'] * 36

stats['FG'] = stats['FG'] / stats['MP'] * 36
stats['FGA'] = stats['FGA'] / stats['MP'] * 36
stats['3P'] = stats['3P'] / stats['MP'] * 36
stats['3PA'] = stats['3PA'] / stats['MP'] * 36
stats['2P'] = stats['2P'] / stats['MP'] * 36
stats['2PA'] = stats['2PA'] / stats['MP'] * 36
stats['FT'] = stats['FT'] / stats['MP'] * 36
stats['FTA'] = stats['FTA'] / stats['MP'] * 36

stats['FG%'] = stats['FG'] / stats['FGA']
stats['3P%'] = stats['3P'] / stats['3PA']
stats['2P%'] = stats['2P'] / stats['2PA']
stats['FT%'] = stats['FT'] / stats['FTA']

stats.drop(['MP', 'FG', '3P', '2P', 'FT', 'FGA', '3PA', '2PA', 'FTA'], axis=1, inplace=True)

stats = stats.sort_values(['AST'], ascending=False)

stats = stats.round(decimals=2)

columns = ['Pos', 'RB', 'AST', 'STL', 'BLK', 'TOV', 'PPG', 'FG%','3P%', '2P%', 'FT%']
stats.columns = columns;


#Convert to CSV
stats.to_csv('statsSP.csv', index=False)

