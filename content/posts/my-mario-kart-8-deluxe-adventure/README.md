## python
```nushell
virtualenv .venv
overlay use .venv/bin/activate.nu
pip install matplotlib
```

## generate the image
```nushell
let scores = open content/posts/my-mario-kart-8-deluxe-adventure/scores.nuon
    | get score

let days = open content/posts/my-mario-kart-8-deluxe-adventure/scores.nuon
    | enumerate
    | flatten
    | update date { format date "%Y-%m-%d"}
    | group-by date
    | items {|k, v| {
        date: $k,
        index: ($v | last).index,
        score: ($v | last | get score | into int),
    }}

python ...[
    content/posts/my-mario-kart-8-deluxe-adventure/plot.py,
    $"($scores | to text)",
    ($days | to json),
]
```

```nushell
use content/posts/my-mario-kart-8-deluxe-adventure/math.nu *

let scores = open content/posts/my-mario-kart-8-deluxe-adventure/scores.nuon
    | get score
let norm_acc_scores = $scores | math zip-diff | math normalize
python ...[
    content/posts/my-mario-kart-8-deluxe-adventure/plot-normalized.py,
    ...($norm_acc_scores | math acc),
]
```
