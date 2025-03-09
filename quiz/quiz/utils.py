import pandas as pd

<<<<<<< HEAD
def getAimeProblems():
    problems = pd.read_csv('./quiz/bmt-problems.csv', on_bad_lines='skip')
    DifVar = "Difficulty"
    df_3_3_5 = problems[(problems[DifVar] >= 3) & (problems[DifVar] <= 3.5)]
    df_4_4_5 = problems[(problems[DifVar] >= 4) & (problems[DifVar] <= 4.5)]
    df_5_5_5 = problems[(problems[DifVar] >= 5) & (problems[DifVar] <= 5.5)]
    df_6_7 = problems[(problems[DifVar] >= 6) & (problems[DifVar] <= 7)]
    sample_3_3_5 = df_3_3_5.sample(n=5)
    sample_4_4_5 = df_4_4_5.sample(n=4)
    sample_5_5_5 = df_5_5_5.sample(n=3)
    sample_6_7 = df_6_7.sample(n=3)
    return pd.concat([sample_3_3_5, sample_4_4_5, sample_5_5_5, sample_6_7])
=======
def get_sample_sizes(difficulty):
    sample_sizes = {
        1: (6, 5, 4, 0),
        2: (5, 5, 5, 0),
        3: (5, 5, 4, 1),
        4: (5, 5, 3, 2),
        5: (5, 4, 4, 2),
        6: (5, 4, 3, 3),
        7: (4, 5, 3, 3),
        8: (4, 4, 4, 3),
        9: (4, 4, 3, 4),
        10: (3, 4, 4, 4)
    }
    return sample_sizes.get(difficulty, (5, 5, 4, 1))

def getAimeProblems(difficulty):
    problems = pd.read_csv('bmt-problems.csv')
    df_3_3_5 = problems[(problems['Difficulty'] >= 3) & (problems['Difficulty'] <= 3.5)]
    df_4_4_5 = problems[(problems['Difficulty'] >= 4) & (problems['Difficulty'] <= 4.5)]
    df_5_5_5 = problems[(problems['Difficulty'] >= 5) & (problems['Difficulty'] <= 5.5)]
    df_6_7 = problems[(problems['Difficulty'] >= 6) & (problems['Difficulty'] <= 7)]
    
    sample_sizes = get_sample_sizes(difficulty)
    
    sample_3_3_5 = df_3_3_5.sample(n=sample_sizes[0])
    sample_4_4_5 = df_4_4_5.sample(n=sample_sizes[1])
    sample_5_5_5 = df_5_5_5.sample(n=sample_sizes[2])
    sample_6_7 = df_6_7.sample(n=sample_sizes[3])
    
    problems = pd.concat([sample_3_3_5, sample_4_4_5, sample_5_5_5, sample_6_7])
    max_category_count = 6
    problems = problems.groupby('category').apply(lambda x: x.sample(min(len(x), max_category_count))).reset_index(drop=True)
    return problems
>>>>>>> 372a5f6487b68296aac527480b3fd4254b0a0636
