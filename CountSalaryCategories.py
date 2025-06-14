# Method 1
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = 0
    avg = 0
    hgh = 0

    for i in range(len(accounts)):
        inc = accounts['income'][i]

        if inc < 20000:
            low += 1
        elif inc >= 20000 and inc <= 50000:
            avg += 1
        else:
            hgh += 1
    
    df = [['Low Salary', low], ['Average Salary', avg], ['High Salary', hgh]]
    # print(df)

    return pd.DataFrame(df, columns = ['category','accounts_count'])


# Method 2
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = accounts[accounts['income'] < 20000]
    avg = accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)]
    hgh = accounts[accounts['income'] > 50000]
    
    df = [['Low Salary', len(low)], ['Average Salary', len(avg)], ['High Salary', len(hgh)]]

    return pd.DataFrame(df, columns = ['category','accounts_count'])