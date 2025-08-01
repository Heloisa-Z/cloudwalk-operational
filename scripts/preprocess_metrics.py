import os
import pandas as pd
import numpy as np

OUTPUT_DIR = 'output'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def carregar_dados():
    df = pd.read_csv(os.path.join(OUTPUT_DIR, 'transactions_consolidados.csv'))
    return df

def preprocessar(df):
    #'day' to datetime
    df['day'] = pd.to_datetime(df['day'], errors='coerce')
    
    # weekday
    df['weekday'] = df['day'].dt.day_name()
    
    # month and year
    df['month_year'] = df['day'].dt.to_period('M').astype(str)
    
    # average ticket
    df['ticket_medio'] = df.apply(
        lambda r: r['amount_transacted'] / r['quantity_transactions'] if r['quantity_transactions'] > 0 else 0,
        axis=1
    )
    
    # transactions per merchant
    df['transactions_per_merchant'] = df.apply(
        lambda r: r['quantity_transactions'] / r['quantity_of_merchants'] if r['quantity_of_merchants'] > 0 else 0,
        axis=1
    )
    
    # amount per merchant
    df['amount_per_merchant'] = df.apply(
        lambda r: r['amount_transacted'] / r['quantity_of_merchants'] if r['quantity_of_merchants'] > 0 else 0,
        axis=1
    )
    
    # avg installment value
    df['avg_installment_value'] = df.apply(
        lambda r: r['amount_transacted'] / r['installments'] if r['installments'] > 0 else 0,
        axis=1
    )
    
    # log of the amount transacted for analysis
    df['log_amount_transacted'] = np.log1p(df['amount_transacted'])
    
    # flag if average ticket is higher than overall average
    avg_ticket_global = df['ticket_medio'].mean()
    df['is_high_ticket'] = df['ticket_medio'] > avg_ticket_global
    
    return df

#save
def salvar_csv(df):
    output_path = os.path.join(OUTPUT_DIR, 'transactions_preprocessados.csv')
    df.to_csv(output_path, index=False)
    print(f"file saved successfully: {output_path}")

def main():
    df = carregar_dados()
    df = preprocessar(df)
    salvar_csv(df)

if __name__ == '__main__':
    main()