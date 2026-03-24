import pandas as pd
import numpy as np
import tempfile
import os
import sqlite3

# =============================================================================
# COMPREHENSIVE PANDAS DEMONSTRATION FOR DATA SCIENCE
# =============================================================================

print("=" * 70)
print("PANDAS: ALL CORE FUNCTIONALITIES DEMONSTRATED")
print("=" * 70)

# -----------------------------------------------------------------------------
# 1. DATA STRUCTURES
# -----------------------------------------------------------------------------
print("\n1. DATA STRUCTURES")
print("-" * 40)

# Series
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'], name='scores')
print("Series:\n", s)

# DataFrame from dictionary
df_dict = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                        'Age': [25, 30, 35],
                        'Salary': [50000, 60000, 70000]})
print("\nDataFrame from dict:\n", df_dict)

# DataFrame from list of lists
df_list = pd.DataFrame([[1, 2], [3, 4]], columns=['X', 'Y'])
print("\nDataFrame from list:\n", df_list)

# Index
idx = pd.Index([1, 2, 3], name='id')
print("\nIndex object:", idx)

# -----------------------------------------------------------------------------
# 2. DATA INPUT / OUTPUT (using temporary files)
# -----------------------------------------------------------------------------
print("\n2. DATA INPUT / OUTPUT")
print("-" * 40)

with tempfile.TemporaryDirectory() as tmpdir:
    # CSV
    csv_path = os.path.join(tmpdir, 'data.csv')
    df_dict.to_csv(csv_path, index=False)
    df_csv = pd.read_csv(csv_path)
    print("CSV read:\n", df_csv)

    # Excel
    excel_path = os.path.join(tmpdir, 'data.xlsx')
    df_dict.to_excel(excel_path, index=False)
    df_excel = pd.read_excel(excel_path)
    print("\nExcel read:\n", df_excel)

    # JSON
    json_path = os.path.join(tmpdir, 'data.json')
    df_dict.to_json(json_path, orient='records')
    df_json = pd.read_json(json_path)
    print("\nJSON read:\n", df_json)

    # SQL (in-memory SQLite)
    conn = sqlite3.connect(':memory:')
    df_dict.to_sql('employees', conn, index=False)
    df_sql = pd.read_sql('SELECT * FROM employees', conn)
    print("\nSQL read:\n", df_sql)
    conn.close()

    # Parquet (requires pyarrow or fastparquet)
    try:
        parquet_path = os.path.join(tmpdir, 'data.parquet')
        df_dict.to_parquet(parquet_path, index=False)
        df_parquet = pd.read_parquet(parquet_path)
        print("\nParquet read:\n", df_parquet)
    except ImportError:
        print("\nParquet engine not installed, skipping.")

# -----------------------------------------------------------------------------
# 3. DATA INSPECTION
# -----------------------------------------------------------------------------
print("\n3. DATA INSPECTION")
print("-" * 40)

df_inspect = pd.DataFrame({'A': np.random.randn(100),
                           'B': np.random.randint(0, 10, 100),
                           'C': ['cat', 'dog'] * 50})

print("head(3):\n", df_inspect.head(3))
print("\ntail(2):\n", df_inspect.tail(2))
print("\nsample(3):\n", df_inspect.sample(3))
print("\ninfo():")
df_inspect.info()
print("\ndescribe():\n", df_inspect.describe())
print("\ndtypes:\n", df_inspect.dtypes)
print("\nshape:", df_inspect.shape)
print("size:", df_inspect.size)
print("columns:", df_inspect.columns.tolist())
print("index:", df_inspect.index)

# -----------------------------------------------------------------------------
# 4. SELECTION & INDEXING
# -----------------------------------------------------------------------------
print("\n4. SELECTION & INDEXING")
print("-" * 40)

df_sel = pd.DataFrame({'X': [1,2,3,4], 'Y': [5,6,7,8]}, index=['a','b','c','d'])
print("DataFrame:\n", df_sel)

# Label-based
print("\nloc['b':'c']:\n", df_sel.loc['b':'c'])
# Position-based
print("\niloc[1:3, 0:1]:\n", df_sel.iloc[1:3, 0:1])
# Scalar access
print("\nat['b','Y']:", df_sel.at['b','Y'])
print("iat[2,1]:", df_sel.iat[2,1])
# Boolean filtering
print("\nBoolean (X>2):\n", df_sel[df_sel['X'] > 2])
# Column selection
print("\nSingle column:\n", df_sel['X'])

