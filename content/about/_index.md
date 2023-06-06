---
author: amtoine
color: blue
date: 2023-04-16T14:58:22+02:00
draft: false
lastMod: 2023-05-28T13:23:36+02:00
title: About
---

{{< readme-header >}}

{{< bar >}}

> **Note**  
> these days, i'm mostly focused on [`nushell`] :innocent:

a typical FOSS day unwraps as follows for me:
- **help the community** a bit during my breaks
- **chat with the *core team*** once home
- do **some triage** on new and existing issues
- **review** **P**ull **R**equests

and if i have a bit more time (*which happens rarely* :scream:)
- **implement ideas** i have
- work on **personal projects**
- write posts for my [personal website](https://amtoine.github.io)

{{< bar >}}

> **Note**  
> this is actual [NUON] data, which would work in [`nushell`](https://nushell.sh)
```bash
{
    # my previous dev-related professional experience
    work: [
        {
            name: "oberonforall"
            link: "https://github.com/oberonforall"
            projects: [
                {
                    name: "compiler"
                    description: "A cross-compiler for the Oberon programming language."
                    status: "coming soon"
                }
            ]
            status: "internship"
            where: {country: France, city: Toulouse, employer: ISAE}
            dates: {start: 2022-09-04, end: 2022-12-22}
        }
        {
            name: "Dragoon"
            status: "CDD"
            where: {country: France, city: Toulouse, employer: DGA}
        }
    ]

    # what i like to do during my free time, helping the FOSS community a bit
    open-source: {
        goatfiles: {
            description: "linux configuration files"
            roles: [creator, owner, maintainer]
            link: "https://github.com/goatfiles"
            top-projects: {
                dotfiles: "https://github.com/goatfiles/dotfiles"
                kickstart.nvim: "https://github.com/goatfiles/kickstart.nvim"
                nu_scripts: "https://github.com/goatfiles/nu_scripts"
            }
        }
        personal: {
            roles: [well-that-s-me, keys-of-the-kingdom]
            top-projects: {
                qmk: "https://github.com/amtoine/qmk_firmware"
                nushell: [
                    https://github.com/amtoine/nu_plugin_len
                    https://github.com/amtoine/nu_ec_curve_parse
                ]
                gitox: "https://github.com/amtoine/gitox"
            }
            all: "https://github.com/amtoine?tab=repositories&sort=stargazers"
        }
        nushell: {
            roles: [contributor, 'core-team(?)']
            top-projects: [
                https://github.com/nushell/nushell
                https://github.com/nushell/nu_scripts
                https://github.com/nushell/nushell.github.io
                https://github.com/fdncred/nufmt
            ]
        }
        all-my-forks: "https://github.com/amtoine?tab=repositories&q=&type=fork&language=&sort=stargazers"
    }
}
```

{{< bar >}}
Go back to the [front page](/).

[NUON]: https://www.nushell.sh/book/loading_data.html#nuon
[`nushell`]: https://github.com/nushell
