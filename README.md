## Formula1Py

### Ergast API Python Wrapper

### Install

```
pip install formula1py
```

---

### Usage

```python
import json
from formula1py import F1

# no args
f1 = F1()

# http[s]
f1 = F1(secure=True)

# the api supports an offset and a limit
f1 = F1(secure=False, offset=20, limit=20)

# defaults to text/xml
f1.current_schedule().json
f1.all_drivers().json
f1.all_circuits().xml

# adding season to some endpoints
f1.season_schedule(season=2004).json
f1.race_standings(season=2020).json
f1.constructor_standings(season=2013).xml

# just the url
f1.driver_season(season=2020).url

# also supports random
print(json.dumps(f1.random(season=2020).json, indent=2)
```

```python
>> > from formula1py import F1
>> > f1 = F1(secure=True)
>> > f1_season = f1.driver_season(season=2002)
>> > print(f1_season.url)
>> > print(f1_season.json)
```

### Example Response

```json
{
  "season": "2021",
  "round": "1",
  "url": "https://en.wikipedia.org/wiki/2021_Bahrain_Grand_Prix",
  "raceName": "Bahrain Grand Prix",
  "Circuit": {
    "circuitId": "bahrain",
    "url": "http://en.wikipedia.org/wiki/Bahrain_International_Circuit",
    "circuitName": "Bahrain International Circuit",
    "Location": {
      "lat": "26.0325",
      "long": "50.5106",
      "locality": "Sakhir",
      "country": "Bahrain"
    }
  },
  "date": "2021-03-28",
  "time": "15:00:00Z"
}
```

---

### Dev

```makefile
make deps
make test
```

---

### ToDo

- More Tests
- More Endpoints
