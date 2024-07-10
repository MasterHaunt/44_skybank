from src import masks, utils

sample_card_number_1 = "4200568974529687"
sample_card_number_2 = "420O568974529687"
sample_account_number_1 = "73654108430135874305"
sample_account_number_2 = "736541084301358743053"

if __name__ == "__main__":
    # masks.get_mask_account(sample_account_number_1)
    # masks.get_mask_account(sample_account_number_2)
    # masks.get_mask_card_number(sample_card_number_1)
    # masks.get_mask_card_number(sample_card_number_2)
    # print('json')
    # print(utils.import_json_transactions("./data/operations.json"))
    print('xlsx')
    print(utils.import_xlsx_transactions("./data/transactions_excel.xlsx"))
