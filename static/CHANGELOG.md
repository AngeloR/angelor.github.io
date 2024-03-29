# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

### [0.4.1](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.4.1;hp=v0.4.0;ds=sidebyside) (2023-09-29)


### Bug Fixes

* add missing migration 34d64f8
* remove clickhouse f7a8ccf

## [0.4.0](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.4.0;hp=v0.3.6;ds=sidebyside) (2023-09-29)


### ⚠ BREAKING CHANGES

* dungeon traversal

### Features

* cleanup chat commands 074d6ad
* dungeon traversal 2ec43df
* min level for all locations 2be0160
* psql based event system 43f0bc3


### Bug Fixes

* auto-enter dungeon if you are in it dfa62a7
* remove log of 0 events being flushed 552c744

### [0.3.6](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.3.6;hp=v0.3.5;ds=sidebyside) (2023-09-06)


### Features

* chat command to set player level 9ced477
* rbac support with admin permission 940079d

### [0.3.5](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.3.5;hp=v0.3.4;ds=sidebyside) (2023-09-06)


### Bug Fixes

* reduce specials to 10% 5beba79

### [0.3.4](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.3.4;hp=v0.3.3;ds=sidebyside) (2023-09-06)


### Bug Fixes

* add missing migration d7268ba

### [0.3.3](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.3.3;hp=v0.3.2;ds=sidebyside) (2023-09-06)


### Features

* add debug/error methods to logger 3238965
* display equippable hand option only d7569d3
* migrate to augmenting express.Request interface d820e11
* monster variants b8bed23
* remove body-part targeting c6a5f62
* variable level monsters b5577b4


### Bug Fixes

* min/max level definitions for monsters bedec85

### [0.3.2](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.3.2;hp=v0.3.1;ds=sidebyside) (2023-09-01)


### Features

* `/online` to list usernames of all online players 3e37d7f


### Bug Fixes

* add missing "Back to Town" button 0752f70
* skills not progressing with use 36b7b7c
* small chat style tweaks e6b5884

### [0.3.1](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.3.1;hp=v0.3.0;ds=sidebyside) (2023-08-31)


### Bug Fixes

* add button that goes back to town from any page 06c0e48
* spells support durability 2dbb9b8
* stop z-stacking alert messages 6e756e8
* tooltip text centered due to media-query cbfebd1

## [0.3.0](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.3.0;hp=v0.2.17;ds=sidebyside) (2023-08-30)


### ⚠ BREAKING CHANGES

* vigor mortensen

### Features

* display optimal level range for monsters 5878793
* move alerts to bottom of main section 9575cfb
* repairing damaged equipment 161b5bf
* unequip items if they hit 0 ap in battle bc9e05f
* vigor mortensen f6aba7a


### Bug Fixes

* spacing for stat increase button 61e6d07

### [0.2.17](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.2.17;hp=v0.2.16;ds=sidebyside) (2023-08-25)


### Bug Fixes

* xss username on signup a827642

### [0.2.16](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.2.16;hp=v0.2.15;ds=sidebyside) (2023-08-25)


### Bug Fixes

* properly increment skill level 24e6b3b

### [0.2.15](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.2.15;hp=v0.2.14;ds=sidebyside) (2023-08-25)


### Features

* expoential exp drop-off/gain c8bd4d6


### Bug Fixes

* add block timer for casting and clear after fight bffb415
* make signup collapsible 97b3c28
* rate limit fights! 235d836
* standardize blocking timeouts for buttons 01d06ca
* time displays at 0 for midnight 789380b

### [0.2.14](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.2.14;hp=v0.2.13;ds=sidebyside) (2023-08-21)


### Features

* display travel progress d66fcf8

### [0.2.13](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.2.13;hp=v0.2.12;ds=sidebyside) (2023-08-21)


### Bug Fixes

* strip all tags in chat 9da5336

### [0.2.12](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.2.12;hp=v0.2.11;ds=sidebyside) (2023-08-21)


### Features

* return to town button while travelling fd070de


### Bug Fixes

* xss chat input 943cbc3

### [0.2.11](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.2.11;hp=v0.2.10;ds=sidebyside) (2023-08-21)


### Bug Fixes

* chat history clearning existing chat on load 8a7161c
* green button colors b8755db
* migrate recruiter to htmx 8f42a66

### [0.2.10](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.2.10;hp=v0.2.9;ds=sidebyside) (2023-08-18)


### Features

* add icons for beginner equipment 218a9ee
* increase hp gain rate 1f9aaf6


### Bug Fixes

* background not appearing if reload during fight 64a76af
* cant perform other actions in a fight b1a1999
* chat timeline to messages show up chronologically b82a2ef
* dont display death text after fleeing 2a1bffe
* missing % from player bar a0606a5
* move purchase button under icon in stores 93aeef5
* only disable equipping/unequipping in a fight b6e9f9a

### [0.2.9](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.2.9;hp=v0.2.8;ds=sidebyside) (2023-08-15)


### Features

* default player to the Explore tab 9b5b9fa
* new UI c793612


### Bug Fixes

* avatar takes up too much space on mobile dced2d0

