import dlt

#Customer expections
customer_rules={
    "rule_1":"customer_id is not null",
    "rule_2":"customer_name is not null"
}

#Ingesting customers
@dlt.table(
    name="customers_stg"
)
@dlt.expect_all_or_drop(customer_rules)
def customers_stg():
    df= spark.readStream.table("dltprasad.source.customers")
    return df