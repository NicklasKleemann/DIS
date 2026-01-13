# Distributed Query Processing and Optimization

This section covers how queries are processed when data is distributed across multiple sites. The key challenges are minimizing network transfer costs and exploiting parallelism.

### **Core Principle**

In distributed query processing, it is possible to construct a relation $r$  from its fragments. The query processor must **replace** relation names with expressions that reconstruct them, then **optimize** to minimize cross-site data movement.

[Cost Model in Distributed Queries](Distributed%20Query%20Processing%20and%20Optimization/Cost%20Model%20in%20Distributed%20Queries%202e67c6b7cc2f806a9efed486c9c6fa37.md)

[Query Processing on Fragmented Data](Distributed%20Query%20Processing%20and%20Optimization/Query%20Processing%20on%20Fragmented%20Data%202e67c6b7cc2f8040a3e0d951d2109baf.md)

[Query Transformation and Reduction](Distributed%20Query%20Processing%20and%20Optimization/Query%20Transformation%20and%20Reduction%202e67c6b7cc2f8094b229ca9bf76f5d89.md)

[Reduced Query Trees](Distributed%20Query%20Processing%20and%20Optimization/Reduced%20Query%20Trees%202e67c6b7cc2f80feaaa2fa48127c60a9.md)

[Distributed Join Processing](Distributed%20Query%20Processing%20and%20Optimization/Distributed%20Join%20Processing%202e67c6b7cc2f8002b041d0ab50d62e3e.md)

[Join Strategies](Distributed%20Query%20Processing%20and%20Optimization/Join%20Strategies%202e67c6b7cc2f80c99661d6717cfc175f.md)

[Semijoin Strategy](Distributed%20Query%20Processing%20and%20Optimization/Semijoin%20Strategy%202e67c6b7cc2f804cb7afe98a8aa938b6.md)

[Cost Analysis of Join Strategies](Distributed%20Query%20Processing%20and%20Optimization/Cost%20Analysis%20of%20Join%20Strategies%202e67c6b7cc2f804b9284da316ca45269.md)