
from datetime import datetime

from rfcentral.model import FrequencyPowerTime


def test_model()->None:
    f: FrequencyPowerTime  = FrequencyPowerTime(1.0, 2.0, str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    assert f.frequency == 1.0
    assert f.power == 2.0
    assert f.date_time is not None
