# Distributed Data Storage

This section addresses the fundamental question: *Where should data physically live?*

### **Distributed Database Design**

How should the database and applications on top of it be placed **across the sites**? We assume the relational data model, but the techniques can be applied to others.

### **Two Orthogonal Strategies**

| Strategy | Description | Key Trade-off |
| --- | --- | --- |
| **Replication** | Maintain multiple copies of data at different sites | Read performance vs. write complexity |
| **Fragmentation** | Partition a relation into fragments stored at distinct sites | Locality vs. reconstruction cost |

**These can be combined:** A relation is partitioned into several fragments, and the system maintains several identical replicas of each fragment.

[Distributed Database Design](Distributed%20Data%20Storage/Distributed%20Database%20Design%202e67c6b7cc2f8096ac62d567c88a0713.md)

[Replication](Distributed%20Data%20Storage/Replication%202e67c6b7cc2f80acb604d3a06474e5fc.md)

[Fragmentation](Distributed%20Data%20Storage/Fragmentation%202e67c6b7cc2f8076aba5c40ad7d2d414.md)

[Data Transparency](Distributed%20Data%20Storage/Data%20Transparency%202e67c6b7cc2f80b0b0a0e23d87e0a0b5.md)

---