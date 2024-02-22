use math.nu *

let data = open content/posts/my-mario-kart-8-deluxe-adventure/scores.nuon

let days = $data
    | enumerate
    | flatten
    | update date { format date "%Y-%m-%d"}
    | group-by date
    | items {|k, v| {
        date: $k,
        index: ($v | last).index,
        score: ($v | last | get score | into int),
    }}

print --no-newline "generating full figure... "
python ...[
    content/posts/my-mario-kart-8-deluxe-adventure/plot.py,
    $"($data.score | to text)",
    ($days | to json),
]
print "done"

print --no-newline "generating normalized figure... "
python ...[
    content/posts/my-mario-kart-8-deluxe-adventure/plot-values.py,
    "normalized-scores.png",
    ...($data.score | math zip-diff | math normalize | math acc),
]
print "done"

print --no-newline "generating rectified figure... "
python ...[
    content/posts/my-mario-kart-8-deluxe-adventure/plot-values.py,
    "rectified-scores.png",
    ...(
        $data.score
            | math zip-diff
            | math map { a: -13., b: 26. } { a: -1., b: 1. }
            | math acc
    )
]
print "done"
