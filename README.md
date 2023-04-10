# Query Refinement for Diversity Constraint Satisfaction

## Abstract
Diversity, group representation, and similar needs often apply to query results, which in turn require constraints on the sizes of various subgroups in the result set. Traditional relational queries only specify conditions as part of the query predicate(s) and do not support such restrictions on the output. In this paper, we study the problem of modifying queries to have the result satisfy constraints on the sizes of multiple subgroups in it. This problem, in the worst case, cannot be solved in polynomial time. Yet, with the help of provenance annotation, we are able to develop a query refinement method that works quite efficiently, as we demonstrate through extensive experiments. 


## Algorithms
baseline algorithm: traverse all possible refinements. located in Algorithm/Baseline.py

our algorithm: use provenance expressions and PVL to accelerate the searching. 
located in Algorithm/ProvenanceSearchValues.py


## How to run experiments
run any .py file under folder Experiment


