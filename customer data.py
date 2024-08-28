import pandas as pd
var1=pd.read_csv("customers-100.csv")
# print(var1)


#head function (from the first 5 records will be printed  )

# print(var1.head())
# print(var1.head(99))#diplays the number of records given in the brackets from the first.
# print(var1.tail(67))#opposite to head>>,.(reverse)
#
# filter_record=var1['Customer Id']
# print(filter_record)

# #
filter_record=var1['Subscription Date']
# print(filter_record)
# print(type(filter_record))


#
# filter_record=var1['Phone 2']
# print(filter_record)


# print(filter_record[0])
# # print(type(filter_record[0]))
# pd.set_option('display.max_rows',None)
# pd.set_option('display.max_columns',None)
# print(var1)
# filter_record1=var1[var1['First Name'].str.startswith('C')]
# print(filter_record1)
#
# var1['Subscription Date']=pd.to_datetime(var1['Subscription Date'])
# print(var1)
# filter_record=var1['Subscription Date']
# print(type(filter_record[67]))
# # print(filter_record[67].dtype)


#homework



# var2=pd.read_csv("customers-1000.csv")
# var2['Subscription Date']=pd.to_datetime(var1['Subscription Date'])

var3=pd.read_csv("organizations-100.csv")
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
print(var3)

filter_record123=var3[var3['Founded']>2000]
print(filter_record123)




