import numpy as np
import tempfile
import os

# =============================================================================
# 1. Core Array Creation
# =============================================================================

print("="*60)
print("1. CORE ARRAY CREATION")
print("="*60)

# array
arr = np.array([1, 2, 3], dtype=np.float32)
print("array:", arr)

# asarray (converts existing array or list)
lst = [4, 5, 6]
arr_as = np.asarray(lst, dtype=np.int32)
print("asarray:", arr_as)

# arange
arr_arange = np.arange(0, 10, 2)  # start, stop, step
print("arange:", arr_arange)

# linspace
arr_lin = np.linspace(0, 1, 5)  # 5 points from 0 to 1 inclusive
print("linspace:", arr_lin)

# logspace
arr_log = np.logspace(0, 2, 4)  # 4 points from 10^0 to 10^2
print("logspace:", arr_log)

# zeros
arr_zeros = np.zeros((2,3), dtype=np.int32, order='C')
print("zeros (C-order):\n", arr_zeros)

# ones
arr_ones = np.ones((2,3), dtype=np.float64, order='F')
print("ones (F-order):\n", arr_ones)

# empty (uninitialized, values may be garbage)
arr_empty = np.empty((2,2))
print("empty:\n", arr_empty)

# full
arr_full = np.full((2,3), 7)
print("full:\n", arr_full)

# eye (identity with offset)
arr_eye = np.eye(3, k=1, dtype=int)
print("eye (k=1):\n", arr_eye)

# identity (square identity)
arr_identity = np.identity(4)
print("identity:\n", arr_identity)

# fromfunction
def f(i, j):
    return i + j
arr_fromfunc = np.fromfunction(f, (3,3), dtype=int)
print("fromfunction (i+j):\n", arr_fromfunc)

# fromiter
iterable = (x**2 for x in range(5))
arr_fromiter = np.fromiter(iterable, dtype=float)
print("fromiter:", arr_fromiter)

# frombuffer (using bytes)
buffer = b'\x01\x02\x03\x04'
arr_frombuffer = np.frombuffer(buffer, dtype=np.uint8)
print("frombuffer:", arr_frombuffer)

# dtype specification (already shown) and memory order examples above.

# =============================================================================
# 2. Array Attributes & Inspection
# =============================================================================

print("\n" + "="*60)
print("2. ARRAY ATTRIBUTES & INSPECTION")
print("="*60)

a = np.array([[1,2,3],[4,5,6]], dtype=np.float32)
print("Array a:\n", a)
print("ndim:", a.ndim)
print("shape:", a.shape)
print("size:", a.size)
print("dtype:", a.dtype)
print("itemsize:", a.itemsize, "bytes")
print("nbytes:", a.nbytes, "bytes")
np.info(a)  # prints info
print("typename for 'f' (float32):", np.typename('f'))

# =============================================================================
# 3. Array Manipulation
# =============================================================================

print("\n" + "="*60)
print("3. ARRAY MANIPULATION")
print("="*60)

# Reshaping
b = np.arange(8)
b_reshaped = b.reshape((2,4))
print("reshape:\n", b_reshaped)

# resize (modifies in-place if used as method, or returns new if np.resize)
b_resized = np.resize(b, (3,3))  # repeats to fill
print("resize (3x3):\n", b_resized)

# ravel (flatten to 1D, returns view if possible)
b_ravel = b_reshaped.ravel()
print("ravel:", b_ravel)

# flatten (always returns copy)
b_flatten = b_reshaped.flatten()
print("flatten:", b_flatten)

# Transpose operations
c = np.arange(6).reshape(2,3)
print("Original c:\n", c)
print("transpose():\n", c.transpose())
print("T property:\n", c.T)

# swapaxes
d = np.arange(24).reshape(2,3,4)
print("swapaxes (swap axis 0 and 2):\n", np.swapaxes(d,0,2).shape)

# moveaxis
e = np.moveaxis(d, 0, -1)  # move axis 0 to last
print("moveaxis: new shape", e.shape)

