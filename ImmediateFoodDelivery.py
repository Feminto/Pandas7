# Method 1
import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immediate = 0
    for i in range(len(delivery)):
        od = delivery['order_date'][i]
        prf_d = delivery['customer_pref_delivery_date'][i]

        if od == prf_d:
            immediate += 1
    
    result = round((immediate / len(delivery)) * 100,2)

    return pd.DataFrame([result], columns = ['immediate_percentage'])

# Method 2
import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immediate = delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']]

    result = round((len(immediate) / len(delivery)) * 100 , 2)

    return pd.DataFrame([result], columns = ['immediate_percentage'])