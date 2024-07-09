from src import masks
from src import utils


sample_card_number_1 = "4200568974529687"
sample_card_number_2 = "420O568974529687"
sample_account_number_1 = "73654108430135874305"
sample_account_number_2 = "736541084301358743053"

if __name__ == "__main__":
    masks.get_mask_account(sample_account_number_1)
    masks.get_mask_account(sample_account_number_2)
    masks.get_mask_card_number(sample_card_number_1)
    masks.get_mask_card_number(sample_card_number_2)
    utils.import_transactions("./data/operations.json")
