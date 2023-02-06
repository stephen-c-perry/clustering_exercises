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
                    SELECT prop.*, predictions_2017.logerror, predictions_2017.transactiondate, 
                            air.airconditioningdesc, arch.architecturalstyledesc, build.buildingclassdesc, 
                            heat.heatingorsystemdesc, land.propertylandusedesc, story.storydesc, 
                            type.typeconstructiondesc
                    FROM properties_2017 prop
                    JOIN (
                        SELECT parcelid, MAX(transactiondate) AS max_transactiondate
                        FROM predictions_2017
                        GROUP BY parcelid
                    ) pred 
                    ON prop.parcelid = pred.parcelid
                    JOIN predictions_2017 
                    ON pred.parcelid = predictions_2017.parcelid
                    AND pred.max_transactiondate = predictions_2017.transactiondate
                    LEFT JOIN airconditioningtype air 
                    ON prop.airconditioningtypeid = air.airconditioningtypeid
                    LEFT JOIN architecturalstyletype arch 
                    ON prop.architecturalstyletypeid = arch.architecturalstyletypeid
                    LEFT JOIN buildingclasstype build 
                    ON prop.buildingclasstypeid = build.buildingclasstypeid
                    LEFT JOIN heatingorsystemtype heat 
                    ON prop.heatingorsystemtypeid = heat.heatingorsystemtypeid
                    LEFT JOIN propertylandusetype land 
                    ON prop.propertylandusetypeid = land.propertylandusetypeid
                    LEFT JOIN storytype story 
                    ON prop.storytypeid = story.storytypeid
                    LEFT JOIN typeconstructiontype type 
                    ON prop.typeconstructiontypeid = type.typeconstructiontypeid
                    WHERE propertylandusedesc = "Single Family Residential"
                    AND transactiondate <= '2017-12-31'
                    AND prop.longitude IS NOT NULL
                    AND prop.latitude IS NOT NULL;

                """
    df = pd.read_sql(sql_query, env.get_connection('zillow'))
    return df


def get_zillow_data():
    if os.path.isfile('zillow_trim.csv'):
        df = pd.read_csv('zillow_trim.csv', index_col=0)
    else:
        df = sql_zillow_data()
        df.to_csv('zillow_trim.csv')
    return df
