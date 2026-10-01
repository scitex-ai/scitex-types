# scitex-types

<p align="center">
  <a href="https://scitex.ai">
    <img src="docs/scitex-logo-blue-cropped.png" alt="SciTeX" width="400">
  </a>
</p>

<p align="center"><b>Scientific type aliases (ArrayLike, ColorLike) + runtime validation predicates.</b></p>

<p align="center">
  <a href="https://scitex-types.readthedocs.io/">Full Documentation</a> · <code>uv pip install scitex-types[all]</code>
</p>

<!-- scitex-badges:start -->
<p align="center">
  <a href="https://pypi.org/project/scitex-types/"><img src="https://img.shields.io/pypi/v/scitex-types?label=pypi" alt="pypi"></a>
  <a href="https://pypi.org/project/scitex-types/"><img src="https://img.shields.io/pypi/pyversions/scitex-types?label=python" alt="python"></a>
  <a href="https://github.com/ywatanabe1989/scitex-types/actions/workflows/rtd-sphinx-build-on-ubuntu-latest.yml"><img src="https://img.shields.io/github/actions/workflow/status/ywatanabe1989/scitex-types/rtd-sphinx-build-on-ubuntu-latest.yml?branch=develop&label=docs" alt="docs"></a>
  <a href="https://scitex-types.readthedocs.io/en/latest/"><img src="https://img.shields.io/readthedocs/scitex-types?label=docs" alt="docs"></a>
</p>
<p align="center">
  <a href="https://github.com/ywatanabe1989/scitex-types/actions/workflows/pytest-matrix-on-ubuntu-py3-11-3-12-3-13.yml"><img src="https://img.shields.io/github/actions/workflow/status/ywatanabe1989/scitex-types/pytest-matrix-on-ubuntu-py3-11-3-12-3-13.yml?branch=develop&label=tests" alt="tests"></a>
  <a href="https://codecov.io/gh/ywatanabe1989/scitex-types"><img src="https://img.shields.io/codecov/c/github/ywatanabe1989/scitex-types/develop?label=cov" alt="cov"></a>
</p>
<!-- scitex-badges:end -->

---

## Problem and Solution

| # | Problem | Solution |
|---|---------|----------|
| 1 | `numpy.typing.ArrayLike` covers only **NumPy** — functions that also accept Torch/DataFrame/Series need a hand-rolled `Union` | `ArrayLike`, `ColorLike` — **stable aliases** spanning `list/tuple/np.ndarray/pd.DataFrame/pd.Series/xr.DataArray/torch.Tensor` + matplotlib color inputs |
| 2 | Checking **list of floats** at runtime ("is this a list of floats?") takes a 3-line comprehension | `is_array_like()`, `is_list_of_type(lst, float)` — clear **predicates**, no isinstance chain |

## Quick Start

```python
from scitex_types import ArrayLike, is_array_like, is_list_of_type

def process(data: ArrayLike) -> None: ...

is_array_like([1, 2, 3])           # True
is_list_of_type([1, 2, 3], int)    # True
```

## Demo

```python
from scitex_types import ArrayLike, is_array_like, is_list_of_type

def normalize(x: ArrayLike) -> ArrayLike:
    assert is_array_like(x)
    return x

normalize([1, 2, 3])             # OK
normalize("not array")           # AssertionError

is_list_of_type([1, 2, 3], int)  # True — uniform int list
is_list_of_type([1, "x"], int)   # False — mixed
```

```mermaid
flowchart LR
    Input[Function input] --> Pred{is_array_like?}
    Pred -- yes --> Proceed[proceed]
    Pred -- no --> Raise[raise / branch]
    style Proceed fill:#27ae60,stroke:#2c3e50,color:#fff
    style Raise fill:#e74c3c,stroke:#2c3e50,color:#fff
```

<p align="center"><sub><b>Figure 1.</b> Demo. Use <code>ArrayLike</code> in annotations, <code>is_array_like</code> as a one-line guard.</sub></p>

## Installation

```bash
uv pip install "scitex-types[all]"
```

<details>
<summary><strong>Extras</strong></summary>

| Extra | Enables |
|-------|---------|
| `all` | Every array-library match (`numpy`, `pandas`, `torch`, `xarray`) |
| `dev` | Maintainer tools (`pytest`, `sphinx` + theme/parser extensions) |

</details>

## Architecture

```
scitex_types/
├── _aliases.py     # ArrayLike, ColorLike unions
└── _predicates.py  # is_array_like, is_list_of_type
```

```mermaid
flowchart LR
    A[list / tuple] --> AL[ArrayLike]
    B[np.ndarray] --> AL
    C[pd.DataFrame / Series] --> AL
    D[xr.DataArray] --> AL
    E[torch.Tensor] --> AL
    AL --> P[is_array_like]
    F[mpl color string / RGB / RGBA] --> CL[ColorLike]
    style AL fill:#4a90d9,stroke:#2c3e50,color:#fff
    style CL fill:#8e44ad,stroke:#2c3e50,color:#fff
```

<p align="center"><sub><b>Figure 2.</b> Type surface. Two aliases unify common scientific containers and matplotlib color inputs; predicates resolve membership at runtime.</sub></p>

## 1 Interfaces

<details open>
<summary><strong>Python API</strong></summary>

<br>

```python
from scitex_types import ArrayLike, ColorLike, is_array_like, is_list_of_type

# Type annotations
def process(data: ArrayLike) -> None: ...
def set_color(c: ColorLike) -> None: ...

# Runtime checks
is_array_like([1, 2, 3])           # True
is_array_like("not array")         # False
is_list_of_type([1, 2, 3], int)    # True
is_list_of_type([1, "x"], int)     # False
```

</details>

## Part of SciTeX

`scitex-types` is part of [**SciTeX**](https://scitex.ai). Install via
the umbrella with `pip install scitex[types]` to use as
`scitex.types` (Python) or `scitex types ...` (CLI).

>Four Freedoms for Research
>
>0. The freedom to **run** your research anywhere — your machine, your terms.
>1. The freedom to **study** how every step works — from raw data to final manuscript.
>2. The freedom to **redistribute** your workflows, not just your papers.
>3. The freedom to **modify** any module and share improvements with the community.
>
>AGPL-3.0 — because we believe research infrastructure deserves the same freedoms as the software it runs on.

## License

AGPL-3.0-only (see [LICENSE](./LICENSE)).

---

<p align="center">
  <a href="https://scitex.ai" target="_blank"><img src="docs/scitex-icon-navy-inverted.png" alt="SciTeX" width="40"/></a>
</p>
