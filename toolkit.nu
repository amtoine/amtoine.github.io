export def now [] {
    date now | date format "%Y-%m-%dT%H:%M:%S%Z"
}

export def "update readme" [] {
    let about = "content/about/_index.md"

    let readme = (http get https://raw.githubusercontent.com/amtoine/amtoine/main/README.md | lines | split list "-----")

    $readme | get 0 | find --invert "<!-- SITE::SKIP -->" | to text | save --force layouts/shortcodes/readme-header.html

    $"---
(open $about | lines | split list "---" | get 0 | to text | from yaml | sort | update lastMod (now) | to yaml | str trim)
---

($readme | update 0 ["{{< readme-header >}}" ""] | each {|| to text } | str join "\n{{< bar >}}\n")

{{< bar >}}
Go back to the [front page](char lparen)/(char rparen).
" | save --force $about
}
