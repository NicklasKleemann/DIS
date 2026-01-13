# The Context of Data-Intensive Systems

# Definition

**Data-Intensive Applications** are systems where **data** is the primary bottleneck rather than CPU cycles. Unlike compute-intensive applications (where CPU power is the limiting factor), data-intensive systems struggle with the **quantity, complexity** and **speed** of data change

# Core Idea

The shift to data-intensive systems is driven by the digitalization of society, where applications (e.g., Google, Facebook, Amazon, IoT weather monitoring) must manage massive, dynamic datasets. To handle this, systems must be designed to be **scalable, available (robust)** and **maintainable**

# The 5 Vs of Big Data

The primary challenges in data-intensive systems are often summarised as the **5 Vs**

- **Volume:** The quantity of data
- **Variety:** The complexity of data types
- **Velocity:** The speed of data change
- **Veracity:** The uncertainty or accuracy of the data
- **Value:** The utility of data for good

# Building Blocks of Data Systems

A data system is rarely a single tool; it is a composition of hardware and software designed to store, manage and process data. Common building blocks include:

- **Databases:** For persistent storage
- **Indexes:** For efficient data search
- **Caching:** To reuse results of expensive operations
- **Stream Processing:** For sending messages to be handled asynchronously
- **Batch Processing:** To periodically handle large amounts of accumulated data

# System Architecture

**Composition over Monoliths:** A complete data system is often built by stitching together various tools (databases, caches, queues, full-text indexes) via application code and APIs

- **Example:** An architecture might use a primary database for storage, separate full-text