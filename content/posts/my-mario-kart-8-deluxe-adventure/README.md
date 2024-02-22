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
