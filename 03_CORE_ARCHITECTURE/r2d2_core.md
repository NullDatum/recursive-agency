# R2D2 Recursive Problem-Solving Loop

> "Divide, recurse, resolve."

This document captures the core loop used throughout the repository for recursive discovery.

## Steps

1. **Decompose**
   - Split the problem into the smallest meaningful subproblems.
   - If a subproblem remains unsolved, break it down further.
2. **Hypothesize**
   - Generate candidate explanations for each atomic part.
3. **Mutate**
   - Produce variations of each hypothesis: reorder, invert, combine, or adjust parameters.
4. **Test**
   - Apply hypotheses to the data and observe outcomes.
5. **Score & Select**
   - Evaluate candidates by match quality, novelty, and alignment with prior insights.
6. **Aggregate**
   - Merge solved subparts into larger structures; recurse on any fragments that remain unsolved.
7. **Compress → Capsule**
   - Distill new insights and discard dead ends. Each capsule becomes memory for the next pass.
8. **Recursive Restart**
   - Feed the capsule forward and repeat until the problem is resolved or no new signal emerges.

## Pseudocode Skeleton
```python
seed = initial_problem
memory = []

while not solved:
    hypotheses = mutate(generate(seed, memory))
    results = [test(h, data) for h in hypotheses]
    scores = [score(r) for r in results]
    best = select(results, scores)
    capsule = compress(best, memory)
    if no_new_signal or repeats_detected:
        capsule = radical_compress(memory)
    memory.append(capsule)
    seed = capsule
```

Each iteration sharpens the search space, with only new signal surviving.

For a minimal working implementation that prints each capsule while solving a toy
summation problem, see
[`examples/basic_r2d2_usage.py`](../examples/basic_r2d2_usage.py).
