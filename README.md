
# Exercises: Git Repo Merging and Python Loop-Append

## Git Merging Pattern: Fork, Clone, Commit, Push, and Pull-Request

  1. **Fork**: Github-specific, it makes a copy of a repo that you can write to.
  2. **Clone**: Make a Git copy of the Github repo on your local computer.
  3. **Commit**: Snapshot any changes you made
  4. **Push**: Upload the new snapshots to your forked repo
  5. **Pull-Request**: Send a message to the original repo owner asking them to accept your changes.


## Syntax Vocabulary: 

### "Level 1": Characters Alone

Having similar vocabulary helps improve communication.  Especially confusing sometimes are the symbols that don't appear in our daily language--particularly the various types of brackets

| **Symbol**      | **Spoken Name** |
| ----------      | -------- |
|  \(  \[  \{  \< | "Open"  |
|  \)  \]  \}  \> | "Closed"  |
|  \(   \)        | "Parentheses" or "Parens" |
| \[  \]          | "Square Brackets" |
| \{  \}          | "Curly Braces"   |
|  \.             | "Dot" |
| \:              |  "Colon"  |
|  \;             |  "Semicolon"  |
|  \=          |   "an equals sign"      |
|  \=\=        |   "is equal"          |
| \'    |  "single quote" or "apostrophe"  |
| \`  | "back tick"  |
| \"    |   "double quote" or "quotation mark"   |
| \\  |  "back slash"  |
|  \/  | "forward slash"  |



### "Level 2":  Combinations of characters

| **Symbol** | **Spoken Name** |
| ---------- | -------- |
|  x = 3  |  "assign 3 to x"  |
|  x = [] |  "make x an empty list"  |
  |  x[2]   |  "get item", "get the third item from x", "get the element from x with the index two" |
|  x = {}  | "make an empty dict/dictionary |
| x = {"nick": False, "doug": True} |  "Make a dict with names as *keys* and attendance as boolean *values*"  |
|  x["nick"]  | "get the nick item from the x dict"  |
| x[2] = "hi" | "set the third item in x to hi"  |
|   mean(data=x)  | "call the mean function on x" |
|  \"\"\"   |  "docstring" |



### "Level 3":  Blocks of code

"If x is greater than 4, set y to 3.  Else set y to 10."
```python
if x > 4:
    y = 3
else:
    y = 10
````

"print the value of x as long as x is less than 5"
```python
while x < 5:
  print(x)
```

"for each name in the list of names, print the length of the name"
```python
names = ["alice", "bob", "charlie"]

for i in range(len(names)):
  name = names[i] 
  print(len(name))
```

```python
names = ["alice", "bob", "charlie"]
for name in names:
  print(len(name))
```

```python
names = ["alice", "bob", "charlie"]
ages = [4, 5, 6]

for name, age in zip(names, ages):
  print(len(name))
```

## The "Loop-Append" Pattern

```python
names = ["alice", "bob", "charlie"]  # List of Strings

big_names = []
for name in names:
    big_name = name.capitalize()
    big_names.append(big_name)
```

General Tips around this pattern:

  1. Put the empty new list as close to the start of the loop as you can (preferably right above).  It helps define the goal of the loop and makes the code more readable.
  2. Try thinking of these lists in terms of a type structure (e.g. "a List of Strings" or "a Tuple of Ints").  It will help with building a mental model of what code goes where.
  3. Name your sequences (tuples, lists, dicts) as plural nouns.  It will make it easier to name the items in a loop, and make the code readable.
