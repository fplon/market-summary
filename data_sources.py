equity_indices = {
    "S&P 500": "^GSPC",
    "russel 2000": "^RUT",  # not bang on
    "nasdaq": "^IXIC",  # composite, CCMP not NDX
    "ftse100": "^FTSE",
    "ftse250": "^FTMC",
    "stoxx50": "^STOXX50E",  # SX5P not SX5E?
    "euronext 100": "^N100",  # N100
    "msci japan": "EWJ",  # in USD
    "nikkei": "^N225",
    "msci em": "EEM",  # USD
    "sse composite": "000001.SS",  # Think this is Shanghai, not Shenzhen
    "msci ap ex japan": "AAXJ",  # USD
    "moex russia": "IMOEX.ME",
}


countries = [
    "US",
    "UK",
    "Europe...",
    "Japan",
    "China",
    "India",
    "Australia",
    "Russia",
]

macro_indicators = [
    "GDP",
    "Inflation",
    "Bank rates",
    "Producer Index",
    "Consumer Index",
    "Employment",
    "Debt",
    "Trade Balance",
    "Budget Deficit",
]

econdb_labels = {
    "fields": {
        "Real Growth": "RGDP",
        "Inflation": "CPI",
        # "Industrial Production": "IP",
        # "Consumer Confidence": "CONF",
        # "Unemployment": "URATE",
        # "Policy Rate": "POLIR",
        # "Exports": "EXP",
        # "Imports": "IMP",
        # "Current Acount": "CA",
        # ### 'House Price':,
        # "Producer Prices": "PPI",
        # "Retail Sales": "RETA",
        # "Government Balance": "GBAL",
        # "Government Debt": "GDEBT",
    },
    "countries": {
        "UK": "UK",
        # "USA": "US",
        # "Japan": "JP",
        # "Germany": "DE",
        # "France": "FR",
        # "Australia": "AU",
        # "India": "IN",
        # "China": "CN",
        # "Canada": "CA",
        # "Spain": "ES",
        # "Italy": "IT",
    },
}
