# Distributed Database Design

## Definition

Distributed Database Design is the process of deciding how a database and the applications that use it should be placed across multiple sites in a distributed system.

Instead of storing all data in one central location, a distributed database stores data on several machines that are connected by a network. These machines work together so that, to the user, the system appears as a single database.

The design involves deciding:

- Where data should be stored
- Which data should be replicated
- Which data should be fragmented
- How applications and queries access the distributed data

The goal is to achieve high performance, reliability, and scalability while hiding the complexity of distribution from users.

---

## Advantages of Distributed Database Design

### High Availability

If one site fails, other sites can continue to provide access to the data. This makes the system more reliable and fault tolerant than a single centralized database.

---

### Better Performance

Data can be stored closer to where it is used. This reduces network traffic and query response time, especially when users are spread across different locations.

---

### Scalability

New machines and storage can be added to the system without stopping it. This allows the database to grow as the amount of data and the number of users increase.

---

### Local Autonomy

Each site can handle its own local data and operations. This allows organizations to manage their own data while still being part of a larger distributed system.

---

## Disadvantages of Distributed Database Design

### Increased Complexity

Designing a distributed database is much more complicated than designing a centralized one. The system must handle communication between sites, data placement, and coordination between nodes.

---

### Consistency and Synchronization Issues

Because data is stored at multiple sites, keeping all copies consistent is difficult. Network delays and failures can cause sites to have different versions of the same data.

---

### Higher Cost

Distributed systems require more hardware, more network infrastructure, and more software for coordination and fault tolerance. This makes them more expensive to build and maintain.

---

### Security Challenges

Data is transmitted across networks and stored in multiple locations, which increases the risk of unauthorized access and data breaches.

---

## Primary Copy in Distributed Database Design

### What is the Primary Copy?

In a distributed database that uses replication, one site is chosen as the primary copy. This site is responsible for all updates to the data.

All other sites store replica copies that are synchronized with the primary.

---

### How It Works

All write operations are sent to the primary site.

The primary site performs the update and then sends the changes to the replica sites.

The replicas update their copies to stay consistent with the primary.

Read operations can be handled either by the primary or by the replicas.

---

### Why Primary Copy Is Used

Using a primary copy simplifies the management of consistency because only one site is allowed to modify the data. This avoids conflicting updates and makes transaction control easier.

However, the primary site can become a bottleneck and a single point of failure, so systems must have mechanisms to replace it if it goes down.