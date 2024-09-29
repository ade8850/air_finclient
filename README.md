# air_finclient

A simple utility for analyzing personal financial data based on income, expenses, savings, and withdrawals. It calculates monthly spendable savings and your overall financial balance starting from your data.

You need an **Airtable** database with a table (months) containing the following fields:

- year
- month
- income
- outcome
- savings
- withdrawals
- closed (bool)

You also need to set the following environment variables:

- FINCLIENT_AIRTABLE_API_KEY
- FINCLIENT_AIRTABLE_BASE_ID
- FINCLIENT_AIRTABLE_TBL_MONTHS_ID

After installing the dependencies, simply run the `months.py` script to generate your report.

If you have [uv](https://github.com/astral-sh/uv) installed, just:

```
uv run months.py
```

