+++
title = "My Mario Kart 8 Deluxe Adventure"
date = 2024-02-20T10:53:00+02:00
lastMod = 2024-04-19T19:15:32+02:00
author = "amtoine"
authorTwitter = "" #do not include @
cover = "/posts/my-mario-kart-8-deluxe-adventure.gif"
tags = ["gaming", "nintendo", "mario"]
keywords = ["", ""]
description = "Showcasing my progress and scores on MK8."
showFullContent = false
readingTime = true
hideComments = false
color = "green" #color from the theme settings
+++

hello there {{<image
    src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif"
    alt="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif"
    title="Wave hand"
    height="25"
    width="25"
    position="center"
>}}

In february 2024, i've started playing [Mario Kart 8 Deluxe] online: it's fun to
run against bots and complete the full solo _campaign_ but it's even more fun to
compete against real humans, stronger and stronger as you become better yourself.

> **Note**  
> i'll be posting regular updates on that page to make sure the VR plots are up
> to date!

As a kind of _scientific experiment_, i've started recording my points after
each race.
In fact, i was just curious to see what the shape of the resulting curve would
look like over time :yum:

## My personal leaderboard
{{<image
    src="/posts/my-mario-kart-8-deluxe-adventure/scores.png"
    alt="/posts/my-mario-kart-8-deluxe-adventure/scores.png"
    title="MK8 scores"
    position="center"
>}}

One might notice that the range of points a player can earn after each course is
not centered around 0. In fact, as far as i know, the possible values range from
around 26 when winning a race to -13 when losing.

What happens to the global VR graph when we try to _rectify_ the possible values
a _point delta_ can take?

#### Normalizing
The first naive method would be to normalize the _deltas_ so that the
distribution of values, between 26 and -13, becomes a normal distribution with
mean 0 and standard deviation 1:
{{<image
    src="/posts/my-mario-kart-8-deluxe-adventure/normalized-scores.png"
    alt="/posts/my-mario-kart-8-deluxe-adventure/normalized-scores.png"
    title="MK8 normalized scores"
    position="center"
>}}

The biggest and immediate flaw with that is that, as the _deltas_ become evenly
distributed around 0, the overall VR graph stays near 0 :thinking:

However, we can see a few things
- there has been a steep improvement with the first 50 races
- then there is a plateau until around the 120th race
- then there is a negative slope, probably some hard times lol
- finally the start of another plateau?

#### Rectifying
Another idea would be to _rectify_ the _deltas_. By that i mean, as i know their
possible values range from around 26 to -13, it's quite easy to just shift and
squeeze them inside the range from -1 to 1 and see what it looks like:
{{<image
    src="/posts/my-mario-kart-8-deluxe-adventure/rectified-scores.png"
    alt="/posts/my-mario-kart-8-deluxe-adventure/rectified-scores.png"
    title="MK8 rectified scores"
    position="center"
>}}

This time, it's quite similar to the first graph, except the values are hopefully
more meaningful, e.g. if i were to only earn a few points in a row, that would
likely translate into negative points once rectified and thus we would see a
negative slope rather than a positive one with the official MK8 VR system.

#### My score deltas
Another thing that can be nice to investigate is the distribution of my score deltas.

What is a score delta?
Here, it's simply the difference between two consecutive VR snapshots, i.e. the amount
of points i loose or gain after a given race.

{{<image
    src="/posts/my-mario-kart-8-deluxe-adventure/deltas-distribution.png"
    alt="/posts/my-mario-kart-8-deluxe-adventure/deltas-distribution.png"
    title="Score deltas"
    position="center"
>}}

And here is the evolution of the deltas distribution over time:
{{<image
    src="/posts/my-mario-kart-8-deluxe-adventure/deltas-distribution.gif"
    alt="/posts/my-mario-kart-8-deluxe-adventure/deltas-distribution.gif"
    title="Score deltas animation"
    position="center"
>}}

{{< bar >}}

{{< comments >}}

[Mario Kart 8 Deluxe]: https://www.nintendo.com/us/store/products/mario-kart-8-deluxe-switch/
