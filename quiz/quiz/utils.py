import pandas as pd

def getAimeProblems():
    problems = pd.read_csv('bmt-problems.csv')
    df_3_3_5 = problems[(problems['difficulty'] >= 3) & (problems['difficulty'] <= 3.5)]
    df_4_4_5 = problems[(problems['difficulty'] >= 4) & (problems['difficulty'] <= 4.5)]
    df_5_5_5 = problems[(problems['difficulty'] >= 5) & (problems['difficulty'] <= 5.5)]
    df_6_7 = problems[(problems['difficulty'] >= 6) & (problems['difficulty'] <= 7)]
    sample_3_3_5 = df_3_3_5.sample(n=5)
    sample_4_4_5 = df_4_4_5.sample(n=4)
    sample_5_5_5 = df_5_5_5.sample(n=3)
    sample_6_7 = df_6_7.sample(n=3)
    return pd.concat([sample_3_3_5, sample_4_4_5, sample_5_5_5, sample_6_7])