# expand_dims
f = np.array([1,2,3])
f_expanded = np.expand_dims(f, axis=1)
print("expand_dims (add column axis):\n", f_expanded)

# squeeze
g = np.array([[[1]],[[2]]])  # shape (2,1,1)
g_squeezed = np.squeeze(g)
print("squeeze: from", g.shape, "to", g_squeezed.shape)

# Joining
a1 = np.array([[1,2],[3,4]])
a2 = np.array([[5,6],[7,8]])

# concatenate
conc = np.concatenate((a1, a2), axis=0)
print("concatenate (axis=0):\n", conc)

# stack (new axis)
st = np.stack((a1, a2), axis=0)
print("stack (axis=0) shape:", st.shape)

# vstack
vs = np.vstack((a1, a2))
print("vstack:\n", vs)

# hstack
hs = np.hstack((a1, a2))
print("hstack:\n", hs)

# dstack (depth)
ds = np.dstack((a1, a2))
print("dstack shape:", ds.shape)

# column_stack
col = np.column_stack((a1, a2))
print("column_stack:\n", col)

# row_stack (same as vstack)
row = np.row_stack((a1, a2))
print("row_stack:\n", row)

# Splitting
arr = np.arange(12).reshape(3,4)
print("Array to split:\n", arr)

# split (into 3 equal parts along axis 0)
spl = np.split(arr, 3)
print("split into 3:\n", spl)

# array_split (allows unequal splits)
arr_spl = np.array_split(arr, 2, axis=1)
print("array_split along axis=1 into 2:\n", arr_spl)

# hsplit
hspl = np.hsplit(arr, 2)
print("hsplit into 2:\n", hspl)

# vsplit
vspl = np.vsplit(arr, 3)
print("vsplit into 3:\n", vspl)

# dsplit (needs 3D)
arr3d = np.arange(24).reshape(2,3,4)
dspl = np.dsplit(arr3d, 2)
print("dsplit into 2 (depth) shapes:", [d.shape for d in dspl])

# =============================================================================
# 4. Indexing & Slicing
# =============================================================================

print("\n" + "="*60)
print("4. INDEXING & SLICING")
print("="*60)

arr_idx = np.arange(12).reshape(3,4)
print("Array:\n", arr_idx)

# Basic slicing
print("Basic slicing [1:3, 0:2]:\n", arr_idx[1:3, 0:2])

# Integer indexing
print("Integer indexing [[0,2], [1,3]]:\n", arr_idx[[0,2], [1,3]])

# Boolean masking
mask = arr_idx > 5
print("Boolean mask >5:\n", arr_idx[mask])

# where
print("where >5:", np.where(arr_idx > 5))

# nonzero
print("nonzero indices:", np.nonzero(arr_idx > 5))

# argwhere
print("argwhere >5:\n", np.argwhere(arr_idx > 5))

# take
print("take indices [0,2,5]:", np.take(arr_idx, [0,2,5]))

# put (modifies array)
arr_put = np.array([10,20,30,40])
np.put(arr_put, [1,3], [99,100])
print("put (indices 1,3 -> 99,100):", arr_put)

# choose (using index array)
choices = np.array([[1,2],[3,4],[5,6]])
idx = np.array([0,1])
print("choose (from choices):", np.choose(idx, choices))

# compress (using condition)
cond = [True, False, True]
arr_comp = np.array([10,20,30])
print("compress (cond):", np.compress(cond, arr_comp))

# =============================================================================
# 5. Mathematical Operations
# =============================================================================

print("\n" + "="*60)
print("5. MATHEMATICAL OPERATIONS")
print("="*60)

x = np.array([1,2,3])
y = np.array([4,5,6])

# Element-wise
print("add:", np.add(x,y))
print("subtract:", np.subtract(x,y))
print("multiply:", np.multiply(x,y))
print("divide:", np.divide(x,y))
print("power:", np.power(x,2))
print("mod:", np.mod(y,x))

# Aggregate
print("sum:", np.sum(x))
print("prod:", np.prod(x))
print("mean:", np.mean(x))
print("median:", np.median(x))
print("std:", np.std(x))
print("var:", np.var(x))

