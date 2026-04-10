import dlt

#Sales expections
sales_rules={
   "rule_1" : "sales_id Is not null"  
}

#Empty sterming table
dlt.create_streaming_table(
    name = "sales_stg",
    expect_all_or_drop = sales_rules
)

#creating east flow
@dlt.append_flow(target="sales_stg")
def east_Sales():
    df = spark.readStream.table("dltprasad.source.sales_east")
    return df

#creating west flow
@dlt.append_flow(target="sales_stg")
def west_Sales():
    df = spark.readStream.table("dltprasad.source.sales_west")
    return df