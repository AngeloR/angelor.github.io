---
title: "Dungeon Generation in Roguelikes"
date: 2021-04-23T09:44:35-04:00
tags: ["roguelike", "explanation"]
summary: A simple dungeon generation algorithm for organic rooms
---


## Intro  
As always, I've been working on a terrible browser-based game. This time, it
will be revolving around gameplay mechanics from roguelikes(or roguelites
technically)+jrpgs.

The thing I specifically want to look at today is the topic of Dungeon
Generation - both in and out of code.

Roguelikes all tend to share one mechanic: Procedurally Generated Dungeons. The
idea is that every play-through is different, every floor of a dungeon is
completely unique. As a result, it requires the player to learn the mechanics of
the game over multiple runs as most roguelikes also include perma-death as a
required feature.

Dungeon Generation in roguelikes are a very interesting topic for two reasons.
There is a definite technical component to being able to generate "good"
dungeons quickly. Dungeons that are large enough, with enough rooms/pathways to
be interesting, but that don't take forever to generate. The goal is each floor
is generated randomly when the player enters - we don't want load times
equivalent to stepping into a room in Morrowind. The second reason is one that I
think roguelikes can miss out on - dungeon generation must fit the environment. 

Most roguelikes have a generation alorithm that gets assigned to every single
floor. But that's not really that helpful. Dungeons should reflect the
environment the player is in. Having square rooms in a castle dungeon makes
sense. Having square rooms in a cave, not so much. 

A lot of dungeon generation information you find online tend to focus on the
techtechnical component: HOW do you generate a dungeon. I'm hoping to also cover
the second bit here.

## Random
The easiest to explain algorithm is the "Random" one, but it's probably the
hardest to get right. Random dungeons are exactly what you'd think -> just
randomly place obstacles and interaction points around the dungeon. As a result
it's very easy to actually MAKE the dungeon. 

It also has the added benefit that the "random" look works really well for open
fields. Think areas that are strewn with trees or rocks or something like that.
It could also work really well for large underground caverns since you would be
peppering the inside with obstances.

But we're not just making a dungeon - we're making a game. And truly-random
dungeons are hard to tune. How do you ensure that every chest you place is
actually reachable by the player? How about the one set of stairs? How do you
ensure that the player doesn't spawn in a box, closed off from the rest of the
dungeon. How do you ensure that they don't spawn right next to some stairs?

Each of these questions (and many many more) result in you tuning you random
generation more and more. You'll never get it 100% right. There'll always be
edge cases reported by your places that you didn't even think about (did a
monster spawn in deep water so the player didn't even know it was there and is
now reporting that they didn't get an achievement for killing all the monsters
on a foor?).

I started with a purly random dungeon generation system myeself. It's definitely
not a bad call to make - but you just have to be aware of the edge cases. But I
kept having to tune/adjust things and I'd still end up with play testers saying
they got spawned in a box, or couldn't reach the stairs. That's frustrating
enough to probably just stop playing.

The nice thing about random, however, is that you don't NEED to generate the map
in its entirety. Nor do you need it to be entirely random.


### On-demand generation
So you have the container for your map.. and your character is spawned in a
particular point `(x,y)`. Given a field of view (`v`) really you only need to
generate a box defined by the points `(x-v, y-v)`, `(x+v, y-v)`, `(x-v, y+v)`,
and `(x+v, y+v)`.

If the player steps in a direction, you only need to expand the generated
portion of the map by 1 tile (or whatever your fov is). In this way, your entire
dungeon is being generated as the player discovers it. You get a few benefits
like not needing to store the entirety of the map if the player doesn't visit
it. You can tune drop rates for everything just by how much of the map is
discovered vs. isn't. You can also almost guarantee that EVERY point on the map is
reachable by the player and that they'll discover the stairs exactly when you'd
like them to.

### Pseudo-random Fabrication
Now, lets get the pedantics out of the way - nothing we're doing is random, it's
all pseudo-random. The difference is that in this generation mechanic we're
actually building the map from pre-defined map parts. 

The downside, of course, is that you have to spend a bunch of time generating
the pieces of map and you do have to have to have some guidelines. But, being
able to tune each individual section of map gives you a ton of control over the
actual gameplay. It also allows you to use non-standard map shapes (get outta
here square rooms) and generate really unique looking maps.

You would need to rotate the location of interactables, but with enough of these
map pieces being put together in random orders it gives you a lot of variation
for your players. And if the unlikely event that they end up getting the EXACT
same map somehow (you know, cause random), the locations of all the interactable
items will be randomized.

## Standard Dungeons (Connected Squares)  
There are a million of these tutorials as this is the standard look for
dungeons. I think they work wonderfully when you're actually exploring a dungeon
in a castle or something - but otherwise they seem out of place

The premise is pretty simplem but it involves iterating over the map numerous
times to achieve the look you want. The steps themselves are pretty
straight-foward.

1. First go over the map and generate rooms (squares or rectangles, whatever you
   want).
2. Then go over the map again and connect the rooms together via pathways. 

Normally you'll make multiple passes over the map to generate the appropriate
room density that you want. The more rooms, the easier it is to connect them
all.

The connection part CAN be confusing, but the easiest way is to actually look at
various path-finding algorithms. Since the map doesn't actually exist, any
pathfinding algorithms will find the straightest line possible between your
rooms. 

Simply iterate over each pair of rooms and connect them using your chosen
path-finding algorithm. [A\*](https://csis.pace.edu/~benjamin/teaching/cs627/webfiles/Astar.pdf) 
is always a good choice to understand the real basics of the algorithm so that
you can implement it yourself. Or at least so you understand what's happening
before using whatever package in your programming language of choice.

The pro's of this technique is that it's a very well documented approach. You
can adjust the density of the map very easily. 

So easily, in fact, that you can ramp up the density to the point that all of
the rooms overlap. The iterate to remove random sections of obstacles (walls)
that are inside the room. That will allow you to generate LARGE rooms where
everything is accessible.

## Drunk Walking
The Drunkards Walk is a very simple algorithm and one that I stumbled upon 
without really knowing about it. The idea is simple and is based on these requirements:  

1. You want to generate organic looking maps
2. You want to ensure that all sections of the map are reachable

The organic maps requirement is probably the most interesting one to me. The
ability to random generate maps that don't look like a bunch of pre-defined
shapes. You could, technically, achieve that same look a myriad of ways, but
this seems the easiest.

The method is as follows:  
1. Create a "walker" on your map of some size (maybe 4 tiles? maybe 9? whatever
   you feel like)
2. Start them on one side of the map, with their edges being walls, and their
   interiors being walkable floors.
3. Make them march to the opposite side, adding some jitter along the other
   axis.

The size of the "walker" dictates the minimum width of the space you're
generating. If you want something to feel more open, make it larger. But if
you're making caves or something, just make them smaller.

The "drunken walk" step sounds confusing, but it's pretty straight-forward. If,
for example, we start the walker on the west side of the map, they will be
walking to the east. Every step they take to the east should be coupled with
them randomly shifting north/south by a MAX of the size of the walker.

That's it.

When you're done, you have a single corridor. To build a map, add more walkers 
all moving along the same plane (west->east for example), and then add one or
two walkers moving from the perpendiclar plane (north->south in this case). This
ensures that all corridors will be connected, and gives you really neat looking
maps. To me, they work wonderfully for caves/pathways. 


But, by playing with the size of the walker you can change the entire look of
the map. Really wide players give you huge open spaces! 

the only thing this DOESN'T do, is actual square looking rooms like if you were
in a real dungeon..
