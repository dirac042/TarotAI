import pandas as pd


class PandasToList:
    def up_deck(self, up_file):
        df_up_tarot = pd.read_csv(up_file)
        list_up_card = df_up_tarot["CARD"].values
        list_up_desc = df_up_tarot["DESCRIPTION"].values
        list_up_tarot = [[card, desc] for card, desc in zip(list_up_card, list_up_desc)]
        return list_up_tarot

    def rev_deck(self, rev_file):
        df_rev_tarot = pd.read_csv(rev_file)
        list_rev_card = df_rev_tarot["CARD"].values
        list_rev_desc = df_rev_tarot["DESCRIPTION"].values
        list_rev_tarot = [
            [card, desc] for card, desc in zip(list_rev_card, list_rev_desc)
        ]
        return list_rev_tarot
