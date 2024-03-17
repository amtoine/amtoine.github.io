## add new scores
```nushell
let scores = open raw.txt
    | split row "amtoine — "
    | where not ($it | is-empty)
    | each { str trim | lines }
    | each {|it|
        let date = $it.0 | into datetime
        $it | skip 1 | each {{ date: $date, score: ($in | into int) }}
    }
    | flatten
```
```nushell
open content/posts/my-mario-kart-8-deluxe-adventure/scores.nuon
    | append $scores
    | save --force content/posts/my-mario-kart-8-deluxe-adventure/scores.nuon
```

## setup python
```nushell
virtualenv .venv
overlay use .venv/bin/activate.nu
pip install matplotlib
```

## generate the figures
```nushell
overlay use .venv/bin/activate.nu
nu content/posts/my-mario-kart-8-deluxe-adventure/main.nu
```
