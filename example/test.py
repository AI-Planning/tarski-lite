
import tarskilite as tl

problem = tl.STRIPS('domain.pddl', 'problem.pddl')

# Set of Fluent objects
print(problem.fluents)

# Easy progression / regression
s0 = problem.init
a1 = problem.action('(go-out hoist0 depot0-1-1 loadarea)')
a2 = problem.action('drop(hoist0, crate0,depot0-1-1, loadarea, depot0)')
s1 = tl.progress(s0, a1)
s2 = tl.regress(problem.goal, a2)

# Easy action/fluent lookup
fluent = problem.fluent('connected loc1 loc2')
assert fluent == problem.fluent('(connected loc1 loc2)')
