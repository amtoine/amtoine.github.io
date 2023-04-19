export def now [] {
    date now | date format "%Y-%m-%dT%H:%M:%S%Z"
}
