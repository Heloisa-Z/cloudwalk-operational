import os
import pandas as pd

OUTPUT_DIR = 'output'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def carregar_dados():
    df_ops = pd.read_csv('data/Operations_analyst_data.csv')
    df_intel = pd.read_csv('data/operational_intelligence_transactions_db.csv')
    return df_ops, df_intel

def normalizar_dados(df):
    cols_str = ['entity', 'product', 'price_tier', 'anticipation_method', 'payment_method', 'installments']
    for c in cols_str:
        if c in df.columns:
            df[c] = df[c].astype(str).str.strip().str.lower()
    return df

def juntar_e_consolidar(df_ops, df_intel):
    merge_keys = ['day', 'entity', 'product', 'price_tier', 'anticipation_method', 'payment_method', 'installments']
    df_merged = pd.merge(df_ops, df_intel, on=merge_keys, suffixes=('_op', '_oi'), how='outer')

    df_merged['amount_transacted'] = df_merged[['amount_transacted_op', 'amount_transacted_oi']].sum(axis=1, skipna=True)
    df_merged['quantity_transactions'] = df_merged[['quantity_transactions_op', 'quantity_transactions_oi']].sum(axis=1, skipna=True)

    df_merged.drop(columns=['amount_transacted_op', 'amount_transacted_oi', 'quantity_transactions_op', 'quantity_transactions_oi'], inplace=True)

    return df_merged

#save
def salvar_csv(df):
    output_path = os.path.join(OUTPUT_DIR, 'transactions_consolidados.csv')
    df.to_csv(output_path, index=False)
    print(f"file saved successfully:{output_path}")

def main():
    df_ops, df_intel = carregar_dados()
    df_ops = normalizar_dados(df_ops)
    df_intel = normalizar_dados(df_intel)
    df_final = juntar_e_consolidar(df_ops, df_intel)
    salvar_csv(df_final)

if __name__ == '__main__':
    main()