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
