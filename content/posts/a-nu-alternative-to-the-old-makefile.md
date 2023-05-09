+++
title = "A Nu Alternative to the Old Makefile"
date = 2023-05-08T12:25:18+02:00
lastMod = 2023-05-08T12:25:18+02:00
author = "@amtoine"
authorTwitter = "" #do not include @
cover = "/posts/a-nu-alternative-to-the-old-makefile.gif"
tags = ["nushell", "nu", "makefile", "project", "alternative"]
keywords = ["", ""]
description = "How to setup a Nushell-based alternative to `make`"
showFullContent = false
readingTime = true
hideComments = false
color = "green" #color from the theme settings
+++

i've been using [Nushell] for a few months now as my daily and only shell.
i love it and could not get back to POSIX shells like `bash` or `fish`, that'd
be a real pain :sob:

i could talk about why it's so great all day, but in this blog post, i'd like
to focus on a small detail i find really cool :smirk:

{{< bar >}}

## i've always looked for a `Makefile` alternative
this is the main observation. i find the syntax of `Makefile`s very confusing
- based on `bash` which is not great in itself
- but not totally `bash` so it very often feels confusing and frustrating...

### `cmake`, i hear you say?
well, `cmake` is definitely better!  
but, in the end, it's just a wrapper around `make` => it only gives a bit of
syntactic sugar but produces regular `Makefile`s which are then run with `make`...

### other tools?
they are not as common most of the time, poorly documented, etc, etc, ...

{{< bar >}}

## here comes [Nushell]
in [Nushell], one can write scripts called [*modules*][Nushell modules].  
modules are a bit like [regular *scripts*][Nushell scripts] but integrate
in the shell much better
- better `help` pages
- custom completion

> **Note**  
> the following will work with the latest revision of `nushell` only.  
> not the latest release, the latest revision!
>
> in fact, one would need to have installed a version of `nushell` after
> [nushell/nushell#9066], e.g. from any branch / commit based on [`a2a346e39`].

the idea here is to define a `toolkit` module to replace any `Makefile` and thus
only have [Nushell] as the main dependency... and we are already in [Nushell]! so
that's a free dependency :partying:

### where to put the `toolkit` module?
the main answer to this is "*in the root of the project*"!  
and there are two ways to do that:
- as a regular file module: `toolkit.nu`
- as a directory module: `toolkit/mod.nu` (only available after [nushell/nushell#9066])

### how to use this `toolkit`?
once in the root of your project, simply run
```nu
use toolkit.nu  # with a regular module
```
or
```nu
use toolkit/  # with a directory module
```

### an example of `toolkit`
let's have a look maybe at the most [Nushell]y `toolkit` of all: the [`nushell` toolkit].

> **Note**  
> in this section, i use the `toolkit` of the latest revision of `nushell` AT THE TIME I WRITE THIS.  
> it might have changed now :wink:

> **Note**  
> [Nushell] is written in Rust and thus its `toolkit` wraps some `cargo` commands.

the `toolkit` exposes the following API
{{< code language="nu" title="the Nushell toolkit API" id="1" expand="Show" collapse="Hide" isCollapsed="false" >}}
fmt [
    --check: bool
    --verbose: bool
];

clippy [
    --verbose: bool
];

test [
    --fast: bool
];

test stdlib [];

check pr [
    --fast: bool
];

setup-git-hooks [];
{{< /code >}}

`fmt`, `clippy` and the `test` commands are here to check the source base for
- bad formatting
- lint errors
- failing tests, both for the main source base in Rust and the [standard library] written in [Nushell]

`check pr` wraps them all and says if a **PR** will be valid or not.

finally `setup-git-hooks`... well sets `git` hooks up :wink:

> **Note**  
> more information is available by running `help toolkit ...`

### a nice addition: automatic loading of the `toolkit` with *hooks*
in order to have any `toolkit` available at anytime when i enter a directory containing a `toolkit` module,
i've written a little *hook*.

> **Note**  
> in [Nushell], a [*hook*][Nushell hooks] is a piece of code which runs on some condition, e.g. changing directory,
> displaying output, ...

for this, i've used the `env_change.PWD` hook, which activates when the environment changes, more precisely
the `PWD` variable, i.e. the current directory!

the *hook* will consist of a list of `{condition: closure, code: closure}` records.
- the first one always runs and deactivates any previous toolkit
```nu
{ code: "hide toolkit" }
```
- next, we activate the toolkit if we find one.  
the `condition` part of the *hook* record has access to the `before` and `after` directories,
we can thus check if there is a `toolkit.nu` or a `toolkit/mod.nu` inside the `after` directory!
```nu
{|_, after| $after | path join 'toolkit.nu' | path exists }
```
or
```nu
{|_, after| $after | path join 'toolkit' 'mod.nu' | path exists }
```
and the actual `code` is then respectively
```nu
use toolkit.nu
```
or
```nu
use toolkit/
```

to wrap this all in a single command, i've written the following
{{< code language="nu" title="the `env-change pwd toolkit` command" id="1" expand="Show" collapse="Hide" isCollapsed="false" >}}
def "env-change pwd toolkit" [
  --directory: bool
] {{
    condition: (if $directory {
        {|_, after| $after | path join 'toolkit' 'mod.nu' | path exists }
    } else {
        {|_, after| $after | path join 'toolkit.nu' | path exists }
    })
    code: ([
        "print -n $'(ansi default_underline)(ansi default_bold)toolkit(ansi reset) module (ansi yellow_italic)detected(ansi reset)... '"
        $"use (if $directory { 'toolkit/' } else { 'toolkit.nu' })"
        "print $'(ansi green_bold)activated!(ansi reset)'"
    ] | str join "\n")
}}
{{< /code >}}

and the final *hook* looks like

{{< code language="nu" title="the `env_change.PWD` *hook*" id="1" expand="Show" collapse="Hide" isCollapsed="false" >}}
env_change: {
    PWD: [
        { code: "hide toolkit" }
        (env-change pwd toolkit)
        (env-change pwd toolkit --directory)
    ]
}
{{< /code >}}

{{< bar >}}

## and that's it
with all this, any time you enter a directory with either a `toolkit.nu` or a `toolkit/` module,
it will be activated and ready to use, with a little message :relieved:

{{< comments >}}

[Nushell]: https://www.nushell.sh/
[Nushell modules]: https://www.nushell.sh/book/modules.html
[Nushell scripts]: https://www.nushell.sh/book/scripts.html
[Nushell hooks]: https://www.nushell.sh/book/hooks.html
[nushell/nushell#9066]: https://github.com/nushell/nushell/pull/9066
[`a2a346e39`]: https://github.com/nushell/nushell/commit/a2a346e39c53e386b97d8d7f9a05ed58298e8789
[`nushell` toolkit]: https://github.com/nushell/nushell/blob/a2dd948e71c3cbdecfa1a2dbf35282707e151b02/toolkit.nu
[standard library]: https://www.nushell.sh/book/standard_library.html
