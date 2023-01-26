import os
import pandas as pd
import env

def sql_mall_data():
    sql_query = """
                SELECT * 
                FROM customers
                """
    df = pd.read_sql(sql_query, env.get_connection('mall_customers'))
    return df

def get_mall_data():
    if os.path.isfile('mall_customers.csv'):
        df = pd.read_csv('mall_customers.csv', index_col=0)
    else:
        df = sql_mall_data()
        df.to_csv('mall_customers.csv')
    return df


def sql_zillow_data():
    sql_query = """
                select prop.parcelid as parcel_id, prop.id as property_id, prop.bathroomcnt, prop.bedroomcnt, prop.regionidzip, prop.yearbuilt, prop.calculatedfinishedsquarefeet, prop.fips, prop.taxvaluedollarcnt
                from predictions_2017 as pred
                join properties_2017 as prop 
                on pred.parcelid = prop.parcelid
                where transactiondate is not null and
                propertylandusetypeid = 261 and
                regionidzip is not null and
                yearbuilt is not null and
                calculatedfinishedsquarefeet is not null and
                prop.taxvaluedollarcnt is not null;
                """
    df = pd.read_sql(sql_query, env.get_connection('zillow'))
    return df

def get_zillow_data():
    if os.path.isfile('zillow.csv'):
        df = pd.read_csv('zillow.csv', index_col=0)
    else:
        df = sql_zillow_data()
        df.to_csv('zillow.csv')
    return df