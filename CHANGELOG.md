# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

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
