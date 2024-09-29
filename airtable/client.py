from pyairtable import Api
import pandas as pd
#import numpy as np

class AirtableFinClient:

    def __init__(
            self,
            api_key: str,
            base_id: str,
            tbl_months_id: str
    ):
        self.api = Api(api_key)
        self.tbl_months = self.api.table(base_id, tbl_months_id)

    def all_months(self) -> list[dict]:
        extracted_data = []
        for record in self.tbl_months.all():
            fields = record['fields']
            extracted_record = {
                'year': fields['year'],
                'month': fields['month'],
                'income': fields['income'],
                'outcome': fields['outcome'],
                'saving': fields.get('saving', 0), 
                'closed': fields.get('closed', False),
                'withdrawals': fields.get('withdrawals', 0)  
            }
            extracted_data.append(extracted_record)
        return extracted_data
    
    def all_months_df(self):
        df = pd.DataFrame(self.all_months())

        df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'].astype(str).str.zfill(2) + '-01')
        df = df.sort_values('date').reset_index(drop=True)

        df['availability'] = 0.0

        for i in range(len(df)):
            if i == 0:
                df.loc[i, 'availability'] = 0.0
            else:
                df.loc[i, 'availability'] = df.loc[i-1, 'availability'] + df.loc[i-1, 'saving'] - df.loc[i, 'withdrawals']

        df['balance'] = df['income'].cumsum() - df['outcome'].cumsum() # + df['saving'].cumsum() - df['withdrawals'].cumsum()

        df = df.sort_values('date', ascending=False).reset_index(drop=True)

        return df[['year', 'month', 'income', 'outcome', 'saving', 'withdrawals', 'availability', 'balance', 'closed']]