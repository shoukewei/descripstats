
import pandas as pd
import numpy as np

def Describe(data):
    """
    Enhanced pandas describe() with additional statistics:
    - mad: mean absolute deviation
    - variance
    - sem: standard error of the mean
    - sum
    - skewness
    - kurtosis
    """

    data = pd.DataFrame(data)

    describe = data.describe()

    # numeric-only columns
    num = data.select_dtypes(include="number")

    # --- FIX: pandas 2.x compatible MAD ---
    mad = num.apply(lambda x: np.mean(np.abs(x - x.mean())))

    var = num.var()
    sem = num.sem()
    sum_ = num.sum()
    skew = num.skew()
    kurt = num.kurt()

    # build DataFrames
    mad_df = pd.DataFrame([mad], index=["mad"])
    var_df = pd.DataFrame([var], index=["variance"])
    sem_df = pd.DataFrame([sem], index=["sem"])
    sum_df = pd.DataFrame([sum_], index=["sum"])
    skew_df = pd.DataFrame([skew], index=["skewness"])
    kurt_df = pd.DataFrame([kurt], index=["kurtosis"])

    # combine
    stats = pd.concat(
        [describe, mad_df, var_df, sem_df, sum_df, skew_df, kurt_df]
    )

    return stats