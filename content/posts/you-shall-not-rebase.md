+++
title = "You Shall Not Rebase"
date = 2023-04-18T19:25:49+02:00
lastMod = 2023-05-08T12:27:03+02:00
author = "amtoine"
authorTwitter = "" #do not include @
cover = "/posts/you-shall-not-rebase.gif"
tags = ["git", "github", "reviewing", "rebase"]
keywords = ["", ""]
description = "Some thoughts about rebasing and why it's **so bad**"
showFullContent = false
readingTime = true
hideComments = false
color = "green" #color from the theme settings
+++

hello there {{<image
    src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif"
    alt="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif"
    title="Wave hand"
    height="25"
    width="25"
    position="center"
>}}

this is my very first post about a controversial subject :scream: :crossed_fingers:

> **Note**  
> see the [*TL;DR*](#tldr) for a short summary

{{< bar >}}

# **Important Disclaimers**  
## the development flow
before writing a comment, please note that this blog post applies to a particular
`git` workflow:
- an open-source project
- pure asynchronous development => no coordination
- potentially unknown *random* contributors => no trust
- *trunk-based* development flow, also called *GitHub* flow
  - a main linear trunk of commits, e.g. the `main` or `master` branch in the following
  - anything is developed on a feature branch, e.g. `feature` or `bug-fix` in the following
  - to merge changes in `main`, everyone goes through a [**P**ull **R**equest (**PR**)][GitHub PR]
  - changes go through an asynchronous review / approval process
  - changes are rebased on top of the `main` trunk and squashed into a single commit to hide
  implementation details

## my personal experience
all this blog post is mainly based on my review experience as a member of the core team of [Nushell]

## `git rebase` is great
finally this blog post is a little rant about `git rebase` but note that i use these feature all
the time!  
because it's great... in some cases...

=> in the following, we'll focus on **PR** reviews only.

will all of this in mind, let's get started :smirk:

{{< bar >}}

## why rebase is bad and why you shall not use in

let's start with a little theoretical masterclass, shall we?
when we use `git` the one and only true object we manipulate is the commit!

> **Note**  
> branches, remotes and tags are just pointers to commits!

a commit is a box which contains a few information about changes applied to some files
- the changes themselves
- the author
- the date
- the commit title and body
- the parent commit hash
- ...
with all this information, we can compute the hash of the commit

> **Note**  
> this hash depends on ALL the information contained in the commit!

rebasing a branch, i.e. a set of commits, on top of another branch or revision
has the effect of applying each commit, in order, on top of the new branch.
1. the first commit has a parent and a hash
2. we apply it on top of *another* revision
3. the parent changes and thus its hash too!
4. we apply the second commit on top of the other
5. the hash of the first commit has changed, so does the hash of the second one!
...
and so on.

running `git rebase`, we have rewritten the history of the worktree!

now, if there are conflicts in the middle of the rebasing process, one would
have to solve them
- it's easy to make mistakes here
- what are the guarantees that the resolutions did not introduce errors?

{{< bar >}}

so let's say you have a **PR** feature branch and you target the `main` branch
```
          a---b---c(author/feature *feature)
         /
A---B---C(origin/main main)
```
where `A` is the initial commit.  
here, there is no problem at all, `feature` can be merged on top of `main` and the **PR** can be closed!

but now let's say we do some review, some time passes and the `main` branch has new commits!
```
          a---b---c---d(author/feature *feature)
         /
A---B---C(main)---D---E---F(origin/main)
```
where `D`, `E` and `F` are three new commits on the main branch and `d` is a **PR** commit to address a review thread.

two things can happen here:
1. the `main` and `feature` branches have no conflicts => the **PR** can be merged by *GitHub* without any issue
2. the `main` branch has now "truely" diverged from the `pr` branch and *GitHub* can't merge...

assume for a minute that @author does a `git rebase` to solve the conflicts (which will eventually solve them!)
- they pull the `main` branch from `origin` to sync their local `main` onto the `F` commit
- rebase `feature` on top of `main`, i.e. `d` on top of `F`
- use `git push --force` to push the new conflict-solved changes
```
          a---b---c---d(author/feature)
         /
A---B---C---D---E---F(origin/main main)---a'---b'---c'---d'(*feature)
```
and then
```
          a---b---c---d
         /
A---B---C---D---E---F(origin/main main)---a'---b'---c'---d'(author/feature *feature)
```
where the `X'` commits are the rebased versions of the `a`, `b`, `c` and `d` commits.

> **Note**  
> - `a`, `b`, `c` and `d` are now leftover commits, i.e. they are still here locally but no branch points to them.
> - `a`, `b`, `c` and `d` and their `a'`, `b'`, `c'` and `d'` rebased counterparts ARE different commits!

here, because the history has been rewritten, invalidates the previous reviews and discussions because a
reviewer had reviewed `a` ... `d`, not `a'` ... `d'`, which can be very different as you rewrite the history
during a `git rebase` :scream:

### has @author properly handled conflicts in the middle of the rebase?

the problem with *GitHub* is that it does not show these kind of changes well,
see [*Pull requests: option to disable force push once opened*](https://github.com/todogroup/gh-issues/issues/53)

so, when this happens, you might want to be ready to review the changes again... :eyes:

{{< bar >}}

## but how one should solve those kind of conflicts?
now here is what i would do and what i do for real when one of my **PR** has conflicts with the `main` trunk!
- `git fetch` the `origin` repository to have latest remote `main`
```
          a---b---c---d(me/feature *feature)
         /
A---B---C(main)---D---E---F(origin/main)
```
- merge the latest `main` branch into my `feature` branch with `git merge origin/main`
```
          a----b----c----d(me/feature)-----e(*feature)
         /                                /
A---B---C(main)---D---E---F(origin/main)-'
```
where `e'` is conflict-resolution merge commit.
- then push your changes to the PR
```
          a-------b-------c-------d--------e(me/feature *feature)
         /                                /
A---B---C(main)---D---E---F(origin/main)-'
```

with this flow
- the conflicts are solved in `e`
- reviewers only have to check that `e'` is valid

:partying_face:

{{< bar >}}

## TL;DR
- this blog post applies to the points in the [disclaimer](#important-disclaimers) only
- `git rebase` rewrites the history of a whole branch
- sometimes, one needs to solve conflicts in the middle of a **P**ull **R**equest (**PR**)
    - `git rebase` would invalide all the previously reviewed commits and make the
    review much harder and longer to do
    - *GitHub* does not show force-pushes that well and makes the **PR** confusing
    - `git merge` only adds a single conflict-resolution merge commit, this means there is a single commit to review, all the previous ones are preserved!

`git rebase`ing in private or WIP branches, before a review or when one knows exactly what to do is fine,
i do it all the time :yum:  
but please use `git merge` to solve conflicts in the middle of a review, this will make it easier for everyone :wink:

{{< bar >}}

{{< comments >}}

[Nushell]: https://www.nushell.sh/
[GitHub PR]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
