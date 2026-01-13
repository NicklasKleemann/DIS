# Programming Model

- Functional Programming Roots
- Map and Reduce
- Key–Value Model
- WordCount Example
- Other Examples

## Key Terms

| Term | Definition |
| --- | --- |
| MapReduce | A programming model that processes data by transforming and then aggregating key–value pairs. |
| Map | A function that takes one key–value pair and produces a list of new key–value pairs. |
| Reduce | A function that takes a key and all its associated values and merges them into a smaller set. |
| Key–Value Pair | The basic data unit in MapReduce: a key identifies data, a value holds the data. |
| Shuffle and Sort | The system operation that groups all intermediate values with the same key and sends them to the same reducer. |
| Mapper | A worker that runs the map function on a subset of the data. |
| Reducer | A worker that runs the reduce function on grouped intermediate data. |

---

## Functional Programming Roots

MapReduce comes from **functional programming**, where two important operations are used:

### Map

Transforms each element in a list independently.

Example from the slides:

To compute the length of a vector

$v = (v_1, v_2, v_3, v_4)$

we first square each value:

$f(x) = x^2$

This step can be fully parallelized.

### Fold (Reduce)

Combines all values into one result.

$g(x_1, x_2) = x_1 + x_2$

This aggregates the squared values to compute:

$|v| = \sum v_i^2$

MapReduce uses exactly this pattern:

**transform first, then aggregate**.

---

## The MapReduce Key–Value Model

The slides define the model as:

**Input:**

A set of key–value pairs

**Output:**

Another set of key–value pairs

The programmer must write two functions:

### Map

$map(k_1, v_1) \rightarrow list(k_2, v_2)$

Takes an input pair and produces intermediate key–value pairs.

### Reduce

$reduce(k_2, list(v_2)) \rightarrow list(v_3)$

Takes one key and all its values and merges them into a smaller set (usually one value).

The system automatically:

- Groups intermediate pairs by key
- Sends all values with the same key to the same reducer

---

## Step-by-Step: How MapReduce Works

1. Input data is split into pieces
2. Each mapper receives a subset of the data
3. The mapper outputs intermediate (key, value) pairs
4. The system performs **Shuffle & Sort**
    - Groups all identical keys
    - Moves data to the right reducers
5. Each reducer processes one key and its list of values
6. Final output is written

This creates **parallelism in both map and reduce phases**.

---

## WordCount Example

Goal:

Count how many times each word appears in a large collection of documents.

### Map step

Each mapper:

- Reads a document
- For each word, outputs:
    
    ```
    (word,1)
    ```
    

### Reduce step

Each reducer:

- Receives all `(word, 1)` pairs for a word
- Adds the values
- Outputs:
    
    ```
    (word, total_count)
    ```
    

### Code from the slides

**Map**

```
map(Stringkey,String value):
foreach word win value:
    emit(w,1)
```

**Reduce**

```
reduce(String key, Iteratorvalues):
intresult=0;
foreach vinvalues:
result+= v;
  emit(result);
```

---

## Why WordCount Scales

- Many mappers can process different documents in parallel
- Many reducers can count different words at the same time
- No shared memory or locks are needed

---

## Other Examples

From the slides:

### Counting URL accesses

- Map outputs `(URL, 1)` for each log entry
- Reduce adds all 1’s per URL

### Reverse web-link graph

- Map outputs `(target, source)` for each link
- Reduce outputs the list of URLs that link to a target

These examples show that MapReduce works for:

- Counting
- Grouping
- Building relationships

---

## Why This Programming Model Works

MapReduce allows:

- Massive parallelism
- Simple programming
- Automatic handling of data distribution

The programmer only writes **map** and **reduce** — everything else is handled by the system.