# -----------------------------------------------------------------------------
# 5. DATA CLEANING
# -----------------------------------------------------------------------------
print("\n5. DATA CLEANING")
print("-" * 40)

df_clean = pd.DataFrame({'A': [1,2,np.nan,4],
                         'B': [5,np.nan,np.nan,8],
                         'C': ['x','y','x','y']})
print("Original:\n", df_clean)

# Missing values
print("\nisnull():\n", df_clean.isnull())
print("notnull():\n", df_clean.notnull())
print("dropna():\n", df_clean.dropna())
print("fillna(0):\n", df_clean.fillna(0))
print("ffill:\n", df_clean.fillna(method='ffill'))

# Duplicates
df_dup = pd.DataFrame({'A': [1,1,2,2], 'B': [10,10,20,30]})
print("\nDuplicates:\n", df_dup)
print("duplicated():\n", df_dup.duplicated())
print("drop_duplicates():\n", df_dup.drop_duplicates())

# Type conversion
df_clean['A'] = df_clean['A'].astype('Int64')  # nullable int
print("\nastype to Int64:\n", df_clean['A'])
df_mixed = pd.DataFrame({'col': ['1', '2', '3.1']})
df_inferred = df_mixed.infer_objects()
print("infer_objects:\n", df_inferred.dtypes)
df_converted = df_mixed.convert_dtypes()
print("convert_dtypes:\n", df_converted.dtypes)

# -----------------------------------------------------------------------------
# 6. DATA TRANSFORMATION
# -----------------------------------------------------------------------------
print("\n6. DATA TRANSFORMATION")
print("-" * 40)

df_trans = pd.DataFrame({'A': [1,2,3], 'B': [4,5,6]})
print("Original:\n", df_trans)

# Column assignment
df_trans['C'] = df_trans['A'] + df_trans['B']
print("\nAfter assignment (C = A+B):\n", df_trans)

# rename
df_renamed = df_trans.rename(columns={'A': 'Alpha', 'B': 'Beta'})
print("rename columns:\n", df_renamed)

# apply
print("\napply (sqrt to A):\n", df_trans['A'].apply(np.sqrt))

# map
print("map on B (square):\n", df_trans['B'].map(lambda x: x**2))

# applymap (element-wise on DataFrame)
print("applymap (multiply by 10):\n", df_trans.applymap(lambda x: x*10))

# replace
df_rep = pd.DataFrame({'X': [1,2,3,2], 'Y': [4,5,6,5]})
print("\nreplace (2->99):\n", df_rep.replace(2, 99))

# -----------------------------------------------------------------------------
# 7. SORTING & RANKING
# -----------------------------------------------------------------------------
print("\n7. SORTING & RANKING")
print("-" * 40)

df_sort = pd.DataFrame({'Name': ['Alice','Bob','Charlie','Alice'],
                        'Score': [90,85,95,88]})
print("Original:\n", df_sort)

# sort_values
print("\nsort_values by Score:\n", df_sort.sort_values('Score', ascending=False))

# sort_index
df_sorted_idx = df_sort.set_index('Name').sort_index()
print("\nsort_index on Name:\n", df_sorted_idx)

# rank
df_sort['Rank'] = df_sort['Score'].rank(ascending=False)
print("\nrank:\n", df_sort)

# nlargest / nsmallest
print("\nnlargest(2, 'Score'):\n", df_sort.nlargest(2, 'Score'))
print("nsmallest(2, 'Score'):\n", df_sort.nsmallest(2, 'Score'))

# -----------------------------------------------------------------------------
# 8. GROUPBY OPERATIONS
# -----------------------------------------------------------------------------
print("\n8. GROUPBY OPERATIONS")
print("-" * 40)

df_group = pd.DataFrame({'Category': ['A','A','B','B','C'],
                         'Value': [10,20,30,40,50],
                         'Count': [1,2,3,4,5]})
print("Original:\n", df_group)

# groupby and agg
grouped = df_group.groupby('Category')
print("\nsum():\n", grouped['Value'].sum())
print("\nagg(['sum','mean']):\n", grouped['Value'].agg(['sum','mean']))

# transform
df_group['Value_norm'] = grouped['Value'].transform(lambda x: x / x.sum())
print("\ntransform (value / sum per group):\n", df_group)

