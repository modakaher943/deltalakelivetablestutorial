import dlt

#Products expections
product_rules={
    "rule_1" : "product_id is not null",
    "rule_2" : "price >=0"
}

#Infesting products
@dlt.table(
    name="products_stg"
)
@dlt.expect_all_or_drop(product_rules)
def products_stg():
    df= spark.readStream.table("dltprasad.source.products")
    return df