### [0.2.8](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.2.8;hp=v0.2.7;ds=sidebyside) (2023-08-10)


### Bug Fixes

* migrate signup/login form to htmx 26e475c

### [0.2.7](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.2.7;hp=v0.2.6;ds=sidebyside) (2023-08-09)


### Bug Fixes

* reduce spam requests on /status 5862d25
* seed equipment info bac2f63
* time displays 0pm at noon instead of 12pm 4993906

### [0.2.6](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.2.6;hp=v0.2.5;ds=sidebyside) (2023-08-09)


### Bug Fixes

* armour icon support 4f6823d
* auto-load player object and place in request 7079401
* chat history calls clearing chat 0d1626c
* migrate stat increase to htmx 734e42d

### [0.2.5](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.2.5;hp=v0.2.4;ds=sidebyside) (2023-08-05)


### Features

* add health-potion functionality 2f13844
* purchasable items from the store 4d8b8b1


### Bug Fixes

* migrate chat to htmx 34c9eae
* migrate explore fight to htmx d955aa8
* migrate exploring to htmx 1580d3a
* migrate healer to htmx 18e87bf
* migrate inventory to htmx 0a45adb
* migrate item usage to htmx 6fb15e2
* migrate shops to htmx 09b3c0d
* migrate skills page to htmx c0de5fa
* profile page to html (wip) eeead89
* remove unnecessary console.log e547728
* rename shop_items to shop_equipment 68d481a
* support time display e110480

### [0.2.4](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.2.4;hp=v0.2.3;ds=sidebyside) (2023-07-29)


### Bug Fixes

* filtered shop views f160ce2
* time gradients not scaled properly 2b5a905

### [0.2.3](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.2.3;hp=v0.2.2;ds=sidebyside) (2023-07-28)


### Bug Fixes

* spacing of time on mobile 1db9c53

### [0.2.2](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.2.2;hp=v0.2.1;ds=sidebyside) (2023-07-28)


### Features

* first profile picture ab0d041


### Bug Fixes

* 3s delay when clicking the button to keep walking 8710ea9, closes #11
* display right background based on travelled distance 5f6b5f9
* extend in-game day to 2 IRL hours 8e44b72

### [0.2.1](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.2.1;hp=v0.2.0;ds=sidebyside) (2023-07-27)


### Bug Fixes

* only run into monsters 20% of the time 84c3282

## [0.2.0](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.2.0;hp=v0.1.1;ds=sidebyside) (2023-07-27)


### ⚠ BREAKING CHANGES

* travelling between towns!

### Features

* paths now define a distance between them 53b5ae7
* return to town button if killed while travelling 9325533
* travelling between towns! 621c35b
* when you die your travel plan is discarded 6f21c21


### Bug Fixes

* back to town button after healing 7f29b2f
* disable switching tabs in a fight ea7eafe
* display stat vals without sign or coloring bf702a6
* display the image from the destination city at 50% progress 084353a
* replace city background if you die while travelling 8a15f77
* travel now takes X steps c4f9b81

### [0.1.1](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.1.1;hp=v0.1.0;ds=sidebyside) (2023-07-13)


### Features

* allow users to log out 22d96bc
* display current deployed version in UI a717a30


### Bug Fixes

* casting now uses INT instead of CON 223bc6d
* check players hp before allowing them to start a battle 4d7a556, closes #2
* move jquery to a webpack external to reduce bundle size 56baafa
* prod build process + migration cecab78

## [0.1.0](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.1.0;hp=v0.0.3;ds=sidebyside) (2023-07-12)


### ⚠ BREAKING CHANGES

* players get stat points on every level up

### Features

* players get stat points on every level up 1c9c8a5, closes #5


### Bug Fixes

* define stats as an enum for easier iteration f113d4a
* spacing of stats/equipped items section on mobile 9f45e48

### [0.0.3](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.0.3;hp=v0.0.2;ds=sidebyside) (2023-07-10)


### Features

* add damage mitigation to armour f8156c8, closes #3

### [0.0.2](https://git.xangelo.ca/?p=risinglegends.git;a=commitdiff;h=v0.0.2;hp=v0.0.1;ds=sidebyside) (2023-07-07)


### Bug Fixes

* give users free healing if they have less than 20g 8dbffa6
* type in temp professional services 5671ff4

### 0.0.1 (2023-07-04)


### Bug Fixes

* background gradient doesnt span full height 20d6206
* cache main map screen 1a5ad09
* client socket sometimes sends events before server finished auth 6d3944f
* display error if trying to log in with invalid creds 5bc3c9f
* display HP+ for restoration spells 39dc648
* display login message to all players 2bb30ea
* display when your armour gets destroyed and actual HP damage 067db3b
* empty skills usage causes fights to freeze 1da6f3b
* level <= 3 is free healing 23646fd
* make main page section more legible f85442e
* missing defined type 7aa155d
* monster selector autoselects previous monster a563227
* new players didn't get profession level set ef3cf37
* new players don't get their profession set 3d591f9
* switching between tabs doesnt always work 375c2fd
* users city location not persisting 86d54fb