# Cumulative
print("cumsum:", np.cumsum(x))
print("cumprod:", np.cumprod(x))

# Differences
z = np.array([1,3,6,10])
print("diff:", np.diff(z))
print("gradient:", np.gradient(z))

# =============================================================================
# 6. Linear Algebra
# =============================================================================

print("\n" + "="*60)
print("6. LINEAR ALGEBRA")
print("="*60)

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

# dot
print("dot product:\n", np.dot(A,B))

# matmul (same for 2D)
print("matmul:\n", np.matmul(A,B))

# inner (inner product, sum of products over last axes)
print("inner (matrix inner):\n", np.inner(A,B))

# outer
v1 = np.array([1,2,3])
v2 = np.array([4,5,6])
print("outer:\n", np.outer(v1,v2))

# SVD
U, s, Vt = np.linalg.svd(A)
print("SVD: U:\n", U, "\ns:", s, "\nVt:\n", Vt)

# eig
eigvals, eigvecs = np.linalg.eig(A)
print("eig: values:", eigvals, "\nvectors:\n", eigvecs)

# QR
q, r = np.linalg.qr(A)
print("QR: Q:\n", q, "\nR:\n", r)

# det
print("det:", np.linalg.det(A))

# inv
print("inv:\n", np.linalg.inv(A))

# norm
print("norm (Frobenius):", np.linalg.norm(A))

# solve (Ax = b)
b = np.array([1,2])
x_sol = np.linalg.solve(A, b)
print("solve Ax=b: x =", x_sol)

# lstsq (least squares)
A_lst = np.array([[1,1],[1,2],[1,3]])
b_lst = np.array([1,2,2])
x_lst, residuals, rank, s = np.linalg.lstsq(A_lst, b_lst, rcond=None)
print("lstsq: x =", x_lst, "residuals =", residuals)

# =============================================================================
# 7. Random Module
# =============================================================================

print("\n" + "="*60)
print("7. RANDOM MODULE")
print("="*60)

np.random.seed(42)  # seed

# Generation
print("rand (uniform 0-1):", np.random.rand(3))
print("randn (standard normal):", np.random.randn(3))
print("randint (0-10, size=5):", np.random.randint(0,10,5))
print("random (same as rand):", np.random.random(3))

# Distributions
print("normal (loc=0, scale=1, size=3):", np.random.normal(0,1,3))
print("uniform (low=0, high=10, size=3):", np.random.uniform(0,10,3))
print("binomial (n=10, p=0.5, size=3):", np.random.binomial(10,0.5,3))
print("poisson (lam=3, size=3):", np.random.poisson(3,3))
print("exponential (scale=1, size=3):", np.random.exponential(1,3))

# Sampling
arr_samp = np.array([1,2,3,4,5])
print("choice (3 from arr):", np.random.choice(arr_samp, 3))
np.random.shuffle(arr_samp)
print("shuffled arr:", arr_samp)
print("permutation (of 5):", np.random.permutation(5))

# =============================================================================
# 8. Statistical Functions
# =============================================================================

print("\n" + "="*60)
print("8. STATISTICAL FUNCTIONS")
print("="*60)

data = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Data:\n", data)

print("mean (axis=0):", np.mean(data, axis=0))
print("median (axis=0):", np.median(data, axis=0))
print("std (axis=0):", np.std(data, axis=0))
print("var (axis=0):", np.var(data, axis=0))
print("corrcoef (row-wise):\n", np.corrcoef(data))
print("cov (row-wise):\n", np.cov(data))
print("percentile (50th, axis=0):", np.percentile(data, 50, axis=0))
print("quantile (0.5, axis=0):", np.quantile(data, 0.5, axis=0))

# =============================================================================
# 9. Sorting & Searching
# =============================================================================

print("\n" + "="*60)
print("9. SORTING & SEARCHING")
print("="*60)

unsorted = np.array([3,1,4,1,5,9,2])
print("Unsorted:", unsorted)

