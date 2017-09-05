# DMST-Algorithms-and-Data-Structures-Assignments (Python assignments)

They are from course **Algorithms and Data Structures** writted by [Panos Louridas](https://github.com/louridas), *Department of Management Science and Technology*, Athens University of Economics and Business. 

## Assignment: Tournament planning

You can find the assignment [here](https://github.com/dmst-algorithms-course/assignment-2017-1).

In this programm we must schedule the tournament so that each competitor has only one match each day.
The program read a file from command prompt like:
`python plan_matches.py graph_file`

* The `graph_file` in the form:

```
a b
a c
b c
c d
d e
e c
...
```

**Example:** For the file [example_graph.txt](tournament_planning/example_graph_1.txt) 
`python plan_matches.py graph_file_1.txt` the output is:

```
(a, b) 0
(a, c) 1
(b, c) 2
(c, d) 0
(c, e) 3
(d, e) 1
```


**More information:**

* The problem that we described is called edge 'colouring problem'

* You can find more at wikipedia's [article] (https://en.wikipedia.org/wiki/Edge_coloring)


## Assignment: Findings groups 

You can find the assignment [here](http://nbviewer.jupyter.org/github/dmst-algorithms-course/assignment-2017-2/blob/master/assignment_2017_2.ipynb).

The program read a file from command prompt like
`python community_structure.py [-n GROUPS ] graph_file` and detects community structure in networks.

* The `graph_file` in the form:

```
1 3
1 10
2 3
4 10
...
```
* The `GROUPS` is the number of the team we want to segmentate. If we don't write any number then it's mean 2 teams.


**Example:** For the file [example_graph_1.txt](finding_groups/example_graph_1.txt) 
`python community_structure.py 3 example_graph_1.txt` the output is:

```
[1, 2, 3, 10]
[4, 5, 6]
[7, 8, 9]
Q = 0.4896
( Q is the segmentation)
```

**More information:**

* The algorithm that we use at the exercise was added by M. E. J. Newman at the article "Fast algorithm for detecting community structure in networks", Phys. Rev. E 69, 066133, 2004. You can find it [here](https://arxiv.org/abs/cond-mat/0309508).


## Assignment: Steiner system (Steiner Triple Systems)

You can find the assignment [here](http://nbviewer.jupyter.org/github/dmst-algorithms-course/assignment-2017-3/blob/master/assignment_2017_3.ipynb).

The program read a file from command prompt like
`python sts.py n`
creates a list with all blocks sorted, and their number.

* A Steiner system with parameters t, k, n, written S(t,k,n), is an n-element set S together with a set of k-element subsets of S (called blocks) with the property that each t-element subset of S is contained in exactly one block.

**Example:**
`python sts.py 9` the output is: 
```
[(1, 2, 8), (1, 3, 5), (1, 4, 6), (1, 7, 9), (2, 3, 6), (2, 4, 7), (2, 5, 9), (3, 4, 9), (3, 7, 8), 
(4, 5, 8), (5, 6, 7), (6, 8, 9)]
12
```

**More information:**

* More information about Steiner systems you can find at this [article of Wikipedia](https://en.wikipedia.org/wiki/Steiner_system).
* you can also see this link about steiner. (http://mathworld.wolfram.com/SteinerTripleSystem.html)


## Bonus Assignment: Gelling and Melting Large Graphs by Edge Manipulation

You can find it [here](https://github.com/stathoula/Gelling-and-Melting-Large-Graphs-by-Edge-Manipulation).
