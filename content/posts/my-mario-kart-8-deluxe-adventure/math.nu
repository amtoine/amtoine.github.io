export def "math normalize" []: [list<int> -> list<int>, list<float> -> list<float>] {
    let values = $in

    let stddev = $values | into float | math stddev
    let avg = $values | into float | math avg

    $values | each { ($in - $avg) / $stddev }
}

export def "math zip-diff" []: [list<int> -> list<int>, list<float> -> list<float>] {
    let values = $in

    $values | zip ($values | skip 1) | each { $in.1 - $in.0 }
}

export def "math acc" []: [list<int> -> list<int>, list<float> -> list<float>] {
    let values = $in
    $values
        | skip 1
        | reduce --fold ($values | take 1) {|it, acc|
            $acc | append ($acc | last | $in + $it)
        }
}

export def "math map" [
    from: record<a: float, b: float>,
    to: record<a: float, b: float>,
]: [list<int> -> list<int>, list<float> -> list<float>] {
    let values = $in
    let m = ($to.a - $to.b) / ($from.a - $from.b)

    $values | each { $m * ($in - $from.a) + $to.a }
}
