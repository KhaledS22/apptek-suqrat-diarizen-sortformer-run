# Meeting Explanation

This repo was created as a clean handoff package for external inference runs. The goal was to give the team a very small repo that focuses only on generating hypothesis RTTM outputs for AppTek and Suqrat.

The workflow is simple: update the manifest audio roots on the target machine, create the output folders, run DiariZen or Sortformer, and return the RTTM outputs. The package does not score results and does not contain private audio.

The most important files are the two manifests and the four run scripts. The main limitation is that successful runtime depends on the target environment having the required model dependencies, especially NeMo for Sortformer.
