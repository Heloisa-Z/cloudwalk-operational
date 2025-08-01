import os
import pandas as pd

OUTPUT_DIR = 'output'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def normalizar_time(df, col='time'):
    df[col] = df[col].astype(str).str.split(' ').str[0]
    return df

def juntar_transactions_checkout():
    trans1 = pd.read_csv('data/transactions_1.csv')
    trans2 = pd.read_csv('data/transactions_2.csv')
    check1 = pd.read_csv('data/checkout_1.csv')
    check2 = pd.read_csv('data/checkout_2.csv')

    trans1 = normalizar_time(trans1)
    trans2 = normalizar_time(trans2)
    checkout = normalizar_time(pd.concat([check1, check2], ignore_index=True))

    transactions = pd.concat([trans1, trans2], ignore_index=True)

    df_joined = pd.merge(
        transactions,
        checkout,
        on='time',
        how='left'
    )

    if 'count' in df_joined.columns:
        df_joined.drop(columns=['count'], inplace=True)

    #save
    output_path = os.path.join(OUTPUT_DIR, 'transactions_checkout_unificado.csv')
    df_joined.to_csv(output_path, index=False)
    print("file saved successfully:", output_path)

    return df_joined

def main():
    juntar_transactions_checkout()

if __name__ == "__main__":
    main()