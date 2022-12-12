import pandas as pd


def json_to_csv(data: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame()
    for index, row in data.iterrows():
        df = pd.DataFrame(data={
            'title': row['title'],
            'price': row['price'],
            'brand': row['brand'],
            'asin': row['asin'],
        }, index=[0])
        for num in range(len(row['features'])):
            key = list(row['features'][num].keys())[0]
            value = list(row['features'][num].values())[0]
            if key in ['Outer Material', 'Inner Material', 'Sole', 'Closure', 'Heel Height', 'Heel Type', 'Shoe Width']:
                df[key] = value
        result = pd.concat([result, df])
    return result
