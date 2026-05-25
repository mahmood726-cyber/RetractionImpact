# RetractionImpact

[![ci](https://github.com/mahmood726-cyber/RetractionImpact/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/mahmood726-cyber/RetractionImpact/actions/workflows/ci.yml) [![codeql](https://github.com/mahmood726-cyber/RetractionImpact/actions/workflows/codeql.yml/badge.svg?branch=master)](https://github.com/mahmood726-cyber/RetractionImpact/actions/workflows/codeql.yml) [![license: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![python: 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)

Retraction Fragility Quantifier — How robust is your meta-analysis to study retractions?

## Methods
- **Retraction Fragility Index (RFI)** — minimum retractions to reverse conclusion
- **Leave-one-out** — impact of each study's removal
- **Greedy sequential removal** — most impactful first
- **Combinatorial search** — exhaustive for depths 1-3

## Plots
- Impact waterfall (sorted by absolute effect change)
- Fragility curve (P-value vs retractions removed)
- Leave-one-out forest plot

## Examples
- Statins & Mortality (robust, RFI > 5)
- Ivermectin & COVID (fragile, RFI = 1)
- Surgery vs Medical (marginal)

## Live Demo
https://mahmood726-cyber.github.io/RetractionImpact/

## Author
Mahmood Ahmad, Tahir Heart Institute
