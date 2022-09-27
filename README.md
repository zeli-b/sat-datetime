# sat-datetime

> 사트 자소크력 계산을 위한 라이브러리

다음 코드를 통해 자소크력 년을 알아낼 수 있습니다.

```python
from datetime import datetime

from sat_datetime import SatDatetime

zasokese_now = SatDatetime.get_from_datetime(datetime.now())
print(zasokese_now)
```
