# E156 Protocol — RetractionImpact

**Project**: RetractionImpact
**Created**: 2026-04-09
**Type**: meta-scientific
**Estimand**: Retraction Fragility Index (minimum retractions to reverse significance)
**Dashboard**: https://mahmood726-cyber.github.io/RetractionImpact/

## E156 Body (156 words, 7 sentences)

How many study retractions would be needed to reverse the conclusion of a meta-analysis? We introduce the Retraction Fragility Index (RFI), defined as the minimum number of studies whose removal changes the pooled result from significant to non-significant (or vice versa), computed via greedy sequential removal and exhaustive combinatorial search for depths up to three. The analysis pipeline performs leave-one-out impact quantification, identifies the single most influential study, and constructs a fragility curve showing p-value degradation as studies are greedily removed in order of maximum impact. Applied to landmark statin mortality trials (11 studies, HR 0.87), the RFI exceeds the search depth — indicating robust conclusions — while a simulated ivermectin-COVID dataset (7 studies) yields RFI = 1, meaning a single retraction reverses significance. Visualizations include impact waterfall charts sorted by absolute effect shift, fragility curves with alpha = 0.05 threshold, and leave-one-out forest plots with reversal flags. The method extends traditional fragility analysis from within-study event modification to between-study retraction scenarios. RFI does not account for correlated retractions from the same research group or institution.
