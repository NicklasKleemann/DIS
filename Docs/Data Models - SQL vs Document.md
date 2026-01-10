# Data Models - SQL vs Document

> **Core question:** How should I structure my data?

---

## Mental Models

| Type | Think of it as... |
|------|-------------------|
| **Relational (SQL)** | Excel spreadsheet with strict columns |
| **Document (NoSQL)** | Folder of Word docs (each can differ) |

---

## Quick Comparison

| Aspect | Relational (SQL) | Document (NoSQL) |
|--------|------------------|------------------|
| Structure | Normalized tables | Denormalized JSON trees |
| Reads | JOINs across tables | Single document fetch |
| Updates | Change once → everywhere | Update every copy |
| Schema | Strict (schema-on-write) | Flexible (schema-on-read) |
| Consistency | Strong (ACID) | Eventually consistent |

---

## 🧠 Reasoning Chain: "Which database should I use?"

### Question 1: How is my data shaped?

```
TREE-like? (one root, nested children)
  → User profile with positions, education, skills
  → ✅ Document DB is natural fit

GRAPH-like? (many-to-many connections)
  → Users follow users, products have categories
  → ✅ Relational DB handles joins
```

---

### Question 2: How often do I update shared data?

**Scenario:** 1000 users have job title "Software Developer". Company renames it to "Software Engineer".

```
SQL:
  UPDATE positions SET title = 'Software Engineer' 
  WHERE title = 'Software Developer'
  → ✅ One query, done

Document:
  Find every document with that title, update each
  → ❌ 1000 updates, error-prone
```

**Rule:** Shared data changes often → SQL

---

### Question 3: What's my typical query?

```
Fetch ONE complete entity?
  → "Give me everything about User #123"
  → Document: GET /users/123 (one fetch)
  → SQL: SELECT + JOIN + JOIN...
  → ✅ Document wins

Fetch ACROSS entities?
  → "All Engineering users who joined after 2020"
  → SQL: Simple WHERE clause
  → Document: Scan all documents
  → ✅ SQL wins
```

---

## Decision Flowchart

```
What are you building?
│
├─→ User profiles, blogs, catalogs
│   └─→ Self-contained? → Document DB
│
├─→ Banking, inventory, e-commerce
│   └─→ Transactions + relationships? → SQL
│
├─→ Social network, recommendations
│   └─→ Many-to-many? → SQL (or Graph DB)
│
└─→ Rapid prototyping
    └─→ Schema still changing? → Document (migrate later)
```

---

## Examples

### Relational: Resume Builder

```
Users:     id=1, name="Alice"
Positions: user_id=1, title="Developer"
Education: user_id=1, school="MIT"

Query: SELECT * FROM users 
       JOIN positions ON users.id = positions.user_id
       JOIN education ON users.id = education.user_id
       WHERE users.id = 1
```

- ✅ Update "Developer" → "Senior Developer" in one place
- ❌ **Impedance mismatch**: Code has objects, DB has tables

### Document: User Profile

```json
{
  "id": 1,
  "name": "Alice",
  "positions": [{"title": "Developer"}],
  "education": [{"school": "MIT"}]
}
```

- ✅ One fetch, no joins
- ❌ Renaming "Developer" requires updating every document

---

## Exam Template: SQL or NoSQL?

```
1. Data shape
   → Tree → Document
   → Graph → SQL

2. Update patterns
   → Shared data changes → SQL
   → Self-contained → Document

3. Query patterns
   → Whole entities → Document
   → Cross-entity queries → SQL
```