print("sort:", np.sort(unsorted))
print("argsort:", np.argsort(unsorted))

# lexsort (indirect stable sort using multiple keys)
a = np.array(['a','b','a','b'])
b = np.array([3,2,1,4])
idx = np.lexsort((b,a))  # sort by a then b
print("lexsort indices:", idx)

# argmax
print("argmax:", np.argmax(unsorted))

# argmin
print("argmin:", np.argmin(unsorted))

# searchsorted (in sorted array)
sorted_arr = np.sort(unsorted)
print("sorted array:", sorted_arr)
print("searchsorted (value 3):", np.searchsorted(sorted_arr, 3))

# unique
print("unique values:", np.unique(unsorted))
print("unique with counts:", np.unique(unsorted, return_counts=True))

# =============================================================================
# 10. Broadcasting
# =============================================================================

print("\n" + "="*60)
print("10. BROADCASTING")
print("="*60)

a_bc = np.array([[1,2,3],[4,5,6]])  # shape (2,3)
b_bc = np.array([10,20,30])          # shape (3,)
print("a:\n", a_bc)
print("b:", b_bc)
print("a + b (broadcast):\n", a_bc + b_bc)

c_bc = np.array([[10],[20]])         # shape (2,1)
print("c:\n", c_bc)
print("a * c (broadcast):\n", a_bc * c_bc)

# =============================================================================
# 11. Universal Functions (ufuncs)
# =============================================================================

print("\n" + "="*60)
print("11. UNIVERSAL FUNCTIONS")
print("="*60)

x_uf = np.array([0, np.pi/2, np.pi])

# Arithmetic ufuncs (already shown, but as ufunc objects)
print("np.add (ufunc):", np.add(x_uf, 1))

# Trigonometric
print("sin:", np.sin(x_uf))
print("cos:", np.cos(x_uf))
print("tan:", np.tan(x_uf))

# Exponential & logarithmic
print("exp:", np.exp([0,1,2]))
print("log:", np.log([1, np.e, np.e**2]))
print("log10:", np.log10([1,10,100]))
print("log2:", np.log2([1,2,4]))

# Comparison
print("greater (2 vs [1,2,3]):", np.greater(2, [1,2,3]))
print("less (2 vs [1,2,3]):", np.less(2, [1,2,3]))
print("equal (2 vs [1,2,3]):", np.equal(2, [1,2,3]))

# Logical
print("logical_and([True,False],[True,True]):", np.logical_and([True,False],[True,True]))
print("logical_or([True,False],[False,False]):", np.logical_or([True,False],[False,False]))
print("logical_not([True,False]):", np.logical_not([True,False]))

# Custom ufunc via frompyfunc
def my_func(x, y):
    return x + y if x > y else x - y
my_ufunc = np.frompyfunc(my_func, 2, 1)
print("frompyfunc result:", my_ufunc([1,5,3], [2,2,2]))

# vectorize (decorator-like)
@np.vectorize
def my_vec(x):
    return x**2 if x%2==0 else x
print("vectorize result:", my_vec([1,2,3,4]))

# =============================================================================
# 12. File Input/Output
# =============================================================================

print("\n" + "="*60)
print("12. FILE INPUT/OUTPUT")
print("="*60)

# Use temporary directory for files
with tempfile.TemporaryDirectory() as tmpdir:
    # Binary
    arr_file = np.array([[1,2,3],[4,5,6]])
    np.save(os.path.join(tmpdir, 'arr.npy'), arr_file)
    loaded = np.load(os.path.join(tmpdir, 'arr.npy'))
    print("load (from .npy):\n", loaded)

    # savez (multiple arrays in uncompressed .npz)
    np.savez(os.path.join(tmpdir, 'arr.npz'), a=arr_file, b=np.array([7,8,9]))
    npz = np.load(os.path.join(tmpdir, 'arr.npz'))
    print("savez: loaded a:\n", npz['a'], "b:", npz['b'])

    # savez_compressed
    np.savez_compressed(os.path.join(tmpdir, 'arr_comp.npz'), a=arr_file, b=np.array([7,8,9]))
    npz_comp = np.load(os.path.join(tmpdir, 'arr_comp.npz'))
    print("savez_compressed: loaded a:\n", npz_comp['a'])

    # Text
    txt_file = os.path.join(tmpdir, 'data.txt')
    np.savetxt(txt_file, arr_file, delimiter=',')
    loaded_txt = np.loadtxt(txt_file, delimiter=',')
    print("loadtxt:\n", loaded_txt)

    # genfromtxt (more options)
    loaded_gen = np.genfromtxt(txt_file, delimiter=',', skip_header=0)
    print("genfromtxt:\n", loaded_gen)

