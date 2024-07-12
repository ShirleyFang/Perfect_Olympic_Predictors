# Perfect_Olympic_Predictors

Project Overview:

Our project aims to use Python to analyze and predict Paris 2024 Olympic medal winners!

Using datasets from the Tokyo 2020 Olympic Games, we hypothesize that countries which have won medals in previous Olympics are more likely to win again in the future. Based on this hypothesis, we aim to predict the likelihood of each country winning a medal at the Paris 2024 Olympic Games. Our model considers various influencing factors, including the probability of a country winning any medal in the past and the percentage of winning teams sent from each country.

    A country's probability of winning in the past is calculated as the number of medals won by the country divided by the total number of medals possible to win (number of sporting disciplines multiplied by three (for gold, silver, and bronze medals)).

    The percentage of teams sent by a country that won is calculated by the number of medals won by the country divided by the number of teams the country sent to that Olympic game.

We utilize the Naive Bayes algorithm to train our machine learning model.

    P(A1 | B1, B2) = P(A1) * P(B1 | A1) * P(B2 | A1)

By leveraging Naive Bayes and historical Olympic data, this project provides a data-driven approach to predict Olympic outcomes, potentially aiding in strategic planning and preparation for future Olympic Games.