# filter
filtered = grouped.filter(lambda g: g['Value'].sum() > 50)
print("\nfilter (groups with sum >50):\n", filtered)

# -----------------------------------------------------------------------------
# 9. MERGING & JOINING
# -----------------------------------------------------------------------------
print("\n9. MERGING & JOINING")
print("-" * 40)

df1 = pd.DataFrame({'key': ['A','B','C'], 'value1': [1,2,3]})
df2 = pd.DataFrame({'key': ['B','C','D'], 'value2': [4,5,6]})
print("df1:\n", df1)
print("df2:\n", df2)

# merge (inner)
inner = pd.merge(df1, df2, on='key', how='inner')
print("\ninner merge:\n", inner)

# left
left = pd.merge(df1, df2, on='key', how='left')
print("left merge:\n", left)

# right
right = pd.merge(df1, df2, on='key', how='right')
print("right merge:\n", right)

# outer
outer = pd.merge(df1, df2, on='key', how='outer')
print("outer merge:\n", outer)

# join (using index)
df1_idx = df1.set_index('key')
df2_idx = df2.set_index('key')
joined = df1_idx.join(df2_idx, how='inner')
print("\njoin on index:\n", joined)

# concat
concat_rows = pd.concat([df1, df2], axis=0, ignore_index=True)
print("\nconcat rows:\n", concat_rows)
concat_cols = pd.concat([df1, df2], axis=1)
print("\nconcat columns:\n", concat_cols)

# -----------------------------------------------------------------------------
# 10. RESHAPING
# -----------------------------------------------------------------------------
print("\n10. RESHAPING")
print("-" * 40)

df_pivot = pd.DataFrame({'Date': ['2023-01-01','2023-01-01','2023-01-02','2023-01-02'],
                         'City': ['NY','LA','NY','LA'],
                         'Sales': [100,200,150,250]})
print("Original:\n", df_pivot)

# pivot
pivoted = df_pivot.pivot(index='Date', columns='City', values='Sales')
print("\npivot:\n", pivoted)

# pivot_table (with aggregation)
df_pt = pd.DataFrame({'Date': ['2023-01-01','2023-01-01','2023-01-01','2023-01-02'],
                      'Product': ['A','B','A','B'],
                      'Sales': [10,20,30,40]})
ptable = pd.pivot_table(df_pt, values='Sales', index='Date', columns='Product', aggfunc='sum')
print("\npivot_table:\n", ptable)

# melt
melted = pd.melt(df_pivot, id_vars=['Date'], value_vars=['City','Sales'])
print("\nmelt:\n", melted)

# stack / unstack
df_stack = pd.DataFrame({'A': [1,2], 'B': [3,4]}, index=['X','Y'])
stacked = df_stack.stack()
print("\nstack:\n", stacked)
unstacked = stacked.unstack()
print("\nunstack:\n", unstacked)

# -----------------------------------------------------------------------------
# 11. TIME SERIES
# -----------------------------------------------------------------------------
print("\n11. TIME SERIES")
print("-" * 40)

# to_datetime
dates = pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03'])
print("to_datetime:", dates)

# date_range
dr = pd.date_range(start='2023-01-01', periods=5, freq='D')
print("date_range:\n", dr)

# Create time series DataFrame
ts_data = pd.Series([1,2,3,4,5], index=dr)
print("Time series:\n", ts_data)

# time-based indexing
print("Indexing '2023-01-03':", ts_data['2023-01-03'])
print("Slicing '2023-01-02':'2023-01-04':\n", ts_data['2023-01-02':'2023-01-04'])

# resample
ts_resampled = ts_data.resample('2D').mean()
print("resample (2D mean):\n", ts_resampled)

# rolling
rolling_mean = ts_data.rolling(window=2).mean()
print("rolling mean (window=2):\n", rolling_mean)

# -----------------------------------------------------------------------------
# 12. WINDOW FUNCTIONS
# -----------------------------------------------------------------------------
print("\n12. WINDOW FUNCTIONS")
print("-" * 40)

df_win = pd.DataFrame({'value': [1,2,3,4,5,6]})
print("Original:\n", df_win)

# rolling
df_win['rolling_mean'] = df_win['value'].rolling(3).mean()
print("\nrolling(3).mean():\n", df_win)

# expanding
df_win['expanding_sum'] = df_win['value'].expanding().sum()
print("\nexpanding().sum():\n", df_win)

