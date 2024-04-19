use math.nu *

let data = open ($env.FILE_PWD | path join "scores.nuon")

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
    ($env.FILE_PWD | path join "plot.py"),
    $"($data.score | to text)",
    ($days | to json),
]
print "done"

print --no-newline "generating normalized figure... "
python ...[
    ($env.FILE_PWD | path join "plot-values.py"),
    "normalized-scores.png",
    ...($data.score | math zip-diff | math normalize | math acc),
]
print "done"

print --no-newline "generating rectified figure... "
let min = $data.score | math zip-diff | math min | into float
let max = $data.score | math zip-diff | math max | into float
python ...[
    ($env.FILE_PWD | path join "plot-values.py"),
    "rectified-scores.png",
    ...(
        $data.score
            | math zip-diff
            | math map { a: $min, b: $max } { a: -1., b: 1. }
            | math acc
    )
]
print "done"

let deltas = $data.score | math zip-diff

print --no-newline "generating deltas distribution figure... "
python ...[
    ($env.FILE_PWD | path join "plot-bars.py"),
    "deltas-distribution.png",
    ...$deltas,
]
print "done"

print --no-newline "generating deltas distribution animation... "
python ...[
    ($env.FILE_PWD | path join "animate-bars.py"),
    "deltas-distribution.gif",
    ...$deltas,
]
print "done"
