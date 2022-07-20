---
# YAML metadata
title: "Resampling as a cure for traditional statistics"
author: Matthew Brett
---

# A mosquito problem

![](mosquito_banner.png)

With thanks to John Rauser: [Statistics Without the Agonizing Pain](https://www.youtube.com/watch?v=5Dnw46eC-0o)

# The data

![](mosquito_data.png)

# The t-test

![](t_test_formula.png)

# The permutation way

* Calculate difference in means
* Pool
* Repeat many times:
    * Shuffle
    * Split
    * Recalculate difference in means
    * Store

# On balls

![](just_balls.png)

# The difference in means

![](beer_mean.png)

# The difference in means: 23.60 - 19.22 4.38

![](water_mean.png)

# Shuffle

![](fake_balls1.png)

# A difference if the null is true

![](fake_beer_mean1.png)

# One difference on null: 22.84 - 20.28 = -1.26

![](fake_water_mean1.png)

# And again

![](fake_beer_mean2.png)

# Another difference on null: 22.20 - 21.17 = 1.03

![](fake_water_mean2.png)

# And so on, 10000 times

![](sampling_distribution.png)

# But how?

On to the notebook.
