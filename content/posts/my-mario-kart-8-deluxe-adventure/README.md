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
python content/posts/my-mario-kart-8-deluxe-adventure/plot.py ...$scores
```
