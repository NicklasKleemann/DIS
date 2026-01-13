# Join Strategies

- Centralized
- Serialized
- Parallel

# Join Strategies

In a distributed database, relations involved in a join may be stored at different sites.

Join strategies describe how and where the join operation is executed.

The choice of strategy has a large impact on:

- Network traffic
- Query response time
- Overall system performance

---

## Centralized Join

In a centralized join, all relations involved in the join are moved to a single site, and the join is executed there.

How it works:

- One site is chosen as the join site
- All other relations are sent to that site
- The join is computed locally
- The result is returned

Advantages:

- Simple to implement
- Only one site performs the join

Disadvantages:

- Can require large amounts of data transfer
- The join site can become a bottleneck
- Not scalable for large data sets

This strategy is usually only used when the relations are small.

---

## Serialized Join

In a serialized join, the join is performed step by step across multiple sites.

How it works:

- One relation is sent to another site
- A partial join is performed
- The result is sent to the next site
- The process continues until the final result is produced

Advantages:

- Reduces the amount of data sent at each step
- Allows filtering at intermediate stages

Disadvantages:

- Slow, because operations happen one after another
- Increases total response time

This strategy is useful when intermediate results become much smaller.

---

## Parallel Join

In a parallel join, multiple join operations are executed at the same time on different sites.

How it works:

- Relations are partitioned into fragments
- Each site performs a local join on its fragments
- The partial results are combined

Advantages:

- Much faster than centralized or serialized joins
- Uses multiple machines at the same time
- Scales well for large data sets

Disadvantages:

- More complex to coordinate
- Requires careful data partitioning

This is the preferred strategy for large distributed systems.

---

## Summary

| Strategy | How it works | Main advantage | Main disadvantage |
| --- | --- | --- | --- |
| Centralized | Move all data to one site and join | Simple | High data transfer |
| Serialized | Join step by step across sites | Reduces data gradually | Slow execution |
| Parallel | Join fragments at many sites at once | Fast and scalable | Complex to manage |