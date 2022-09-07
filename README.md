# tarski-lite

A tiny wrapper for STRIPS-like functionality of the tarski library.

## Installing

For now, just place the `tarskilite.py` file in whatever project you need. If this grows large enough, we'll put it on PyPI.

## Usage

```python
import tarskilite as tl

problem = tl.STRIPS('domain.pddl', 'problem.pddl')

# Set of Fluent objects
problem.fluents

# Easy progression / regression
s0 = problem.init
act = list(problem.actions)[0]
s1 = tl.progress(s0, act)
s2 = tl.regress(problem.goal, act)

# Easy action/fluent lookup
act = problem.action('move loc1 loc2')
fluent = problem.fluent('connected loc1 loc2')
assert fluent == problem.fluent('(connected loc1 loc2)')
```

## Requirements

Just [tarski](https://github.com/aig-upf/tarski) with clingo option installed.

## Citing This Work

Coming soon...
