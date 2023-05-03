import pandas as pd

excel_to_df = pd.read_excel('qrcodes.xlsx', sheet_name='Sheet1')

excel_data_fragment = excel_to_df.where(pd.notnull(excel_to_df), None)

qr_code_table_list = excel_data_fragment.values.tolist()
print(qr_code_table_list)
print(len(qr_code_table_list))
with open('qr_code_whole_table.txt', 'w') as fp:
    fp.write(str(qr_code_table_list))

# excel_to_df = pd.read_excel('qrcodes_1.xlsx', sheet_name='Sheet3')
# new_qr_codes_list = excel_to_df['NEWQRCodes'].tolist()
# print(new_qr_codes_list)
# print(len(new_qr_codes_list))
#
# with open('new_qr_code_list.txt', 'w') as fp:
#     fp.write(str(new_qr_codes_list))
