---
title:  Outliner [Garden]
tags:  ["project", "outliner", "garden"]
summary:  A Garden (Continually updating) post about the current Outliner Status.
date: 2023-11-22T01:03:25.836-05:00
---


This page will serve as the current state of my Outliner project.

Github - https://github.com/angelor/outliner

## Current Version: 0.0.1-alpha-4

### Known Bugs

- None

### Planned Features

There's no timeline on any of these features, but their current order is rougly the order that I'll be working on them on.

#### Mouse Support

I've been holding off on this a bit, mostly because I don't want to deal with the node-reordering during dragging/dropping. However, I think it'll be one of those things that are really helpful even if you're a keyboard only user.

#### Copy Nodes

Hitting `ctrl`+`c` on a hilighted node should all you to copy the content of that particular node. Pasting the node should happen in one of two ways: If you are in edit mode, it should paste just the content of the node in your current editor. If you are in navigation mode, it should paste a new copy of the node at your cursor, pushing the existing content down.

This lends itself really well to "referential nodes" as well

#### General Publishing

General publish is working in alpha-4. I'm actually quite pleased with it so far. The configuration is abstracted away, but does expect that you're going to be operating out of the `/home` directory specifically. But, apart from that, the actual work to generate posts, inculding drag+drop support for images, and also code is allowing this to become a really all-rounded tool for me.

#### Referential Node Links

Each node in the outliner is saved as its own JSON file. The reason for this was to eventually implement the idea of "Referential Node Links". A single node, that can be referenced in multiple outliners. Updating the node from any of the outlines will update the node in every outline. The idea is to give you the ability to re-use certain templates/bits of code. If you hit `ctrl+shift+c` it should copy the node reference and allow you to paste that in










    