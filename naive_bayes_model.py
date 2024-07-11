import pandas as pd
import numpy as np


def main():
    teams_file = "./olympic2021data/Teams.xlsx"
    medals_file = "./olympic2021data/Medals.xlsx"

    # Cleaning teams dataset
    df_teams = pd.read_excel(teams_file, sheet_name="Details")
    df_teams = df_teams.drop(['Name', 'Event'], axis=1)

    # Cleaning medals dataset
    df_medals = pd.read_excel(medals_file, sheet_name="Details")
    df_medals = df_medals.drop(['Rank', 'Rank by Total', 'Gold', 'Silver', "Bronze"], axis=1)

    # Calculating probs
    # ## Probability that a team wins a medal
    country_teams = df_teams.groupby('NOC').count().rename(columns={'Discipline': 'Teams'})

    # How to get info from each dataset
    # print(country_teams.loc['Argentina', 'Teams'])
    # print(df_medals.loc[df_medals['Team/NOC'] == 'Japan', 'Total'].values[0])

    



main()
