# descripstats

`descripstats` is a lightweight Python package that extends pandas `DataFrame.describe()` by adding additional descriptive statistics commonly used in exploratory data analysis (EDA).

It is designed to be simple, minimal, and compatible with modern versions of pandas (2.x+).

---

## ✨ Features

In addition to the default pandas `describe()`, this package provides:

- **mad**: mean absolute deviation  
- **variance**: variance  
- **sem**: standard error of the mean  
- **sum**: column sums  
- **skewness**: distribution skew  
- **kurtosis**: distribution kurtosis  

---

## 📦 Installation

```bash
pip install descripstats
```

---

## 🚀 Usage

### Option 1: Direct import

```python
from descripstats import Describe

import pandas as pd

df = pd.read_csv("your_data.csv")

stats = Describe(df)
print(stats)
```

---

### Option 2: Module import

```python
import descripstats as ds

stats = ds.Describe(df)
print(stats)
```

⚠️ Note: The correct function name is `Describe` (not `Discribe`).

---

## 📊 Example

```python
import pandas as pd
from descripstats import Describe

df = pd.DataFrame({
    "A": [1, 2, 3, 4, 5],
    "B": [10, 20, 30, 40, 50]
})

result = Describe(df)
print(result)
```

---

## ⚙️ Compatibility

- pandas ≥ 2.0
- numpy ≥ 1.21
- Python ≥ 3.9

This package has been updated to remove deprecated pandas APIs such as `DataFrame.mad()`.

---

## 📁 Documentation

Example notebook:

https://github.com/shoukewei/descripstats/blob/main/docs/example.ipynb

---

## 👤 Author

Developed by **Shouke Wei**  
Deepsim Intelligence Technology Inc., Canada  
© 2022–2026

---

## 🧠 Notes

This package is intended for:
- quick EDA (exploratory data analysis)
- educational use
- lightweight statistical summaries

For advanced statistical workflows, consider using:
- pandas
- scipy
- statsmodels