# ewm (exponential weighted)
df_win['ewm_mean'] = df_win['value'].ewm(span=2).mean()
print("\newm(span=2).mean():\n", df_win)

# -----------------------------------------------------------------------------
# 13. STRING OPERATIONS
# -----------------------------------------------------------------------------
print("\n13. STRING OPERATIONS")
print("-" * 40)

df_str = pd.DataFrame({'text': ['Hello World', 'Python is great', 'Pandas is fun']})
print("Original:\n", df_str)

# str methods
df_str['lower'] = df_str['text'].str.lower()
df_str['upper'] = df_str['text'].str.upper()
df_str['contains'] = df_str['text'].str.contains('is')
df_str['replaced'] = df_str['text'].str.replace(' ', '_')
df_str['split'] = df_str['text'].str.split()
print("\nAfter string operations:\n", df_str)

# -----------------------------------------------------------------------------
# 14. CATEGORICAL DATA
# -----------------------------------------------------------------------------
print("\n14. CATEGORICAL DATA")
print("-" * 40)

df_cat = pd.DataFrame({'grade': ['A','B','A','C','B']})
print("Original:\n", df_cat)

# convert to category
df_cat['grade_cat'] = df_cat['grade'].astype('category')
print("\nastype('category'):\n", df_cat['grade_cat'])

# cat methods
print("categories:", df_cat['grade_cat'].cat.categories)
print("codes:", df_cat['grade_cat'].cat.codes)

# -----------------------------------------------------------------------------
# 15. STATISTICAL OPERATIONS
# -----------------------------------------------------------------------------
print("\n15. STATISTICAL OPERATIONS")
print("-" * 40)

df_stats = pd.DataFrame({'A': [1,2,3,4,5], 'B': [2,4,6,8,10]})
print("Data:\n", df_stats)

print("mean:\n", df_stats.mean())
print("median:\n", df_stats.median())
print("mode:\n", df_stats.mode().iloc[0])  # mode may return multiple
print("std:\n", df_stats.std())
print("var:\n", df_stats.var())
print("corr:\n", df_stats.corr())
print("cov:\n", df_stats.cov())

# -----------------------------------------------------------------------------
# 16. ADVANCED INDEXING (MultiIndex)
# -----------------------------------------------------------------------------
print("\n16. ADVANCED INDEXING")
print("-" * 40)

arrays = [['A', 'A', 'B', 'B'], [1, 2, 1, 2]]
index = pd.MultiIndex.from_arrays(arrays, names=('letter', 'number'))
df_multi = pd.DataFrame({'value': [10,20,30,40]}, index=index)
print("MultiIndex DataFrame:\n", df_multi)

# reset_index
reset = df_multi.reset_index()
print("\nreset_index:\n", reset)

# set_index
set_idx = reset.set_index(['letter', 'number'])
print("\nset_index back:\n", set_idx)

# -----------------------------------------------------------------------------
# 17. PERFORMANCE OPTIMIZATION
# -----------------------------------------------------------------------------
print("\n17. PERFORMANCE OPTIMIZATION")
print("-" * 40)

# eval (expression evaluation)
df_perf = pd.DataFrame({'a': np.random.randn(10000), 'b': np.random.randn(10000)})
result = df_perf.eval('c = a + b')
print("eval (c = a + b) computed, first few:\n", result[['a','b','c']].head())

# query
filtered = df_perf.query('a > 0 & b < 0')
print("\nquery (a>0 & b<0) rows:", len(filtered))

# Vectorization is inherent; note that all previous ops are vectorized.

# -----------------------------------------------------------------------------
# 18. INTEROPERABILITY
# -----------------------------------------------------------------------------
print("\n18. INTEROPERABILITY")
print("-" * 40)

df_inter = pd.DataFrame({'x': [1,2,3], 'y': [4,5,6]})
print("DataFrame:\n", df_inter)

# to_numpy
numpy_arr = df_inter.to_numpy()
print("to_numpy():\n", numpy_arr)

# values (old, still works)
values_arr = df_inter.values
print("values:\n", values_arr)

# to_dict
dict_records = df_inter.to_dict(orient='records')
print("to_dict (records):\n", dict_records)

# to_list via numpy
list_from_series = df_inter['x'].tolist()
print("tolist() from Series:", list_from_series)

# =============================================================================
print("\n" + "=" * 70)
print("ALL PANDAS FUNCTIONALITIES DEMONSTRATED SUCCESSFULLY")
print("=" * 70)