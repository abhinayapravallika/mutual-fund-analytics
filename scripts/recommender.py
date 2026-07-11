import pandas as pd

performance = pd.read_csv("../data/processed/07_scheme_performance_clean.csv")

def recommend(risk):

    result = (

        performance

        [

            performance["risk_grade"]

            .str.lower()

            == risk.lower()

        ]

        .sort_values(

            "sharpe_ratio",

            ascending=False

        )

        [

            [

                "scheme_name",

                "fund_house",

                "category",

                "risk_grade",

                "sharpe_ratio"

            ]

        ]

        .head(3)

    )

    print(result)

risk = input("Risk Appetite (Low/Moderate/High): ")

recommend(risk)