# =============================================================================
# 13. Masked Arrays
# =============================================================================

print("\n" + "="*60)
print("13. MASKED ARRAYS")
print("="*60)

data = np.array([1,2,-999,4,5])
masked = np.ma.array(data, mask=(data==-999))
print("Masked array:", masked)
print("Filled (replace masked):", masked.filled(0))

# =============================================================================
# 14. Structured Arrays
# =============================================================================

print("\n" + "="*60)
print("14. STRUCTURED ARRAYS")
print("="*60)

dtype = [('name', 'U10'), ('age', 'i4'), ('weight', 'f8')]
people = np.array([('Alice', 25, 55.5), ('Bob', 30, 75.2)], dtype=dtype)
print("Structured array:\n", people)
print("Names:", people['name'])
print("Ages:", people['age'])

# =============================================================================
# 15. Memory & Performance
# =============================================================================

print("\n" + "="*60)
print("15. MEMORY & PERFORMANCE")
print("="*60)

orig = np.array([1,2,3,4])
print("Original:", orig)

# copy
cp = orig.copy()
cp[0] = 99
print("Copy (modified):", cp, "original unaffected:", orig)

# view
vw = orig.view()
vw[1] = 88
print("View (modified):", vw, "original changed:", orig)

# memory alignment (demonstrate via flags)
print("C-contiguous:", orig.flags['C_CONTIGUOUS'])
print("F-contiguous:", orig.flags['F_CONTIGUOUS'])

# vectorization (already all ops are vectorized)

# =============================================================================
# 16. Interoperability
# =============================================================================

print("\n" + "="*60)
print("16. INTEROPERABILITY")
print("="*60)

arr = np.array([1.1, 2.2, 3.3])
print("Array:", arr)

# tolist
lst = arr.tolist()
print("tolist:", lst)

# astype
arr_int = arr.astype(int)
print("astype (int):", arr_int)

# to/from Python scalars (implicit)
scalar = arr[0]
print("Python scalar from array:", scalar, type(scalar))

# =============================================================================
# 17. Advanced Topics
# =============================================================================

print("\n" + "="*60)
print("17. ADVANCED TOPICS")
print("="*60)

# as_strided (use with caution)
from numpy.lib.stride_tricks import as_strided
a = np.array([1,2,3,4,5,6])
# Create a 2x3 matrix with overlapping rows (shape (2,3), strides (8,4) for int32)
strided = as_strided(a, shape=(2,3), strides=(4*2,4))  # 4 bytes per int32
print("as_strided (overlapping view):\n", strided)

# memmap (create a memory-mapped array)
with tempfile.NamedTemporaryFile(delete=False) as tf:
    mm = np.memmap(tf.name, dtype='float32', mode='write', shape=(3,3))
    mm[:] = 1.0
    mm.flush()
    # read back
    mm_read = np.memmap(tf.name, dtype='float32', mode='readonly', shape=(3,3))
    print("memmap (written then read):\n", mm_read)
os.unlink(tf.name)  # clean up

# custom dtype creation
custom_dt = np.dtype([('x', 'i4'), ('y', 'f4')])
custom_arr = np.array([(1,2.5),(3,4.5)], dtype=custom_dt)
print("Custom dtype array:", custom_arr)
print("Field x:", custom_arr['x'])

print("\nAll functions demonstrated successfully.")