#Graph Theory and Graph Databases


Facebook and Google are built from the use of Graph Data.  Not just the discrete matching of data to individual items,
but also the relationships that exist between them.

Graph Theory - pioneered by Euler in the 18th Century

Open-Source Graph Database - Neo4j

Use this for practice: [Supplemental Material](https://github.com/iansrobinson/graph-databases-use-cases)


# Chapter 1

What is a Graph? - A collection of veritces and edges (set of nodes and the relationships that connect them)


Labeled Property Graph Model

1. It contains nodes and relationships
2. Nodes contain properties (key-value pairs)
3. Nodes can be labeled with one or more labels
4. Relationships are named and directed, and always have a start and end node
5. Relationships can also contain properties


1. Graph Databases
  - Technologies used primarily for transactional online graph persistence, typically accessed directly in real time from 
    an application
  - The equivalent of "normal" online transactional processing (OLTP) databases in the relational world.

2. Graph Computer Engines
  - Technologies used primarily for offline graph analytics, typically performed as a series of batch steps.
  - They can be thought of as being in the same category as other technologies for analysis of data in bulk, such
    as data mining and online analytical processing (OLAP)

#Citing- Graph Databases 2nd Edition - Ian Robinson, Jim Webber & Emil Eifrem
