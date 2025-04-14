# Cost Optimization Solutions for E-Commerce Vendors

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Publication: IJISRT](https://img.shields.io/badge/Publication-IJISRT-blue)](https://www.ijisrt.com/cost-optimization-solutions-for-ecommerce-vendors)

## Table of Contents
- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Mathematical Model](#mathematical-model)
- [Methodology](#methodology)
- [Key Findings](#key-findings)
- [Repository Structure](#repository-structure)
- [Data Description](#data-description)
- [Implementation](#implementation)
- [Future Scope](#future-scope)
- [Publication](#publication)
- [License](#license)

## Overview
This repository contains the code, analysis, and findings from research on cost optimization solutions for e-commerce vendors. The project aims to provide vendors with methods to optimize their supply chain costs while maintaining high customer satisfaction levels, with a particular focus on perishable products like milk.

## Problem Statement
In today's competitive e-commerce landscape, smaller vendors struggle to compete with established market giants. With online sales increasing from 34.5% in 2017 to 53.9% in 2021 in the US alone, vendors need to:
- Deliver products quickly to satisfy customer expectations
- Minimize expenditure to maintain profit margins
- Effectively manage perishable product supply chains

## Mathematical Model
The project employs a comprehensive cost optimization model with multiple components:

- **Material Cost (MC)**: Cost of raw materials from vendors to facilities
  MC = ∑ Av,m x Cv,m v,m

- **Production Cost (PC)**: Cost of producing finished goods at facilities
  PC = ∑ Ag,f x Cg,f f,g

- **Transportation Cost (TC)**: Includes multiple transportation phases
  TC = ∑ Am,v,f x Cm,v,f v,f,m + ∑ Ag,f,w x Cg,w,f f,w,g + ∑ Ag,w,c x Cg,w,c w,c,g

- **Inventory Cost (IC)**: Specifically modeled for perishable goods

- **Objective Function**: Minimization of the total cost
  Min (∑ Av,m x Cv,m v,m + ∑ Ag,f x Cg,f f,g + ∑ Am,v,f x Cm,v,f v,f,m + ∑ Ag,f,w x Cg,w,f f,w,g + ∑ Ag,w,c x Cg,w,c w,c,g + IC)

## Methodology
The problem is solved using the **Differential Evolution (DE)** algorithm, a population-based metaheuristic optimization technique with several key advantages:

- Does not make assumptions about the underlying problem
- Efficiently explores the entire search space
- Requires minimal parameter adjustments
- Works well with real-world, multi-dimensional optimization problems

The implementation follows a standard DE workflow:
1. Initialization of random population
2. Mutation to create donor vectors
3. Crossover to create trial vectors
4. Selection of the best solutions
5. Iteration until convergence criteria are met

## Key Findings
- The Differential Evolution algorithm efficiently minimizes supply chain costs
- Optimization includes both scenarios with and without inventory costs
- Real-world data validation confirms the model's practical applicability
- Same-day delivery optimization requires special consideration for perishable products
- Multi-depot utilization provides significant cost advantages when properly optimized

## Repository Structure
- **code/** - Implementation of the Differential Evolution algorithm
- `main.py` - Core implementation of the cost optimization model
- `placeholder.md` - Placeholder file
- **data/** - Data files used for optimization
- `data2.xlsx` - Real-world dataset containing cost information
- `placeholder.md` - Placeholder file
- **report-presentation-poster/** - Documentation of the project
- **report/** - Detailed research paper (IJISRT23SEP1103.pdf)
- **presentation/** - Slide deck explaining the project
- **poster/** - Visual summary of the project
- `placeholder.md` - Placeholder file
- **LICENSE** - MIT License
- **README.md** - Project documentation

## Data Description
The model utilizes real-world data including:
- Material costs (MC): 43.12 per unit
- Production costs: 5.70 (milk) + 1.00 (add-on) per unit
- Transportation costs: Varying by distance and method
- Inbound: 0.04-1.30 per unit (open), 0.03-0.91 per unit (tanker)
- Outbound: 0.05-1.75 per unit (wholesale), 0.03-0.87 per unit (retailer)
- Inventory costs: Based on refrigerated storage requirements

## Implementation
The implementation uses Python with NumPy for the Differential Evolution algorithm:

```python
# Define objective function
def obj(x):
  total = []
  for i in range(len(x)-1):
      total += 100 * math.pow((x[i+1] - math.pow(x[i], 2)), 2) + math.pow((x[i]-1), 2)
  return total

# Define population size and parameters
pop_size = 500
bounds = asarray([(-5.0, 5.0), (-5.0, 5.0)])
iter = 50
F = 0.5  # Scale factor for mutation
cr = 0.7  # Crossover rate

# Perform differential evolution
solution = differential_evolution(pop_size, bounds, iter, F, cr)
```

## Future Scope
Future enhancements for this project include:
* Integration with AI, blockchain, and IoT for enhanced supply chain visibility
* Implementation of sustainability measures in the optimization model
* Development of collaborative partnerships within supply chains to improve resilience
* Real-time optimization models that adapt to changing market conditions

## Publication
This work has been published in the International Journal of Innovative Science and Research Technology (IJISRT):

**Citation:**  
Sashwat Desai. (Volume 8, Issue 9, September - 2023) "Cost Optimization Solutions for E-Commerce Vendors". International Journal of Innovative Science and Research Technology (IJISRT), www.ijisrt.com. ISSN - 2456-2165, PP: 1317-1337. https://doi.org/10.5281/zenodo.8397926

## License
This project is licensed under the MIT License - see the LICENSE file for details.
