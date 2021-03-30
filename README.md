
# Exercises: Git Repo Merging and Python Loop-Append

## Git Merging Pattern: Fork, Clone, Commit, Push, and Pull-Request

  1. **Fork**: Github-specific, it makes a copy of a repo that you can write to.
  2. **Clone**: Make a Git copy of the Github repo on your local computer.
  3. **Commit**: Snapshot any changes you made
  4. **Push**: Upload the new snapshots to your forked repo
  5. **Pull-Request**: Send a message to the original repo owner asking them to accept your changes.


## The "Loop-Append" Pattern

```python
names = ["alice", "bob", "charlie"]

big_names = []
for name in names:
    big_name = name.capitalize()
    big_names.append(big_name)
```

General Tips around this pattern:

  1. Put the empty new list as close to the start of the loop as you can (preferably right above).  It helps define the goal of the loop and makes the code more readable.
  2. Try thinking of these lists in terms of a type structure (e.g. "a List of Strings" or "a Tuple of Ints").  It will help with building a mental model of what code goes where.
  3. Name your sequences (tuples, lists, dicts) as plural nouns.  It will make it easier to name the items in a loop, and make the code readable.
