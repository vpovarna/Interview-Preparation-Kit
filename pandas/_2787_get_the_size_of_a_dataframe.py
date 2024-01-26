from typing import List

import pandas as pd


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [i for i in players.shape]
