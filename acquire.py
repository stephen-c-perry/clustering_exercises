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
                    SELECT prop.*,
                        predictions_2017.logerror,
                        predictions_2017.transactiondate as Transaction_Date,
                        air.airconditioningdesc as AC_type,
                        arch.architecturalstyledesc as Architectural_Style,
                        build.buildingclassdesc as Building_Class,
                        heat.heatingorsystemdesc as Heating_or_System,
                        land.propertylandusedesc as Property_Land_Use,
                        story.storydesc as Stories,
                        type.typeconstructiondesc as Construction_Type
                    FROM properties_2017 prop
                    JOIN (
                        SELECT parcelid, MAX(transactiondate) AS Max_Transaction_Date
                        FROM predictions_2017
                        GROUP BY parcelid
                        ) pred USING(parcelid)
                    JOIN predictions_2017 ON pred.parcelid = predictions_2017.parcelid
                        AND pred.max_transactiondate = predictions_2017.transactiondate
                    LEFT JOIN airconditioningtype USING(airconditioningtypeid)
                    LEFT JOIN architecturalstyletype USING(architecturalstyletypeid)
                    LEFT JOIN buildingclasstype USING(buildingclasstypeid)
                    LEFT JOIN heatingorsystemtype USING(heatingorsystemtypeid)
                    LEFT JOIN propertylandusetype USING(propertylandusetypeid)
                    LEFT JOIN storytype USING(storytypeid)
                    LEFT JOIN typeconstructiontype USING(typeconstructiontypeid)
                    WHERE propertylandusedesc = "Single Family Residential"
                        AND transactiondate <= '2017-12-31'
                        AND prop.longitude IS NOT NULL
                        AND prop.latitude IS NOT NULL
                """
    df = pd.read_sql(sql_query, env.get_connection('zillow'))
    return df




'''
  SELECT prop.*,
        predictions_2017.logerror,
        predictions_2017.transactiondate as Transaction_Date,
        air.airconditioningdesc as A/C_type,
        arch.architecturalstyledesc as Architectural_Style,
        build.buildingclassdesc as Building_Class,
        heat.heatingorsystemdesc as Heating_or_System,
        land.propertylandusedesc as Property_Land_Use,
        story.storydesc as Stories,
        type.typeconstructiondesc as Construction_Type
        FROM properties_2017 prop
        JOIN (
            SELECT parcelid, MAX(transactiondate) AS Max_Transaction_Date
            FROM predictions_2017
            GROUP BY parcelid
            ) pred USING(parcelid)
        JOIN predictions_2017 ON pred.parcelid = predictions_2017.parcelid
                          AND pred.max_transactiondate = predictions_2017.transactiondate
        LEFT JOIN airconditioningtype air USING(airconditioningtypeid)
        LEFT JOIN architecturalstyletype arch USING(architecturalstyletypeid)
        LEFT JOIN buildingclasstype build USING(buildingclasstypeid)
        LEFT JOIN heatingorsystemtype heat USING(heatingorsystemtypeid)
        LEFT JOIN propertylandusetype land USING(propertylandusetypeid)
        LEFT JOIN storytype story USING(storytypeid)
        LEFT JOIN typeconstructiontype type USING(typeconstructiontypeid)
        WHERE propertylandusedesc = "Single Family Residential"
            AND transactiondate <= '2017-12-31'
            AND prop.longitude IS NOT NULL
            AND prop.latitude IS NOT NULL
'''



def get_zillow_data():
    if os.path.isfile('zillow.csv'):
        df = pd.read_csv('zillow.csv', index_col=0)
    else:
        df = sql_zillow_data()
        df.to_csv('zillow.csv')
    return df





#original query brought over from regression project
    '''
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
    '''