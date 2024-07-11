import pandas as pd
import numpy as np


def main():
    teams_file = "./Teams.xlsx"
    medals_file = "./Medals.xlsx"

    # Cleaning teams dataset
    df_teams = pd.read_excel(teams_file, sheet_name="Details")
    df_teams = df_teams.drop(['Name', 'Event'], axis=1)

    # Cleaning medals dataset
    df_medals = pd.read_excel(medals_file, sheet_name="Details")
    df_medals = df_medals.drop(['Rank', 'Rank by Total'], axis=1)

    # Calculating probs
    # ## Probability that a team wins a medal
    country_teams = df_teams.groupby("NOC").count()
    print(country_teams)


main()
