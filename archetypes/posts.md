+++
title = "{{ replace .Name "-" " " | title }}"
date =  {{ .Date }}
lastMod =  {{ .Date }}
author = "AUTHOR"
authorTwitter = "" #do not include @
cover = ""
tags = ["TAG1", "TAG2"]
keywords = ["KEY1", "KEY2"]
description = "DESCRIPTION"
showFullContent = false
readingTime = false
hideComments = false
color = "green" #color from the theme settings
+++

NEW POST: {{ replace .Name "-" " " | title }}
