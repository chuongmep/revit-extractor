
![Platform](https://img.shields.io/badge/platform-Windows/MacOS/Linux-lightgray.svg) [![License: GNU v3](https://img.shields.io/badge/License-GNU-yellow.svg)](https://opensource.org/licenses/MIT)


![PyPI](https://img.shields.io/pypi/v/revit-extractor?label=pypi%20revit-extractor-python)
![PyPI - Downloads](https://img.shields.io/pypi/dm/revit-extractor?label=pipy-download)

<a href="https://twitter.com/intent/follow?screen_name=chuongmep">
<img src="https://img.shields.io/twitter/follow/chuongmep?style=social&logo=twitter"
alt="follow on Twitter"></a>

## Revit Extractor

Revit Extractor is a library that allows you to export native data from Revit files without needing to open Revit. It’s particularly useful for extracting data from Revit files and integrating it into other systems.

![](./samples/background.png)


## Requirements

- Make sure you have Revit installed on your machine.
- Make sure you have Python installed on your machine version `3.9` or later.
- Make sure you are running on Windows Platform. MacOS and Linux are not supported. 

## How to use

1. Install the library by using pip:
```bash
pip install revit-extractor --upgrade
```

2. Get Revit Version 

```
from revit_extract import RevitExtractor
rvt_path = r"D:\_WIP\Download\Sample Office Building Model V1.rvt"
version = RevitExtractor.get_version(rvt_path)
print(version)
```

3. Use the library in your code:

- Extract all categories from Revit file:

```python
from revit_extract import RevitExtractor
rvt_path = r"D:\_WIP\Download\Sample Office Building Model V1.rvt"
prodb = RevitExtractor(rvt_path).read_prob_data()
categories = prodb.get_all_categories()
for key in categories:
    print(key, categories[key])
```

- Extract data by categories and parameters from Revit file:
```python
from revit_extract import RevitExtractor
rvt_path = r"D:\_WIP\Download\Sample Office Building Model V1.rvt"
prodb = RevitExtractor(rvt_path).read_prob_data()
categories =["Walls", "Doors"]
params = ["Name", "Type", "Level"]
data_frame = prodb.get_data_by_categories_and_params(categories, params)
data_frame.to_excel("output.xlsx", index=False)
```

More ???

## Limitation

- Export Schedule table data is not supported with svf format.

- Geometry data is limit supported to read at the moment (But can export and use APS-Toolkit)


## References

- [Use Revit Extractor](https://chuongmep.com/posts/2024-09-25-revit-extractor.html)