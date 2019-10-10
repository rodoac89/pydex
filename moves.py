def get_move(move):
    moves = {
        "10000000voltthunderbolt": {
            "num": 719,
            "accuracy": True,
            "basePower": 195,
            "category": "Special",
            "desc": "Has a very high chance for a critical hit.",
            "shortDesc": "Very high critical hit ratio.",
            "id": "10000000voltthunderbolt",
            "name": "10,000,000 Volt Thunderbolt",
            "pp": 1,
            "priority": 0,
            "flags": {},
            "isZ": "pikashuniumz",
            "critRatio": 3,
            "secondary": None,
            "target": "normal",
            "type": "Electric",
            "contestType": "Cool"
        },
        "absorb": {
            "num": 71,
            "accuracy": 100,
            "basePower": 20,
            "category": "Special",
            "desc": "The user recovers 1/2 the HP lost by the target, rounded half up. If Big Root is held by the user, the HP recovered is 1.3x normal, rounded half down.",
            "shortDesc": "User recovers 50% of the damage dealt.",
            "id": "absorb",
            "name": "Absorb",
            "pp": 25,
            "priority": 0,
            "flags": {
                "protect": 1,
                "mirror": 1,
                "heal": 1
            },
            "drain": [
                1,
                2
            ],
            "secondary": None,
            "target": "normal",
            "type": "Grass",
            "zMovePower": 100,
            "contestType": "Clever"
        },
        "accelerock": {
            "num": 709,
            "accuracy": 100,
            "basePower": 40,
            "category": "Physical",
            "desc": "No additional effect.",
            "shortDesc": "Usually goes first.",
            "id": "accelerock",
            "isViable": True,
            "name": "Accelerock",
            "pp": 20,
            "priority": 1,
            "flags": {
                "contact": 1,
                "protect": 1,
                "mirror": 1
            },
            "secondary": None,
            "target": "normal",
            "type": "Rock",
            "zMovePower": 100,
            "contestType": "Cool"
        },
        "acid": {
            "num": 51,
            "accuracy": 100,
            "basePower": 40,
            "category": "Special",
            "desc": "Has a 10% chance to lower the target's Special Defense by 1 stage.",
            "shortDesc": "10% chance to lower the foe(s) Sp. Def by 1.",
            "id": "acid",
            "name": "Acid",
            "pp": 30,
            "priority": 0,
            "flags": {
                "protect": 1,
                "mirror": 1
            },
            "secondary": {
                "chance": 10,
                "boosts": {
                    "spd": -1
                }
            },
            "target": "allAdjacentFoes",
            "type": "Poison",
            "zMovePower": 100,
            "contestType": "Clever"
        },
        "acidarmor": {
            "num": 151,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "Raises the user's Defense by 2 stages.",
            "shortDesc": "Raises the user's Defense by 2.",
            "id": "acidarmor",
            "name": "Acid Armor",
            "pp": 20,
            "priority": 0,
            "flags": {
                "snatch": 1
            },
            "boosts": {
                "def": 2
            },
            "secondary": None,
            "target": "self",
            "type": "Poison",
            "zMoveEffect": "clearnegativeboost",
            "contestType": "Tough"
        },
        "aciddownpour": {
            "num": 628,
            "accuracy": True,
            "basePower": 1,
            "category": "Physical",
            "shortDesc": "Power is equal to the base move's Z-Power.",
            "id": "aciddownpour",
            "isViable": True,
            "name": "Acid Downpour",
            "pp": 1,
            "priority": 0,
            "flags": {},
            "isZ": "poisoniumz",
            "secondary": None,
            "target": "normal",
            "type": "Poison",
            "contestType": "Cool"
        },
        "acidspray": {
            "num": 491,
            "accuracy": 100,
            "basePower": 40,
            "category": "Special",
            "desc": "Has a 100% chance to lower the target's Special Defense by 2 stages.",
            "shortDesc": "100% chance to lower the target's Sp. Def by 2.",
            "id": "acidspray",
            "isViable": True,
            "name": "Acid Spray",
            "pp": 20,
            "priority": 0,
            "flags": {
                "bullet": 1,
                "protect": 1,
                "mirror": 1
            },
            "secondary": {
                "chance": 100,
                "boosts": {
                    "spd": -2
                }
            },
            "target": "normal",
            "type": "Poison",
            "zMovePower": 100,
            "contestType": "Beautiful"
        },
        "acrobatics": {
            "num": 512,
            "accuracy": 100,
            "basePower": 55,
            "category": "Physical",
            "shortDesc": "Power doubles if the user has no held item.",
            "id": "acrobatics",
            "isViable": True,
            "name": "Acrobatics",
            "pp": 15,
            "priority": 0,
            "flags": {
                "contact": 1,
                "protect": 1,
                "mirror": 1,
                "distance": 1
            },
            "secondary": None,
            "target": "any",
            "type": "Flying",
            "zMovePower": 100,
            "contestType": "Cool"
        },
        "acupressure": {
            "num": 367,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "Raises a random stat by 2 stages as long as the stat is not already at stage 6. The user can choose to use this move on itself or an adjacent ally. Fails if no stat stage can be raised or if used on an ally with a substitute.",
            "shortDesc": "Raises a random stat of the user or an ally by 2.",
            "id": "acupressure",
            "name": "Acupressure",
            "pp": 30,
            "priority": 0,
            "flags": {},
            "secondary": None,
            "target": "adjacentAllyOrSelf",
            "type": "Normal",
            "zMoveEffect": "crit2",
            "contestType": "Tough"
        },
        "aerialace": {
            "num": 332,
            "accuracy": True,
            "basePower": 60,
            "category": "Physical",
            "shortDesc": "This move does not check 'accuracy'.",
            "id": "aerialace",
            "isViable": True,
            "name": "Aerial Ace",
            "pp": 20,
            "priority": 0,
            "flags": {
                "contact": 1,
                "protect": 1,
                "mirror": 1,
                "distance": 1
            },
            "secondary": None,
            "target": "any",
            "type": "Flying",
            "zMovePower": 120,
            "contestType": "Cool"
        },
        "aeroblast": {
            "num": 177,
            "accuracy": 95,
            "basePower": 100,
            "category": "Special",
            "desc": "Has a higher chance for a critical hit.",
            "shortDesc": "High critical hit ratio.",
            "id": "aeroblast",
            "isViable": True,
            "name": "Aeroblast",
            "pp": 5,
            "priority": 0,
            "flags": {
                "protect": 1,
                "mirror": 1,
                "distance": 1
            },
            "critRatio": 2,
            "secondary": None,
            "target": "any",
            "type": "Flying",
            "zMovePower": 180,
            "contestType": "Cool"
        },
        "afteryou": {
            "num": 495,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "The target makes its move immediately after the user this turn, no matter the priority of its selected move. Fails if the target would have moved next anyway, or if the target already moved this turn.",
            "shortDesc": "The target makes its move right after the user.",
            "id": "afteryou",
            "name": "After You",
            "pp": 15,
            "priority": 0,
            "flags": {
                "authentic": 1,
                "mystery": 1
            },
            "secondary": None,
            "target": "normal",
            "type": "Normal",
            "zMoveBoost": {
                "spe": 1
            },
            "contestType": "Cute"
        },
        "agility": {
            "num": 97,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "Raises the user's Speed by 2 stages.",
            "shortDesc": "Raises the user's Speed by 2.",
            "id": "agility",
            "isViable": True,
            "name": "Agility",
            "pp": 30,
            "priority": 0,
            "flags": {
                "snatch": 1
            },
            "boosts": {
                "spe": 2
            },
            "secondary": None,
            "target": "self",
            "type": "Psychic",
            "zMoveEffect": "clearnegativeboost",
            "contestType": "Cool"
        },
        "aircutter": {
            "num": 314,
            "accuracy": 95,
            "basePower": 60,
            "category": "Special",
            "desc": "Has a higher chance for a critical hit.",
            "shortDesc": "High critical hit ratio. Hits adjacent foes.",
            "id": "aircutter",
            "name": "Air Cutter",
            "pp": 25,
            "priority": 0,
            "flags": {
                "protect": 1,
                "mirror": 1
            },
            "critRatio": 2,
            "secondary": None,
            "target": "allAdjacentFoes",
            "type": "Flying",
            "zMovePower": 120,
            "contestType": "Cool"
        },
        "airslash": {
            "num": 403,
            "accuracy": 95,
            "basePower": 75,
            "category": "Special",
            "desc": "Has a 30% chance to flinch the target.",
            "shortDesc": "30% chance to flinch the target.",
            "id": "airslash",
            "isViable": True,
            "name": "Air Slash",
            "pp": 15,
            "priority": 0,
            "flags": {
                "protect": 1,
                "mirror": 1,
                "distance": 1
            },
            "secondary": {
                "chance": 30,
                "volatileStatus": "flinch"
            },
            "target": "any",
            "type": "Flying",
            "zMovePower": 140,
            "contestType": "Cool"
        },
        "alloutpummeling": {
            "num": 624,
            "accuracy": True,
            "basePower": 1,
            "category": "Physical",
            "shortDesc": "Power is equal to the base move's Z-Power.",
            "id": "alloutpummeling",
            "isViable": True,
            "name": "All-Out Pummeling",
            "pp": 1,
            "priority": 0,
            "flags": {},
            "isZ": "fightiniumz",
            "secondary": None,
            "target": "normal",
            "type": "Fighting",
            "contestType": "Cool"
        },
        "allyswitch": {
            "num": 502,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "The user swaps positions with its ally. Fails if the user is the only Pokemon on its side.",
            "shortDesc": "The user swaps positions with its ally.",
            "id": "allyswitch",
            "name": "Ally Switch",
            "pp": 15,
            "priority": 2,
            "flags": {},
            "secondary": None,
            "target": "self",
            "type": "Psychic",
            "zMoveBoost": {
                "spe": 2
            },
            "contestType": "Clever"
        },
        "amnesia": {
            "num": 133,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "Raises the user's Special Defense by 2 stages.",
            "shortDesc": "Raises the user's Sp. Def by 2.",
            "id": "amnesia",
            "name": "Amnesia",
            "pp": 20,
            "priority": 0,
            "flags": {
                "snatch": 1
            },
            "boosts": {
                "spd": 2
            },
            "secondary": None,
            "target": "self",
            "type": "Psychic",
            "zMoveEffect": "clearnegativeboost",
            "contestType": "Cute"
        },
        "anchorshot": {
            "num": 677,
            "accuracy": 100,
            "basePower": 80,
            "category": "Physical",
            "desc": "Prevents the target from switching out. The target can still switch out if it is holding Shed Shell or uses Baton Pass, Parting Shot, U-turn, or Volt Switch. If the target leaves the field using Baton Pass, the replacement will remain trapped. The effect ends if the user leaves the field.",
            "shortDesc": "Prevents the target from switching out.",
            "id": "anchorshot",
            "isViable": True,
            "name": "Anchor Shot",
            "pp": 20,
            "priority": 0,
            "flags": {
                "contact": 1,
                "protect": 1,
                "mirror": 1
            },
            "secondary": {
                "chance": 100
            },
            "target": "normal",
            "type": "Steel",
            "zMovePower": 160,
            "contestType": "Tough"
        },
        "ancientpower": {
            "num": 246,
            "accuracy": 100,
            "basePower": 60,
            "category": "Special",
            "desc": "Has a 10% chance to raise the user's Attack, Defense, Special Attack, Special Defense, and Speed by 1 stage.",
            "shortDesc": "10% chance to raise all stats by 1 (not acc/eva).",
            "id": "ancientpower",
            "name": "Ancient Power",
            "pp": 5,
            "priority": 0,
            "flags": {
                "protect": 1,
                "mirror": 1
            },
            "secondary": {
                "chance": 10,
                "self": {
                    "boosts": {
                        "atk": 1,
                        "def": 1,
                        "spa": 1,
                        "spd": 1,
                        "spe": 1
                    }
                }
            },
            "target": "normal",
            "type": "Rock",
            "zMovePower": 120,
            "contestType": "Tough"
        },
        "aquajet": {
            "num": 453,
            "accuracy": 100,
            "basePower": 40,
            "category": "Physical",
            "desc": "No additional effect.",
            "shortDesc": "Usually goes first.",
            "id": "aquajet",
            "isViable": True,
            "name": "Aqua Jet",
            "pp": 20,
            "priority": 1,
            "flags": {
                "contact": 1,
                "protect": 1,
                "mirror": 1
            },
            "secondary": None,
            "target": "normal",
            "type": "Water",
            "zMovePower": 100,
            "contestType": "Cool"
        },
        "aquaring": {
            "num": 392,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "The user has 1/16 of its maximum HP, rounded down, restored at the end of each turn while it remains active. If Big Root is held by the user, the HP recovered is 1.3x normal, rounded half down. If the user uses Baton Pass, the replacement will receive the healing effect.",
            "shortDesc": "User recovers 1/16 max HP per turn.",
            "id": "aquaring",
            "name": "Aqua Ring",
            "pp": 20,
            "priority": 0,
            "flags": {
                "snatch": 1
            },
            "volatileStatus": "aquaring",
            "secondary": None,
            "target": "self",
            "type": "Water",
            "zMoveBoost": {
                "def": 1
            },
            "contestType": "Beautiful"
        },
        "aquatail": {
            "num": 401,
            "accuracy": 90,
            "basePower": 90,
            "category": "Physical",
            "shortDesc": "No additional effect.",
            "id": "aquatail",
            "isViable": True,
            "name": "Aqua Tail",
            "pp": 10,
            "priority": 0,
            "flags": {
                "contact": 1,
                "protect": 1,
                "mirror": 1
            },
            "secondary": None,
            "target": "normal",
            "type": "Water",
            "zMovePower": 175,
            "contestType": "Beautiful"
        },
        "armthrust": {
            "num": 292,
            "accuracy": 100,
            "basePower": 15,
            "category": "Physical",
            "desc": "Hits two to five times. Has a 1/3 chance to hit two or three times, and a 1/6 chance to hit four or five times. If one of the hits breaks the target's substitute, it will take damage for the remaining hits. If the user has the Skill Link Ability, this move will always hit five times.",
            "shortDesc": "Hits 2-5 times in one turn.",
            "id": "armthrust",
            "name": "Arm Thrust",
            "pp": 20,
            "priority": 0,
            "flags": {
                "contact": 1,
                "protect": 1,
                "mirror": 1
            },
            "multihit": [
                2,
                5
            ],
            "secondary": None,
            "target": "normal",
            "type": "Fighting",
            "zMovePower": 100,
            "contestType": "Tough"
        },
        "aromatherapy": {
            "num": 312,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "Every Pokemon in the user's party is cured of its major status condition. Active Pokemon with the Sap Sipper Ability are not cured, unless they are the user.",
            "shortDesc": "Cures the user's party of all status conditions.",
            "id": "aromatherapy",
            "isViable": True,
            "name": "Aromatherapy",
            "pp": 5,
            "priority": 0,
            "flags": {
                "snatch": 1,
                "distance": 1
            },
            "target": "allyTeam",
            "type": "Grass",
            "zMoveEffect": "heal",
            "contestType": "Clever"
        },
        "aromaticmist": {
            "num": 597,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "Raises the target's Special Defense by 1 stage. Fails if there is no ally adjacent to the user.",
            "shortDesc": "Raises an ally's Sp.Def by 1. ",
            "id": "aromaticmist",
            "name": "Aromatic Mist",
            "pp": 20,
            "priority": 0,
            "flags": {
                "authentic": 1
            },
            "boosts": {
                "spd": 1
            },
            "secondary": None,
            "target": "adjacentAlly",
            "type": "Fairy",
            "zMoveBoost": {
                "spd": 2
            },
            "contestType": "Beautiful"
        },
        "assist": {
            "num": 274,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "A random move among those known by the user's party members is selected for use. Does not select Assist, Baneful Bunker, Beak Blast, Belch, Bestow, Bounce, Celebrate, Chatter, Circle Throw, Copycat, Counter, Covet, Destiny Bond, Detect, Dig, Dive, Dragon Tail, Endure, Feint, Fly, Focus Punch, Follow Me, Helping Hand, Hold Hands, King'sShield,Mat Block,Me First,Metronome,Mimic,Mirror Coat,Mirror Move,Nature Power,Phantom Force,Protect,Rage Powder,Roar,Shadow Force,Shell Trap,Sketch,Sky Drop,Sleep Talk,Snatch,Spiky Shield,Spotlight,Struggle,Switcheroo,Thief,Transform,Trick,Whirlwind,or any Z - Move.",
            "shortDesc": "Uses a random move known by a team member.",
            "id": "assist",
            "name": "Assist",
            "pp": 20,
            "priority": 0,
            "flags": {},
            "secondary": None,
            "target": "self",
            "type": "Normal",
            "contestType": "Cute"
        },
        "assurance": {
            "num": 372,
            "accuracy": 100,
            "basePower": 60,
            "category": "Physical",
            "desc": "Power doubles if the target has already taken damage this turn, other than direct damage from Belly Drum, confusion, Curse, or Pain Split.",
            "shortDesc": "Power doubles if target was damaged this turn.",
            "id": "assurance",
            "name": "Assurance",
            "pp": 10,
            "priority": 0,
            "flags": {
                "contact": 1,
                "protect": 1,
                "mirror": 1
            },
            "secondary": None,
            "target": "normal",
            "type": "Dark",
            "zMovePower": 120,
            "contestType": "Clever"
        },
        "astonish": {
            "num": 310,
            "accuracy": 100,
            "basePower": 30,
            "category": "Physical",
            "desc": "Has a 30% chance to flinch the target.",
            "shortDesc": "30% chance to flinch the target.",
            "id": "astonish",
            "name": "Astonish",
            "pp": 15,
            "priority": 0,
            "flags": {
                "contact": 1,
                "protect": 1,
                "mirror": 1
            },
            "secondary": {
                "chance": 30,
                "volatileStatus": "flinch"
            },
            "target": "normal",
            "type": "Ghost",
            "zMovePower": 100,
            "contestType": "Cute"
        },
        "attackorder": {
            "num": 454,
            "accuracy": 100,
            "basePower": 90,
            "category": "Physical",
            "desc": "Has a higher chance for a critical hit.",
            "shortDesc": "High critical hit ratio.",
            "id": "attackorder",
            "isViable": True,
            "name": "Attack Order",
            "pp": 15,
            "priority": 0,
            "flags": {
                "protect": 1,
                "mirror": 1
            },
            "critRatio": 2,
            "secondary": None,
            "target": "normal",
            "type": "Bug",
            "zMovePower": 175,
            "contestType": "Clever"
        },
        "attract": {
            "num": 213,
            "accuracy": 100,
            "basePower": 0,
            "category": "Status",
            "desc": "Causes the target to become infatuated, making it unable to attack 50% of the time. Fails if both the user and the target are the same gender, if either is genderless, or if the target is already infatuated. The effect ends when either the user or the target is no longer active. Pokemon with the Oblivious Ability or protected by the Aroma Veil Ability are immune.",
            "shortDesc": "A target of the opposite gender gets infatuated.",
            "id": "attract",
            "name": "Attract",
            "pp": 15,
            "priority": 0,
            "flags": {
                "protect": 1,
                "reflectable": 1,
                "mirror": 1,
                "authentic": 1
            },
            "volatileStatus": "attract"
        },
        "aurasphere": {
            "num": 396,
            "accuracy": True,
            "basePower": 80,
            "category": "Special",
            "shortDesc": "This move does not check 'accuracy'.",
            "id": "aurasphere",
            "isViable": True,
            "name": "Aura Sphere",
            "pp": 20,
            "priority": 0,
            "flags": {
                "bullet": 1,
                "protect": 1,
                "pulse": 1,
                "mirror": 1,
                "distance": 1
            },
            "secondary": None,
            "target": "any",
            "type": "Fighting",
            "zMovePower": 160,
            "contestType": "Beautiful"
        },
        "aurorabeam": {
            "num": 62,
            "accuracy": 100,
            "basePower": 65,
            "category": "Special",
            "desc": "Has a 10% chance to lower the target's Attack by 1 stage.",
            "shortDesc": "10% chance to lower the target's Attack by 1.",
            "id": "aurorabeam",
            "name": "Aurora Beam",
            "pp": 20,
            "priority": 0,
            "flags": {
                "protect": 1,
                "mirror": 1
            },
            "secondary": {
                "chance": 10,
                "boosts": {
                    "atk": -1
                }
            },
            "target": "normal",
            "type": "Ice",
            "zMovePower": 120,
            "contestType": "Beautiful"
        },
        "auroraveil": {
            "num": 694,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "For 5 turns, the user and its party members take 0.5x damage from physical and special attacks, or 0.66x damage if in a Double Battle; does not reduce damage further with Reflect or Light Screen. Critical hits ignore this protection. It is removed from the user's side if the user or an ally is successfully hit by Brick Break, Psychic Fangs, or Defog. Brick Break and Psychic Fangs remove the effect before damage is calculated. Lasts for 8 turns if the user is holding Light Clay. Fails unless the weather is Hail.",
            "shortDesc": "For 5 turns, damage to allies is halved. Hail only.",
            "id": "auroraveil",
            "isViable": True,
            "name": "Aurora Veil",
            "pp": 20,
            "priority": 0,
            "flags": {
                "snatch": 1
            },
            "secondary": None,
            "target": "allySide",
            "type": "Ice",
            "zMoveBoost": {
                "spe": 1
            },
            "contestType": "Beautiful"
        },
        "autotomize": {
            "num": 475,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "Raises the user's Speed by 2 stages. If the user's Speed was changed, the user's weight is reduced by 100 kg as long as it remains active. This effect is stackable but cannot reduce the user's weight to less than 0.1 kg.",
            "shortDesc": "Raises the user's Speed by 2; user loses 100 kg.",
            "id": "autotomize",
            "isViable": True,
            "name": "Autotomize",
            "pp": 15,
            "priority": 0,
            "flags": {
                "snatch": 1
            },
            "boosts": {
                "spe": 2
            },
            "secondary": None,
            "target": "self",
            "type": "Steel",
            "zMoveEffect": "clearnegativeboost",
            "contestType": "Beautiful"
        },
        "avalanche": {
            "num": 419,
            "accuracy": 100,
            "basePower": 60,
            "category": "Physical",
            "desc": "Power doubles if the user was hit by the target this turn.",
            "shortDesc": "Power doubles if user is damaged by the target.",
            "id": "avalanche",
            "isViable": True,
            "name": "Avalanche",
            "pp": 10,
            "priority": -4,
            "flags": {
                "contact": 1,
                "protect": 1,
                "mirror": 1
            },
            "secondary": None,
            "target": "normal",
            "type": "Ice",
            "zMovePower": 120,
            "contestType": "Beautiful"
        },
        "babydolleyes": {
            "num": 608,
            "accuracy": 100,
            "basePower": 0,
            "category": "Status",
            "desc": "Lowers the target's Attack by 1 stage.",
            "shortDesc": "Lowers the target's Attack by 1.",
            "id": "babydolleyes",
            "name": "Baby-Doll Eyes",
            "pp": 30,
            "priority": 1,
            "flags": {
                "protect": 1,
                "reflectable": 1,
                "mirror": 1,
                "mystery": 1
            },
            "boosts": {
                "atk": -1
            },
            "secondary": None,
            "target": "normal",
            "type": "Fairy",
            "zMoveBoost": {
                "def": 1
            },
            "contestType": "Cute"
        },
        "baddybad": {
            "num": 737,
            "accuracy": 100,
            "basePower": 90,
            "category": "Special",
            "desc": "This move summons Reflect for 5 turns upon use.",
            "shortDesc": "Summons Reflect.",
            "id": "baddybad",
            "isNonstandard": "LGPE",
            "isUnreleased": True,
            "isViable": True,
            "name": "Baddy Bad",
            "pp": 15,
            "priority": 0,
            "flags": {
                "protect": 1
            },
            "secondary": None,
            "target": "normal",
            "type": "Dark",
            "contestType": "Clever"
        },
        "banefulbunker": {
            "num": 661,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "The user is protected from most attacks made by other Pokemon during this turn, and Pokemon making contact with the user become poisoned. This move has a 1/X chance of being successful, where X starts at 1 and triples each time this move is successfully used. X resets to 1 if this move fails, if the user's last move used is not Baneful Bunker, Detect, Endure, King'sShield,Protect,Quick Guard,Spiky Shield,or Wide Guard,or if it was one of those moves and the user's protection was broken. Fails if the user moves last this turn.",
            "shortDesc": "Protects from moves contact poison.",
            "id": "banefulbunker",
            "isViable": True,
            "name": "Baneful Bunker",
            "pp": 10,
            "priority": 4,
            "flags": {},
            "stallingMove": True,
            "volatileStatus": "banefulbunker",
            "secondary": None,
            "target": "self",
            "type": "Poison",
            "zMoveBoost": {
                "def": 1
            },
            "contestType": "Tough"
        },
        "barrage": {
            "num": 140,
            "accuracy": 85,
            "basePower": 15,
            "category": "Physical",
            "desc": "Hits two to five times. Has a 1/3 chance to hit two or three times, and a 1/6 chance to hit four or five times. If one of the hits breaks the target's substitute, it will take damage for the remaining hits. If the user has the Skill Link Ability, this move will always hit five times.",
            "shortDesc": "Hits 2-5 times in one turn.",
            "id": "barrage",
            "name": "Barrage",
            "pp": 20,
            "priority": 0,
            "flags": {
                "bullet": 1,
                "protect": 1,
                "mirror": 1
            },
            "multihit": [
                2,
                5
            ],
            "secondary": None,
            "target": "normal",
            "type": "Normal",
            "zMovePower": 100,
            "contestType": "Cute"
        },
        "barrier": {
            "num": 112,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "Raises the user's Defense by 2 stages.",
            "shortDesc": "Raises the user's Defense by 2.",
            "id": "barrier",
            "name": "Barrier",
            "pp": 20,
            "priority": 0,
            "flags": {
                "snatch": 1
            },
            "boosts": {
                "def": 2
            },
            "secondary": None,
            "target": "self",
            "type": "Psychic",
            "zMoveEffect": "clearnegativeboost",
            "contestType": "Cool"
        },
        "batonpass": {
            "num": 226,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "The user is replaced with another Pokemon in its party. The selected Pokemon has the user's stat stage changes, confusion, and certain move effects transferred to it.",
            "shortDesc": "User switches, passing stat changes and more.",
            "id": "batonpass",
            "isViable": True,
            "name": "Baton Pass",
            "pp": 40,
            "priority": 0,
            "flags": {},
            "selfSwitch": "copyvolatile",
            "secondary": None,
            "target": "self",
            "type": "Normal",
            "zMoveEffect": "clearnegativeboost",
            "contestType": "Cute"
        },
        "beakblast": {
            "num": 690,
            "accuracy": 100,
            "basePower": 100,
            "category": "Physical",
            "desc": "If the user is hit by a contact move this turn before it can execute this move, the attacker is burned.",
            "shortDesc": "Burns on contact with the user before it moves.",
            "id": "beakblast",
            "isViable": True,
            "name": "Beak Blast",
            "pp": 15,
            "priority": -3,
            "flags": {
                "bullet": 1,
                "protect": 1
            },
            "secondary": None,
            "target": "normal",
            "type": "Flying",
            "zMovePower": 180,
            "contestType": "Tough"
        },
        "beatup": {
            "num": 251,
            "accuracy": 100,
            "basePower": 0,
            "category": "Physical",
            "desc": "Hits one time for the user and one time for each unfainted Pokemon without a major status condition in the user's party. The power of each hit is equal to 5+(X/10), where X is each participating Pokemon's base Attack;each hit is considered to come from the user.",
            "shortDesc": "All healthy allies aid in damaging the target.",
            "id": "beatup",
            "name": "Beat Up",
            "pp": 10,
            "priority": 0,
            "flags": {
                "protect": 1,
                "mirror": 1,
                "mystery": 1
            },
            "secondary": None,
            "target": "normal",
            "type": "Dark",
            "zMovePower": 100,
            "contestType": "Clever"
        },
        "belch": {
            "num": 562,
            "accuracy": 90,
            "basePower": 120,
            "category": "Special",
            "desc": "This move cannot be selected until the user eats a Berry, either by eating one that was held, stealing and eating one off another Pokemon with Bug Bite or Pluck, or eating one that was thrown at it with Fling. Once the condition is met, this move can be selected and used for the rest of the battle even if the user gains or uses another item or switches out. Consuming a Berry with Natural Gift does not count for the purposes of eating one.",
            "shortDesc": "Cannot be selected until the user eats a Berry.",
            "id": "belch",
            "name": "Belch",
            "pp": 10,
            "priority": 0,
            "flags": {
                "protect": 1
            },
            "secondary": None,
            "target": "normal",
            "type": "Poison",
            "zMovePower": 190,
            "contestType": "Tough"
        },
        "bellydrum": {
            "num": 187,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "Raises the user's Attack by 12 stages in exchange for the user losing 1/2 of its maximum HP, rounded down. Fails if the user would faint or if its Attack stat stage is 6.",
            "shortDesc": "User loses 50% max HP. Maximizes Attack.",
            "id": "bellydrum",
            "name": "Belly Drum",
            "pp": 10,
            "priority": 0,
            "flags": {
                "snatch": 1
            },
            "secondary": None,
            "target": "self",
            "type": "Normal",
            "zMoveEffect": "heal",
            "contestType": "Cute"
        },
        "bestow": {
            "num": 516,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "The target receives the user's held item. Fails if the user has no item or is holding a Mail or Z-Crystal, if the target is already holding an item, if the user is a Kyogre holding a Blue Orb, a Groudon holding a Red Orb, a Giratina holding a Griseous Orb, an Arceus holding a Plate, a Genesect holding a Drive, a Silvally holding a Memory, a Pokemon that can Mega Evolve holding the Mega Stone for its species, or if the target is one of those Pokemon and the user is holding the respective item.",
            "shortDesc": "User passes its held item to the target.",
            "id": "bestow",
            "name": "Bestow",
            "pp": 15,
            "priority": 0,
            "flags": {
                "mirror": 1,
                "authentic": 1,
                "mystery": 1
            },
        },
        "bide": {
            "num": 117,
            "accuracy": True,
            "basePower": 0,
            "category": "Physical",
            "desc": "The user spends two turns locked into this move and then, on the second turn after using this move, the user attacks the last Pokemon that hit it, inflicting double the damage in HP it lost to attacks during the two turns. If the last Pokemon that hit it is no longer active, the user attacks a random opposing Pokemon instead. If the user is prevented from moving during this move's use, the effect ends. This move does not check 'accuracy' and does not ignore type immunity.",
            "shortDesc": "Waits 2 turns; deals double the damage taken.",
            "id": "bide",
            "name": "Bide",
            "pp": 10,
            "priority": 1,
            "flags": {
                "contact": 1,
                "protect": 1
            },
            "volatileStatus": "bide",
            "ignoreImmunity": True,
        },
        "bodyslam": {
            "num": 34,
            "accuracy": 100,
            "basePower": 85,
            "category": "Physical",
            "desc": "Has a 30% chance to paralyze the target. Damage doubles and no accuracy check is done if the target has used Minimize while active.",
            "shortDesc": "30% chance to paralyze the target.",
            "id": "bodyslam",
            "isViable": True,
            "name": "Body Slam",
            "pp": 15,
            "priority": 0,
            "flags": {"contact": 1, "protect": 1, "mirror": 1, "nonsky": 1},
            "secondary": {
                "chance": 30,
                "status": 'par',
            },
            "target": "normal",
            "type": "Normal",
            "zMovePower": 160,
            "contestType": "Tough",
        },
        "chargebeam": {
            "num": 451,
            "accuracy": 90,
            "basePower": 50,
            "category": "Special",
            "desc": "Has a 70% chance to raise the user's Special Attack by 1 stage.",
            "shortDesc": "70% chance to raise the user's Sp. Atk by 1.",
            "id": "chargebeam",
            "name": "Charge Beam",
            "pp": 10,
            "priority": 0,
            "flags": {
                "protect": 1,
                "mirror": 1
            },
            "secondary": {
                "chance": 70
            },
            "target": "normal",
            "type": "Electric",
            "zMovePower": 100,
            "contestType": "Beautiful"
        },
        "charm": {
            "num": 204,
            "accuracy": 100,
            "basePower": 0,
            "category": "Status",
            "desc": "Lowers the target's Attack by 2 stages.",
            "shortDesc": "Lowers the target's Attack by 2.",
            "id": "charm",
            "name": "Charm",
            "pp": 20,
            "priority": 0,
            "flags": {
                "protect": 1,
                "reflectable": 1,
                "mirror": 1,
                "mystery": 1
            },
            "boosts": {
                "atk": -2
            },
            "secondary": None,
            "target": "normal",
            "type": "Fairy",
            "zMoveBoost": {
                "def": 1
            },
            "contestType": "Cute"
        },
        "chatter": {
            "num": 448,
            "accuracy": 100,
            "basePower": 65,
            "category": "Special",
            "desc": "Has a 100% chance to confuse the target.",
            "shortDesc": "100% chance to confuse the target.",
            "id": "chatter",
            "isViable": True,
            "name": "Chatter",
            "pp": 20,
            "priority": 0,
            "flags": {
                "protect": 1,
                "mirror": 1,
                "sound": 1,
                "distance": 1,
                "authentic": 1
            },
            "noSketch": True,
            "secondary": {
                "chance": 100,
                "volatileStatus": "confusion",
            },
            "target": "any",
            "type": "Flying",
            "zMovePower": 120,
            "contestType": "Cute"
        },
        "chipaway": {
            "num": 498,
            "accuracy": 100,
            "basePower": 70,
            "category": "Physical",
            "desc": "Ignores the target's stat stage changes, including evasiveness.",
            "shortDesc": "Ignores the target's stat stage changes.",
            "id": "chipaway",
            "name": "Chip Away",
            "pp": 20,
            "priority": 0,
            "flags": {
                "contact": 1,
                "protect": 1,
                "mirror": 1
            },
            "ignoreDefensive": True,
            "ignoreEvasion": True,
            "secondary": None,
            "target": "normal",
            "type": "Normal",
            "zMovePower": 140,
            "contestType": "Tough"
        },
        "circlethrow": {
            "num": 509,
            "accuracy": 90,
            "basePower": 60,
            "category": "Physical",
            "desc": "If both the user and the target have not fainted, the target is forced to switch out and be replaced with a random unfainted ally. This effect fails if the target is under the effect of Ingrain, has the Suction Cups Ability, or this move hit a substitute.",
            "shortDesc": "Forces the target to switch to a random ally.",
            "id": "circlethrow",
            "isViable": True,
            "name": "Circle Throw",
            "pp": 10,
            "priority": -6,
            "flags": {
                "contact": 1,
                "protect": 1,
                "mirror": 1
            },
            "forceSwitch": True,
            "target": "normal",
            "type": "Fighting",
            "zMovePower": 120,
            "contestType": "Cool"
        },
        "clamp": {
            "num": 128,
            "accuracy": 85,
            "basePower": 35,
            "category": "Physical",
            "desc": "Prevents the target from switching for four or five turns (seven turns if the user is holding Grip Claw). Causes damage to the target equal to 1/8 of its maximum HP (1/6 if the user is holding Binding Band), rounded down, at the end of each turn during effect. The target can still switch out if it is holding Shed Shell or uses Baton Pass, Parting Shot, U-turn, or Volt Switch. The effect ends if either the user or the target leaves the field, or if the target uses Rapid Spin or Substitute successfully. This effect is not stackable or reset by using this or another binding move.",
            "shortDesc": "Traps and damages the target for 4-5 turns.",
            "id": "clamp",
            "name": "Clamp",
            "pp": 15,
            "priority": 0,
            "flags": {
                "contact": 1,
                "protect": 1,
                "mirror": 1
            },
            "volatileStatus": "partiallytrapped",
            "secondary": None,
            "target": "normal",
            "type": "Water",
            "zMovePower": 100,
            "contestType": "Tough"
        },
        "clangingscales": {
            "num": 691,
            "accuracy": 100,
            "basePower": 110,
            "category": "Special",
            "desc": "Lowers the user's Defense by 1 stage.",
            "shortDesc": "Lowers the user's Defense by 1.",
            "id": "clangingscales",
            "isViable": True,
            "name": "Clanging Scales",
            "pp": 5,
            "priority": 0,
            "flags": {
                "protect": 1,
                "mirror": 1,
                "sound": 1,
                "authentic": 1
            },
            "selfBoost": {
                "boosts": {
                    "def": -1,
                },
            },
            "secondary": None,
            "target": "allAdjacentFoes",
            "type": "Dragon",
            "zMovePower": 185,
            "contestType": "Tough"
        },
        "clangoroussoulblaze": {
            "num": 728,
            "accuracy": True,
            "basePower": 185,
            "category": "Special",
            "desc": "Raises the user's Attack, Defense, Special Attack, Special Defense, and Speed by 1 stage.",
            "shortDesc": "Raises the user's Atk/Def/SpAtk/SpDef/Spe by 1.",
            "id": "clangoroussoulblaze",
            "name": "Clangorous Soulblaze",
            "pp": 1,
            "priority": 0,
            "flags": {
                "sound": 1,
                "authentic": 1
            },
            "selfBoost": {
                "boosts": {
                    "atk": 1,
                    "def": 1,
                    "spa": 1,
                    "spd": 1,
                    "spe": 1
                },
            },
            "isZ": "kommoniumz",
            "target": "allAdjacentFoes",
            "type": "Dragon",
            "contestType": "Cool"
        },
        "clearsmog": {
            "num": 499,
            "accuracy": True,
            "basePower": 50,
            "category": "Special",
            "shortDesc": "Resets all of the target's stat stages to 0.",
            "id": "clearsmog",
            "isViable": True,
            "name": "Clear Smog",
            "pp": 15,
            "priority": 0,
            "flags": {
                "protect": 1,
                "mirror": 1
            },
            "secondary": None,
            "target": "normal",
            "type": "Poison",
            "zMovePower": 100,
            "contestType": "Beautiful"
        },
        "closecombat": {
            "num": 370,
            "accuracy": 100,
            "basePower": 120,
            "category": "Physical",
            "desc": "Lowers the user's Defense and Special Defense by 1 stage.",
            "shortDesc": "Lowers the user's Defense and Sp. Def by 1.",
            "id": "closecombat",
            "isViable": True,
            "name": "Close Combat",
            "pp": 5,
            "priority": 0,
            "flags": {
                "contact": 1,
                "protect": 1,
                "mirror": 1
            },
            "self": {
                "boosts": {
                    "def": -1,
                    "spd": -1
                },
            },
            "secondary": None,
            "target": "normal",
            "type": "Fighting",
            "zMovePower": 190,
            "contestType": "Tough"
        },
        "coil": {
            "num": 489,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "Raises the user's Attack, Defense, and 'accuracy' by 1 stage.",
            "shortDesc": "Raises user's Attack, Defense, 'accuracy' by 1.",
            "id": "coil",
            "isViable": True,
            "name": "Coil",
            "pp": 20,
            "priority": 0,
            "flags": {
                "snatch": 1
            },
            "boosts": {
                "atk": 1,
                "def": 1,
                "accuracy": 1
            },
            "secondary": None,
            "target": "self",
            "type": "Poison",
            "zMoveEffect": "clearnegativeboost",
            "contestType": "Tough"
        },
        "cometpunch": {
            "num": 4,
            "accuracy": 85,
            "basePower": 18,
            "category": "Physical",
            "desc": "Hits two to five times. Has a 1/3 chance to hit two or three times, and a 1/6 chance to hit four or five times. If one of the hits breaks the target's substitute, it will take damage for the remaining hits. If the user has the Skill Link Ability, this move will always hit five times.",
            "shortDesc": "Hits 2-5 times in one turn.",
            "id": "cometpunch",
            "name": "Comet Punch",
            "pp": 15,
            "priority": 0,
            "flags": {
                "contact": 1,
                "protect": 1,
                "mirror": 1,
                "powder": 1
            },
            "multihit": [
                2,
                5
            ],
            "secondary": None,
            "target": "normal",
            "type": "Normal",
            "zMovePower": 100,
            "contestType": "Tough"
        },
        "confide": {
            "num": 590,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "Lowers the target's Special Attack by 1 stage.",
            "shortDesc": "Lowers the target's Sp. Atk by 1.",
            "id": "confide",
            "name": "Confide",
            "pp": 20,
            "priority": 0,
            "flags": {
                "reflectable": 1,
                "mirror": 1,
                "sound": 1,
                "authentic": 1
            },
            "boosts": {
                "spa": -1,
            },
            "secondary": None,
            "target": "normal",
            "type": "Normal",
            "zMoveBoost": {
                "spd": 1
            },
            "contestType": "Cute"
        },
        "confuseray": {
            "num": 109,
            "accuracy": 100,
            "basePower": 0,
            "category": "Status",
            "desc": "Causes the target to become confused.",
            "shortDesc": "Confuses the target.",
            "id": "confuseray",
            "name": "Confuse Ray",
            "pp": 10,
            "priority": 0,
            "flags": {
                "protect": 1,
                "reflectable": 1,
                "mirror": 1
            },
            "volatileStatus": "confusion",
            "secondary": None,
            "target": "normal",
            "type": "Ghost",
            "zMoveBoost": {
                "spa": 1
            },
            "contestType": "Clever"
        },
        "confusion": {
            "num": 93,
            "accuracy": 100,
            "basePower": 50,
            "category": "Special",
            "desc": "Has a 10% chance to confuse the target.",
            "shortDesc": "10% chance to confuse the target.",
            "id": "confusion",
            "name": "Confusion",
            "pp": 25,
            "priority": 0,
            "flags": {
                "protect": 1,
                "mirror": 1
            },
            "secondary": {
                "chance": 10,
                "volatileStatus": "confusion",
            },
            "target": "normal",
            "type": "Psychic",
            "zMovePower": 100,
            "contestType": "Clever"
        },
        "constrict": {
            "num": 132,
            "accuracy": 100,
            "basePower": 10,
            "category": "Physical",
            "desc": "Has a 10% chance to lower the target's Speed by 1 stage.",
            "shortDesc": "10% chance to lower the target's Speed by 1.",
            "id": "constrict",
            "name": "Constrict",
            "pp": 35,
            "priority": 0,
            "flags": {
                "contact": 1,
                "protect": 1,
                "mirror": 1
            },
            "secondary": {
                "chance": 10,
                "boosts": {
                    "spe": -1,
                },
            },
            "target": "normal",
            "type": "Normal",
            "zMovePower": 100,
            "contestType": "Tough"
        },
        "continentalcrush": {
            "num": 632,
            "accuracy": True,
            "basePower": 1,
            "category": "Physical",
            "shortDesc": "Power is equal to the base move's Z-Power.",
            "id": "continentalcrush",
            "isViable": True,
            "name": "Continental Crush",
            "pp": 1,
            "priority": 0,
            "flags": {},
            "isZ": "rockiumz",
            "secondary": None,
            "target": "normal",
            "type": "Rock",
            "contestType": "Cool"
        },
        "conversion": {
            "num": 160,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "The user's type changes to match the original type of the move in its first move slot. Fails if the user cannot change its type, or if the type is one of the user's current types.",
            "shortDesc": "Changes user's type to match its first move.",
            "id": "conversion",
            "name": "Conversion",
            "pp": 30,
            "priority": 0,
            "flags": {
                "snatch": 1
            },
            "secondary": None,
            "target": "self",
            "type": "Normal",
            "zMoveBoost": {
                "atk": 1,
                "def": 1,
                "spa": 1,
                "spd": 1,
                "spe": 1
            },
            "contestType": "Beautiful"
        },
        "conversion2": {
            "num": 176,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "The user's type changes to match a type that resists or is immune to the type of the last move used by the target, but not either of its current types. The determined type of the move is used rather than the original type. Fails if the target has not made a move, if the user cannot change its type, or if this move would only be able to select one of the user's current types.",
            "shortDesc": "Changes user's type to resist target's last move.",
            "id": "conversion2",
            "name": "Conversion 2",
            "pp": 30,
            "priority": 0,
            "flags": {
                "authentic": 1
            },
            "secondary": None,
            "target": "normal",
            "type": "Normal",
            "zMoveEffect": "heal",
            "contestType": "Beautiful"
        },
        "copycat": {
            "num": 383,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "The user uses the last move used by any Pokemon, including itself. Fails if no move has been used, or if the last move used was Assist, Baneful Bunker, Beak Blast, Belch, Bestow, Celebrate, Chatter, Circle Throw, Copycat, Counter, Covet, Destiny Bond, Detect, Dragon Tail, Endure, Feint, Focus Punch, Follow Me, Helping Hand, Hold Hands, King's Shield, Mat Block, Me First, Metronome, Mimic, Mirror Coat, Mirror Move, Nature Power, Protect, Rage Powder, Roar, Shell Trap, Sketch, Sleep Talk, Snatch, Spiky Shield, Spotlight, Struggle, Switcheroo, Thief, Transform, Trick, Whirlwind, or any Z - Move.",
            "shortDesc": "Uses the last move used in the battle.",
            "id": "copycat",
            "name": "Copycat",
            "pp": 20,
            "priority": 0,
            "flags": {},    
            "secondary": None,
            "target": "self",
            "type": "Normal",
            "zMoveBoost": {
                "accuracy": 1
            },
            "contestType": "Cute"
        },
        "coreenforcer": {
            "num": 687,
            "accuracy": 100,
            "basePower": 100,
            "category": "Special",
            "desc": "If the user moves after the target, the target's Ability is rendered ineffective as long as it remains active. If the target uses Baton Pass, the replacement will remain under this effect. If the target's Ability is Battle Bond, Comatose, Disguise, Multitype, Power Construct, RKS System, Schooling, Shields Down, Stance Change, or Zen Mode, this effect does not happen, and receiving the effect through Baton Pass ends the effect immediately.",
            "shortDesc": "Noneifies the foe(s) Ability if the foe(s) move first.",
            "id": "coreenforcer",
            "isViable": True,
            "name": "Core Enforcer",
            "pp": 10,
            "priority": 0,
            "flags": {
                "protect": 1,
                "mirror": 1
            },
            "secondary": None,
            "target": "allAdjacentFoes",
            "type": "Dragon",
            "zMovePower": 140,
            "contestType": "Tough"
        },
        "corkscrewcrash": {
            "num": 638,
            "accuracy": True,
            "basePower": 1,
            "category": "Physical",
            "shortDesc": "Power is equal to the base move's Z-Power.",
            "id": "corkscrewcrash",
            "isViable": True,
            "name": "Corkscrew Crash",
            "pp": 1,
            "priority": 0,
            "flags": {},
            "isZ": "steeliumz",
            "secondary": None,
            "target": "normal",
            "type": "Steel",
            "contestType": "Cool"
        },
        "cosmicpower": {
            "num": 322,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "Raises the user's Defense and Special Defense by 1 stage.",
            "shortDesc": "Raises the user's Defense and Sp. Def by 1.",
            "id": "cosmicpower",
            "name": "Cosmic Power",
            "pp": 20,
            "priority": 0,
            "flags": {
                "snatch": 1
            },
            "boosts": {
                "def": 1,
                "spd": 1,
            },
            "secondary": None,
            "target": "self",
            "type": "Psychic",
            "zMoveBoost": {
                "spd": 1
            },
            "contestType": "Beautiful"
        },
        "cottonguard": {
            "num": 538,
            "accuracy": True,
            "basePower": 0,
            "category": "Status",
            "desc": "Raises the user's Defense by 3 stages.",
            "shortDesc": "Raises the user's Defense by 3.",
            "id": "cottonguard",
            "isViable": True,
            "name": "Cotton Guard",
            "pp": 10,
            "priority": 0,
            "flags": {
                "snatch": 1
            },
            "boosts": {
                "def": 3,
            },
            "secondary": None,
            "target": "self",
            "type": "Grass",
            "zMoveEffect": "clearnegativeboost",
            "contestType": "Cute"
        },
        "cottonspore": {
            "num": 178,
            "accuracy": 100,
            "basePower": 0,
            "category": "Status",
            "desc": "Lowers the target's Speed by 2 stages.",
            "shortDesc": "Lowers the target's Speed by 2.",
            "id": "cottonspore",
            "name": "Cotton Spore",
            "pp": 40,
            "priority": 0,
            "flags": {
                "powder": 1,
                "protect": 1,
                "reflectable": 1,
                "mirror": 1
            },
            "boosts": {
                "spe": -2,
            },
            "secondary": None,
            "target": "allAdjacentFoes",
            "type": "Grass",
            "zMoveEffect": "clearnegativeboost",
            "contestType": "Beautiful"
        },
        "counter": {
            "num": 68,
            "accuracy": 100,
            "basePower": 0,
            "category": "Physical",
            "desc": "Deals damage to the last opposing Pokemon to hit the user with a physical attack this turn equal to twice the HP lost by the user from that attack. If the user did not lose HP from the attack, this move deals 1 HP of damage instead. If that opposing Pokemon's position is no longer in use and there is another opposing Pokemon on the field the damage is done to it instead.Only the last hit of a multi - hit attack is counted. Fails if the user was not hit by an opposing Pokemon's physical attack this turn.",
            "shortDesc": "If hit by physical attack, returns double damage.",
            "id": "counter",
            "name": "Counter",
            "pp": 20,
            "priority": -5,
            "flags": {
                "contact": 1,
                "protect": 1
            },
            "secondary": None,
            "target": "scripted",
            "type": "Fighting",
            "zMovePower": 100,
            "contestType": "Tough"
        },
        "covet": {
            "num": 343,
            "accuracy": 100,
            "basePower": 60,
            "category": "Physical",
            "desc": "If this attack was successful and the user has not fainted, it steals the target's held item if the user is not holding one. The target's item is not stolen if it is a Mail or Z-Crystal, or if the target is a Kyogre holding a Blue Orb, a Groudon holding a Red Orb, a Giratina holding a Griseous Orb, an Arceus holding a Plate, a Genesect holding a Drive, a Silvally holding a Memory, or a Pokemon that can Mega Evolve holding the Mega Stone for its species. Items lost to this move cannot be regained with Recycle or the Harvest Ability.",
            "shortDesc": "If the user has no item, it steals the target's.",
            "id": "covet",
            "name": "Covet",
            "pp": 25,
            "priority": 0,
            "flags": {
                "contact": 1,
                "protect": 1,
                "mirror": 1
            },
        },
        "crabhammer": {
            "num": 152,
            "accuracy": 90,
            "basePower": 100,
            "category": "Physical",
            "desc": "Has a higher chance for a critical hit.",
            "shortDesc": "High critical hit ratio.",
            "id": "crabhammer",
            "isViable": True,
            "name": "Crabhammer",
            "pp": 10,
            "priority": 0,
            "flags": {
                "contact": 1,
                "protect": 1,
                "mirror": 1
            },
            "critRatio": 2,
            "secondary": None,
            "target": "normal",
            "type": "Water",
            "zMovePower": 180,
            "contestType": "Tough"
        },
                "craftyshield": {
                    "num": 578,
                    "accuracy": True,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "The user and its party members are protected from non-damaging attacks made by other Pokemon, including allies, during this turn. Fails if the user moves last this turn or if this move is already in effect for the user's side.",
                    "shortDesc": "Protects allies from Status moves this turn.",
                    "id": "craftyshield",
                    "name": "Crafty Shield",
                    "pp": 10,
                    "priority": 3,
                    "flags": {},
                    "secondary": None,
                    "target": "allySide",
                    "type": "Fairy",
                    "zMoveBoost": {
                        "spd": 1
                    },
                    "contestType": "Clever"
                },
                "crosschop": {
                    "num": 238,
                    "accuracy": 80,
                    "basePower": 100,
                    "category": "Physical",
                    "desc": "Has a higher chance for a critical hit.",
                    "shortDesc": "High critical hit ratio.",
                    "id": "crosschop",
                    "isViable": True,
                    "name": "Cross Chop",
                    "pp": 5,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "critRatio": 2,
                    "secondary": None,
                    "target": "normal",
                    "type": "Fighting",
                    "zMovePower": 180,
                    "contestType": "Cool"
                },
                "crosspoison": {
                    "num": 440,
                    "accuracy": 100,
                    "basePower": 70,
                    "category": "Physical",
                    "desc": "Has a 10% chance to poison the target and a higher chance for a critical hit.",
                    "shortDesc": "High critical hit ratio. 10% chance to poison.",
                    "id": "crosspoison",
                    "name": "Cross Poison",
                    "pp": 20,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": {
                        "chance": 10,
                        "status": "psn",
                    },
                    "critRatio": 2,
                    "target": "normal",
                    "type": "Poison",
                    "zMovePower": 140,
                    "contestType": "Cool"
                },
                "crunch": {
                    "num": 242,
                    "accuracy": 100,
                    "basePower": 80,
                    "category": "Physical",
                    "desc": "Has a 20% chance to lower the target's Defense by 1 stage.",
                    "shortDesc": "20% chance to lower the target's Defense by 1.",
                    "id": "crunch",
                    "isViable": True,
                    "name": "Crunch",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "bite": 1,
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": {
                        "chance": 20,
                        "boosts": {
                            "def": -1,
                        },
                    },
                    "target": "normal",
                    "type": "Dark",
                    "zMovePower": 160,
                    "contestType": "Tough"
                },
                "crushclaw": {
                    "num": 306,
                    "accuracy": 95,
                    "basePower": 75,
                    "category": "Physical",
                    "desc": "Has a 50% chance to lower the target's Defense by 1 stage.",
                    "shortDesc": "50% chance to lower the target's Defense by 1.",
                    "id": "crushclaw",
                    "name": "Crush Claw",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": {
                        "chance": 50,
                        "boosts": {
                            "def": -1,
                        },
                    },
                    "target": "normal",
                    "type": "Normal",
                    "zMovePower": 140,
                    "contestType": "Cool"
                },
                "crushgrip": {
                    "num": 462,
                    "accuracy": 100,
                    "basePower": 0,
                    "category": "Physical",
                    "desc": "Power is equal to 120 * (target's current HP / target's maximum HP), rounded half down, but not less than 1.",
                    "shortDesc": "More power the more HP the target has left.",
                    "id": "crushgrip",
                    "name": "Crush Grip",
                    "pp": 5,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Normal",
                    "zMovePower": 190,
                    "contestType": "Tough"
                },
                "curse": {
                    "num": 174,
                    "accuracy": True,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "If the user is not a Ghost type, lowers the user's Speed by 1 stage and raises the user's Attack and Defense by 1 stage. If the user is a Ghost type, the user loses 1/2 of its maximum HP, rounded down and even if it would cause fainting, in exchange for the target losing 1/4 of its maximum HP, rounded down, at the end of each turn while it is active. If the target uses Baton Pass, the replacement will continue to be affected. Fails if there is no target or if the target is already affected.",
                    "shortDesc": "Curses if Ghost, else -1 Spe, +1 Atk, +1 Def.",
                    "id": "curse",
                    "name": "Curse",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "authentic": 1
                    },
                    "volatileStatus": "curse",
                    "secondary": None,
                    "target": "normal",
                    "nonGhostTarget": "self",
                    "type": "Ghost",
                    "zMoveEffect": "curse",
                    "contestType": "Tough"
                },
                "cut": {
                    "num": 15,
                    "accuracy": 95,
                    "basePower": 50,
                    "category": "Physical",
                    "shortDesc": "No additional effect.",
                    "id": "cut",
                    "name": "Cut",
                    "pp": 30,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Normal",
                    "zMovePower": 100,
                    "contestType": "Cool"
                },
                "darkestlariat": {
                    "num": 663,
                    "accuracy": 100,
                    "basePower": 85,
                    "category": "Physical",
                    "desc": "Ignores the target's stat stage changes, including evasiveness.",
                    "shortDesc": "Ignores the target's stat stage changes.",
                    "id": "darkestlariat",
                    "isViable": True,
                    "name": "Darkest Lariat",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "ignoreEvasion": True,
                    "ignoreDefensive": True,
                    "secondary": None,
                    "target": "normal",
                    "type": "Dark",
                    "zMovePower": 160,
                    "contestType": "Cool"
                },
                "darkpulse": {
                    "num": 399,
                    "accuracy": 100,
                    "basePower": 80,
                    "category": "Special",
                    "desc": "Has a 20% chance to flinch the target.",
                    "shortDesc": "20% chance to flinch the target.",
                    "id": "darkpulse",
                    "isViable": True,
                    "name": "Dark Pulse",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "pulse": 1,
                        "mirror": 1,
                        "distance": 1
                    },
                    "secondary": {
                        "chance": 20,
                        "volatileStatus": "flinch"
                    },
                    "target": "any",
                    "type": "Dark",
                    "zMovePower": 160,
                    "contestType": "Cool"
                },
                "darkvoid": {
                    "num": 464,
                    "accuracy": 50,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "Causes the target to fall asleep. This move cannot be used successfully unless the user's current form, while considering Transform, is Darkrai.",
                    "shortDesc": "Darkrai: Causes the foe(s) to fall asleep.",
                    "id": "darkvoid",
                    "isViable": True,
                    "name": "Dark Void",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "reflectable": 1,
                        "mirror": 1
                    },
                    "status": "slp",
                    "secondary": None,
                    "target": "allAdjacentFoes",
                    "type": "Dark",
                    "zMoveEffect": "clearnegativeboost",
                    "contestType": "Clever"
                },
                "dazzlinggleam": {
                    "num": 605,
                    "accuracy": 100,
                    "basePower": 80,
                    "category": "Special",
                    "desc": "No additional effect.",
                    "shortDesc": "No additional effect. Hits adjacent foes.",
                    "id": "dazzlinggleam",
                    "isViable": True,
                    "name": "Dazzling Gleam",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": None,
                    "target": "allAdjacentFoes",
                    "type": "Fairy",
                    "zMovePower": 160,
                    "contestType": "Beautiful"
                },
                "defendorder": {
                    "num": 455,
                    "accuracy": True,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "Raises the user's Defense and Special Defense by 1 stage.",
                    "shortDesc": "Raises the user's Defense and Sp. Def by 1.",
                    "id": "defendorder",
                    "isViable": True,
                    "name": "Defend Order",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "snatch": 1
                    },
                    "boosts": {
                        "def": 1,
                        "spd": 1,
                    },
                    "secondary": None,
                    "target": "self",
                    "type": "Bug",
                    "zMoveBoost": {
                        "def": 1
                    },
                    "contestType": "Clever"
                },
                "defensecurl": {
                    "num": 111,
                    "accuracy": True,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "Raises the user's Defense by 1 stage. As long as the user remains active, the power of the user's Ice Ball and Rollout will be doubled (this effect is not stackable).",
                    "shortDesc": "Raises the user's Defense by 1.",
                    "id": "defensecurl",
                    "name": "Defense Curl",
                    "pp": 40,
                    "priority": 0,
                    "flags": {
                        "snatch": 1
                    },
                    "boosts": {
                        "def": 1,
                    },
                    "volatileStatus": "defensecurl",
                    "secondary": None,
                    "target": "self",
                    "type": "Normal",
                    "zMoveBoost": {
                        "accuracy": 1
                    },
                    "contestType": "Cute"
                },
                "defog": {
                    "num": 432,
                    "accuracy": True,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "Lowers the target's evasiveness by 1 stage. If this move is successful and whether or not the target's evasiveness was affected, the effects of Reflect, Light Screen, Aurora Veil, Safeguard, Mist, Spikes, Toxic Spikes, Stealth Rock, and Sticky Web end for the target's side, and the effects of Spikes, Toxic Spikes, Stealth Rock, and Sticky Web end for the user's side. Ignores a target's substitute, although a substitute will still block the lowering of evasiveness.",
                    "shortDesc": "-1 evasion; clears user and target side's hazards.",
                    "id": "defog",
                    "isViable": True,
                    "name": "Defog",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "reflectable": 1,
                        "mirror": 1,
                        "authentic": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Flying",
                    "zMoveBoost": {
                        "accuracy": 1
                    },
                    "contestType": "Cool"
                },
                "destinybond": {
                    "num": 194,
                    "accuracy": True,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "Until the user's next move, if an opposing Pokemon's attack knocks the user out, that Pokemon faints as well, unless the attack was Doom Desire or Future Sight.Fails if the user used this move successfully as its last move, disregarding moves used through the Dancer Ability.",
                    "shortDesc": "If an opponent knocks out the user, it also faints.",
                    "id": "destinybond",
                    "isViable": True,
                    "name": "Destiny Bond",
                    "pp": 5,
                    "priority": 0,
                    "flags": {
                        "authentic": 1
                    },
                    "volatileStatus": "destinybond",
                    "secondary": None,
                    "target": "self",
                    "type": "Ghost",
                    "zMoveEffect": "redirect",
                    "contestType": "Clever"
                },
                "detect": {
                    "num": 197,
                    "accuracy": True,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "The user is protected from most attacks made by other Pokemon during this turn. This move has a 1/X chance of being successful, where X starts at 1 and triples each time this move is successfully used. X resets to 1 if this move fails, if the user's last move used is not Baneful Bunker, Detect, Endure, King's Shield,Protect,Quick Guard,Spiky Shield,or Wide Guard,orif it was one of those moves and the user 's protection was broken. Fails if the user moves last this turn.",
                    "shortDesc": "Prevents moves from affecting the user this turn.",
                    "id": "detect",
                    "isViable": True,
                    "name": "Detect",
                    "pp": 5,
                    "priority": 4,
                    "flags": {},
                    "stallingMove": True,
                    "volatileStatus": "protect",
                    "secondary": None,
                    "target": "self",
                    "type": "Fighting",
                    "zMoveBoost": {
                        "evasion": 1
                    },
                    "contestType": "Cool"
                },
                "devastatingdrake": {
                    "num": 652,
                    "accuracy": True,
                    "basePower": 1,
                    "category": "Physical",
                    "shortDesc": "Power is equal to the base move's Z-Power.",
                    "id": "devastatingdrake",
                    "name": "Devastating Drake",
                    "pp": 1,
                    "priority": 0,
                    "flags": {},
                    "isZ": "dragoniumz",
                    "secondary": None,
                    "target": "normal",
                    "type": "Dragon",
                    "contestType": "Cool"
                },
                "diamondstorm": {
                    "num": 591,
                    "accuracy": 95,
                    "basePower": 100,
                    "category": "Physical",
                    "desc": "Has a 50% chance to raise the user's Defense by 2 stages.",
                    "shortDesc": "50% chance to raise user's Def by 2 for each hit.",
                    "id": "diamondstorm",
                    "isViable": True,
                    "name": "Diamond Storm",
                    "pp": 5,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": {
                        "chance": 50,
                    },
                    "target": "allAdjacentFoes",
                    "type": "Rock",
                    "zMovePower": 180,
                    "contestType": "Beautiful"
                },
                "dig": {
                    "num": 91,
                    "accuracy": 100,
                    "basePower": 80,
                    "category": "Physical",
                    "desc": "This attack charges on the first turn and executes on the second. On the first turn, the user avoids all attacks other than Earthquake and Magnitude but takes double damage from them, and is also unaffected by weather. If the user is holding a Power Herb, the move completes in one turn.",
                    "shortDesc": "Digs underground turn 1, strikes turn 2.",
                    "id": "dig",
                    "name": "Dig",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "charge": 1,
                        "protect": 1,
                        "mirror": 1,
                        "nonsky": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Ground",
                    "zMovePower": 160,
                    "contestType": "Tough"
                },
                "disable": {
                    "num": 50,
                    "accuracy": 100,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "For 4 turns, the target's last move used becomes disabled. Fails if one of the target's moves is already disabled, if the target has not made a move, or if the target no longer knows the move.",
                    "shortDesc": "For 4 turns, disables the target's last move used.",
                    "id": "disable",
                    "isViable": True,
                    "name": "Disable",
                    "pp": 20,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "reflectable": 1,
                        "mirror": 1,
                        "authentic": 1
                    },
                    "volatileStatus": "disable",
                    "secondary": None,
                    "target": "normal",
                    "type": "Normal",
                    "zMoveEffect": "clearnegativeboost",
                    "contestType": "Clever"
                },
                "disarmingvoice": {
                    "num": 574,
                    "accuracy": True,
                    "basePower": 40,
                    "category": "Special",
                    "desc": "This move does not check 'accuracy'.",
                    "shortDesc": "This move does not check 'accuracy'. Hits foes.",
                    "id": "disarmingvoice",
                    "name": "Disarming Voice",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1,
                        "sound": 1,
                        "authentic": 1
                    },
                    "secondary": None,
                    "target": "allAdjacentFoes",
                    "type": "Fairy",
                    "zMovePower": 100,
                    "contestType": "Cute"
                },
                "discharge": {
                    "num": 435,
                    "accuracy": 100,
                    "basePower": 80,
                    "category": "Special",
                    "desc": "Has a 30% chance to paralyze the target.",
                    "shortDesc": "30% chance to paralyze adjacent Pokemon.",
                    "id": "discharge",
                    "isViable": True,
                    "name": "Discharge",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": {
                        "chance": 30,
                        "status": "par",
                    },
                    "target": "allAdjacent",
                    "type": "Electric",
                    "zMovePower": 160,
                    "contestType": "Beautiful"
                },
                "dive": {
                    "num": 291,
                    "accuracy": 100,
                    "basePower": 80,
                    "category": "Physical",
                    "desc": "This attack charges on the first turn and executes on the second. On the first turn, the user avoids all attacks other than Surf and Whirlpool but takes double damage from them, and is also unaffected by weather. If the user is holding a Power Herb, the move completes in one turn.",
                    "shortDesc": "Dives underwater turn 1, strikes turn 2.",
                    "id": "dive",
                    "name": "Dive",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "charge": 1,
                        "protect": 1,
                        "mirror": 1,
                        "nonsky": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Water",
                    "zMovePower": 160,
                    "contestType": "Beautiful"
                },
                "dizzypunch": {
                    "num": 146,
                    "accuracy": 100,
                    "basePower": 70,
                    "category": "Physical",
                    "desc": "Has a 20% chance to confuse the target.",
                    "shortDesc": "20% chance to confuse the target.",
                    "id": "dizzypunch",
                    "name": "Dizzy Punch",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1,
                        "powder": 1
                    },
                    "secondary": {
                        "chance": 20,
                        "volatileStatus": "confusion",
                    },
                    "target": "normal",
                    "type": "Normal",
                    "zMovePower": 140,
                    "contestType": "Cute"
                },
                "doomdesire": {
                    "num": 353,
                    "accuracy": 100,
                    "basePower": 140,
                    "category": "Special",
                    "desc": "Deals damage two turns after this move is used. At the end of that turn, the damage is calculated at that time and dealt to the Pokemon at the position the target had when the move was used. If the user is no longer active at the time, damage is calculated based on the user's natural Special Attack stat, types, and level, with no boosts from its held item or Ability. Fails if this move or Future Sight is already in effect for the target's position.",
                    "shortDesc": "Hits two turns after being used.",
                    "id": "doomdesire",
                    "name": "Doom Desire",
                    "pp": 5,
                    "priority": 0,
                    "flags": {},
                    "secondary": None,
                    "target": "normal",
                    "type": "Steel",
                    "zMovePower": 200,
                    "contestType": "Beautiful"
                },
                "doubleedge": {
                    "num": 38,
                    "accuracy": 100,
                    "basePower": 120,
                    "category": "Physical",
                    "desc": "If the target lost HP, the user takes recoil damage equal to 33% the HP lost by the target, rounded half up, but not less than 1 HP.",
                    "shortDesc": "Has 33% recoil.",
                    "id": "doubleedge",
                    "isViable": True,
                    "name": "Double-Edge",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "recoil": [
                        33,
                        100
                    ],
                    "secondary": None,
                    "target": "normal",
                    "type": "Normal",
                    "zMovePower": 190,
                    "contestType": "Tough"
                },
                "doublehit": {
                    "num": 458,
                    "accuracy": 90,
                    "basePower": 35,
                    "category": "Physical",
                    "desc": "Hits twice. If the first hit breaks the target's substitute, it will take damage for the second hit.",
                    "shortDesc": "Hits 2 times in one turn.",
                    "id": "doublehit",
                    "name": "Double Hit",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "multihit": 2,
                    "secondary": None,
                    "target": "normal",
                    "type": "Normal",
                    "zMovePower": 140,
                    "contestType": "Cool"
                },
                "doubleironbash": {
                    "num": 742,
                    "accuracy": 100,
                    "basePower": 60,
                    "category": "Physical",
                    "desc": "Hits twice. If the first hit breaks the target's substitute, it will take damage for the second hit. Has a 30% chance to flinch the target.",
                    "shortDesc": "Hits twice. 30% chance to flinch.",
                    "id": "doubleironbash",
                    "isNonstandard": "LGPE",
                    "isUnreleased": True,
                    "isViable": True,
                    "name": "Double Iron Bash",
                    "pp": 5,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1,
                        "powder": 1
                    },
                    "multihit": 2,
                    "secondary": {
                        "chance": 30,
                        "volatileStatus": "flinch"
                    },
                    "target": "normal",
                    "type": "Steel",
                    "zMovePower": 180,
                    "contestType": "Clever"
                },
                "doublekick": {
                    "num": 24,
                    "accuracy": 100,
                    "basePower": 30,
                    "category": "Physical",
                    "desc": "Hits twice. If the first hit breaks the target's substitute, it will take damage for the second hit.",
                    "shortDesc": "Hits 2 times in one turn.",
                    "id": "doublekick",
                    "name": "Double Kick",
                    "pp": 30,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "multihit": 2,
                    "secondary": None,
                    "target": "normal",
                    "type": "Fighting",
                    "zMovePower": 100,
                    "contestType": "Cool"
                },
                "doubleslap": {
                    "num": 3,
                    "accuracy": 85,
                    "basePower": 15,
                    "category": "Physical",
                    "desc": "Hits two to five times. Has a 1/3 chance to hit two or three times, and a 1/6 chance to hit four or five times. If one of the hits breaks the target's substitute, it will take damage for the remaining hits. If the user has the Skill Link Ability, this move will always hit five times.",
                    "shortDesc": "Hits 2-5 times in one turn.",
                    "id": "doubleslap",
                    "name": "Double Slap",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "multihit": [
                        2,
                        5
                    ],
                    "secondary": None,
                    "target": "normal",
                    "type": "Normal",
                    "zMovePower": 100,
                    "contestType": "Cute"
                },
                "doubleteam": {
                    "num": 104,
                    "accuracy": True,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "Raises the user's evasiveness by 1 stage.",
                    "shortDesc": "Raises the user's evasiveness by 1.",
                    "id": "doubleteam",
                    "name": "Double Team",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "snatch": 1
                    },
                    "boosts": {
                        "evasion": 1,
                    },
                    "secondary": None,
                    "target": "self",
                    "type": "Normal",
                    "zMoveEffect": "clearnegativeboost",
                    "contestType": "Cool"
                },
                "dracometeor": {
                    "num": 434,
                    "accuracy": 90,
                    "basePower": 130,
                    "category": "Special",
                    "desc": "Lowers the user's Special Attack by 2 stages.",
                    "shortDesc": "Lowers the user's Sp. Atk by 2.",
                    "id": "dracometeor",
                    "isViable": True,
                    "name": "Draco Meteor",
                    "pp": 5,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Dragon",
                    "zMovePower": 195,
                    "contestType": "Beautiful"
                },
                "dragonascent": {
                    "num": 620,
                    "accuracy": 100,
                    "basePower": 120,
                    "category": "Physical",
                    "desc": "Lowers the user's Defense and Special Defense by 1 stage.",
                    "shortDesc": "Lowers the user's Defense and Sp. Def by 1.",
                    "id": "dragonascent",
                    "isViable": True,
                    "name": "Dragon Ascent",
                    "pp": 5,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1,
                        "distance": 1
                    },
                    "self": {
                        "boosts": {
                            "def": -1,
                            "spd": -1
                        },
                    },
                    "target": "any",
                    "type": "Flying",
                    "zMovePower": 190,
                    "contestType": "Beautiful"
                },
                "dragonbreath": {
                    "num": 225,
                    "accuracy": 100,
                    "basePower": 60,
                    "category": "Special",
                    "desc": "Has a 30% chance to paralyze the target.",
                    "shortDesc": "30% chance to paralyze the target.",
                    "id": "dragonbreath",
                    "name": "Dragon Breath",
                    "pp": 20,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": {
                        "chance": 30,
                        "status": "par",
                    },
                    "target": "normal",
                    "type": "Dragon",
                    "zMovePower": 120,
                    "contestType": "Cool"
                },
                "dragonclaw": {
                    "num": 337,
                    "accuracy": 100,
                    "basePower": 80,
                    "category": "Physical",
                    "shortDesc": "No additional effect.",
                    "id": "dragonclaw",
                    "isViable": True,
                    "name": "Dragon Claw",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Dragon",
                    "zMovePower": 160,
                    "contestType": "Cool"
                },
                "dragondance": {
                    "num": 349,
                    "accuracy": True,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "Raises the user's Attack and Speed by 1 stage.",
                    "shortDesc": "Raises the user's Attack and Speed by 1.",
                    "id": "dragondance",
                    "isViable": True,
                    "name": "Dragon Dance",
                    "pp": 20,
                    "priority": 0,
                    "flags": {
                        "snatch": 1,
                        "dance": 1
                    },
                    "boosts": {
                        "atk": 1,
                        "spe": 1
                    },
                    "secondary": None,
                    "target": "self",
                    "type": "Dragon",
                    "zMoveEffect": "clearnegativeboost",
                    "contestType": "Cool"
                },
                "dragonhammer": {
                    "num": 692,
                    "accuracy": 100,
                    "basePower": 90,
                    "category": "Physical",
                    "shortDesc": "No additional effect.",
                    "id": "dragonhammer",
                    "isViable": True,
                    "name": "Dragon Hammer",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Dragon",
                    "zMovePower": 175,
                    "contestType": "Tough"
                },
                "dragonpulse": {
                    "num": 406,
                    "accuracy": 100,
                    "basePower": 85,
                    "category": "Special",
                    "shortDesc": "No additional effect.",
                    "id": "dragonpulse",
                    "isViable": True,
                    "name": "Dragon Pulse",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "pulse": 1,
                        "mirror": 1,
                        "distance": 1
                    },
                    "secondary": None,
                    "target": "any",
                    "type": "Dragon",
                    "zMovePower": 160,
                    "contestType": "Beautiful"
                },
                "dragonrage": {
                    "num": 82,
                    "accuracy": 100,
                    "basePower": 0,
                    "damage": 40,
                    "category": "Special",
                    "shortDesc": "Deals 40 HP of damage to the target.",
                    "id": "dragonrage",
                    "name": "Dragon Rage",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Dragon",
                    "zMovePower": 100,
                    "contestType": "Cool"
                },
                "dragonrush": {
                    "num": 407,
                    "accuracy": 75,
                    "basePower": 100,
                    "category": "Physical",
                    "desc": "Has a 20% chance to flinch the target. Damage doubles and no 'accuracy' check is done if the target has used Minimize while active.",
                    "shortDesc": "20% chance to flinch the target.",
                    "id": "dragonrush",
                    "name": "Dragon Rush",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": {
                        "chance": 20,
                        "volatileStatus": "flinch"
                    },
                    "target": "normal",
                    "type": "Dragon",
                    "zMovePower": 180,
                    "contestType": "Tough"
                },
                "dragontail": {
                    "num": 525,
                    "accuracy": 90,
                    "basePower": 60,
                    "category": "Physical",
                    "desc": "If both the user and the target have not fainted, the target is forced to switch out and be replaced with a random unfainted ally. This effect fails if the target used Ingrain previously, has the Suction Cups Ability, or this move hit a substitute.",
                    "shortDesc": "Forces the target to switch to a random ally.",
                    "id": "dragontail",
                    "isViable": True,
                    "name": "Dragon Tail",
                    "pp": 10,
                    "priority": -6,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "forceSwitch": True,
                    "target": "normal",
                    "type": "Dragon",
                    "zMovePower": 120,
                    "contestType": "Tough"
                },
                "drainingkiss": {
                    "num": 577,
                    "accuracy": 100,
                    "basePower": 50,
                    "category": "Special",
                    "desc": "The user recovers 3/4 the HP lost by the target, rounded half up. If Big Root is held by the user, the HP recovered is 1.3x normal, rounded half down.",
                    "shortDesc": "User recovers 75% of the damage dealt.",
                    "id": "drainingkiss",
                    "name": "Draining Kiss",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1,
                        "heal": 1
                    },
                    "drain": [
                        3,
                        4
                    ],
                    "secondary": None,
                    "target": "normal",
                    "type": "Fairy",
                    "zMovePower": 100,
                    "contestType": "Cute"
                },
                "drainpunch": {
                    "num": 409,
                    "accuracy": 100,
                    "basePower": 75,
                    "category": "Physical",
                    "desc": "The user recovers 1/2 the HP lost by the target, rounded half up. If Big Root is held by the user, the HP recovered is 1.3x normal, rounded half down.",
                    "shortDesc": "User recovers 50% of the damage dealt.",
                    "id": "drainpunch",
                    "isViable": True,
                    "name": "Drain Punch",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1,
                        "powder": 1,
                        "heal": 1
                    },
                    "drain": [
                        1,
                        2
                    ],
                    "secondary": None,
                    "target": "normal",
                    "type": "Fighting",
                    "zMovePower": 140,
                    "contestType": "Tough"
                },
                "dreameater": {
                    "num": 138,
                    "accuracy": 100,
                    "basePower": 100,
                    "category": "Special",
                    "desc": "The target is unaffected by this move unless it is asleep. The user recovers 1/2 the HP lost by the target, rounded half up. If Big Root is held by the user, the HP recovered is 1.3x normal, rounded half down.",
                    "shortDesc": "User gains 1/2 HP inflicted. Sleeping target only.",
                    "id": "dreameater",
                    "name": "Dream Eater",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1,
                        "heal": 1
                    },
                    "drain": [
                        1,
                        2
                    ],
                    "secondary": None,
                    "target": "normal",
                    "type": "Psychic",
                    "zMovePower": 180,
                    "contestType": "Clever"
                },
                "drillpeck": {
                    "num": 65,
                    "accuracy": 100,
                    "basePower": 80,
                    "category": "Physical",
                    "shortDesc": "No additional effect.",
                    "id": "drillpeck",
                    "isViable": True,
                    "name": "Drill Peck",
                    "pp": 20,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1,
                        "distance": 1
                    },
                    "secondary": None,
                    "target": "any",
                    "type": "Flying",
                    "zMovePower": 160,
                    "contestType": "Cool"
                },
                "drillrun": {
                    "num": 529,
                    "accuracy": 95,
                    "basePower": 80,
                    "category": "Physical",
                    "desc": "Has a higher chance for a critical hit.",
                    "shortDesc": "High critical hit ratio.",
                    "id": "drillrun",
                    "isViable": True,
                    "name": "Drill Run",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "critRatio": 2,
                    "secondary": None,
                    "target": "normal",
                    "type": "Ground",
                    "zMovePower": 160,
                    "contestType": "Tough"
                },
                "dualchop": {
                    "num": 530,
                    "accuracy": 90,
                    "basePower": 40,
                    "category": "Physical",
                    "desc": "Hits twice. If the first hit breaks the target's substitute, it will take damage for the second hit.",
                    "shortDesc": "Hits 2 times in one turn.",
                    "id": "dualchop",
                    "name": "Dual Chop",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "multihit": 2,
                    "secondary": None,
                    "target": "normal",
                    "type": "Dragon",
                    "zMovePower": 100,
                    "contestType": "Tough"
                },
                "dynamicpunch": {
                    "num": 223,
                    "accuracy": 50,
                    "basePower": 100,
                    "category": "Physical",
                    "desc": "Has a 100% chance to confuse the target.",
                    "shortDesc": "100% chance to confuse the target.",
                    "id": "dynamicpunch",
                    "name": "Dynamic Punch",
                    "pp": 5,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1,
                        "powder": 1
                    },
                    "secondary": {
                        "chance": 100,
                        "volatileStatus": "confusion",
                    },
                    "target": "normal",
                    "type": "Fighting",
                    "zMovePower": 180,
                    "contestType": "Cool"
                },
                "earthpower": {
                    "num": 414,
                    "accuracy": 100,
                    "basePower": 90,
                    "category": "Special",
                    "desc": "Has a 10% chance to lower the target's Special Defense by 1 stage.",
                    "shortDesc": "10% chance to lower the target's Sp. Def by 1.",
                    "id": "earthpower",
                    "isViable": True,
                    "name": "Earth Power",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1,
                        "nonsky": 1
                    },
                    "secondary": {
                        "chance": 10,
                        "boosts": {
                            "spd": -1
                        },
                    },
                    "target": "normal",
                    "type": "Ground",
                    "zMovePower": 175,
                    "contestType": "Beautiful"
                },
                "earthquake": {
                    "num": 89,
                    "accuracy": 100,
                    "basePower": 100,
                    "category": "Physical",
                    "desc": "Damage doubles if the target is using Dig.",
                    "shortDesc": "Hits adjacent Pokemon. Double damage on Dig.",
                    "id": "earthquake",
                    "isViable": True,
                    "name": "Earthquake",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1,
                        "nonsky": 1
                    },
                    "secondary": None,
                    "target": "allAdjacent",
                    "type": "Ground",
                    "zMovePower": 180,
                    "contestType": "Tough"
                },
                "echoedvoice": {
                    "num": 497,
                    "accuracy": 100,
                    "basePower": 40,
                    "category": "Special",
                    "desc": "For every consecutive turn that this move is used by at least one Pokemon, this move's power is multiplied by the number of turns to pass, but not more than 5.",
                    "shortDesc": "Power increases when used on consecutive turns.",
                    "id": "echoedvoice",
                    "name": "Echoed Voice",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1,
                        "sound": 1,
                        "authentic": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Normal",
                    "zMovePower": 100,
                    "contestType": "Beautiful"
                },
                "eerieimpulse": {
                    "num": 598,
                    "accuracy": 100,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "Lowers the target's Special Attack by 2 stages.",
                    "shortDesc": "Lowers the target's Sp. Atk by 2.",
                    "id": "eerieimpulse",
                    "name": "Eerie Impulse",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "reflectable": 1,
                        "mirror": 1
                    },
                    "boosts": {
                        "spa": -2,
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Electric",
                    "zMoveBoost": {
                        "spd": 1
                    },
                    "contestType": "Clever"
                },
                "eggbomb": {
                    "num": 121,
                    "accuracy": 75,
                    "basePower": 100,
                    "category": "Physical",
                    "shortDesc": "No additional effect.",
                    "id": "eggbomb",
                    "name": "Egg Bomb",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "bullet": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Normal",
                    "zMovePower": 180,
                    "contestType": "Cute"
                },
                "electricterrain": {
                    "num": 604,
                    "accuracy": True,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "For 5 turns, the terrain becomes Electric Terrain. During the effect, the power of Electric-type attacks made by grounded Pokemon is multiplied by 1.5 and grounded Pokemon cannot fall asleep; Pokemon already asleep do not wake up. Camouflage transforms the user into an Electric type, Nature Power becomes Thunderbolt, and Secret Power has a 30% chance to cause paralysis. Fails if the current terrain is Electric Terrain.",
                    "shortDesc": "5 turns. Grounded: +Electric power, can't sleep.",
                    "id": "electricterrain",
                    "name": "Electric Terrain",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "nonsky": 1
                    },
                    "terrain": "electricterrain",
                    "secondary": None,
                    "target": "all",
                    "type": "Electric",
                    "zMoveBoost": {
                        "spe": 1
                    },
                    "contestType": "Clever"
                },
                "electrify": {
                    "num": 582,
                    "accuracy": True,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "Causes the target's move to become Electric type this turn. Among effects that can change a move's type, this effect happens last. Fails if the target already moved this turn.",
                    "shortDesc": "Changes the target's move to Electric this turn.",
                    "id": "electrify",
                    "name": "Electrify",
                    "pp": 20,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1,
                        "mystery": 1
                    },
                    "volatileStatus": "electrify",
                    "secondary": None,
                    "target": "normal",
                    "type": "Electric",
                    "zMoveBoost": {
                        "spa": 1
                    },
                    "contestType": "Clever"
                },
                "electroball": {
                    "num": 486,
                    "accuracy": 100,
                    "basePower": 0,
                    "category": "Special",
                    "desc": "The power of this move depends on (user's current Speed / target's current Speed), rounded down. Power is equal to 150 if the result is 4 or more, 120 if 3, 80 if 2, 60 if 1, 40 if less than 1. If the target's current Speed is 0, this move's power is 40.",
                    "shortDesc": "More power the faster the user is than the target.",
                    "id": "electroball",
                    "name": "Electro Ball",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "bullet": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Electric",
                    "zMovePower": 160,
                    "contestType": "Cool"
                },
                "electroweb": {
                    "num": 527,
                    "accuracy": 95,
                    "basePower": 55,
                    "category": "Special",
                    "desc": "Has a 100% chance to lower the target's Speed by 1 stage.",
                    "shortDesc": "100% chance to lower the foe(s) Speed by 1.",
                    "id": "electroweb",
                    "name": "Electroweb",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": {
                        "chance": 100,
                        "boosts": {
                            "spe": -1,
                        },
                    },
                    "target": "allAdjacentFoes",
                    "type": "Electric",
                    "zMovePower": 100,
                    "contestType": "Beautiful"
                },
                "embargo": {
                    "num": 373,
                    "accuracy": 100,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "For 5 turns, the target's held item has no effect. An item's effect of causing forme changes is unaffected, but any other effects from such items are negated.During the effect, Fling and Natural Gift are prevented from being used by the target.Items thrown at the target with Fling will still activate for it.If the target uses Baton Pass, the replacement will remain unable to use items. ",
                    "shortDesc": "For 5 turns, the target's item has no effect.",
                    "id": "embargo",
                    "name": "Embargo",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "reflectable": 1,
                        "mirror": 1
                    },
                    "volatileStatus": "embargo",
                    "secondary": None,
                    "target": "normal",
                    "type": "Dark",
                    "zMoveBoost": {
                        "spa": 1
                    },
                    "contestType": "Clever"
                },
                "ember": {
                    "num": 52,
                    "accuracy": 100,
                    "basePower": 40,
                    "category": "Special",
                    "desc": "Has a 10% chance to burn the target.",
                    "shortDesc": "10% chance to burn the target.",
                    "id": "ember",
                    "name": "Ember",
                    "pp": 25,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": {
                        "chance": 10,
                        "status": "brn",
                    },
                    "target": "normal",
                    "type": "Fire",
                    "zMovePower": 100,
                    "contestType": "Cute"
                },
                "encore": {
                    "num": 227,
                    "accuracy": 100,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "For its next 3 turns, the target is forced to repeat its last move used. If the affected move runs out of PP, the effect ends. Fails if the target is already under this effect, if it has not made a move, if the move has 0 PP, or if the move is Assist, Copycat, Encore, Me First, Metronome, Mimic, Mirror Move, Nature Power, Sketch, Sleep Talk, Struggle, Transform, or any Z-Move.",
                    "shortDesc": "Target repeats its last move for its next 3 turns.",
                    "id": "encore",
                    "isViable": True,
                    "name": "Encore",
                    "pp": 5,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "reflectable": 1,
                        "mirror": 1,
                        "authentic": 1
                    },
                    "volatileStatus": "encore",
                    "secondary": None,
                    "target": "normal",
                    "type": "Normal",
                    "zMoveBoost": {
                        "spe": 1
                    },
                    "contestType": "Cute"
                },
                "endeavor": {
                    "num": 283,
                    "accuracy": 100,
                    "basePower": 0,
                    "category": "Physical",
                    "desc": "Deals damage to the target equal to (target's current HP - user's current HP). The target is unaffected if its current HP is less than or equal to the user's current HP.",
                    "shortDesc": "Lowers the target's HP to the user's HP.",
                    "id": "endeavor",
                    "isViable": True,
                    "name": "Endeavor",
                    "pp": 5,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Normal",
                    "zMovePower": 160,
                    "contestType": "Tough"
                },
                "endure": {
                    "num": 203,
                    "accuracy": True,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "The user will survive attacks made by other Pokemon during this turn with at least 1 HP. This move has a 1/X chance of being successful, where X starts at 1 and triples each time this move is successfully used. X resets to 1 if this move fails, if the user's last move used is not Baneful Bunker, Detect, Endure, King's Shield, Protect, Quick Guard, Spiky Shield, or Wide Guard, or if it was one of those moves and the user 's protection was broken. Fails if the user moves last this turn.",
                    "shortDesc": "User survives attacks this turn with at least 1 HP.",
                    "id": "endure",
                    "name": "Endure",
                    "pp": 10,
                    "priority": 4,
                    "flags": {},
                    "stallingMove": True,
                    "volatileStatus": "endure",
                    "secondary": None,
                    "target": "self",
                    "type": "Normal",
                    "zMoveEffect": "clearnegativeboost",
                    "contestType": "Tough"
                },
                "energyball": {
                    "num": 412,
                    "accuracy": 100,
                    "basePower": 90,
                    "category": "Special",
                    "desc": "Has a 10% chance to lower the target's Special Defense by 1 stage.",
                    "shortDesc": "10% chance to lower the target's Sp. Def by 1.",
                    "id": "energyball",
                    "isViable": True,
                    "name": "Energy Ball",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "bullet": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": {
                        "chance": 10,
                        "boosts": {
                            "spd": -1
                        },
                    },
                    "target": "normal",
                    "type": "Grass",
                    "zMovePower": 175,
                    "contestType": "Beautiful"
                },
                "entrainment": {
                    "num": 494,
                    "accuracy": 100,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "Causes the target's Ability to become the same as the user's. Fails if the target's Ability is Battle Bond, Comatose, Disguise, Multitype, Power Construct, RKS System, Schooling, Shields Down, Stance Change, Truant, or the same Ability as the user, or if the user's Ability is Battle Bond, Comatose, Disguise, Flower Gift, Forecast, Illusion, Imposter, Multitype, Power Construct, Power of Alchemy, Receiver, RKS System, Schooling, Shields Down, Stance Change, Trace, or Zen Mode.",
                    "shortDesc": "The target's Ability changes to match the user's.",
                    "id": "entrainment",
                    "name": "Entrainment",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "reflectable": 1,
                        "mirror": 1,
                        "mystery": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Normal",
                    "zMoveBoost": {
                        "spd": 1
                    },
                    "contestType": "Cute"
                },
                "eruption": {
                    "num": 284,
                    "accuracy": 100,
                    "basePower": 150,
                    "category": "Special",
                    "desc": "Power is equal to (user's current HP * 150 / user's maximum HP), rounded down, but not less than 1.",
                    "shortDesc": "Less power as user's HP decreases. Hits foe(s).",
                    "id": "eruption",
                    "isViable": True,
                    "name": "Eruption",
                    "pp": 5,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": None,
                    "target": "allAdjacentFoes",
                    "type": "Fire",
                    "zMovePower": 200,
                    "contestType": "Beautiful"
                },
                "explosion": {
                    "num": 153,
                    "accuracy": 100,
                    "basePower": 250,
                    "category": "Physical",
                    "desc": "The user faints after using this move, even if this move fails for having no target. This move is prevented from executing if any active Pokemon has the Damp Ability.",
                    "shortDesc": "Hits adjacent Pokemon. The user faints.",
                    "id": "explosion",
                    "isViable": True,
                    "name": "Explosion",
                    "pp": 5,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1
                    },
                    "selfdestruct": "always",
                    "secondary": None,
                    "target": "allAdjacent",
                    "type": "Normal",
                    "zMovePower": 200,
                    "contestType": "Beautiful"
                },
                "extrasensory": {
                    "num": 326,
                    "accuracy": 100,
                    "basePower": 80,
                    "category": "Special",
                    "desc": "Has a 10% chance to flinch the target.",
                    "shortDesc": "10% chance to flinch the target.",
                    "id": "extrasensory",
                    "isViable": True,
                    "name": "Extrasensory",
                    "pp": 20,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": {
                        "chance": 10,
                        "volatileStatus": "flinch"
                    },
                    "target": "normal",
                    "type": "Psychic",
                    "zMovePower": 160,
                    "contestType": "Cool"
                },
                "extremeevoboost": {
                    "num": 702,
                    "accuracy": True,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "Raises the user's Attack, Defense, Special Attack, Special Defense, and Speed by 2 stages.",
                    "shortDesc": "Raises user's Atk, Def, SpA, SpD, and Spe by 2.",
                    "id": "extremeevoboost",
                    "isViable": True,
                    "name": "Extreme Evoboost",
                    "pp": 1,
                    "priority": 0,
                    "flags": {},
                    "isZ": "eeviumz",
                    "boosts": {
                        "atk": 2,
                        "def": 2,
                        "spa": 2,
                        "spd": 2,
                        "spe": 2
                    },
                    "secondary": None,
                    "target": "self",
                    "type": "Normal",
                    "contestType": "Beautiful"
                },
                "extremespeed": {
                    "num": 245,
                    "accuracy": 100,
                    "basePower": 80,
                    "category": "Physical",
                    "desc": "No additional effect.",
                    "shortDesc": "Nearly always goes first.",
                    "id": "extremespeed",
                    "isViable": True,
                    "name": "Extreme Speed",
                    "pp": 5,
                    "priority": 2,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Normal",
                    "zMovePower": 160,
                    "contestType": "Cool"
                },
                "facade": {
                    "num": 263,
                    "accuracy": 100,
                    "basePower": 70,
                    "category": "Physical",
                    "desc": "Power doubles if the user is burned, paralyzed, or poisoned. The physical damage halving effect from the user's burn is ignored.",
                    "shortDesc": "Power doubles if user is burn/poison/paralyzed.",
                    "id": "facade",
                    "isViable": True,
                    "name": "Facade",
                    "pp": 20,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Normal",
                    "zMovePower": 140,
                    "contestType": "Cute"
                },
                "fairylock": {
                    "num": 587,
                    "accuracy": True,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "Prevents all active Pokemon from switching next turn. A Pokemon can still switch out if it is holding Shed Shell or uses Baton Pass, Parting Shot, U-turn, or Volt Switch. Fails if the effect is already active.",
                    "shortDesc": "Prevents all Pokemon from switching next turn.",
                    "id": "fairylock",
                    "name": "Fairy Lock",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "mirror": 1,
                        "authentic": 1
                    },
                    "secondary": None,
                    "target": "all",
                    "type": "Fairy",
                    "zMoveBoost": {
                        "def": 1
                    },
                    "contestType": "Clever"
                },
                "fairywind": {
                    "num": 584,
                    "accuracy": 100,
                    "basePower": 40,
                    "category": "Special",
                    "shortDesc": "No additional effect.",
                    "id": "fairywind",
                    "name": "Fairy Wind",
                    "pp": 30,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Fairy",
                    "zMovePower": 100,
                    "contestType": "Beautiful"
                },
                "fakeout": {
                    "num": 252,
                    "accuracy": 100,
                    "basePower": 40,
                    "category": "Physical",
                    "desc": "Has a 100% chance to flinch the target. Fails unless it is the user's first turn on the field.",
                    "shortDesc": "Hits first. First turn out only. 100% flinch chance.",
                    "id": "fakeout",
                    "isViable": True,
                    "name": "Fake Out",
                    "pp": 10,
                    "priority": 3,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": {
                        "chance": 100,
                        "volatileStatus": "flinch"
                    },
                    "target": "normal",
                    "type": "Normal",
                    "zMovePower": 100,
                    "contestType": "Cute"
                },
                "faketears": {
                    "num": 313,
                    "accuracy": 100,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "Lowers the target's Special Defense by 2 stages.",
                    "shortDesc": "Lowers the target's Sp. Def by 2.",
                    "id": "faketears",
                    "name": "Fake Tears",
                    "pp": 20,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "reflectable": 1,
                        "mirror": 1,
                        "mystery": 1
                    },
                    "boosts": {
                        "spd": -2
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Dark",
                    "zMoveBoost": {
                        "spa": 1
                    },
                    "contestType": "Cute"
                },
                "falseswipe": {
                    "num": 206,
                    "accuracy": 100,
                    "basePower": 40,
                    "category": "Physical",
                    "desc": "Leaves the target with at least 1 HP.",
                    "shortDesc": "Always leaves the target with at least 1 HP.",
                    "id": "falseswipe",
                    "name": "False Swipe",
                    "pp": 40,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "noFaint": True,
                    "secondary": None,
                    "target": "normal",
                    "type": "Normal",
                    "zMovePower": 100,
                    "contestType": "Cool"
                },
                "featherdance": {
                    "num": 297,
                    "accuracy": 100,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "Lowers the target's Attack by 2 stages.",
                    "shortDesc": "Lowers the target's Attack by 2.",
                    "id": "featherdance",
                    "name": "Feather Dance",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "reflectable": 1,
                        "mirror": 1,
                        "mystery": 1,
                        "dance": 1
                    },
                    "boosts": {
                        "atk": -2,
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Flying",
                    "zMoveBoost": {
                        "def": 1
                    },
                    "contestType": "Beautiful"
                },
                "feint": {
                    "num": 364,
                    "accuracy": 100,
                    "basePower": 30,
                    "category": "Physical",
                    "desc": "If this move is successful, it breaks through the target's Baneful Bunker, Detect, King's Shield, Protect, or Spiky Shield for this turn, allowing other Pokemon to attack the target normally. If the target 's side is protected by Crafty Shield, Mat Block, Quick Guard, or Wide Guard, that protection is also broken for this turn and other Pokemon may attack the target' s side normally.",
                    "shortDesc": "Noneifies Detect, Protect, and Quick/Wide Guard.",
                    "id": "feint",
                    "name": "Feint",
                    "pp": 10,
                    "priority": 2,
                    "flags": {
                        "mirror": 1
                    },
                    "breaksProtect": True,
                    "secondary": None,
                    "target": "normal",
                    "type": "Normal",
                    "zMovePower": 100,
                    "contestType": "Clever"
                },
                "feintattack": {
                    "num": 185,
                    "accuracy": True,
                    "basePower": 60,
                    "category": "Physical",
                    "shortDesc": "This move does not check 'accuracy'.",
                    "id": "feintattack",
                    "name": "Feint Attack",
                    "pp": 20,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Dark",
                    "zMovePower": 120,
                    "contestType": "Clever"
                },
                "fellstinger": {
                    "num": 565,
                    "accuracy": 100,
                    "basePower": 50,
                    "category": "Physical",
                    "desc": "Raises the user's Attack by 3 stages if this move knocks out the target.",
                    "shortDesc": "Raises user's Attack by 3 if this KOes the target.",
                    "id": "fellstinger",
                    "name": "Fell Stinger",
                    "pp": 25,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Bug",
                    "zMovePower": 100,
                    "contestType": "Cool"
                },
                "fierydance": {
                    "num": 552,
                    "accuracy": 100,
                    "basePower": 80,
                    "category": "Special",
                    "desc": "Has a 50% chance to raise the user's Special Attack by 1 stage.",
                    "shortDesc": "50% chance to raise the user's Sp. Atk by 1.",
                    "id": "fierydance",
                    "isViable": True,
                    "name": "Fiery Dance",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1,
                        "dance": 1
                    },
                    "target": "normal",
                    "type": "Fire",
                    "zMovePower": 160,
                    "contestType": "Beautiful"
                },
                "finalgambit": {
                    "num": 515,
                    "accuracy": 100,
                    "basePower": 0,
                    "category": "Special",
                    "desc": "Deals damage to the target equal to the user's current HP. If this move is successful, the user faints.",
                    "shortDesc": "Does damage equal to the user's HP. User faints.",
                    "id": "finalgambit",
                    "isViable": True,
                    "name": "Final Gambit",
                    "pp": 5,
                    "priority": 0,
                    "flags": {
                        "protect": 1
                    },
                    "selfdestruct": "ifHit",
                    "secondary": None,
                    "target": "normal",
                    "type": "Fighting",
                    "zMovePower": 180,
                    "contestType": "Tough"
                },
                "fireblast": {
                    "num": 126,
                    "accuracy": 85,
                    "basePower": 110,
                    "category": "Special",
                    "desc": "Has a 10% chance to burn the target.",
                    "shortDesc": "10% chance to burn the target.",
                    "id": "fireblast",
                    "isViable": True,
                    "name": "Fire Blast",
                    "pp": 5,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": {
                        "chance": 10,
                        "status": "brn",
                    },
                    "target": "normal",
                    "type": "Fire",
                    "zMovePower": 185,
                    "contestType": "Beautiful"
                },
                "firefang": {
                    "num": 424,
                    "accuracy": 95,
                    "basePower": 65,
                    "category": "Physical",
                    "desc": "Has a 10% chance to burn the target and a 10% chance to flinch it.",
                    "shortDesc": "10% chance to burn. 10% chance to flinch.",
                    "id": "firefang",
                    "isViable": True,
                    "name": "Fire Fang",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "bite": 1,
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "target": "normal",
                    "type": "Fire",
                    "zMovePower": 120,
                    "contestType": "Cool"
                },
                "firelash": {
                    "num": 680,
                    "accuracy": 100,
                    "basePower": 80,
                    "category": "Physical",
                    "desc": "Has a 100% chance to lower the target's Defense by 1 stage.",
                    "shortDesc": "100% chance to lower the target's Defense by 1.",
                    "id": "firelash",
                    "isViable": True,
                    "name": "Fire Lash",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": {
                        "chance": 100,
                        "boosts": {
                            "def": -1,
                        },
                    },
                    "target": "normal",
                    "type": "Fire",
                    "zMovePower": 160,
                    "contestType": "Cute"
                },
                "firepledge": {
                    "num": 519,
                    "accuracy": 100,
                    "basePower": 80,
                    "category": "Special",
                    "desc": "If one of the user's allies chose to use Grass Pledge or Water Pledge this turn and has not moved yet, it takes its turn immediately after the user and the user's move does nothing. If combined with Grass Pledge, the ally uses Fire Pledge with 150 power and a sea of fire appears on the target's side for 4 turns, which causes damage to non-Fire types equal to 1/8 of their maximum HP, rounded down, at the end of each turn during effect, including the last turn. If combined with Water Pledge, the ally uses Water Pledge with 150 power and a rainbow appears on the user's side for 4 turns, which doubles secondary effect chances but does not stack with the Serene Grace Ability. When used as a combined move, this move gains STAB no matter what the user's type is. This move does not consume the user's Fire Gem.",
                    "shortDesc": "Use with Grass or Water Pledge for added effect.",
                    "id": "firepledge",
                    "name": "Fire Pledge",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1,
                        "nonsky": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Fire",
                    "zMovePower": 160,
                    "contestType": "Beautiful"
                },
                "firepunch": {
                    "num": 7,
                    "accuracy": 100,
                    "basePower": 75,
                    "category": "Physical",
                    "desc": "Has a 10% chance to burn the target.",
                    "shortDesc": "10% chance to burn the target.",
                    "id": "firepunch",
                    "isViable": True,
                    "name": "Fire Punch",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1,
                        "powder": 1
                    },
                    "secondary": {
                        "chance": 10,
                        "status": "brn",
                    },
                    "target": "normal",
                    "type": "Fire",
                    "zMovePower": 140,
                    "contestType": "Tough"
                },
                "firespin": {
                    "num": 83,
                    "accuracy": 85,
                    "basePower": 35,
                    "category": "Special",
                    "desc": "Prevents the target from switching for four or five turns (seven turns if the user is holding Grip Claw). Causes damage to the target equal to 1/8 of its maximum HP (1/6 if the user is holding Binding Band), rounded down, at the end of each turn during effect. The target can still switch out if it is holding Shed Shell or uses Baton Pass, Parting Shot, U-turn, or Volt Switch. The effect ends if either the user or the target leaves the field, or if the target uses Rapid Spin or Substitute successfully. This effect is not stackable or reset by using this or another binding move.",
                    "shortDesc": "Traps and damages the target for 4-5 turns.",
                    "id": "firespin",
                    "name": "Fire Spin",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1
                    },
                    "volatileStatus": "partiallytrapped",
                    "secondary": None,
                    "target": "normal",
                    "type": "Fire",
                    "zMovePower": 100,
                    "contestType": "Beautiful"
                },
                "firstimpression": {
                    "num": 660,
                    "accuracy": 100,
                    "basePower": 90,
                    "category": "Physical",
                    "desc": "Fails unless it is the user's first turn on the field.",
                    "shortDesc": "Hits first. First turn out only.",
                    "id": "firstimpression",
                    "isViable": True,
                    "name": "First Impression",
                    "pp": 10,
                    "priority": 2,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Bug",
                    "zMovePower": 175,
                    "contestType": "Cute"
                },
                "fissure": {
                    "num": 90,
                    "accuracy": 30,
                    "basePower": 0,
                    "category": "Physical",
                    "desc": "Deals damage to the target equal to the target's maximum HP. Ignores 'accuracy' and evasiveness modifiers. This attack's 'accuracy' is equal to(user 's level - target's level + 30) % , and fails if the target is at a higher level.Pokemon with the Sturdy Ability are immune.",
                    "shortDesc": "OHKOs the target. Fails if user is a lower level.",
                    "id": "fissure",
                    "name": "Fissure",
                    "pp": 5,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1,
                        "nonsky": 1
                    },
                    "ohko": True,
                    "secondary": None,
                    "target": "normal",
                    "type": "Ground",
                    "zMovePower": 180,
                    "contestType": "Tough"
                },
                "flail": {
                    "num": 175,
                    "accuracy": 100,
                    "basePower": 0,
                    "category": "Physical",
                    "desc": "The power of this move is 20 if X is 33 to 48, 40 if X is 17 to 32, 80 if X is 10 to 16, 100 if X is 5 to 9, 150 if X is 2 to 4, and 200 if X is 0 or 1, where X is equal to (user's current HP * 48 / user's maximum HP), rounded down.",
                    "shortDesc": "More power the less HP the user has left.",
                    "id": "flail",
                    "name": "Flail",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Normal",
                    "zMovePower": 160,
                    "contestType": "Cute"
                },
                "flameburst": {
                    "num": 481,
                    "accuracy": 100,
                    "basePower": 70,
                    "category": "Special",
                    "desc": "If this move is successful, the target's ally loses 1/16 of its maximum HP, rounded down, unless it has the Magic Guard Ability.",
                    "shortDesc": "Damages Pokemon next to the target as well.",
                    "id": "flameburst",
                    "name": "Flame Burst",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Fire",
                    "zMovePower": 140,
                    "contestType": "Beautiful"
                },
                "flamecharge": {
                    "num": 488,
                    "accuracy": 100,
                    "basePower": 50,
                    "category": "Physical",
                    "desc": "Has a 100% chance to raise the user's Speed by 1 stage.",
                    "shortDesc": "100% chance to raise the user's Speed by 1.",
                    "id": "flamecharge",
                    "isViable": True,
                    "name": "Flame Charge",
                    "pp": 20,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": {
                        "chance": 100
                    },
                    "target": "normal",
                    "type": "Fire",
                    "zMovePower": 100,
                    "contestType": "Cool"
                },
                "flamewheel": {
                    "num": 172,
                    "accuracy": 100,
                    "basePower": 60,
                    "category": "Physical",
                    "desc": "Has a 10% chance to burn the target.",
                    "shortDesc": "10% chance to burn the target. Thaws user.",
                    "id": "flamewheel",
                    "name": "Flame Wheel",
                    "pp": 25,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1,
                        "defrost": 1
                    },
                    "secondary": {
                        "chance": 10,
                        "status": "brn",
                    },
                    "target": "normal",
                    "type": "Fire",
                    "zMovePower": 120,
                    "contestType": "Beautiful"
                },
                "flamethrower": {
                    "num": 53,
                    "accuracy": 100,
                    "basePower": 90,
                    "category": "Special",
                    "desc": "Has a 10% chance to burn the target.",
                    "shortDesc": "10% chance to burn the target.",
                    "id": "flamethrower",
                    "isViable": True,
                    "name": "Flamethrower",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": {
                        "chance": 10,
                        "status": "brn",
                    },
                    "target": "normal",
                    "type": "Fire",
                    "zMovePower": 175,
                    "contestType": "Beautiful"
                },
                "flareblitz": {
                    "num": 394,
                    "accuracy": 100,
                    "basePower": 120,
                    "category": "Physical",
                    "desc": "Has a 10% chance to burn the target. If the target lost HP, the user takes recoil damage equal to 33% the HP lost by the target, rounded half up, but not less than 1 HP.",
                    "shortDesc": "Has 33% recoil. 10% chance to burn. Thaws user.",
                    "id": "flareblitz",
                    "isViable": True,
                    "name": "Flare Blitz",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1,
                        "defrost": 1
                    },
                    "recoil": [
                        33,
                        100
                    ],
                    "secondary": {
                        "chance": 10,
                        "status": "brn",
                    },
                    "target": "normal",
                    "type": "Fire",
                    "zMovePower": 190,
                    "contestType": "Cool"
                },
                "flash": {
                    "num": 148,
                    "accuracy": 100,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "Lowers the target's 'accuracy' by 1 stage.",
                    "shortDesc": "Lowers the target's 'accuracy' by 1.",
                    "id": "flash",
                    "name": "Flash",
                    "pp": 20,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "reflectable": 1,
                        "mirror": 1
                    },
                    "boosts": {
                        "accuracy": -1,
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Normal",
                    "zMoveBoost": {
                        "evasion": 1
                    },
                    "contestType": "Beautiful"
                },
                "flashcannon": {
                    "num": 430,
                    "accuracy": 100,
                    "basePower": 80,
                    "category": "Special",
                    "desc": "Has a 10% chance to lower the target's Special Defense by 1 stage.",
                    "shortDesc": "10% chance to lower the target's Sp. Def by 1.",
                    "id": "flashcannon",
                    "isViable": True,
                    "name": "Flash Cannon",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": {
                        "chance": 10,
                        "boosts": {
                            "spd": -1
                        },
                    },
                    "target": "normal",
                    "type": "Steel",
                    "zMovePower": 160,
                    "contestType": "Beautiful"
                },
                "flatter": {
                    "num": 260,
                    "accuracy": 100,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "Raises the target's Special Attack by 1 stage and confuses it.",
                    "shortDesc": "Raises the target's Sp. Atk by 1 and confuses it.",
                    "id": "flatter",
                    "name": "Flatter",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "reflectable": 1,
                        "mirror": 1,
                        "mystery": 1
                    },
                    "volatileStatus": "confusion",
                    "boosts": {
                        "spa": 1,
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Dark",
                    "zMoveBoost": {
                        "spd": 1
                    },
                    "contestType": "Clever"
                },
                "fleurcannon": {
                    "num": 705,
                    "accuracy": 90,
                    "basePower": 130,
                    "category": "Special",
                    "desc": "Lowers the user's Special Attack by 2 stages.",
                    "shortDesc": "Lowers the user's Sp. Atk by 2.",
                    "id": "fleurcannon",
                    "isViable": True,
                    "name": "Fleur Cannon",
                    "pp": 5,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Fairy",
                    "zMovePower": 195,
                    "contestType": "Beautiful"
                },
                "fling": {
                    "num": 374,
                    "accuracy": 100,
                    "basePower": 0,
                    "category": "Physical",
                    "desc": "The power of this move is based on the user's held item. The held item is lost and it activates for the target if applicable. If there is no target or the target avoids this move by protecting itself, the user's held item is still lost. The user can regain a thrown item with Recycle or the Harvest Ability. Fails if the user has no held item, if the held item cannot be thrown, if the user is under the effect of Embargo or Magic Room, or if the user has the Klutz Ability.",
                    "shortDesc": "Flings the user's item at the target. Power varies.",
                    "id": "fling",
                    "name": "Fling",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "mirror": 1,
                        "mystery": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Dark",
                    "zMovePower": 100,
                    "contestType": "Cute"
                },
                "floatyfall": {
                    "num": 731,
                    "accuracy": 95,
                    "basePower": 90,
                    "category": "Physical",
                    "desc": "Has a 30% chance to flinch the target.",
                    "shortDesc": "30% chance to flinch the target.",
                    "id": "floatyfall",
                    "isNonstandard": "LGPE",
                    "isUnreleased": True,
                    "isViable": True,
                    "name": "Floaty Fall",
                    "pp": 15,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "gravity": 1
                    },
                    "secondary": {
                        "chance": 30,
                        "volatileStatus": "flinch"
                    },
                    "target": "normal",
                    "type": "Flying",
                    "contestType": "Cool"
                },
                "floralhealing": {
                    "num": 666,
                    "accuracy": True,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "The target restores 1/2 of its maximum HP, rounded half up. If the terrain is Grassy Terrain, the target instead restores 2/3 of its maximum HP, rounded half down.",
                    "shortDesc": "Heals the target by 50% of its max HP.",
                    "id": "floralhealing",
                    "name": "Floral Healing",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "reflectable": 1,
                        "heal": 1,
                        "mystery": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Fairy",
                    "zMoveEffect": "clearnegativeboost",
                    "contestType": "Beautiful"
                },
                "flowershield": {
                    "num": 579,
                    "accuracy": True,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "Raises the Defense of all active Grass-type Pokemon by 1 stage. Fails if there are no active Grass-type Pokemon.",
                    "shortDesc": "Raises Defense by 1 of all active Grass types.",
                    "id": "flowershield",
                    "name": "Flower Shield",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "distance": 1
                    },
                    "secondary": None,
                    "target": "all",
                    "type": "Fairy",
                    "zMoveBoost": {
                        "def": 1
                    },
                    "contestType": "Beautiful"
                },
                "fly": {
                    "num": 19,
                    "accuracy": 95,
                    "basePower": 90,
                    "category": "Physical",
                    "desc": "This attack charges on the first turn and executes on the second. On the first turn, the user avoids all attacks other than Gust, Hurricane, Sky Uppercut, Smack Down, Thousand Arrows, Thunder, and Twister, and Gust and Twister have doubled power when used against it. If the user is holding a Power Herb, the move completes in one turn.",
                    "shortDesc": "Flies up on first turn, then strikes the next turn.",
                    "id": "fly",
                    "name": "Fly",
                    "pp": 15,
                    "priority": 0,
                    "secondary": None,
                    "target": "any",
                    "type": "Flying",
                    "zMovePower": 175,
                    "contestType": "Clever"
                },
                "flyingpress": {
                    "num": 560,
                    "accuracy": 95,
                    "basePower": 100,
                    "category": "Physical",
                    "desc": "This move combines Flying in its type effectiveness against the target. Damage doubles and no 'accuracy' check is done if the target has used Minimize while active.",
                    "shortDesc": "Combines Flying in its type effectiveness.",
                    "id": "flyingpress",
                    "name": "Flying Press",
                    "pp": 10,
                    "priority": 0,
                    "secondary": None,
                    "target": "any",
                    "type": "Fighting",
                    "zMovePower": 170,
                    "contestType": "Tough"
                },
                "focusblast": {
                    "num": 411,
                    "accuracy": 70,
                    "basePower": 120,
                    "category": "Special",
                    "desc": "Has a 10% chance to lower the target's Special Defense by 1 stage.",
                    "shortDesc": "10% chance to lower the target's Sp. Def by 1.",
                    "id": "focusblast",
                    "isViable": True,
                    "name": "Focus Blast",
                    "pp": 5,
                    "priority": 0,
                    "flags": {
                        "bullet": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": {
                        "chance": 10,
                        "boosts": {
                            "spd": -1
                        },
                    },
                    "target": "normal",
                    "type": "Fighting",
                    "zMovePower": 190,
                    "contestType": "Cool"
                },
                "focusenergy": {
                    "num": 116,
                    "accuracy": True,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "Raises the user's chance for a critical hit by 2 stages. Fails if the user already has the effect. Baton Pass can be used to transfer this effect to an ally.",
                    "shortDesc": "Raises the user's critical hit ratio by 2.",
                    "id": "focusenergy",
                    "name": "Focus Energy",
                    "pp": 30,
                    "priority": 0,
                    "flags": {
                        "snatch": 1
                    },
                    "volatileStatus": "focusenergy",
                    "secondary": None,
                    "target": "self",
                    "type": "Normal",
                    "zMoveBoost": {
                        "accuracy": 1
                    },
                    "contestType": "Cool"
                },
                "focuspunch": {
                    "num": 264,
                    "accuracy": 100,
                    "basePower": 150,
                    "category": "Physical",
                    "desc": "The user loses its focus and does nothing if it is hit by a damaging attack this turn before it can execute the move.",
                    "shortDesc": "Fails if the user takes damage before it hits.",
                    "id": "focuspunch",
                    "isViable": True,
                    "name": "Focus Punch",
                    "pp": 20,
                    "priority": -3,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "powder": 1
                    },
                    "secondary": None,
                    "target": "normal",
                    "type": "Fighting",
                    "zMovePower": 200,
                    "contestType": "Tough"
                },
                "followme": {
                    "num": 266,
                    "accuracy": True,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "Until the end of the turn, all single-target attacks from the opposing side are redirected to the user. Such attacks are redirected to the user before they can be reflected by Magic Coat or the Magic Bounce Ability, or drawn in by the Lightning Rod or Storm drain Abilities. Fails if it is not a Double Battle or Battle Royal. This effect is ignored while the user is under the effect of Sky Drop.",
                    "shortDesc": "The foes moves target the user on the turn used.",
                    "id": "followme",
                    "name": "Follow Me",
                    "pp": 20,
                    "priority": 2,
                    "flags": {},
                    "volatileStatus": "followme",
                    "secondary": None,
                    "target": "self",
                    "type": "Normal",
                    "zMoveEffect": "clearnegativeboost",
                    "contestType": "Cute"
                },
                "forcepalm": {
                    "num": 395,
                    "accuracy": 100,
                    "basePower": 60,
                    "category": "Physical",
                    "desc": "Has a 30% chance to paralyze the target.",
                    "shortDesc": "30% chance to paralyze the target.",
                    "id": "forcepalm",
                    "name": "Force Palm",
                    "pp": 10,
                    "priority": 0,
                    "flags": {
                        "contact": 1,
                        "protect": 1,
                        "mirror": 1
                    },
                    "secondary": {
                        "chance": 30,
                        "status": "par",
                    },
                    "target": "normal",
                    "type": "Fighting",
                    "zMovePower": 120,
                    "contestType": "Cool"
                },
                "foresight": {
                    "num": 193,
                    "accuracy": True,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "As long as the target remains active, its evasiveness stat stage is ignored during 'accuracy' checks against it if it is greater than 0, and Normal- and Fighting-type attacks can hit the target if it is a Ghost type. Fails if the target is already affected, or affected by Miracle Eye or Odor Sleuth.",
                    "shortDesc": "Fighting, Normal hit Ghost. Evasiveness ignored.",
                    "id": "foresight",
                    "name": "Foresight",
                    "pp": 40,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "reflectable": 1,
                        "mirror": 1,
                        "authentic": 1
                    },
                    "volatileStatus": "foresight",
                    "secondary": None,
                    "target": "normal",
                    "type": "Normal",
                    "zMoveEffect": "crit2",
                    "contestType": "Clever"
                },
                "forestscurse": {
                    "num": 571,
                    "accuracy": 100,
                    "basePower": 0,
                    "category": "Status",
                    "desc": "Causes the Grass type to be added to the target, effectively making it have two or three types. Fails if the target is already a Grass type. If Trick-or-Treat adds a type to the target, it replaces the type added by this move and vice versa.",
                    "shortDesc": "Adds Grass to the target's type(s).",
                    "id": "forestscurse",
                    "name": "Forest's Curse",
                    "pp": 20,
                    "priority": 0,
                    "flags": {
                        "protect": 1,
                        "reflectable": 1,
                        "mirror": 1,
                        "mystery": 1
                    },
                },
                    "foulplay": {
                        "num": 492,
                        "accuracy": 100,
                        "basePower": 95,
                        "category": "Physical",
                        "desc": "Damage is calculated using the target's Attack stat, including stat stage changes. The user's Ability, item, and burn are used as normal.",
                        "shortDesc": "Uses target's Attack stat in damage calculation.",
                        "id": "foulplay",
                        "isViable": True,
                        "name": "Foul Play",
                        "pp": 15,
                        "priority": 0,
                        "flags": {
                            "contact": 1,
                            "protect": 1,
                            "mirror": 1
                        },
                        "useTargetOffensive": True,
                        "secondary": None,
                        "target": "normal",
                        "type": "Dark",
                        "zMovePower": 175,
                        "contestType": "Clever"
                    },
                    "freezedry": {
                        "num": 573,
                        "accuracy": 100,
                        "basePower": 70,
                        "category": "Special",
                        "desc": "Has a 10% chance to freeze the target. This move's type effectiveness against Water is changed to be super effective no matter what this move's type is.",
                        "shortDesc": "10% chance to freeze. Super effective on Water.",
                        "id": "freezedry",
                        "isViable": True,
                        "name": "Freeze-Dry",
                        "pp": 20,
                        "priority": 0,
                        "flags": {
                            "protect": 1,
                            "mirror": 1
                        },
                        "secondary": {
                            "chance": 10,
                            "status": "frz",
                        },
                        "target": "normal",
                        "type": "Ice",
                        "zMovePower": 140,
                        "contestType": "Beautiful"
                    },
                    "freezeshock": {
                        "num": 553,
                        "accuracy": 90,
                        "basePower": 140,
                        "category": "Physical",
                        "desc": "Has a 30% chance to paralyze the target. This attack charges on the first turn and executes on the second. If the user is holding a Power Herb, the move completes in one turn.",
                        "shortDesc": "Charges turn 1. Hits turn 2. 30% paralyze.",
                        "id": "freezeshock",
                        "name": "Freeze Shock",
                        "pp": 5,
                        "priority": 0,
                        "flags": {
                            "charge": 1,
                            "protect": 1,
                            "mirror": 1
                        },
                        "secondary": {
                            "chance": 30,
                            "status": "par",
                        },
                        "target": "normal",
                        "type": "Ice",
                        "zMovePower": 200,
                        "contestType": "Beautiful"
                    },
                    "freezyfrost": {
                        "num": 739,
                        "accuracy": 100,
                        "basePower": 90,
                        "category": "Special",
                        "desc": "Resets the stat stages of all active Pokemon to 0.",
                        "shortDesc": "Eliminates all stat changes.",
                        "id": "freezyfrost",
                        "isNonstandard": "LGPE",
                        "isUnreleased": True,
                        "isViable": True,
                        "name": "Freezy Frost",
                        "pp": 15,
                        "priority": 0,
                        "flags": {
                            "protect": 1
                        },
                        "secondary": None,
                        "target": "normal",
                        "type": "Ice",
                        "contestType": "Clever"
                    },
                    "frenzyplant": {
                        "num": 338,
                        "accuracy": 90,
                        "basePower": 150,
                        "category": "Special",
                        "desc": "If this move is successful, the user must recharge on the following turn and cannot select a move.",
                        "shortDesc": "User cannot move next turn.",
                        "id": "frenzyplant",
                        "name": "Frenzy Plant",
                        "pp": 5,
                        "priority": 0,
                        "flags": {
                            "recharge": 1,
                            "protect": 1,
                            "mirror": 1,
                            "nonsky": 1
                        },
                        "self": {
                            "volatileStatus": "mustrecharge",
                        },
                        "secondary": None,
                        "target": "normal",
                        "type": "Grass",
                        "zMovePower": 200,
                        "contestType": "Cool"
                    },
                    "frostbreath": {
                        "num": 524,
                        "accuracy": 90,
                        "basePower": 60,
                        "category": "Special",
                        "desc": "This move is always a critical hit unless the target is under the effect of Lucky Chant or has the Battle Armor or Shell Armor Abilities.",
                        "shortDesc": "Always results in a critical hit.",
                        "id": "frostbreath",
                        "name": "Frost Breath",
                        "pp": 10,
                        "priority": 0,
                        "flags": {
                            "protect": 1,
                            "mirror": 1
                        },
                        "willCrit": True,
                        "secondary": None,
                        "target": "normal",
                        "type": "Ice",
                        "zMovePower": 120,
                        "contestType": "Beautiful"
                    },
                    "frustration": {
                        "num": 218,
                        "accuracy": 100,
                        "basePower": 0,
                        "category": "Physical",
                        "desc": "Power is equal to the greater of ((255 - user's Happiness) * 2/5), rounded down, or 1.",
                        "shortDesc": "Max 102 power at minimum Happiness.",
                        "id": "frustration",
                        "isViable": True,
                        "name": "Frustration",
                        "pp": 20,
                        "priority": 0,
                        "flags": {
                            "contact": 1,
                            "protect": 1,
                            "mirror": 1
                        },
                        "secondary": None,
                        "target": "normal",
                        "type": "Normal",
                        "zMovePower": 160,
                        "contestType": "Cute"
                    },
                    "furyattack": {
                        "num": 31,
                        "accuracy": 85,
                        "basePower": 15,
                        "category": "Physical",
                        "desc": "Hits two to five times. Has a 1/3 chance to hit two or three times, and a 1/6 chance to hit four or five times. If one of the hits breaks the target's substitute, it will take damage for the remaining hits. If the user has the Skill Link Ability, this move will always hit five times.",
                        "shortDesc": "Hits 2-5 times in one turn.",
                        "id": "furyattack",
                        "name": "Fury Attack",
                        "pp": 20,
                        "priority": 0,
                        "flags": {
                            "contact": 1,
                            "protect": 1,
                            "mirror": 1
                        },
                        "multihit": [
                            2,
                            5
                        ],
                        "secondary": None,
                        "target": "normal",
                        "type": "Normal",
                        "zMovePower": 100,
                        "contestType": "Cool"
                    },
                    "furycutter": {
                        "num": 210,
                        "accuracy": 95,
                        "basePower": 40,
                        "category": "Physical",
                        "desc": "Power doubles with each successful hit, up to a maximum of 160 power. The power is reset if this move misses or another move is used.",
                        "shortDesc": "Power doubles with each hit, up to 160.",
                        "id": "furycutter",
                        "name": "Fury Cutter",
                        "pp": 20,
                        "priority": 0,
                        "flags": {
                            "contact": 1,
                            "protect": 1,
                            "mirror": 1
                        },
                        "secondary": None,
                        "target": "normal",
                        "type": "Bug",
                        "zMovePower": 100,
                        "contestType": "Cool"
                    },
                    "furyswipes": {
                        "num": 154,
                        "accuracy": 80,
                        "basePower": 18,
                        "category": "Physical",
                        "desc": "Hits two to five times. Has a 1/3 chance to hit two or three times, and a 1/6 chance to hit four or five times. If one of the hits breaks the target's substitute, it will take damage for the remaining hits. If the user has the Skill Link Ability, this move will always hit five times.",
                        "shortDesc": "Hits 2-5 times in one turn.",
                        "id": "furyswipes",
                        "name": "Fury Swipes",
                        "pp": 15,
                        "priority": 0,
                        "flags": {
                            "contact": 1,
                            "protect": 1,
                            "mirror": 1
                        },
                        "multihit": [
                            2,
                            5
                        ],
                        "secondary": None,
                        "target": "normal",
                        "type": "Normal",
                        "zMovePower": 100,
                        "contestType": "Tough"
                    },
                    "fusionbolt": {
                        "num": 559,
                        "accuracy": 100,
                        "basePower": 100,
                        "category": "Physical",
                        "desc": "Power doubles if the last move used by any Pokemon this turn was Fusion Flare.",
                        "shortDesc": "Power doubles if used after Fusion Flare.",
                        "id": "fusionbolt",
                        "isViable": True,
                        "name": "Fusion Bolt",
                        "pp": 5,
                        "priority": 0,
                        "flags": {
                            "protect": 1,
                            "mirror": 1
                        },
                        "secondary": None,
                        "target": "normal",
                        "type": "Electric",
                        "zMovePower": 180,
                        "contestType": "Cool"
                    },
                    "fusionflare": {
                        "num": 558,
                        "accuracy": 100,
                        "basePower": 100,
                        "category": "Special",
                        "desc": "Power doubles if the last move used by any Pokemon this turn was Fusion Bolt.",
                        "shortDesc": "Power doubles if used after Fusion Bolt.",
                        "id": "fusionflare",
                        "isViable": True,
                        "name": "Fusion Flare",
                        "pp": 5,
                        "priority": 0,
                        "flags": {
                            "protect": 1,
                            "mirror": 1,
                            "defrost": 1
                        },
                        "secondary": None,
                        "target": "normal",
                        "type": "Fire",
                        "zMovePower": 180,
                        "contestType": "Beautiful"
                    },
                    "futuresight": {
                        "num": 248,
                        "accuracy": 100,
                        "basePower": 120,
                        "category": "Special",
                        "desc": "Deals damage two turns after this move is used. At the end of that turn, the damage is calculated at that time and dealt to the Pokemon at the position the target had when the move was used. If the user is no longer active at the time, damage is calculated based on the user's natural Special Attack stat, types, and level, with no boosts from its held item or Ability. Fails if this move or Doom Desire is already in effect for the target's position.",
                        "shortDesc": "Hits two turns after being used.",
                        "id": "futuresight",
                        "name": "Future Sight",
                        "pp": 10,
                        "priority": 0,
                        "flags": {},
                        "ignoreImmunity": True,
                        "isFutureMove": True,
                        "secondary": None,
                        "target": "normal",
                        "type": "Psychic",
                        "zMovePower": 190,
                        "contestType": "Clever"
                    },
                    "gastroacid": {
                        "num": 380,
                        "accuracy": 100,
                        "basePower": 0,
                        "category": "Status",
                        "desc": "Causes the target's Ability to be rendered ineffective as long as it remains active. If the target uses Baton Pass, the replacement will remain under this effect. If the target's Ability is Battle Bond, Comatose, Disguise, Multitype, Power Construct, RKS System, Schooling, Shields Down, Stance Change, or Zen Mode, this move fails, and receiving the effect through Baton Pass ends the effect immediately.",
                        "shortDesc": "Noneifies the target's Ability.",
                        "id": "gastroacid",
                        "name": "Gastro Acid",
                        "pp": 10,
                        "priority": 0,
                        "flags": {
                            "protect": 1,
                            "reflectable": 1,
                            "mirror": 1,
                            "mystery": 1
                        },
                        "volatileStatus": "gastroacid",
                        "secondary": None,
                        "target": "normal",
                        "type": "Poison",
                        "zMoveBoost": {
                            "spe": 1
                        },
                        "contestType": "Tough"
                    },
                    "geargrind": {
                        "num": 544,
                        "accuracy": 85,
                        "basePower": 50,
                        "category": "Physical",
                        "desc": "Hits twice. If the first hit breaks the target's substitute, it will take damage for the second hit.",
                        "shortDesc": "Hits 2 times in one turn.",
                        "id": "geargrind",
                        "isViable": True,
                        "name": "Gear Grind",
                        "pp": 15,
                        "priority": 0,
                        "flags": {
                            "contact": 1,
                            "protect": 1,
                            "mirror": 1
                        },
                        "multihit": 2,
                        "secondary": None,
                        "target": "normal",
                        "type": "Steel",
                        "zMovePower": 180,
                        "contestType": "Clever"
                    },
                    "gearup": {
                        "num": 674,
                        "accuracy": True,
                        "basePower": 0,
                        "category": "Status",
                        "desc": "Raises the Attack and Special Attack of Pokemon on the user's side with the Plus or Minus Abilities by 1 stage.",
                        "shortDesc": "Raises Atk, Sp. Atk of allies with Plus/Minus by 1.",
                        "id": "gearup",
                        "name": "Gear Up",
                        "pp": 20,
                        "priority": 0,
                        "flags": {
                            "snatch": 1,
                            "authentic": 1
                        },
                        "secondary": None,
                        "target": "allySide",
                        "type": "Steel",
                        "zMoveBoost": {
                            "spa": 1
                        },
                        "contestType": "Clever"
                    },
                    "genesissupernova": {
                        "num": 703,
                        "accuracy": True,
                        "basePower": 185,
                        "category": "Special",
                        "desc": "If this move is successful, the terrain becomes Psychic Terrain.",
                        "shortDesc": "Summons Psychic Terrain.",
                        "id": "genesissupernova",
                        "name": "Genesis Supernova",
                        "pp": 1,
                        "priority": 0,
                        "flags": {},
                        "isZ": "mewniumz",
                        "secondary": {
                            "chance": 100
                        },
                        "target": "normal",
                        "type": "Psychic",
                        "contestType": "Cool"
                    },
                    "geomancy": {
                        "num": 601,
                        "accuracy": True,
                        "basePower": 0,
                        "category": "Status",
                        "desc": "Raises the user's Special Attack, Special Defense, and Speed by 2 stages. This attack charges on the first turn and executes on the second. If the user is holding a Power Herb, the move completes in one turn.",
                        "shortDesc": "Charges, then raises SpA, SpD, Spe by 2 turn 2.",
                        "id": "geomancy",
                        "isViable": True,
                        "name": "Geomancy",
                        "pp": 10,
                        "priority": 0,
                        "flags": {
                            "charge": 1,
                            "nonsky": 1
                        },
                        "boosts": {
                            "spa": 2,
                            "spd": 2,
                            "spe": 2
                        },
                        "secondary": None,
                        "target": "self",
                        "type": "Fairy",
                        "zMoveBoost": {
                            "atk": 1,
                            "def": 1,
                            "spa": 1,
                            "spd": 1,
                            "spe": 1
                        },
                        "contestType": "Beautiful"
                    },
                    "gigadrain": {
                        "num": 202,
                        "accuracy": 100,
                        "basePower": 75,
                        "category": "Special",
                        "desc": "The user recovers 1/2 the HP lost by the target, rounded half up. If Big Root is held by the user, the HP recovered is 1.3x normal, rounded half down.",
                        "shortDesc": "User recovers 50% of the damage dealt.",
                        "id": "gigadrain",
                        "isViable": True,
                        "name": "Giga Drain",
                        "pp": 10,
                        "priority": 0,
                        "flags": {
                            "protect": 1,
                            "mirror": 1,
                            "heal": 1
                        },
                        "drain": [
                            1,
                            2
                        ],
                        "secondary": None,
                        "target": "normal",
                        "type": "Grass",
                        "zMovePower": 140,
                        "contestType": "Clever"
                    },
                    "gigaimpact": {
                        "num": 416,
                        "accuracy": 90,
                        "basePower": 150,
                        "category": "Physical",
                        "desc": "If this move is successful, the user must recharge on the following turn and cannot select a move.",
                        "shortDesc": "User cannot move next turn.",
                        "id": "gigaimpact",
                        "name": "Giga Impact",
                        "pp": 5,
                        "priority": 0,
                        "flags": {
                            "contact": 1,
                            "recharge": 1,
                            "protect": 1,
                            "mirror": 1
                        },
                        "self": {
                            "volatileStatus": "mustrecharge",
                        },
                        "secondary": None,
                        "target": "normal",
                        "type": "Normal",
                        "zMovePower": 200,
                        "contestType": "Tough"
                    },
                    "gigavolthavoc": {
                        "num": 646,
                        "accuracy": True,
                        "basePower": 1,
                        "category": "Physical",
                        "shortDesc": "Power is equal to the base move's Z-Power.",
                        "id": "gigavolthavoc",
                        "isViable": True,
                        "name": "Gigavolt Havoc",
                        "pp": 1,
                        "priority": 0,
                        "flags": {},
                        "isZ": "electriumz",
                        "secondary": None,
                        "target": "normal",
                        "type": "Electric",
                        "contestType": "Cool"
                    },
                    "glaciate": {
                        "num": 549,
                        "accuracy": 95,
                        "basePower": 65,
                        "category": "Special",
                        "desc": "Has a 100% chance to lower the target's Speed by 1 stage.",
                        "shortDesc": "100% chance to lower the foe(s) Speed by 1.",
                        "id": "glaciate",
                        "name": "Glaciate",
                        "pp": 10,
                        "priority": 0,
                        "flags": {
                            "protect": 1,
                            "mirror": 1
                        },
                        "secondary": {
                            "chance": 100,
                            "boosts": {
                                "spe": -1,
                            },
                        },
                        "target": "allAdjacentFoes",
                        "type": "Ice",
                        "zMovePower": 120,
                        "contestType": "Beautiful"
                    },
                    "glare": {
                        "num": 137,
                        "accuracy": 100,
                        "basePower": 0,
                        "category": "Status",
                        "desc": "Paralyzes the target.",
                        "shortDesc": "Paralyzes the target.",
                        "id": "glare",
                        "isViable": True,
                        "name": "Glare",
                        "pp": 30,
                        "priority": 0,
                        "flags": {
                            "protect": 1,
                            "reflectable": 1,
                            "mirror": 1
                        },
                        "status": "par",
                        "secondary": None,
                        "target": "normal",
                        "type": "Normal",
                        "zMoveBoost": {
                            "spd": 1
                        },
                        "contestType": "Tough"
                    },
                    "glitzyglow": {
                        "num": 736,
                        "accuracy": 100,
                        "basePower": 90,
                        "category": "Special",
                        "desc": "This move summons Light Screen for 5 turns upon use.",
                        "shortDesc": "Summons Light Screen.",
                        "id": "glitzyglow",
                        "isNonstandard": "LGPE",
                        "isUnreleased": True,
                        "isViable": True,
                        "name": "Glitzy Glow",
                        "pp": 15,
                        "priority": 0,
                        "flags": {
                            "protect": 1
                        },
                        "self": {
                            "sideCondition": "lightscreen",
                        },
                        "secondary": None,
                        "target": "normal",
                        "type": "Psychic",
                        "contestType": "Clever"
                    },
                    "grassknot": {
                        "num": 447,
                        "accuracy": 100,
                        "basePower": 0,
                        "category": "Special",
                        "desc": "This move's power is 20 if the target weighs less than 10 kg, 40 if less than 25 kg, 60 if less than 50 kg, 80 if less than 100 kg, 100 if less than 200 kg, and 120 if greater than or equal to 200 kg.",
                        "shortDesc": "More power the heavier the target.",
                        "id": "grassknot",
                        "isViable": True,
                        "name": "Grass Knot",
                        "pp": 20,
                        "priority": 0,
                        "flags": {
                            "contact": 1,
                            "protect": 1,
                            "mirror": 1,
                            "nonsky": 1
                        },
                        "secondary": None,
                        "target": "normal",
                        "type": "Grass",
                        "zMovePower": 160,
                        "contestType": "Cute"
                    },
                    "grasspledge": {
                        "num": 520,
                        "accuracy": 100,
                        "basePower": 80,
                        "category": "Special",
                        "desc": "If one of the user's allies chose to use Fire Pledge or Water Pledge this turn and has not moved yet, it takes its turn immediately after the user and the user's move does nothing. If combined with Fire Pledge, the ally uses Fire Pledge with 150 power and a sea of fire appears on the target's side for 4 turns, which causes damage to non-Fire types equal to 1/8 of their maximum HP, rounded down, at the end of each turn during effect, including the last turn. If combined with Water Pledge, the ally uses Grass Pledge with 150 power and a swamp appears on the target's side for 4 turns, which quarters the Speed of each Pokemon on that side. When used as a combined move, this move gains STAB no matter what the user's type is. This move does not consume the user's Grass Gem.",
                        "shortDesc": "Use with Fire or Water Pledge for added effect.",
                        "id": "grasspledge",
                        "name": "Grass Pledge",
                        "pp": 10,
                        "priority": 0,
                        "flags": {
                            "protect": 1,
                            "mirror": 1,
                            "nonsky": 1
                        },
                        "secondary": None,
                        "target": "normal",
                        "type": "Grass",
                        "zMovePower": 160,
                        "contestType": "Beautiful"
                    },
                    "grasswhistle": {
                        "num": 320,
                        "accuracy": 55,
                        "basePower": 0,
                        "category": "Status",
                        "shortDesc": "Causes the target to fall asleep.",
                        "id": "grasswhistle",
                        "name": "Grass Whistle",
                        "pp": 15,
                        "priority": 0,
                        "flags": {
                            "protect": 1,
                            "reflectable": 1,
                            "mirror": 1,
                            "sound": 1,
                            "authentic": 1
                        },
                        "status": "slp",
                        "secondary": None,
                        "target": "normal",
                        "type": "Grass",
                        "zMoveBoost": {
                            "spe": 1
                        },
                        "contestType": "Clever"
                    },
                    "grassyterrain": {
                        "num": 580,
                        "accuracy": True,
                        "basePower": 0,
                        "category": "Status",
                        "desc": "For 5 turns, the terrain becomes Grassy Terrain. During the effect, the power of Grass-type attacks used by grounded Pokemon is multiplied by 1.5, the power of Bulldoze, Earthquake, and Magnitude used against grounded Pokemon is multiplied by 0.5, and grounded Pokemon have 1/16 of their maximum HP, rounded down, restored at the end of each turn, including the last turn. Camouflage transforms the user into a Grass type, Nature Power becomes Energy Ball, and Secret Power has a 30% chance to cause sleep. Fails if the current terrain is Grassy Terrain.",
                        "shortDesc": "5 turns. Grounded: +Grass power, +1/16 max HP.",
                        "id": "grassyterrain",
                        "name": "Grassy Terrain",
                        "pp": 10,
                        "priority": 0,
                        "flags": {
                            "nonsky": 1
                        },
                        "terrain": "grassyterrain",
                        "secondary": None,
                        "target": "all",
                        "type": "Grass",
                        "zMoveBoost": {
                            "def": 1
                        },
                        "contestType": "Beautiful"
                    },
                    "gravity": {
                        "num": 356,
                        "accuracy": True,
                        "basePower": 0,
                        "category": "Status",
                        "desc": "For 5 turns, the evasiveness of all active Pokemon is multiplied by 0.6. At the time of use, Bounce, Fly, Magnet Rise, Sky Drop, and Telekinesis end immediately for all active Pokemon. During the effect, Bounce, Fly, Flying Press, High Jump Kick, Jump Kick, Magnet Rise, Sky Drop, Splash, and Telekinesis are prevented from being used by all active Pokemon. Ground-type attacks, Spikes, Toxic Spikes, Sticky Web, and the Arena Trap Ability can affect Flying types or Pokemon with the Levitate Ability. Fails if this move is already in effect.",
                        "shortDesc": "For 5 turns, negates all Ground immunities.",
                        "id": "gravity",
                        "name": "Gravity",
                        "pp": 5,
                        "priority": 0,
                        "flags": {
                            "nonsky": 1
                        },
                        "pseudoWeather": "gravity",
                        "secondary": None,
                        "target": "all",
                        "type": "Psychic",
                        "zMoveBoost": {
                            "spa": 1
                        },
                        "contestType": "Clever"
                    },
                    "growl": {
                        "num": 45,
                        "accuracy": 100,
                        "basePower": 0,
                        "category": "Status",
                        "desc": "Lowers the target's Attack by 1 stage.",
                        "shortDesc": "Lowers the foe(s) Attack by 1.",
                        "id": "growl",
                        "name": "Growl",
                        "pp": 40,
                        "priority": 0,
                        "flags": {
                            "protect": 1,
                            "reflectable": 1,
                            "mirror": 1,
                            "sound": 1,
                            "authentic": 1
                        },
                        "boosts": {
                            "atk": -1
                        },
                        "secondary": None,
                        "target": "allAdjacentFoes",
                        "type": "Normal",
                        "zMoveBoost": {
                            "def": 1
                        },
                        "contestType": "Cute"
                    },
                    "growth": {
                        "num": 74,
                        "accuracy": True,
                        "basePower": 0,
                        "category": "Status",
                        "desc": "Raises the user's Attack and Special Attack by 1 stage. If the weather is Sunny Day, raises the user's Attack and Special Attack by 2 stages.",
                        "shortDesc": "Raises user's Attack and Sp. Atk by 1; 2 in Sun.",
                        "id": "growth",
                        "name": "Growth",
                        "pp": 20,
                        "priority": 0,
                        "flags": {
                            "snatch": 1
                        },
                        "boosts": {
                            "atk": 1,
                            "spa": 1,
                        },
                        "secondary": None,
                        "target": "self",
                        "type": "Normal",
                        "zMoveBoost": {
                            "spa": 1
                        },
                        "contestType": "Beautiful"
                    },
                    "grudge": {
                        "num": 288,
                        "accuracy": True,
                        "basePower": 0,
                        "category": "Status",
                        "desc": "Until the user's next turn, if an opposing Pokemon's attack knocks the user out, that move loses all its remaining PP.",
                        "shortDesc": "If the user faints, the attack used loses all its PP.",
                        "id": "grudge",
                        "name": "Grudge",
                        "pp": 5,
                        "priority": 0,
                        "flags": {
                            "authentic": 1
                        },
                        "volatileStatus": "grudge",
                        "secondary": None,
                        "target": "self",
                        "type": "Ghost",
                        "zMoveEffect": "redirect",
                        "contestType": "Tough"
                    },
                    "guardianofalola": {
                        "num": 698,
                        "accuracy": True,
                        "basePower": 0,
                        "category": "Special",
                        "desc": "Deals damage to the target equal to 3/4 of its current HP, rounded down, but not less than 1 HP.",
                        "shortDesc": "Does damage equal to 3/4 target's current HP.",
                        "id": "guardianofalola",
                        "name": "Guardian of Alola",
                        "pp": 1,
                        "priority": 0,
                        "flags": {},
                        "isZ": "tapuniumz",
                        "secondary": None,
                        "target": "normal",
                        "type": "Fairy",
                        "contestType": "Tough"
                    },
                    "guardsplit": {
                        "num": 470,
                        "accuracy": True,
                        "basePower": 0,
                        "category": "Status",
                        "desc": "The user and the target have their Defense and Special Defense stats set to be equal to the average of the user and the target's Defense and Special Defense stats, respectively, rounded down. Stat stage changes are unaffected.",
                        "shortDesc": "Averages Defense and Sp. Def stats with target.",
                        "id": "guardsplit",
                        "name": "Guard Split",
                        "pp": 10,
                        "priority": 0,
                        "flags": {
                            "protect": 1,
                            "mystery": 1
                        },
                    },
                    "guardswap": {
                            "num": 385,
                            "accuracy": True,
                            "basePower": 0,
                            "category": "Status",
                            "desc": "The user swaps its Defense and Special Defense stat stage changes with the target.",
                            "shortDesc": "Swaps Defense and Sp. Def changes with target.",
                            "id": "guardswap",
                            "name": "Guard Swap",
                            "pp": 10,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1,
                                "authentic": 1,
                                "mystery": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Psychic",
                            "zMoveBoost": {
                                "spe": 1
                            },
                            "contestType": "Clever"
                        },
                        "guillotine": {
                            "num": 12,
                            "accuracy": 30,
                            "basePower": 0,
                            "category": "Physical",
                            "desc": "Deals damage to the target equal to the target's maximum HP. Ignores 'accuracy' and evasiveness modifiers. This attack's 'accuracy' is equal to(user 's level - target's level + 30) % , and fails if the target is at a higher level.Pokemon with the Sturdy Ability are immune.",
                            "shortDesc": "OHKOs the target. Fails if user is a lower level.",
                            "id": "guillotine",
                            "name": "Guillotine",
                            "pp": 5,
                            "priority": 0,
                            "flags": {
                                "contact": 1,
                                "protect": 1,
                                "mirror": 1
                            },
                            "ohko": True,
                            "secondary": None,
                            "target": "normal",
                            "type": "Normal",
                            "zMovePower": 180,
                            "contestType": "Cool"
                        },
                        "gunkshot": {
                            "num": 441,
                            "accuracy": 80,
                            "basePower": 120,
                            "category": "Physical",
                            "desc": "Has a 30% chance to poison the target.",
                            "shortDesc": "30% chance to poison the target.",
                            "id": "gunkshot",
                            "isViable": True,
                            "name": "Gunk Shot",
                            "pp": 5,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": {
                                "chance": 30,
                                "status": "psn",
                            },
                            "target": "normal",
                            "type": "Poison",
                            "zMovePower": 190,
                            "contestType": "Tough"
                        },
                        "gust": {
                            "num": 16,
                            "accuracy": 100,
                            "basePower": 40,
                            "category": "Special",
                            "desc": "Power doubles if the target is using Bounce, Fly, or Sky Drop, or is under the effect of Sky Drop.",
                            "shortDesc": "Power doubles during Bounce, Fly, and Sky Drop.",
                            "id": "gust",
                            "name": "Gust",
                            "pp": 35,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1,
                                "distance": 1
                            },
                            "secondary": None,
                            "target": "any",
                            "type": "Flying",
                            "zMovePower": 100,
                            "contestType": "Clever"
                        },
                        "gyroball": {
                            "num": 360,
                            "accuracy": 100,
                            "basePower": 0,
                            "category": "Physical",
                            "desc": "Power is equal to (25 * target's current Speed / user's current Speed) + 1, rounded down, but not more than 150. If the user's current Speed is 0, this move's power is 1.",
                            "shortDesc": "More power the slower the user than the target.",
                            "id": "gyroball",
                            "isViable": True,
                            "name": "Gyro Ball",
                            "pp": 5,
                            "priority": 0,
                            "flags": {
                                "bullet": 1,
                                "contact": 1,
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Steel",
                            "zMovePower": 160,
                            "contestType": "Cool"
                        },
                        "hail": {
                            "num": 258,
                            "accuracy": True,
                            "basePower": 0,
                            "category": "Status",
                            "desc": "For 5 turns, the weather becomes Hail. At the end of each turn except the last, all active Pokemon lose 1/16 of their maximum HP, rounded down, unless they are an Ice type or have the Ice Body, Magic Guard, Overcoat, or Snow Cloak Abilities. Lasts for 8 turns if the user is holding Icy Rock. Fails if the current weather is Hail.",
                            "shortDesc": "For 5 turns, hail crashes down.",
                            "id": "hail",
                            "name": "Hail",
                            "pp": 10,
                            "priority": 0,
                            "flags": {},
                            "weather": "hail",
                            "secondary": None,
                            "target": "all",
                            "type": "Ice",
                            "zMoveBoost": {
                                "spe": 1
                            },
                            "contestType": "Beautiful"
                        },
                        "hammerarm": {
                            "num": 359,
                            "accuracy": 90,
                            "basePower": 100,
                            "category": "Physical",
                            "desc": "Lowers the user's Speed by 1 stage.",
                            "shortDesc": "Lowers the user's Speed by 1.",
                            "id": "hammerarm",
                            "isViable": True,
                            "name": "Hammer Arm",
                            "pp": 10,
                            "priority": 0,
                            "flags": {
                                "contact": 1,
                                "protect": 1,
                                "mirror": 1,
                                "powder": 1
                            },
                            "self": {
                                "boosts": {
                                    "spe": -1,
                                },
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Fighting",
                            "zMovePower": 180,
                            "contestType": "Tough"
                        },
                        "happyhour": {
                            "num": 603,
                            "accuracy": True,
                            "basePower": 0,
                            "category": "Status",
                            "shortDesc": "No competitive use.",
                            "id": "happyhour",
                            "name": "Happy Hour",
                            "pp": 30,
                            "priority": 0,
                            "flags": {},
                            "secondary": None,
                            "target": "allySide",
                            "type": "Normal",
                            "zMoveBoost": {
                                "atk": 1,
                                "def": 1,
                                "spa": 1,
                                "spd": 1,
                                "spe": 1
                            },
                            "contestType": "Cute"
                        },
                        "harden": {
                            "num": 106,
                            "accuracy": True,
                            "basePower": 0,
                            "category": "Status",
                            "desc": "Raises the user's Defense by 1 stage.",
                            "shortDesc": "Raises the user's Defense by 1.",
                            "id": "harden",
                            "name": "Harden",
                            "pp": 30,
                            "priority": 0,
                            "flags": {
                                "snatch": 1
                            },
                            "boosts": {
                                "def": 1,
                            },
                            "secondary": None,
                            "target": "self",
                            "type": "Normal",
                            "zMoveBoost": {
                                "def": 1
                            },
                            "contestType": "Tough"
                        },
                        "haze": {
                            "num": 114,
                            "accuracy": True,
                            "basePower": 0,
                            "category": "Status",
                            "desc": "Resets the stat stages of all active Pokemon to 0.",
                            "shortDesc": "Eliminates all stat changes.",
                            "id": "haze",
                            "isViable": True,
                            "name": "Haze",
                            "pp": 30,
                            "priority": 0,
                            "flags": {
                                "authentic": 1
                            },
                            "secondary": None,
                            "target": "all",
                            "type": "Ice",
                            "zMoveEffect": "heal",
                            "contestType": "Beautiful"
                        },
                        "headbutt": {
                            "num": 29,
                            "accuracy": 100,
                            "basePower": 70,
                            "category": "Physical",
                            "desc": "Has a 30% chance to flinch the target.",
                            "shortDesc": "30% chance to flinch the target.",
                            "id": "headbutt",
                            "name": "Headbutt",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "contact": 1,
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": {
                                "chance": 30,
                                "volatileStatus": "flinch"
                            },
                            "target": "normal",
                            "type": "Normal",
                            "zMovePower": 140,
                            "contestType": "Tough"
                        },
                        "headcharge": {
                            "num": 543,
                            "accuracy": 100,
                            "basePower": 120,
                            "category": "Physical",
                            "desc": "If the target lost HP, the user takes recoil damage equal to 1/4 the HP lost by the target, rounded half up, but not less than 1 HP.",
                            "shortDesc": "Has 1/4 recoil.",
                            "id": "headcharge",
                            "isViable": True,
                            "name": "Head Charge",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "contact": 1,
                                "protect": 1,
                                "mirror": 1
                            },
                            "recoil": [
                                1,
                                4
                            ],
                            "secondary": None,
                            "target": "normal",
                            "type": "Normal",
                            "zMovePower": 190,
                            "contestType": "Tough"
                        },
                        "headsmash": {
                            "num": 457,
                            "accuracy": 80,
                            "basePower": 150,
                            "category": "Physical",
                            "desc": "If the target lost HP, the user takes recoil damage equal to 1/2 the HP lost by the target, rounded half up, but not less than 1 HP.",
                            "shortDesc": "Has 1/2 recoil.",
                            "id": "headsmash",
                            "isViable": True,
                            "name": "Head Smash",
                            "pp": 5,
                            "priority": 0,
                            "flags": {
                                "contact": 1,
                                "protect": 1,
                                "mirror": 1
                            },
                            "recoil": [
                                1,
                                2
                            ],
                            "secondary": None,
                            "target": "normal",
                            "type": "Rock",
                            "zMovePower": 200,
                            "contestType": "Tough"
                        },
                        "healbell": {
                            "num": 215,
                            "accuracy": True,
                            "basePower": 0,
                            "category": "Status",
                            "desc": "Every Pokemon in the user's party is cured of its major status condition. Active Pokemon with the Soundproof Ability are not cured.",
                            "shortDesc": "Cures the user's party of all status conditions.",
                            "id": "healbell",
                            "isViable": True,
                            "name": "Heal Bell",
                            "pp": 5,
                            "priority": 0,
                            "flags": {
                                "snatch": 1,
                                "sound": 1,
                                "distance": 1,
                                "authentic": 1
                            },
                            "target": "allyTeam",
                            "type": "Normal",
                            "zMoveEffect": "heal",
                            "contestType": "Beautiful"
                        },
                        "healblock": {
                            "num": 377,
                            "accuracy": 100,
                            "basePower": 0,
                            "category": "Status",
                            "desc": "For 5 turns, the target is prevented from restoring any HP as long as it remains active. During the effect, healing and draining moves are unusable, and Abilities and items that grant healing will not heal the user. If an affected Pokemon uses Baton Pass, the replacement will remain unable to restore its HP. Pain Split and the Regenerator Ability are unaffected.",
                            "shortDesc": "For 5 turns, the foe(s) is prevented from healing.",
                            "id": "healblock",
                            "name": "Heal Block",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "reflectable": 1,
                                "mirror": 1
                            },
                            "volatileStatus": "healblock",
                            "secondary": None,
                            "target": "allAdjacentFoes",
                            "type": "Psychic",
                            "zMoveBoost": {
                                "spa": 2
                            },
                            "contestType": "Clever"
                        },
                        "healingwish": {
                            "num": 361,
                            "accuracy": True,
                            "basePower": 0,
                            "category": "Status",
                            "desc": "The user faints and the Pokemon brought out to replace it has its HP fully restored along with having any major status condition cured. The new Pokemon is sent out at the end of the turn, and the healing happens before hazards take effect. Fails if the user is the last unfainted Pokemon in its party.",
                            "shortDesc": "User faints. Replacement is fully healed.",
                            "id": "healingwish",
                            "isViable": True,
                            "name": "Healing Wish",
                            "pp": 10,
                            "priority": 0,
                            "flags": {
                                "snatch": 1,
                                "heal": 1
                            },
                            "selfdestruct": "ifHit",
                            "slotCondition": "healingwish",
                            "secondary": None,
                            "target": "self",
                            "type": "Psychic",
                            "contestType": "Beautiful"
                        },
                        "healorder": {
                            "num": 456,
                            "accuracy": True,
                            "basePower": 0,
                            "category": "Status",
                            "desc": "The user restores 1/2 of its maximum HP, rounded half up.",
                            "shortDesc": "Heals the user by 50% of its max HP.",
                            "id": "healorder",
                            "isViable": True,
                            "name": "Heal Order",
                            "pp": 10,
                            "priority": 0,
                            "flags": {
                                "snatch": 1,
                                "heal": 1
                            },
                            "heal": [
                                1,
                                2
                            ],
                            "secondary": None,
                            "target": "self",
                            "type": "Bug",
                            "zMoveEffect": "clearnegativeboost",
                            "contestType": "Clever"
                        },
                        "healpulse": {
                            "num": 505,
                            "accuracy": True,
                            "basePower": 0,
                            "category": "Status",
                            "desc": "The target restores 1/2 of its maximum HP, rounded half up. If the user has the Mega Launcher Ability, the target instead restores 3/4 of its maximum HP, rounded half down.",
                            "shortDesc": "Heals the target by 50% of its max HP.",
                            "id": "healpulse",
                            "name": "Heal Pulse",
                            "pp": 10,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "pulse": 1,
                                "reflectable": 1,
                                "distance": 1,
                                "heal": 1,
                                "mystery": 1
                            },
                            "secondary": None,
                            "target": "any",
                            "type": "Psychic",
                            "zMoveEffect": "clearnegativeboost",
                            "contestType": "Beautiful"
                        },
                        "heartstamp": {
                            "num": 531,
                            "accuracy": 100,
                            "basePower": 60,
                            "category": "Physical",
                            "desc": "Has a 30% chance to flinch the target.",
                            "shortDesc": "30% chance to flinch the target.",
                            "id": "heartstamp",
                            "name": "Heart Stamp",
                            "pp": 25,
                            "priority": 0,
                            "flags": {
                                "contact": 1,
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": {
                                "chance": 30,
                                "volatileStatus": "flinch"
                            },
                            "target": "normal",
                            "type": "Psychic",
                            "zMovePower": 120,
                            "contestType": "Cute"
                        },
                        "heartswap": {
                            "num": 391,
                            "accuracy": True,
                            "basePower": 0,
                            "category": "Status",
                            "desc": "The user swaps all its stat stage changes with the target.",
                            "shortDesc": "Swaps all stat changes with target.",
                            "id": "heartswap",
                            "name": "Heart Swap",
                            "pp": 10,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1,
                                "authentic": 1,
                                "mystery": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Psychic",
                            "zMoveEffect": "crit2",
                            "contestType": "Clever"
                        },
                        "heatcrash": {
                            "num": 535,
                            "accuracy": 100,
                            "basePower": 0,
                            "category": "Physical",
                            "desc": "The power of this move depends on (user's weight / target's weight), rounded down. Power is equal to 120 if the result is 5 or more, 100 if 4, 80 if 3, 60 if 2, and 40 if 1 or less. Damage doubles and no 'accuracy' check is done if the target has used Minimize while active.",
                            "shortDesc": "More power the heavier the user than the target.",
                            "id": "heatcrash",
                            "name": "Heat Crash",
                            "pp": 10,
                            "priority": 0,
                            "flags": {
                                "contact": 1,
                                "protect": 1,
                                "mirror": 1,
                                "nonsky": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Fire",
                            "zMovePower": 160,
                            "contestType": "Tough"
                        },
                        "heatwave": {
                            "num": 257,
                            "accuracy": 90,
                            "basePower": 95,
                            "category": "Special",
                            "desc": "Has a 10% chance to burn the target.",
                            "shortDesc": "10% chance to burn the foe(s).",
                            "id": "heatwave",
                            "isViable": True,
                            "name": "Heat Wave",
                            "pp": 10,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": {
                                "chance": 10,
                                "status": "brn",
                            },
                            "target": "allAdjacentFoes",
                            "type": "Fire",
                            "zMovePower": 175,
                            "contestType": "Beautiful"
                        },
                        "heavyslam": {
                            "num": 484,
                            "accuracy": 100,
                            "basePower": 0,
                            "category": "Physical",
                            "desc": "The power of this move depends on (user's weight / target's weight), rounded down. Power is equal to 120 if the result is 5 or more, 100 if 4, 80 if 3, 60 if 2, and 40 if 1 or less. Damage doubles and no 'accuracy' check is done if the target has used Minimize while active.",
                            "shortDesc": "More power the heavier the user than the target.",
                            "id": "heavyslam",
                            "isViable": True,
                            "name": "Heavy Slam",
                            "pp": 10,
                            "priority": 0,
                            "flags": {
                                "contact": 1,
                                "protect": 1,
                                "mirror": 1,
                                "nonsky": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Steel",
                            "zMovePower": 160,
                            "contestType": "Tough"
                        },
                        "helpinghand": {
                            "num": 270,
                            "accuracy": True,
                            "basePower": 0,
                            "category": "Status",
                            "desc": "The power of the target's attack this turn is multiplied by 1.5 (this effect is stackable). Fails if there is no ally adjacent to the user or if the ally already moved this turn, but does not fail if the ally is using a two-turn move.",
                            "shortDesc": "One adjacent ally's move power is 1.5 x this turn.",
                            "id": "helpinghand",
                            "name": "Helping Hand",
                            "pp": 20,
                            "priority": 5,
                            "flags": {
                                "authentic": 1
                            },
                            "volatileStatus": "helpinghand",
                            "secondary": None,
                            "target": "adjacentAlly",
                            "type": "Normal",
                            "zMoveEffect": "clearnegativeboost",
                            "contestType": "Clever"
                        },
                        "hex": {
                            "num": 506,
                            "accuracy": 100,
                            "basePower": 65,
                            "category": "Special",
                            "desc": "Power doubles if the target has a major status condition.",
                            "shortDesc": "Power doubles if the target has a status ailment.",
                            "id": "hex",
                            "isViable": True,
                            "name": "Hex",
                            "pp": 10,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Ghost",
                            "zMovePower": 160,
                            "contestType": "Clever"
                        },
                        "hiddenpower": {
                            "num": 237,
                            "accuracy": 100,
                            "basePower": 60,
                            "category": "Special",
                            "desc": "This move's type depends on the user's individual values (IVs), and can be any type but Fairy and Normal.",
                            "shortDesc": "Varies in type based on the user's IVs.",
                            "id": "hiddenpower",
                            "name": "Hidden Power",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Normal",
                            "zMovePower": 120,
                            "contestType": "Clever"
                        },
                        "hiddenpowerbug": {
                            "num": 237,
                            "accuracy": 100,
                            "basePower": 60,
                            "category": "Special",
                            "desc": "",
                            "shortDesc": "",
                            "id": "hiddenpower",
                            "name": "Hidden Power Bug",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Bug",
                            "contestType": "Clever"
                        },
                        "hiddenpowerdark": {
                            "num": 237,
                            "accuracy": 100,
                            "basePower": 60,
                            "category": "Special",
                            "desc": "",
                            "shortDesc": "",
                            "id": "hiddenpower",
                            "name": "Hidden Power Dark",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Dark",
                            "contestType": "Clever"
                        },
                        "hiddenpowerdragon": {
                            "num": 237,
                            "accuracy": 100,
                            "basePower": 60,
                            "category": "Special",
                            "desc": "",
                            "shortDesc": "",
                            "id": "hiddenpower",
                            "name": "Hidden Power Dragon",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Dragon",
                            "contestType": "Clever"
                        },
                        "hiddenpowerelectric": {
                            "num": 237,
                            "accuracy": 100,
                            "basePower": 60,
                            "category": "Special",
                            "desc": "",
                            "shortDesc": "",
                            "id": "hiddenpower",
                            "isViable": True,
                            "name": "Hidden Power Electric",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Electric",
                            "contestType": "Clever"
                        },
                        "hiddenpowerfighting": {
                            "num": 237,
                            "accuracy": 100,
                            "basePower": 60,
                            "category": "Special",
                            "desc": "",
                            "shortDesc": "",
                            "id": "hiddenpower",
                            "isViable": True,
                            "name": "Hidden Power Fighting",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Fighting",
                            "contestType": "Clever"
                        },
                        "hiddenpowerfire": {
                            "num": 237,
                            "accuracy": 100,
                            "basePower": 60,
                            "category": "Special",
                            "desc": "",
                            "shortDesc": "",
                            "id": "hiddenpower",
                            "isViable": True,
                            "name": "Hidden Power Fire",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Fire",
                            "contestType": "Clever"
                        },
                        "hiddenpowerflying": {
                            "num": 237,
                            "accuracy": 100,
                            "basePower": 60,
                            "category": "Special",
                            "desc": "",
                            "shortDesc": "",
                            "id": "hiddenpower",
                            "name": "Hidden Power Flying",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Flying",
                            "contestType": "Clever"
                        },
                        "hiddenpowerghost": {
                            "num": 237,
                            "accuracy": 100,
                            "basePower": 60,
                            "category": "Special",
                            "desc": "",
                            "shortDesc": "",
                            "id": "hiddenpower",
                            "name": "Hidden Power Ghost",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Ghost",
                            "contestType": "Clever"
                        },
                        "hiddenpowergrass": {
                            "num": 237,
                            "accuracy": 100,
                            "basePower": 60,
                            "category": "Special",
                            "desc": "",
                            "shortDesc": "",
                            "id": "hiddenpower",
                            "isViable": True,
                            "name": "Hidden Power Grass",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Grass",
                            "contestType": "Clever"
                        },
                        "hiddenpowerground": {
                            "num": 237,
                            "accuracy": 100,
                            "basePower": 60,
                            "category": "Special",
                            "desc": "",
                            "shortDesc": "",
                            "id": "hiddenpower",
                            "name": "Hidden Power Ground",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Ground",
                            "contestType": "Clever"
                        },
                        "hiddenpowerice": {
                            "num": 237,
                            "accuracy": 100,
                            "basePower": 60,
                            "category": "Special",
                            "desc": "",
                            "shortDesc": "",
                            "id": "hiddenpower",
                            "isViable": True,
                            "name": "Hidden Power Ice",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Ice",
                            "contestType": "Clever"
                        },
                        "hiddenpowerpoison": {
                            "num": 237,
                            "accuracy": 100,
                            "basePower": 60,
                            "category": "Special",
                            "desc": "",
                            "shortDesc": "",
                            "id": "hiddenpower",
                            "name": "Hidden Power Poison",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Poison",
                            "contestType": "Clever"
                        },
                        "hiddenpowerpsychic": {
                            "num": 237,
                            "accuracy": 100,
                            "basePower": 60,
                            "category": "Special",
                            "desc": "",
                            "shortDesc": "",
                            "id": "hiddenpower",
                            "name": "Hidden Power Psychic",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Psychic",
                            "contestType": "Clever"
                        },
                        "hiddenpowerrock": {
                            "num": 237,
                            "accuracy": 100,
                            "basePower": 60,
                            "category": "Special",
                            "desc": "",
                            "shortDesc": "",
                            "id": "hiddenpower",
                            "name": "Hidden Power Rock",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Rock",
                            "contestType": "Clever"
                        },
                        "hiddenpowersteel": {
                            "num": 237,
                            "accuracy": 100,
                            "basePower": 60,
                            "category": "Special",
                            "desc": "",
                            "shortDesc": "",
                            "id": "hiddenpower",
                            "name": "Hidden Power Steel",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Steel",
                            "contestType": "Clever"
                        },
                        "hiddenpowerwater": {
                            "num": 237,
                            "accuracy": 100,
                            "basePower": 60,
                            "category": "Special",
                            "desc": "",
                            "shortDesc": "",
                            "id": "hiddenpower",
                            "name": "Hidden Power Water",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Water",
                            "contestType": "Clever"
                        },
                        "highhorsepower": {
                            "num": 667,
                            "accuracy": 95,
                            "basePower": 95,
                            "category": "Physical",
                            "shortDesc": "No additional effect.",
                            "id": "highhorsepower",
                            "name": "High Horsepower",
                            "pp": 10,
                            "priority": 0,
                            "flags": {
                                "contact": 1,
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Ground",
                            "zMovePower": 175,
                            "contestType": "Tough"
                        },
                        "highjumpkick": {
                            "num": 136,
                            "accuracy": 90,
                            "basePower": 130,
                            "category": "Physical",
                            "desc": "If this attack is not successful, the user loses half of its maximum HP, rounded down, as crash damage. Pokemon with the Magic Guard Ability are unaffected by crash damage.",
                            "shortDesc": "User is hurt by 50% of its max HP if it misses.",
                            "id": "highjumpkick",
                            "isViable": True,
                            "name": "High Jump Kick",
                            "pp": 10,
                            "priority": 0,
                            "flags": {
                                "contact": 1,
                                "protect": 1,
                                "mirror": 1,
                                "gravity": 1
                            },
                            "hasCustomRecoil": True,
                            "secondary": None,
                            "target": "normal",
                            "type": "Fighting",
                            "zMovePower": 195,
                            "contestType": "Cool"
                        },
                        "holdback": {
                            "num": 610,
                            "accuracy": 100,
                            "basePower": 40,
                            "category": "Physical",
                            "desc": "Leaves the target with at least 1 HP.",
                            "shortDesc": "Always leaves the target with at least 1 HP.",
                            "id": "holdback",
                            "name": "Hold Back",
                            "pp": 40,
                            "priority": 0,
                            "flags": {
                                "contact": 1,
                                "protect": 1,
                                "mirror": 1
                            },
                            "noFaint": True,
                            "secondary": None,
                            "target": "normal",
                            "type": "Normal",
                            "zMovePower": 100,
                            "contestType": "Cool"
                        },
                        "holdhands": {
                            "num": 615,
                            "accuracy": True,
                            "basePower": 0,
                            "category": "Status",
                            "desc": "No competitive use. Fails if there is no ally adjacent to the user.",
                            "shortDesc": "No competitive use.",
                            "id": "holdhands",
                            "name": "Hold Hands",
                            "pp": 40,
                            "priority": 0,
                            "flags": {
                                "authentic": 1
                            },
                            "secondary": None,
                            "target": "adjacentAlly",
                            "type": "Normal",
                            "zMoveBoost": {
                                "atk": 1,
                                "def": 1,
                                "spa": 1,
                                "spd": 1,
                                "spe": 1
                            },
                            "contestType": "Cute"
                        },
                        "honeclaws": {
                            "num": 468,
                            "accuracy": True,
                            "basePower": 0,
                            "category": "Status",
                            "desc": "Raises the user's Attack and 'accuracy' by 1 stage.",
                            "shortDesc": "Raises the user's Attack and 'accuracy' by 1.",
                            "id": "honeclaws",
                            "isViable": True,
                            "name": "Hone Claws",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "snatch": 1
                            },
                            "boosts": {
                                "atk": 1,
                                "accuracy": 1
                            },
                            "secondary": None,
                            "target": "self",
                            "type": "Dark",
                            "zMoveBoost": {
                                "atk": 1
                            },
                            "contestType": "Cute"
                        },
                        "hornattack": {
                            "num": 30,
                            "accuracy": 100,
                            "basePower": 65,
                            "category": "Physical",
                            "shortDesc": "No additional effect.",
                            "id": "hornattack",
                            "name": "Horn Attack",
                            "pp": 25,
                            "priority": 0,
                            "flags": {
                                "contact": 1,
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Normal",
                            "zMovePower": 120,
                            "contestType": "Cool"
                        },
                        "horndrill": {
                            "num": 32,
                            "accuracy": 30,
                            "basePower": 0,
                            "category": "Physical",
                            "desc": "Deals damage to the target equal to the target's maximum HP. Ignores 'accuracy' and evasiveness modifiers. This attack's 'accuracy' is equal to(user 's level - target's level + 30) % , and fails if the target is at a higher level.Pokemon with the Sturdy Ability are immune.",
                            "shortDesc": "OHKOs the target. Fails if user is a lower level.",
                            "id": "horndrill",
                            "name": "Horn Drill",
                            "pp": 5,
                            "priority": 0,
                            "flags": {
                                "contact": 1,
                                "protect": 1,
                                "mirror": 1
                            },
                            "ohko": True,
                            "secondary": None,
                            "target": "normal",
                            "type": "Normal",
                            "zMovePower": 180,
                            "contestType": "Cool"
                        },
                        "hornleech": {
                            "num": 532,
                            "accuracy": 100,
                            "basePower": 75,
                            "category": "Physical",
                            "desc": "The user recovers 1/2 the HP lost by the target, rounded half up. If Big Root is held by the user, the HP recovered is 1.3x normal, rounded half down.",
                            "shortDesc": "User recovers 50% of the damage dealt.",
                            "id": "hornleech",
                            "isViable": True,
                            "name": "Horn Leech",
                            "pp": 10,
                            "priority": 0,
                            "flags": {
                                "contact": 1,
                                "protect": 1,
                                "mirror": 1,
                                "heal": 1
                            },
                            "drain": [
                                1,
                                2
                            ],
                            "secondary": None,
                            "target": "normal",
                            "type": "Grass",
                            "zMovePower": 140,
                            "contestType": "Tough"
                        },
                        "howl": {
                            "num": 336,
                            "accuracy": True,
                            "basePower": 0,
                            "category": "Status",
                            "desc": "Raises the user's Attack by 1 stage.",
                            "shortDesc": "Raises the user's Attack by 1.",
                            "id": "howl",
                            "name": "Howl",
                            "pp": 40,
                            "priority": 0,
                            "flags": {
                                "snatch": 1
                            },
                            "boosts": {
                                "atk": 1,
                            },
                            "secondary": None,
                            "target": "self",
                            "type": "Normal",
                            "zMoveBoost": {
                                "atk": 1
                            },
                            "contestType": "Cool"
                        },
                        "hurricane": {
                            "num": 542,
                            "accuracy": 70,
                            "basePower": 110,
                            "category": "Special",
                            "desc": "Has a 30% chance to confuse the target. This move can hit a target using Bounce, Fly, or Sky Drop, or is under the effect of Sky Drop. If the weather is Primordial Sea or Rain Dance, this move does not check 'accuracy'. If the weather is Desolate Land or Sunny Day, this move's 'accuracy' is 50%.",
                            "shortDesc": "30% chance to confuse target. Can't miss in rain.",
                            "id": "hurricane",
                            "isViable": True,
                            "name": "Hurricane",
                            "pp": 10,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1,
                                "distance": 1
                            },
                            "secondary": {
                                "chance": 30,
                                "volatileStatus": "confusion",
                            },
                            "target": "any",
                            "type": "Flying",
                            "zMovePower": 185,
                            "contestType": "Tough"
                        },
                        "hydrocannon": {
                            "num": 308,
                            "accuracy": 90,
                            "basePower": 150,
                            "category": "Special",
                            "desc": "If this move is successful, the user must recharge on the following turn and cannot select a move.",
                            "shortDesc": "User cannot move next turn.",
                            "id": "hydrocannon",
                            "name": "Hydro Cannon",
                            "pp": 5,
                            "priority": 0,
                            "flags": {
                                "recharge": 1,
                                "protect": 1,
                                "mirror": 1
                            },
                            "self": {
                                "volatileStatus": "mustrecharge",
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Water",
                            "zMovePower": 200,
                            "contestType": "Beautiful"
                        },
                        "hydropump": {
                            "num": 56,
                            "accuracy": 80,
                            "basePower": 110,
                            "category": "Special",
                            "shortDesc": "No additional effect.",
                            "id": "hydropump",
                            "isViable": True,
                            "name": "Hydro Pump",
                            "pp": 5,
                            "priority": 0,
                            "flags": {
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Water",
                            "zMovePower": 185,
                            "contestType": "Beautiful"
                        },
                        "hydrovortex": {
                            "num": 642,
                            "accuracy": True,
                            "basePower": 1,
                            "category": "Physical",
                            "shortDesc": "Power is equal to the base move's Z-Power.",
                            "id": "hydrovortex",
                            "isViable": True,
                            "name": "Hydro Vortex",
                            "pp": 1,
                            "priority": 0,
                            "flags": {},
                            "isZ": "wateriumz",
                            "secondary": None,
                            "target": "normal",
                            "type": "Water",
                            "contestType": "Cool"
                        },
                        "hyperbeam": {
                            "num": 63,
                            "accuracy": 90,
                            "basePower": 150,
                            "category": "Special",
                            "desc": "If this move is successful, the user must recharge on the following turn and cannot select a move.",
                            "shortDesc": "User cannot move next turn.",
                            "id": "hyperbeam",
                            "name": "Hyper Beam",
                            "pp": 5,
                            "priority": 0,
                            "flags": {
                                "recharge": 1,
                                "protect": 1,
                                "mirror": 1
                            },
                            "self": {
                                "volatileStatus": "mustrecharge",
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Normal",
                            "zMovePower": 200,
                            "contestType": "Cool"
                        },
                        "hyperfang": {
                            "num": 158,
                            "accuracy": 90,
                            "basePower": 80,
                            "category": "Physical",
                            "desc": "Has a 10% chance to flinch the target.",
                            "shortDesc": "10% chance to flinch the target.",
                            "id": "hyperfang",
                            "name": "Hyper Fang",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "bite": 1,
                                "contact": 1,
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": {
                                "chance": 10,
                                "volatileStatus": "flinch"
                            },
                            "target": "normal",
                            "type": "Normal",
                            "zMovePower": 160,
                            "contestType": "Cool"
                        },
                        "hyperspacefury": {
                            "num": 621,
                            "accuracy": True,
                            "basePower": 100,
                            "category": "Physical",
                            "desc": "Lowers the user's Defense by 1 stage. This move cannot be used successfully unless the user's current form, while considering Transform, is Hoopa Unbound. If this move is successful, it breaks through the target's Baneful Bunker, Detect, King's Shield, Protect, or Spiky Shield for this turn, allowing other Pokemon to attack the target normally.If the target's side is protected by Crafty Shield, Mat Block, Quick Guard, or Wide Guard, that protection is also broken for this turn and other Pokemon may attack the target's side normally.",
                            "shortDesc": "Hoopa-U: Lowers user's Def by 1; breaks protect.",
                            "id": "hyperspacefury",
                            "isViable": True,
                            "name": "Hyperspace Fury",
                            "pp": 5,
                            "priority": 0,
                            "flags": {
                                "mirror": 1,
                                "authentic": 1
                            },
                            "breaksProtect": True,
                            "hyperspacehole": {
                                "num": 593,
                                "accuracy": True,
                                "basePower": 80,
                                "category": "Special",
                                "desc": "If this move is successful, it breaks through the target's Baneful Bunker, Detect, King's Shield, Protect, or Spiky Shield for this turn, allowing other Pokemon to attack the target normally.If the target 's side is protected by Crafty Shield, Mat Block, Quick Guard, or Wide Guard, that protection is also broken for this turn and other Pokemon may attack the target's side normally.",
                                "shortDesc": "Breaks the target's protection for this turn.",
                                "id": "hyperspacehole",
                                "name": "Hyperspace Hole",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "mirror": 1,
                                    "authentic": 1
                                },
                                "breaksProtect": True,
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "zMovePower": 160,
                                "contestType": "Clever"
                            },
                            "hypervoice": {
                                "num": 304,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Special",
                                "desc": "No additional effect.",
                                "shortDesc": "No additional effect. Hits adjacent foes.",
                                "id": "hypervoice",
                                "isViable": True,
                                "name": "Hyper Voice",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "sound": 1,
                                    "authentic": 1
                                },
                                "secondary": None,
                                "target": "allAdjacentFoes",
                                "type": "Normal",
                                "zMovePower": 175,
                                "contestType": "Cool"
                            },
                            "hypnosis": {
                                "num": 95,
                                "accuracy": 60,
                                "basePower": 0,
                                "category": "Status",
                                "shortDesc": "Causes the target to fall asleep.",
                                "id": "hypnosis",
                                "name": "Hypnosis",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "status": "slp",
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "zMoveBoost": {
                                    "spe": 1
                                },
                                "contestType": "Clever"
                            },
                            "iceball": {
                                "num": 301,
                                "accuracy": 90,
                                "basePower": 30,
                                "category": "Physical",
                                "desc": "If this move is successful, the user is locked into this move and cannot make another move until it misses, 5 turns have passed, or the attack cannot be used. Power doubles with each successful hit of this move and doubles again if Defense Curl was used previously by the user. If this move is called by Sleep Talk, the move is used for one turn. If this move hits an active Disguise during the effect, the power multiplier is paused but the turn counter is not, potentially allowing the multiplier to be used on the user's next move after this effect ends.",
                                "shortDesc": "Power doubles with each hit. Repeats for 5 turns.",
                                "id": "iceball",
                                "name": "Ice Ball",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "bullet": 1,
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Ice",
                                "zMovePower": 100,
                                "contestType": "Beautiful"
                            },
                            "icebeam": {
                                "num": 58,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Special",
                                "desc": "Has a 10% chance to freeze the target.",
                                "shortDesc": "10% chance to freeze the target.",
                                "id": "icebeam",
                                "isViable": True,
                                "name": "Ice Beam",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 10,
                                    "status": "frz",
                                },
                                "target": "normal",
                                "type": "Ice",
                                "zMovePower": 175,
                                "contestType": "Beautiful"
                            },
                            "iceburn": {
                                "num": 554,
                                "accuracy": 90,
                                "basePower": 140,
                                "category": "Special",
                                "desc": "Has a 30% chance to burn the target. This attack charges on the first turn and executes on the second. If the user is holding a Power Herb, the move completes in one turn.",
                                "shortDesc": "Charges turn 1. Hits turn 2. 30% burn.",
                                "id": "iceburn",
                                "name": "Ice Burn",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "charge": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "status": "brn",
                                },
                                "target": "normal",
                                "type": "Ice",
                                "zMovePower": 200,
                                "contestType": "Beautiful"
                            },
                            "icefang": {
                                "num": 423,
                                "accuracy": 95,
                                "basePower": 65,
                                "category": "Physical",
                                "desc": "Has a 10% chance to freeze the target and a 10% chance to flinch it.",
                                "shortDesc": "10% chance to freeze. 10% chance to flinch.",
                                "id": "icefang",
                                "isViable": True,
                                "name": "Ice Fang",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "bite": 1,
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondaries": [{
                                        "chance": 10,
                                        "status": "frz",
                                    },
                                    {
                                        "chance": 10,
                                        "volatileStatus": "flinch"
                                    },
                                ],
                                "target": "normal",
                                "type": "Ice",
                                "zMovePower": 120,
                                "contestType": "Cool"
                            },
                            "icehammer": {
                                "num": 665,
                                "accuracy": 90,
                                "basePower": 100,
                                "category": "Physical",
                                "desc": "Lowers the user's Speed by 1 stage.",
                                "shortDesc": "Lowers the user's Speed by 1.",
                                "id": "icehammer",
                                "isViable": True,
                                "name": "Ice Hammer",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "powder": 1
                                },
                                "self": {
                                    "boosts": {
                                        "spe": -1,
                                    },
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Ice",
                                "zMovePower": 180,
                                "contestType": "Tough"
                            },
                            "icepunch": {
                                "num": 8,
                                "accuracy": 100,
                                "basePower": 75,
                                "category": "Physical",
                                "desc": "Has a 10% chance to freeze the target.",
                                "shortDesc": "10% chance to freeze the target.",
                                "id": "icepunch",
                                "isViable": True,
                                "name": "Ice Punch",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "powder": 1
                                },
                                "secondary": {
                                    "chance": 10,
                                    "status": "frz",
                                },
                                "target": "normal",
                                "type": "Ice",
                                "zMovePower": 140,
                                "contestType": "Beautiful"
                            },
                            "iceshard": {
                                "num": 420,
                                "accuracy": 100,
                                "basePower": 40,
                                "category": "Physical",
                                "desc": "No additional effect.",
                                "shortDesc": "Usually goes first.",
                                "id": "iceshard",
                                "isViable": True,
                                "name": "Ice Shard",
                                "pp": 30,
                                "priority": 1,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Ice",
                                "zMovePower": 100,
                                "contestType": "Beautiful"
                            },
                            "iciclecrash": {
                                "num": 556,
                                "accuracy": 90,
                                "basePower": 85,
                                "category": "Physical",
                                "desc": "Has a 30% chance to flinch the target.",
                                "shortDesc": "30% chance to flinch the target.",
                                "id": "iciclecrash",
                                "isViable": True,
                                "name": "Icicle Crash",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "volatileStatus": "flinch"
                                },
                                "target": "normal",
                                "type": "Ice",
                                "zMovePower": 160,
                                "contestType": "Beautiful"
                            },
                            "iciclespear": {
                                "num": 333,
                                "accuracy": 100,
                                "basePower": 25,
                                "category": "Physical",
                                "desc": "Hits two to five times. Has a 1/3 chance to hit two or three times, and a 1/6 chance to hit four or five times. If one of the hits breaks the target's substitute, it will take damage for the remaining hits. If the user has the Skill Link Ability, this move will always hit five times.",
                                "shortDesc": "Hits 2-5 times in one turn.",
                                "id": "iciclespear",
                                "isViable": True,
                                "name": "Icicle Spear",
                                "pp": 30,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "multihit": [
                                    2,
                                    5
                                ],
                                "secondary": None,
                                "target": "normal",
                                "type": "Ice",
                                "zMovePower": 140,
                                "contestType": "Beautiful"
                            },
                            "icywind": {
                                "num": 196,
                                "accuracy": 95,
                                "basePower": 55,
                                "category": "Special",
                                "desc": "Has a 100% chance to lower the target's Speed by 1 stage.",
                                "shortDesc": "100% chance to lower the foe(s) Speed by 1.",
                                "id": "icywind",
                                "name": "Icy Wind",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 100,
                                    "boosts": {
                                        "spe": -1,
                                    },
                                },
                                "target": "allAdjacentFoes",
                                "type": "Ice",
                                "zMovePower": 100,
                                "contestType": "Beautiful"
                            },
                            "imprison": {
                                "num": 286,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user prevents all opposing Pokemon from using any moves that the user also knows as long as the user remains active.",
                                "shortDesc": "No foe can use any move known by the user.",
                                "id": "imprison",
                                "name": "Imprison",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1,
                                    "authentic": 1
                                },
                                "volatileStatus": "imprison",
                                "secondary": None,
                                "pressureTarget": "foeSide",
                                "target": "self",
                                "type": "Psychic",
                                "zMoveBoost": {
                                    "spd": 2
                                },
                                "contestType": "Clever"
                            },
                            "incinerate": {
                                "num": 510,
                                "accuracy": 100,
                                "basePower": 60,
                                "category": "Special",
                                "desc": "The target loses its held item if it is a Berry or a Gem. This move cannot cause Pokemon with the Sticky Hold Ability to lose their held item. Items lost to this move cannot be regained with Recycle or the Harvest Ability.",
                                "shortDesc": "Destroys the foe(s) Berry/Gem.",
                                "id": "incinerate",
                                "name": "Incinerate",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "allAdjacentFoes",
                                "type": "Fire",
                                "zMovePower": 120,
                                "contestType": "Tough"
                            },
                            "inferno": {
                                "num": 517,
                                "accuracy": 50,
                                "basePower": 100,
                                "category": "Special",
                                "desc": "Has a 100% chance to burn the target.",
                                "shortDesc": "100% chance to burn the target.",
                                "id": "inferno",
                                "name": "Inferno",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 100,
                                    "status": "brn",
                                },
                                "target": "normal",
                                "type": "Fire",
                                "zMovePower": 180,
                                "contestType": "Beautiful"
                            },
                            "infernooverdrive": {
                                "num": 640,
                                "accuracy": True,
                                "basePower": 1,
                                "category": "Physical",
                                "shortDesc": "Power is equal to the base move's Z-Power.",
                                "id": "infernooverdrive",
                                "isViable": True,
                                "name": "Inferno Overdrive",
                                "pp": 1,
                                "priority": 0,
                                "flags": {},
                                "isZ": "firiumz",
                                "secondary": None,
                                "target": "normal",
                                "type": "Fire",
                                "contestType": "Cool"
                            },
                            "infestation": {
                                "num": 611,
                                "accuracy": 100,
                                "basePower": 20,
                                "category": "Special",
                                "desc": "Prevents the target from switching for four or five turns (seven turns if the user is holding Grip Claw). Causes damage to the target equal to 1/8 of its maximum HP (1/6 if the user is holding Binding Band), rounded down, at the end of each turn during effect. The target can still switch out if it is holding Shed Shell or uses Baton Pass, Parting Shot, U-turn, or Volt Switch. The effect ends if either the user or the target leaves the field, or if the target uses Rapid Spin or Substitute successfully. This effect is not stackable or reset by using this or another binding move.",
                                "shortDesc": "Traps and damages the target for 4-5 turns.",
                                "id": "infestation",
                                "name": "Infestation",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "volatileStatus": "partiallytrapped",
                                "secondary": None,
                                "target": "normal",
                                "type": "Bug",
                                "zMovePower": 100,
                                "contestType": "Cute"
                            },
                            "ingrain": {
                                "num": 275,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user has 1/16 of its maximum HP restored at the end of each turn, but it is prevented from switching out and other Pokemon cannot force the user to switch out. The user can still switch out if it uses Baton Pass, Parting Shot, U-turn, or Volt Switch. If the user leaves the field using Baton Pass, the replacement will remain trapped and still receive the healing effect. During the effect, the user can be hit normally by Ground-type attacks and be affected by Spikes, Toxic Spikes, and Sticky Web, even if the user is a Flying type or has the Levitate Ability.",
                                "shortDesc": "Traps/grounds user; heals 1/16 max HP per turn.",
                                "id": "ingrain",
                                "name": "Ingrain",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1,
                                    "nonsky": 1
                                },
                                "volatileStatus": "ingrain",
                                "secondary": None,
                                "target": "self",
                                "type": "Grass",
                                "zMoveBoost": {
                                    "spd": 1
                                },
                                "contestType": "Clever"
                            },
                            "instruct": {
                                "num": 689,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The target immediately uses its last used move. Fails if the target has not made a move, if the move has 0 PP, if the target is preparing to use Beak Blast, Focus Punch, or Shell Trap, or if the move is Assist, Beak Blast, Belch, Bide, Celebrate, Copycat, Focus Punch, Ice Ball, Instruct, King's Shield, Me First, Metronome, Mimic, Mirror Move, Nature Power, Outrage, Petal Dance, Rollout, Shell Trap, Sketch, Sleep Talk, Struggle, Thrash, Transform, Uproar, any two - turn move, any recharge move, or any Z - Move. ",
                                "shortDesc": "The target immediately uses its last used move.",
                                "id": "instruct",
                                "name": "Instruct",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "authentic": 1,
                                    "mystery": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "zMoveBoost": {
                                    "spa": 1
                                },
                                "contestType": "Clever"
                            },
                            "iondeluge": {
                                "num": 569,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Causes Normal-type moves to become Electric type this turn. The effect happens after other effects that change a move's type.",
                                "shortDesc": "Normal moves become Electric type this turn.",
                                "id": "iondeluge",
                                "name": "Ion Deluge",
                                "pp": 25,
                                "priority": 1,
                                "flags": {},
                                "pseudoWeather": "iondeluge",
                                "secondary": None,
                                "target": "all",
                                "type": "Electric",
                                "zMoveBoost": {
                                    "spa": 1
                                },
                                "contestType": "Beautiful"
                            },
                            "irondefense": {
                                "num": 334,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Raises the user's Defense by 2 stages.",
                                "shortDesc": "Raises the user's Defense by 2.",
                                "id": "irondefense",
                                "name": "Iron Defense",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1
                                },
                                "boosts": {
                                    "def": 2
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Steel",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Tough"
                            },
                            "ironhead": {
                                "num": 442,
                                "accuracy": 100,
                                "basePower": 80,
                                "category": "Physical",
                                "desc": "Has a 30% chance to flinch the target.",
                                "shortDesc": "30% chance to flinch the target.",
                                "id": "ironhead",
                                "isViable": True,
                                "name": "Iron Head",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "volatileStatus": "flinch"
                                },
                                "target": "normal",
                                "type": "Steel",
                                "zMovePower": 160,
                                "contestType": "Tough"
                            },
                            "irontail": {
                                "num": 231,
                                "accuracy": 75,
                                "basePower": 100,
                                "category": "Physical",
                                "desc": "Has a 30% chance to lower the target's Defense by 1 stage.",
                                "shortDesc": "30% chance to lower the target's Defense by 1.",
                                "id": "irontail",
                                "name": "Iron Tail",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "boosts": {
                                        "def": -1,
                                    },
                                },
                                "target": "normal",
                                "type": "Steel",
                                "zMovePower": 180,
                                "contestType": "Cool"
                            },
                            "judgment": {
                                "num": 449,
                                "accuracy": 100,
                                "basePower": 100,
                                "category": "Special",
                                "desc": "This move's type depends on the user's held Plate.",
                                "shortDesc": "Type varies based on the held Plate.",
                                "id": "judgment",
                                "isViable": True,
                                "name": "Judgment",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 180,
                                "contestType": "Beautiful"
                            },
                            "jumpkick": {
                                "num": 26,
                                "accuracy": 95,
                                "basePower": 100,
                                "category": "Physical",
                                "desc": "If this attack is not successful, the user loses half of its maximum HP, rounded down, as crash damage. Pokemon with the Magic Guard Ability are unaffected by crash damage.",
                                "shortDesc": "User is hurt by 50% of its max HP if it misses.",
                                "id": "jumpkick",
                                "isViable": True,
                                "name": "Jump Kick",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "gravity": 1
                                },
                                "hasCustomRecoil": True,
                                "secondary": None,
                                "target": "normal",
                                "type": "Fighting",
                                "zMovePower": 180,
                                "contestType": "Cool"
                            },
                            "karatechop": {
                                "num": 2,
                                "accuracy": 100,
                                "basePower": 50,
                                "category": "Physical",
                                "desc": "Has a higher chance for a critical hit.",
                                "shortDesc": "High critical hit ratio.",
                                "id": "karatechop",
                                "name": "Karate Chop",
                                "pp": 25,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "critRatio": 2,
                                "secondary": None,
                                "target": "normal",
                                "type": "Fighting",
                                "zMovePower": 100,
                                "contestType": "Tough"
                            },
                            "kinesis": {
                                "num": 134,
                                "accuracy": 80,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Lowers the target's 'accuracy' by 1 stage.",
                                "shortDesc": "Lowers the target's 'accuracy' by 1.",
                                "id": "kinesis",
                                "name": "Kinesis",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "boosts": {
                                    "accuracy": -1,
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "zMoveBoost": {
                                    "evasion": 1
                                },
                                "contestType": "Clever"
                            },
                            "kingsshield": {
                                "num": 588,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user is protected from most attacks made by other Pokemon during this turn, and Pokemon trying to make contact with the user have their Attack lowered by 2 stages. Non-damaging moves go through this protection. This move has a 1/X chance of being successful, where X starts at 1 and triples each time this move is successfully used. X resets to 1 if this move fails, if the user's last move used is not Baneful Bunker, Detect, Endure, King's Shield, Protect, Quick Guard, Spiky Shield, or Wide Guard, or if it was one of those moves and the user 's protection was broken. Fails if the user moves last this turn.",
                                "shortDesc": "Protects from attacks contact lowers Atk by 2.",
                                "id": "kingsshield",
                                "isViable": True,
                                "name": "King's Shield ",
                                "pp": 10,
                                "priority": 4,
                                "flags": {},
                                "stallingMove": True,
                                "volatileStatus": "kingsshield",
                                "secondary": None,
                                "target": "self",
                                "type": "Steel",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Cool"
                            },
                            "knockoff": {
                                "num": 282,
                                "accuracy": 100,
                                "basePower": 65,
                                "category": "Physical",
                                "desc": "If the target is holding an item that can be removed from it, ignoring the Sticky Hold Ability, this move's power is multiplied by 1.5. If the user has not fainted, the target loses its held item. This move cannot remove Z-Crystals, cause Pokemon with the Sticky Hold Ability to lose their held item, cause Pokemon that can Mega Evolve to lose the Mega Stone for their species, or cause a Kyogre, a Groudon, a Giratina, an Arceus, a Genesect, or a Silvally to lose their Blue Orb, Red Orb, Griseous Orb, Plate, Drive, or Memory respectively. Items lost to this move cannot be regained with Recycle or the Harvest Ability.",
                                "shortDesc": "1.5x damage if foe holds an item. Removes item.",
                                "id": "knockoff",
                                "isViable": True,
                                "name": "Knock Off",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Dark",
                                "zMovePower": 120,
                                "contestType": "Clever"
                            },
                            "landswrath": {
                                "num": 616,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Physical",
                                "desc": "No additional effect.",
                                "shortDesc": "No additional effect. Hits adjacent foes.",
                                "id": "landswrath",
                                "name": "Land's Wrath ",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "nonsky": 1
                                },
                                "secondary": None,
                                "target": "allAdjacentFoes",
                                "type": "Ground",
                                "zMovePower": 185,
                                "contestType": "Beautiful"
                            },
                            "laserfocus": {
                                "num": 673,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Until the end of the next turn, the user's attacks will be critical hits.",
                                "shortDesc": "Until the end of the next turn, user's moves crit.",
                                "id": "laserfocus",
                                "name": "Laser Focus",
                                "pp": 30,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1
                                },
                                "volatileStatus": "laserfocus",
                                "secondary": None,
                                "target": "self",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "atk": 1
                                },
                                "contestType": "Cool"
                            },
                            "lastresort": {
                                "num": 387,
                                "accuracy": 100,
                                "basePower": 140,
                                "category": "Physical",
                                "desc": "This move fails unless the user knows this move and at least one other move, and has used all the other moves it knows at least once each since it became active or Transformed.",
                                "shortDesc": "Fails unless each known move has been used.",
                                "id": "lastresort",
                                "name": "Last Resort",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 200,
                                "contestType": "Cute"
                            },
                            "lavaplume": {
                                "num": 436,
                                "accuracy": 100,
                                "basePower": 80,
                                "category": "Special",
                                "desc": "Has a 30% chance to burn the target.",
                                "shortDesc": "30% chance to burn adjacent Pokemon.",
                                "id": "lavaplume",
                                "isViable": True,
                                "name": "Lava Plume",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "status": "brn",
                                },
                                "target": "allAdjacent",
                                "type": "Fire",
                                "zMovePower": 160,
                                "contestType": "Tough"
                            },
                            "leafage": {
                                "num": 670,
                                "accuracy": 100,
                                "basePower": 40,
                                "category": "Physical",
                                "shortDesc": "No additional effect.",
                                "id": "leafage",
                                "name": "Leafage",
                                "pp": 40,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Grass",
                                "zMovePower": 100,
                                "contestType": "Tough"
                            },
                            "leafblade": {
                                "num": 348,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Physical",
                                "desc": "Has a higher chance for a critical hit.",
                                "shortDesc": "High critical hit ratio.",
                                "id": "leafblade",
                                "isViable": True,
                                "name": "Leaf Blade",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "critRatio": 2,
                                "secondary": None,
                                "target": "normal",
                                "type": "Grass",
                                "zMovePower": 175,
                                "contestType": "Cool"
                            },
                            "leafstorm": {
                                "num": 437,
                                "accuracy": 90,
                                "basePower": 130,
                                "category": "Special",
                                "desc": "Lowers the user's Special Attack by 2 stages.",
                                "shortDesc": "Lowers the user's Sp. Atk by 2.",
                                "id": "leafstorm",
                                "isViable": True,
                                "name": "Leaf Storm",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "self": {
                                    "boosts": {
                                        "spa": -2,
                                    },
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Grass",
                                "zMovePower": 195,
                                "contestType": "Beautiful"
                            },
                            "leaftornado": {
                                "num": 536,
                                "accuracy": 90,
                                "basePower": 65,
                                "category": "Special",
                                "desc": "Has a 50% chance to lower the target's 'accuracy' by 1 stage.",
                                "shortDesc": "50% chance to lower the target's 'accuracy' by 1. ",
                                "id": "leaftornado",
                                "name": "Leaf Tornado",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 50,
                                    "boosts": {
                                        "accuracy": -1,
                                    },
                                },
                                "target": "normal",
                                "type": "Grass",
                                "zMovePower": 120,
                                "contestType": "Cool"
                            },
                            "leechlife": {
                                "num": 141,
                                "accuracy": 100,
                                "basePower": 80,
                                "category": "Physical",
                                "desc": "The user recovers 1/2 the HP lost by the target, rounded half up. If Big Root is held by the user, the HP recovered is 1.3x normal, rounded half down.",
                                "shortDesc": "User recovers 50% of the damage dealt.",
                                "id": "leechlife",
                                "isViable": True,
                                "name": "Leech Life",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "heal": 1
                                },
                                "drain": [
                                    1,
                                    2
                                ],
                                "secondary": None,
                                "target": "normal",
                                "type": "Bug",
                                "zMovePower": 160,
                                "contestType": "Clever"
                            },
                            "leechseed": {
                                "num": 73,
                                "accuracy": 90,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The Pokemon at the user's position steals 1/8 of the target's maximum HP, rounded down, at the end of each turn. If Big Root is held by the recipient, the HP recovered is 1.3x normal, rounded half down. If the target uses Baton Pass, the replacement will continue being leeched. If the target switches out or uses Rapid Spin successfully, the effect ends. Grass-type Pokemon are immune to this move on use, but not its effect.",
                                "shortDesc": "1/8 of target's HP is restored to user every turn.",
                                "id": "leechseed",
                                "isViable": True,
                                "name": "Leech Seed",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "volatileStatus": "leechseed",
                                "secondary": None,
                                "target": "normal",
                                "type": "Grass",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Clever"
                            },
                            "leer": {
                                "num": 43,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Lowers the target's Defense by 1 stage.",
                                "shortDesc": "Lowers the foe(s) Defense by 1.",
                                "id": "leer",
                                "name": "Leer",
                                "pp": 30,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "boosts": {
                                    "def": -1,
                                },
                                "secondary": None,
                                "target": "allAdjacentFoes",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "atk": 1
                                },
                                "contestType": "Cool"
                            },
                            "letssnuggleforever": {
                                "num": 726,
                                "accuracy": True,
                                "basePower": 190,
                                "category": "Physical",
                                "shortDesc": "No additional effect.",
                                "id": "letssnuggleforever",
                                "name": "Let's Snuggle Forever ",
                                "pp": 1,
                                "priority": 0,
                                "flags": {
                                    "contact": 1
                                },
                                "isZ": "mimikiumz",
                                "secondary": None,
                                "target": "normal",
                                "type": "Fairy",
                                "contestType": "Cool"
                            },
                            "lick": {
                                "num": 122,
                                "accuracy": 100,
                                "basePower": 30,
                                "category": "Physical",
                                "desc": "Has a 30% chance to paralyze the target.",
                                "shortDesc": "30% chance to paralyze the target.",
                                "id": "lick",
                                "name": "Lick",
                                "pp": 30,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "status": "par",
                                },
                                "target": "normal",
                                "type": "Ghost",
                                "zMovePower": 100,
                                "contestType": "Cute"
                            },
                            "lightofruin": {
                                "num": 617,
                                "accuracy": 90,
                                "basePower": 140,
                                "category": "Special",
                                "desc": "If the target lost HP, the user takes recoil damage equal to 1/2 the HP lost by the target, rounded half up, but not less than 1 HP.",
                                "shortDesc": "Has 1/2 recoil.",
                                "id": "lightofruin",
                                "isViable": True,
                                "name": "Light of Ruin",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "isUnreleased": True,
                                "recoil": [
                                    1,
                                    2
                                ],
                                "secondary": None,
                                "target": "normal",
                                "type": "Fairy",
                                "zMovePower": 200,
                                "contestType": "Beautiful"
                            },
                            "lightscreen": {
                                "num": 113,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "For 5 turns, the user and its party members take 0.5x damage from special attacks, or 0.66x damage if in a Double Battle. Damage is not reduced further with Aurora Veil. Critical hits ignore this effect. It is removed from the user's side if the user or an ally is successfully hit by Brick Break, Psychic Fangs, or Defog. Lasts for 8 turns if the user is holding Light Clay. Fails if the effect is already active on the user's side.",
                                "shortDesc": "For 5 turns, special damage to allies is halved.",
                                "id": "lightscreen",
                                "isViable": True,
                                "name": "Light Screen",
                                "pp": 30,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1
                                },
                                "sideCondition": "lightscreen",
                                "secondary": None,
                                "target": "allySide",
                                "type": "Psychic",
                                "zMoveBoost": {
                                    "spd": 1
                                },
                                "contestType": "Beautiful"
                            },
                            "lightthatburnsthesky": {
                                "num": 723,
                                "accuracy": True,
                                "basePower": 200,
                                "category": "Special",
                                "desc": "This move becomes a physical attack if the user's Attack is greater than its Special Attack, including stat stage changes. This move and its effects ignore the Abilities of other Pokemon.",
                                "shortDesc": "Physical if user's Atk > Sp. Atk. Ignores Abilities.",
                                "id": "lightthatburnsthesky",
                                "name": "Light That Burns the Sky",
                                "pp": 1,
                                "priority": 0,
                                "flags": {},
                                "ignoreAbility": True,
                                "isZ": "ultranecroziumz",
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "contestType": "Cool"
                            },
                            "liquidation": {
                                "num": 710,
                                "accuracy": 100,
                                "basePower": 85,
                                "category": "Physical",
                                "desc": "Has a 20% chance to lower the target's Defense by 1 stage.",
                                "shortDesc": "20% chance to lower the target's Defense by 1.",
                                "id": "liquidation",
                                "isViable": True,
                                "name": "Liquidation",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 20,
                                    "boosts": {
                                        "def": -1,
                                    },
                                },
                                "target": "normal",
                                "type": "Water",
                                "zMovePower": 160,
                                "contestType": "Cool"
                            },
                            "lockon": {
                                "num": 199,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Until the end of the next turn, the target cannot avoid the user's moves, even if the target is in the middle of a two-turn move. The effect ends if either the user or the target leaves the field. Fails if this effect is active for the user.",
                                "shortDesc": "user's next move will not miss the target.",
                                "id": "lockon",
                                "name": "Lock-On",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "spe": 1
                                },
                                "contestType": "Clever"
                            },
                            "lovelykiss": {
                                "num": 142,
                                "accuracy": 75,
                                "basePower": 0,
                                "category": "Status",
                                "shortDesc": "Causes the target to fall asleep.",
                                "id": "lovelykiss",
                                "isViable": True,
                                "name": "Lovely Kiss",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "status": "slp",
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "spe": 1
                                },
                                "contestType": "Beautiful"
                            },
                            "lowkick": {
                                "num": 67,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Physical",
                                "desc": "This move's power is 20 if the target weighs less than 10 kg, 40 if less than 25 kg, 60 if less than 50 kg, 80 if less than 100 kg, 100 if less than 200 kg, and 120 if greater than or equal to 200 kg.",
                                "shortDesc": "More power the heavier the target.",
                                "id": "lowkick",
                                "isViable": True,
                                "name": "Low Kick",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Fighting",
                                "zMovePower": 160,
                                "contestType": "Tough"
                            },
                            "lowsweep": {
                                "num": 490,
                                "accuracy": 100,
                                "basePower": 65,
                                "category": "Physical",
                                "desc": "Has a 100% chance to lower the target's Speed by 1 stage.",
                                "shortDesc": "100% chance to lower the target's Speed by 1.",
                                "id": "lowsweep",
                                "name": "Low Sweep",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 100,
                                    "boosts": {
                                        "spe": -1,
                                    },
                                },
                                "target": "normal",
                                "type": "Fighting",
                                "zMovePower": 120,
                                "contestType": "Clever"
                            },
                            "luckychant": {
                                "num": 381,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "For 5 turns, the user and its party members cannot be struck by a critical hit. Fails if the effect is already active on the user's side.",
                                "shortDesc": "For 5 turns, shields user's party from critical hits.",
                                "id": "luckychant",
                                "name": "Lucky Chant",
                                "pp": 30,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1
                                },
                                "sideCondition": "luckychant",
                                "secondary": None,
                                "target": "allySide",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "evasion": 1
                                },
                                "contestType": "Cute"
                            },
                            "lunardance": {
                                "num": 461,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user faints and the Pokemon brought out to replace it has its HP and PP fully restored along with having any major status condition cured. The new Pokemon is sent out at the end of the turn, and the healing happens before hazards take effect. Fails if the user is the last unfainted Pokemon in its party.",
                                "shortDesc": "User faints. Replacement is fully healed, with PP.",
                                "id": "lunardance",
                                "isViable": True,
                                "name": "Lunar Dance",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1,
                                    "heal": 1,
                                    "dance": 1
                                },
                                "selfdestruct": "ifHit",
                                "sideCondition": "lunardance",
                                "secondary": None,
                                "target": "self",
                                "type": "Psychic",
                                "contestType": "Beautiful"
                            },
                            "lunge": {
                                "num": 679,
                                "accuracy": 100,
                                "basePower": 80,
                                "category": "Physical",
                                "desc": "Has a 100% chance to lower the target's Attack by 1 stage.",
                                "shortDesc": "100% chance to lower the target's Attack by 1.",
                                "id": "lunge",
                                "isViable": True,
                                "name": "Lunge",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 100,
                                    "boosts": {
                                        "atk": -1
                                    },
                                },
                                "target": "normal",
                                "type": "Bug",
                                "zMovePower": 160,
                                "contestType": "Cute"
                            },
                            "lusterpurge": {
                                "num": 295,
                                "accuracy": 100,
                                "basePower": 70,
                                "category": "Special",
                                "desc": "Has a 50% chance to lower the target's Special Defense by 1 stage.",
                                "shortDesc": "50% chance to lower the target's Sp. Def by 1.",
                                "id": "lusterpurge",
                                "name": "Luster Purge",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 50,
                                    "boosts": {
                                        "spd": -1
                                    },
                                },
                                "target": "normal",
                                "type": "Psychic",
                                "zMovePower": 140,
                                "contestType": "Clever"
                            },
                            "machpunch": {
                                "num": 183,
                                "accuracy": 100,
                                "basePower": 40,
                                "category": "Physical",
                                "desc": "No additional effect.",
                                "shortDesc": "Usually goes first.",
                                "id": "machpunch",
                                "isViable": True,
                                "name": "Mach Punch",
                                "pp": 30,
                                "priority": 1,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "powder": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Fighting",
                                "zMovePower": 100,
                                "contestType": "Cool"
                            },
                            "magicalleaf": {
                                "num": 345,
                                "accuracy": True,
                                "basePower": 60,
                                "category": "Special",
                                "shortDesc": "This move does not check 'accuracy'.",
                                "id": "magicalleaf",
                                "name": "Magical Leaf",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Grass",
                                "zMovePower": 120,
                                "contestType": "Beautiful"
                            },
                            "magiccoat": {
                                "num": 277,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Until the end of the turn, the user is unaffected by certain non-damaging moves directed at it and will instead use such moves against the original user. Moves reflected in this way are unable to be reflected again by this or the Magic Bounce Ability's effect.Spikes, Stealth Rock, Sticky Web, and Toxic Spikes can only be reflected once per side, by the leftmost Pokemon under this or the Magic Bounce Ability's effect. The Lightning Rod and Storm Drain, Abilities redirect their respective moves before this move takes effect.",
                                "shortDesc": "Bounces back certain non-damaging moves.",
                                "id": "magiccoat",
                                "isViable": True,
                                "name": "Magic Coat",
                                "pp": 15,
                                "priority": 4,
                                "flags": {},
                                "volatileStatus": "magiccoat",
                                "secondary": None,
                                "target": "self",
                                "type": "Psychic",
                                "zMoveBoost": {
                                    "spd": 2
                                },
                                "contestType": "Beautiful"
                            },
                            "magicroom": {
                                "num": 478,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "For 5 turns, the held items of all active Pokemon have no effect. An item's effect of causing forme changes is unaffected, but any other effects from such items are negated.During the effect, Fling and Natural Gift are prevented from being used by all active Pokemon.If this move is used during the effect, the effect ends. ",
                                "shortDesc": "For 5 turns, all held items have no effect.",
                                "id": "magicroom",
                                "name": "Magic Room",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "mirror": 1
                                },
                                "pseudoWeather": "magicroom",
                                "secondary": None,
                                "target": "all",
                                "type": "Psychic",
                                "zMoveBoost": {
                                    "spd": 1
                                },
                                "contestType": "Clever"
                            },
                            "magikarpsrevenge": {
                                "num": 0,
                                "accuracy": True,
                                "basePower": 120,
                                "category": "Physical",
                                "desc": "Has a 100% chance to confuse the target and lower its Defense and Special Attack by 1 stage. The user recovers 1/2 the HP lost by the target, rounded half up. If Big Root is held by the user, the HP recovered is 1.3x normal, rounded half down. The user steals the foe's boosts.If this move is successful, the weather changes to rain unless it is already in effect, and the user gains the effects of Aqua Ring and Magic Coat.",
                                "shortDesc": "Does many things turn 1. Can't move turn 2. ",
                                "id": "magikarpsrevenge",
                                "isNonstandard": "Custom",
                                "name": "Magikarp's Revenge ",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "recharge": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "heal": 1
                                },
                                "noSketch": True,
                                "drain": [
                                    1,
                                    2
                                ],
                                "secondary": {
                                    "chance": 100,
                                    "volatileStatus": "confusion",
                                    "boosts": {
                                        "def": -1,
                                        "spa": -1,
                                    },
                                },
                                "stealsBoosts": True,
                                "target": "normal",
                                "type": "Water",
                                "zMovePower": 190,
                                "contestType": "Cute"
                            },
                            "magmastorm": {
                                "num": 463,
                                "accuracy": 75,
                                "basePower": 100,
                                "category": "Special",
                                "desc": "Prevents the target from switching for four or five turns (seven turns if the user is holding Grip Claw). Causes damage to the target equal to 1/8 of its maximum HP (1/6 if the user is holding Binding Band), rounded down, at the end of each turn during effect. The target can still switch out if it is holding Shed Shell or uses Baton Pass, Parting Shot, U-turn, or Volt Switch. The effect ends if either the user or the target leaves the field, or if the target uses Rapid Spin or Substitute successfully. This effect is not stackable or reset by using this or another binding move.",
                                "shortDesc": "Traps and damages the target for 4-5 turns.",
                                "id": "magmastorm",
                                "isViable": True,
                                "name": "Magma Storm",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "volatileStatus": "partiallytrapped",
                                "secondary": None,
                                "target": "normal",
                                "type": "Fire",
                                "zMovePower": 180,
                                "contestType": "Tough"
                            },
                            "magnetbomb": {
                                "num": 443,
                                "accuracy": True,
                                "basePower": 60,
                                "category": "Physical",
                                "shortDesc": "This move does not check 'accuracy'.",
                                "id": "magnetbomb",
                                "name": "Magnet Bomb",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "bullet": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Steel",
                                "zMovePower": 120,
                                "contestType": "Cool"
                            },
                            "magneticflux": {
                                "num": 602,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Raises the Defense and Special Defense of Pokemon on the user's side with the Plus or Minus Abilities by 1 stage.",
                                "shortDesc": "Raises Def, Sp. Def of allies with Plus/Minus by 1.",
                                "id": "magneticflux",
                                "name": "Magnetic Flux",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1,
                                    "distance": 1,
                                    "authentic": 1
                                },
                                "secondary": None,
                                "target": "allySide",
                                "type": "Electric",
                                "zMoveBoost": {
                                    "spd": 1
                                },
                                "contestType": "Clever"
                            },
                            "magnetrise": {
                                "num": 393,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "For 5 turns, the user is immune to Ground-type attacks and the effects of Spikes, Toxic Spikes, Sticky Web, and the Arena Trap Ability as long as it remains active. If the user uses Baton Pass, the replacement will gain the effect. Ingrain, Smack Down, Thousand Arrows, and Iron Ball override this move if the user is under any of their effects. Fails if the user is already under this effect or the effects of Ingrain, Smack Down, or Thousand Arrows.",
                                "shortDesc": "For 5 turns, the user has immunity to Ground.",
                                "id": "magnetrise",
                                "name": "Magnet Rise",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1,
                                    "gravity": 1
                                },
                                "volatileStatus": "magnetrise",
                                "secondary": None,
                                "target": "self",
                                "type": "Electric",
                                "zMoveBoost": {
                                    "evasion": 1
                                },
                                "contestType": "Clever"
                            },
                            "magnitude": {
                                "num": 222,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Physical",
                                "desc": "The power of this move varies; 5% chances for 10 and 150 power, 10% chances for 30 and 110 power, 20% chances for 50 and 90 power, and 30% chance for 70 power. Damage doubles if the target is using Dig.",
                                "shortDesc": "Hits adjacent Pokemon. Power varies; 2x on Dig.",
                                "id": "magnitude",
                                "name": "Magnitude",
                                "pp": 30,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "nonsky": 1
                                },
                                "secondary": None,
                                "target": "allAdjacent",
                                "type": "Ground",
                                "zMovePower": 140,
                                "contestType": "Tough"
                            },
                            "maliciousmoonsault": {
                                "num": 696,
                                "accuracy": True,
                                "basePower": 180,
                                "category": "Physical",
                                "desc": "Damage doubles and no 'accuracy' check is done if the target has used Minimize while active.",
                                "shortDesc": "Damage doubles if the target used Minimize.",
                                "id": "maliciousmoonsault",
                                "name": "Malicious Moonsault",
                                "pp": 1,
                                "priority": 0,
                                "flags": {
                                    "contact": 1
                                },
                                "isZ": "inciniumz",
                                "secondary": None,
                                "target": "normal",
                                "type": "Dark",
                                "contestType": "Cool"
                            },
                            "matblock": {
                                "num": 561,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user and its party members are protected from damaging attacks made by other Pokemon, including allies, during this turn. Fails unless it is the user's first turn on the field, if the user moves last this turn, or if this move is already in effect for the user's side.",
                                "shortDesc": "Protects allies from attacks. First turn out only.",
                                "id": "matblock",
                                "name": "Mat Block",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1,
                                    "nonsky": 1
                                },
                                "stallingMove": True,
                                "sideCondition": "matblock",
                                "secondary": None,
                                "target": "allySide",
                                "type": "Fighting",
                                "zMoveBoost": {
                                    "def": 1
                                },
                                "contestType": "Cool"
                            },
                            "meanlook": {
                                "num": 212,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Prevents the target from switching out. The target can still switch out if it is holding Shed Shell or uses Baton Pass, Parting Shot, U-turn, or Volt Switch. If the target leaves the field using Baton Pass, the replacement will remain trapped. The effect ends if the user leaves the field.",
                                "shortDesc": "Prevents the target from switching out.",
                                "id": "meanlook",
                                "name": "Mean Look",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "spd": 1
                                },
                                "contestType": "Beautiful"
                            },
                            "meditate": {
                                "num": 96,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Raises the user's Attack by 1 stage.",
                                "shortDesc": "Raises the user's Attack by 1.",
                                "id": "meditate",
                                "name": "Meditate",
                                "pp": 40,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1
                                },
                                "boosts": {
                                    "atk": 1,
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Psychic",
                                "zMoveBoost": {
                                    "atk": 1
                                },
                                "contestType": "Beautiful"
                            },
                            "mefirst": {
                                "num": 382,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user uses the move the target chose for use this turn against it, if possible, with its power multiplied by 1.5. The move must be a damaging move other than Beak Blast, Chatter, Counter, Covet, Focus Punch, Me First, Metal Burst, Mirror Coat, Shell Trap, Struggle, Thief, or any Z-Move. Fails if the target moves before the user. Ignores the target's substitute for the purpose of copying the move.",
                                "shortDesc": "Copies a foe at 1.5x power. User must be faster.",
                                "id": "mefirst",
                                "name": "Me First",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "authentic": 1
                                },
                                "secondary": None,
                                "target": "adjacentFoe",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "spe": 2
                                },
                                "contestType": "Clever"
                            },
                            "megadrain": {
                                "num": 72,
                                "accuracy": 100,
                                "basePower": 40,
                                "category": "Special",
                                "desc": "The user recovers 1/2 the HP lost by the target, rounded half up. If Big Root is held by the user, the HP recovered is 1.3x normal, rounded half down.",
                                "shortDesc": "User recovers 50% of the damage dealt.",
                                "id": "megadrain",
                                "name": "Mega Drain",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "heal": 1
                                },
                                "drain": [
                                    1,
                                    2
                                ],
                                "secondary": None,
                                "target": "normal",
                                "type": "Grass",
                                "zMovePower": 120,
                                "contestType": "Clever"
                            },
                            "megahorn": {
                                "num": 224,
                                "accuracy": 85,
                                "basePower": 120,
                                "category": "Physical",
                                "shortDesc": "No additional effect.",
                                "id": "megahorn",
                                "isViable": True,
                                "name": "Megahorn",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Bug",
                                "zMovePower": 190,
                                "contestType": "Cool"
                            },
                            "megakick": {
                                "num": 25,
                                "accuracy": 75,
                                "basePower": 120,
                                "category": "Physical",
                                "shortDesc": "No additional effect.",
                                "id": "megakick",
                                "name": "Mega Kick",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 190,
                                "contestType": "Cool"
                            },
                            "megapunch": {
                                "num": 5,
                                "accuracy": 85,
                                "basePower": 80,
                                "category": "Physical",
                                "shortDesc": "No additional effect.",
                                "id": "megapunch",
                                "name": "Mega Punch",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "powder": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 160,
                                "contestType": "Tough"
                            },
                            "memento": {
                                "num": 262,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Lowers the target's Attack and Special Attack by 2 stages. The user faints unless this move misses or there is no target. Fails entirely if this move hits a substitute, but does not fail if the target's stats cannot be changed.",
                                "shortDesc": "Lowers target's Attack, Sp. Atk by 2. User faints.",
                                "id": "memento",
                                "isViable": True,
                                "name": "Memento",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "boosts": {
                                    "atk": -2,
                                    "spa": -2,
                                },
                                "selfdestruct": "ifHit",
                                "secondary": None,
                                "target": "normal",
                                "type": "Dark",
                                "zMoveEffect": "healreplacement",
                                "contestType": "Tough"
                            },
                            "menacingmoonrazemaelstrom": {
                                "num": 725,
                                "accuracy": True,
                                "basePower": 200,
                                "category": "Special",
                                "desc": "This move and its effects ignore the Abilities of other Pokemon.",
                                "shortDesc": "Ignores the Abilities of other Pokemon.",
                                "id": "menacingmoonrazemaelstrom",
                                "name": "Menacing Moonraze Maelstrom",
                                "pp": 1,
                                "priority": 0,
                                "flags": {},
                                "isZ": "lunaliumz",
                                "ignoreAbility": True,
                                "secondary": None,
                                "target": "normal",
                                "type": "Ghost",
                                "contestType": "Cool"
                            },
                            "metalburst": {
                                "num": 368,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Physical",
                                "desc": "Deals damage to the last opposing Pokemon to hit the user with an attack this turn equal to 1.5 times the HP lost by the user from that attack, rounded down. If the user did not lose HP from the attack, this move deals 1 HP of damage instead. If that opposing Pokemon's position is no longer in use and there is another opposing Pokemon on the field, the damage is done to it instead.Only the last hit of a multi - hit attack is counted.Fails if the user was not hit by an opposing Pokemon's attack this turn.",
                                "shortDesc": "If hit by an attack, returns 1.5x damage.",
                                "id": "metalburst",
                                "name": "Metal Burst",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "scripted",
                                "type": "Steel",
                                "zMovePower": 100,
                                "contestType": "Cool"
                            },
                            "metalclaw": {
                                "num": 232,
                                "accuracy": 95,
                                "basePower": 50,
                                "category": "Physical",
                                "desc": "Has a 10% chance to raise the user's Attack by 1 stage.",
                                "shortDesc": "10% chance to raise the user's Attack by 1.",
                                "id": "metalclaw",
                                "name": "Metal Claw",
                                "pp": 35,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 10,
                                    "self": {
                                        "boosts": {
                                            "atk": 1,
                                        },
                                    },
                                },
                                "target": "normal",
                                "type": "Steel",
                                "zMovePower": 100,
                                "contestType": "Cool"
                            },
                            "metalsound": {
                                "num": 319,
                                "accuracy": 85,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Lowers the target's Special Defense by 2 stages.",
                                "shortDesc": "Lowers the target's Sp. Def by 2.",
                                "id": "metalsound",
                                "name": "Metal Sound",
                                "pp": 40,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "sound": 1,
                                    "authentic": 1,
                                    "mystery": 1
                                },
                                "boosts": {
                                    "spd": -2
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Steel",
                                "zMoveBoost": {
                                    "spa": 1
                                },
                                "contestType": "Clever"
                            },
                            "meteormash": {
                                "num": 309,
                                "accuracy": 90,
                                "basePower": 90,
                                "category": "Physical",
                                "desc": "Has a 20% chance to raise the user's Attack by 1 stage.",
                                "shortDesc": "20% chance to raise the user's Attack by 1.",
                                "id": "meteormash",
                                "isViable": True,
                                "name": "Meteor Mash",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "powder": 1
                                },
                                "secondary": {
                                    "chance": 20,
                                    "self": {
                                        "boosts": {
                                            "atk": 1,
                                        },
                                    },
                                },
                                "target": "normal",
                                "type": "Steel",
                                "zMovePower": 175,
                                "contestType": "Cool"
                            },
                            "metronome": {
                                "num": 118,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "A random move is selected for use, other than After You, Assist, Baneful Bunker, Beak Blast, Belch, Bestow, Celebrate, Chatter, Copycat, Counter, Covet, Crafty Shield, Destiny Bond, Detect, Diamond Storm, Endure, Feint, Fleur Cannon, Focus Punch, Follow Me, Freeze Shock, Helping Hand, Hold Hands, Hyperspace Hole, Ice Burn, Instruct, King's Shield, Light of Ruin, Mat Block, Me First, Metronome, Mimic, Mind Blown, Mirror Coat, Mirror Move, Nature Power, Photon Geyser, Plasma Fists, Protect, Quash, Quick Guard, Rage Powder, Relic Song, Secret Sword, Shell Trap, Sketch, Sleep Talk, Snarl, Snatch, Snore, Spectral Thief, Spiky Shield, Spotlight, Steam Eruption, Struggle, Switcheroo, Techno Blast, Thief, Thousand Arrows, Thousand Waves, Transform, Trick, V - create, or Wide Guard.",
                                "shortDesc": "Picks a random move.",
                                "id": "metronome",
                                "name": "Metronome",
                                "pp": 10,
                                "priority": 0,
                                "flags": {},
                                "noMetronome": [
                                    "afteryou",
                                    "assist",
                                    "banefulbunker",
                                    "beakblast",
                                    "belch",
                                    "bestow",
                                    "celebrate",
                                    "chatter",
                                    "copycat",
                                    "counter",
                                    "covet",
                                    "craftyshield",
                                    "destinybond",
                                    "detect",
                                    "diamondstorm",
                                    "dragonascent",
                                    "endure",
                                    "feint",
                                    "fleurcannon",
                                    "focuspunch",
                                    "followme",
                                    "freezeshock",
                                    "helpinghand",
                                    "holdhands",
                                    "hyperspacefury",
                                    "hyperspacehole",
                                    "iceburn",
                                    "instruct",
                                    "kingsshield",
                                    "lightofruin",
                                    "matblock",
                                    "mefirst",
                                    "metronome",
                                    "mimic",
                                    "mindblown",
                                    "mirrorcoat",
                                    "mirrormove",
                                    "naturepower",
                                    "originpulse",
                                    "photongeyser",
                                    "plasmafists",
                                    "precipiceblades",
                                    "protect",
                                    "quash",
                                    "quickguard",
                                    "ragepowder",
                                    "relicsong",
                                    "secretsword",
                                    "shelltrap",
                                    "sketch",
                                    "sleeptalk",
                                    "snarl",
                                    "snatch",
                                    "snore",
                                    "spectralthief",
                                    "spikyshield",
                                    "spotlight",
                                    "steameruption",
                                    "struggle",
                                    "switcheroo",
                                    "technoblast",
                                    "thief",
                                    "thousandarrows",
                                    "thousandwaves",
                                    "transform",
                                    "trick",
                                    "vcreate",
                                    "wideguard"
                                ],
                                "secondary": None,
                                "target": "self",
                                "type": "Normal",
                                "contestType": "Cute"
                            },
                            "milkdrink": {
                                "num": 208,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user restores 1/2 of its maximum HP, rounded half up.",
                                "shortDesc": "Heals the user by 50% of its max HP.",
                                "id": "milkdrink",
                                "isViable": True,
                                "name": "Milk Drink",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1,
                                    "heal": 1
                                },
                                "heal": [
                                    1,
                                    2
                                ],
                                "secondary": None,
                                "target": "self",
                                "type": "Normal",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Cute"
                            },
                            "mimic": {
                                "num": 102,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "While the user remains active, this move is replaced by the last move used by the target. The copied move has the maximum PP for that move. Fails if the target has not made a move, if the user has Transformed, if the user already knows the move, or if the move is Chatter, Mimic, Sketch, Struggle, Transform, or any Z-Move.",
                                "shortDesc": "The last move the target used replaces this one.",
                                "id": "mimic",
                                "name": "Mimic",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "authentic": 1,
                                    "mystery": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "accuracy": 1
                                },
                                "contestType": "Cute"
                            },
                            "mindblown": {
                                "num": 720,
                                "accuracy": 100,
                                "basePower": 150,
                                "category": "Special",
                                "desc": "Whether or not this move is successful and even if it would cause fainting, the user loses 1/2 of its maximum HP, rounded up, unless the user has the Magic Guard Ability. This move is prevented from executing and the user does not lose HP if any active Pokemon has the Damp Ability, or if this move is Fire type and the user is affected by Powder or the weather is Primordial Sea.",
                                "shortDesc": "User loses 50% max HP. Hits adjacent Pokemon.",
                                "id": "mindblown",
                                "isViable": True,
                                "name": "Mind Blown",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "allAdjacent",
                                "type": "Fire",
                                "zMovePower": 200,
                                "contestType": "Cool"
                            },
                            "mindreader": {
                                "num": 170,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Until the end of the next turn, the target cannot avoid the user's moves, even if the target is in the middle of a two-turn move. The effect ends if either the user or the target leaves the field. Fails if this effect is active for the user.",
                                "shortDesc": "user's next move will not miss the target.",
                                "id": "mindreader",
                                "name": "Mind Reader",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "spa": 1
                                },
                                "contestType": "Clever"
                            },
                            "minimize": {
                                "num": 107,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Raises the user's evasiveness by 2 stages. Whether or not the user's evasiveness was changed, Body Slam, Dragon Rush, Flying Press, Heat Crash, Heavy Slam, Malicious Moonsault, Steamroller, and Stomp will not check 'accuracy' and have their damage doubled if used against the user while it is active.",
                                "shortDesc": "Raises the user's evasiveness by 2.",
                                "id": "minimize",
                                "name": "Minimize",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1
                                },
                                "volatileStatus": "minimize",
                                "secondary": None,
                                "target": "self",
                                "type": "Normal",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Cute"
                            },
                            "miracleeye": {
                                "num": 357,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "As long as the target remains active, its evasiveness stat stage is ignored during 'accuracy' checks against it if it is greater than 0, and Psychic-type attacks can hit the target if it is a Dark type. Fails if the target is already affected, or affected by Foresight or Odor Sleuth.",
                                "shortDesc": "Psychic hits Dark. Evasiveness ignored.",
                                "id": "miracleeye",
                                "name": "Miracle Eye",
                                "pp": 40,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "authentic": 1
                                },
                                "volatileStatus": "miracleeye",
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "zMoveBoost": {
                                    "spa": 1
                                },
                                "contestType": "Clever"
                            },
                            "mirrorcoat": {
                                "num": 243,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Special",
                                "desc": "Deals damage to the last opposing Pokemon to hit the user with a special attack this turn equal to twice the HP lost by the user from that attack. If the user did not lose HP from the attack, this move deals 1 HP of damage instead. If that opposing Pokemon's position is no longer in use and there is another opposing Pokemon on the field, the damage is done to it instead.Only the last hit of a multi - hit attack is counted.Fails if the user was not hit by an opposing Pokemon's special attack this turn.",
                                "shortDesc": "If hit by special attack, returns double damage.",
                                "id": "mirrorcoat",
                                "name": "Mirror Coat",
                                "pp": 20,
                                "priority": -5,
                                "flags": {
                                    "protect": 1
                                },
                                "secondary": None,
                                "target": "scripted",
                                "type": "Psychic",
                                "zMovePower": 100,
                                "contestType": "Beautiful"
                            },
                            "mirrormove": {
                                "num": 119,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user uses the last move used by the target. The copied move is used against that target, if possible. Fails if the target has not made a move, or if the last move used cannot be copied by this move.",
                                "shortDesc": "User uses the target's last used move against it.",
                                "id": "mirrormove",
                                "name": "Mirror Move",
                                "pp": 20,
                                "priority": 0,
                                "flags": {},
                                "secondary": None,
                                "target": "normal",
                                "type": "Flying",
                                "zMoveBoost": {
                                    "atk": 2
                                },
                                "contestType": "Clever"
                            },
                            "mirrorshot": {
                                "num": 429,
                                "accuracy": 85,
                                "basePower": 65,
                                "category": "Special",
                                "desc": "Has a 30% chance to lower the target's 'accuracy' by 1 stage.",
                                "shortDesc": "30% chance to lower the target's 'accuracy' by 1. ",
                                "id": "mirrorshot",
                                "name": "Mirror Shot",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "boosts": {
                                        "accuracy": -1,
                                    },
                                },
                                "target": "normal",
                                "type": "Steel",
                                "zMovePower": 120,
                                "contestType": "Beautiful"
                            },
                            "mist": {
                                "num": 54,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "For 5 turns, the user and its party members are protected from having their stat stages lowered by other Pokemon. Fails if the effect is already active on the user's side.",
                                "shortDesc": "For 5 turns, protects user's party from stat drops.",
                                "id": "mist",
                                "name": "Mist",
                                "pp": 30,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1
                                },
                                "sideCondition": "mist",
                                "secondary": None,
                                "target": "allySide",
                                "type": "Ice",
                                "zMoveEffect": "heal",
                                "contestType": "Beautiful"
                            },
                            "mistball": {
                                "num": 296,
                                "accuracy": 100,
                                "basePower": 70,
                                "category": "Special",
                                "desc": "Has a 50% chance to lower the target's Special Attack by 1 stage.",
                                "shortDesc": "50% chance to lower the target's Sp. Atk by 1.",
                                "id": "mistball",
                                "name": "Mist Ball",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "bullet": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 50,
                                    "boosts": {
                                        "spa": -1,
                                    },
                                },
                                "target": "normal",
                                "type": "Psychic",
                                "zMovePower": 140,
                                "contestType": "Clever"
                            },
                            "mistyterrain": {
                                "num": 581,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "For 5 turns, the terrain becomes Misty Terrain. During the effect, the power of Dragon-type attacks used against grounded Pokemon is multiplied by 0.5 and grounded Pokemon cannot be inflicted with a major status condition nor confusion. Camouflage transforms the user into a Fairy type, Nature Power becomes Moonblast, and Secret Power has a 30% chance to lower Special Attack by 1 stage. Fails if the current terrain is Misty Terrain.",
                                "shortDesc": "5 turns. Can't status, -Dragon power vs grounded.",
                                "id": "mistyterrain",
                                "name": "Misty Terrain",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "nonsky": 1
                                },
                                "terrain": "mistyterrain",
                                "secondary": None,
                                "target": "all",
                                "type": "Fairy",
                                "zMoveBoost": {
                                    "spd": 1
                                },
                                "contestType": "Beautiful"
                            },
                            "moonblast": {
                                "num": 585,
                                "accuracy": 100,
                                "basePower": 95,
                                "category": "Special",
                                "desc": "Has a 30% chance to lower the target's Special Attack by 1 stage.",
                                "shortDesc": "30% chance to lower the target's Sp. Atk by 1.",
                                "id": "moonblast",
                                "isViable": True,
                                "name": "Moonblast",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "boosts": {
                                        "spa": -1,
                                    },
                                },
                                "target": "normal",
                                "type": "Fairy",
                                "zMovePower": 175,
                                "contestType": "Beautiful"
                            },
                            "moongeistbeam": {
                                "num": 714,
                                "accuracy": 100,
                                "basePower": 100,
                                "category": "Special",
                                "desc": "This move and its effects ignore the Abilities of other Pokemon.",
                                "shortDesc": "Ignores the Abilities of other Pokemon.",
                                "id": "moongeistbeam",
                                "isViable": True,
                                "name": "Moongeist Beam",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "ignoreAbility": True,
                                "secondary": None,
                                "target": "normal",
                                "type": "Ghost",
                                "zMovePower": 180,
                                "contestType": "Cool"
                            },
                            "moonlight": {
                                "num": 236,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user restores 1/2 of its maximum HP if Delta Stream or no weather conditions are in effect, 2/3 of its maximum HP if the weather is Desolate Land or Sunny Day, and 1/4 of its maximum HP if the weather is Hail, Primordial Sea, Rain Dance, or Sandstorm, all rounded half down.",
                                "shortDesc": "Heals the user by a weather-dependent amount.",
                                "id": "moonlight",
                                "isViable": True,
                                "name": "Moonlight",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1,
                                    "heal": 1
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Fairy",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Beautiful"
                            },
                            "morningsun": {
                                "num": 234,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user restores 1/2 of its maximum HP if Delta Stream or no weather conditions are in effect, 2/3 of its maximum HP if the weather is Desolate Land or Sunny Day, and 1/4 of its maximum HP if the weather is Hail, Primordial Sea, Rain Dance, or Sandstorm, all rounded half down.",
                                "shortDesc": "Heals the user by a weather-dependent amount.",
                                "id": "morningsun",
                                "isViable": True,
                                "name": "Morning Sun",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1,
                                    "heal": 1
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Normal",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Beautiful"
                            },
                            "mudbomb": {
                                "num": 426,
                                "accuracy": 85,
                                "basePower": 65,
                                "category": "Special",
                                "desc": "Has a 30% chance to lower the target's 'accuracy' by 1 stage.",
                                "shortDesc": "30% chance to lower the target's 'accuracy' by 1.",
                                "id": "mudbomb",
                                "name": "Mud Bomb",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "bullet": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "boosts": {
                                        "accuracy": -1,
                                    },
                                },
                                "target": "normal",
                                "type": "Ground",
                                "zMovePower": 120,
                                "contestType": "Cute"
                            },
                            "mudshot": {
                                "num": 341,
                                "accuracy": 95,
                                "basePower": 55,
                                "category": "Special",
                                "desc": "Has a 100% chance to lower the target's Speed by 1 stage.",
                                "shortDesc": "100% chance to lower the target's Speed by 1.",
                                "id": "mudshot",
                                "name": "Mud Shot",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 100,
                                    "boosts": {
                                        "spe": -1,
                                    },
                                },
                                "target": "normal",
                                "type": "Ground",
                                "zMovePower": 100,
                                "contestType": "Tough"
                            },
                            "mudslap": {
                                "num": 189,
                                "accuracy": 100,
                                "basePower": 20,
                                "category": "Special",
                                "desc": "Has a 100% chance to lower the target's 'accuracy' by 1 stage.",
                                "shortDesc": "100% chance to lower the target's 'accuracy' by 1.",
                                "id": "mudslap",
                                "name": "Mud-Slap",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 100,
                                    "boosts": {
                                        "accuracy": -1,
                                    },
                                },
                                "target": "normal",
                                "type": "Ground",
                                "zMovePower": 100,
                                "contestType": "Cute"
                            },
                            "mudsport": {
                                "num": 300,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "For 5 turns, all Electric-type attacks used by any active Pokemon have their power multiplied by 0.33. Fails if this effect is already active.",
                                "shortDesc": "For 5 turns, Electric-type attacks have 1/3 power.",
                                "id": "mudsport",
                                "name": "Mud Sport",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "nonsky": 1
                                },
                                "pseudoWeather": "mudsport",
                                "secondary": None,
                                "target": "all",
                                "type": "Ground",
                                "zMoveBoost": {
                                    "spd": 1
                                },
                                "contestType": "Cute"
                            },
                            "muddywater": {
                                "num": 330,
                                "accuracy": 85,
                                "basePower": 90,
                                "category": "Special",
                                "desc": "Has a 30% chance to lower the target's 'accuracy' by 1 stage.",
                                "shortDesc": "30% chance to lower the foe(s) 'accuracy' by 1.",
                                "id": "muddywater",
                                "name": "Muddy Water",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "nonsky": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "boosts": {
                                        "accuracy": -1,
                                    },
                                },
                                "target": "allAdjacentFoes",
                                "type": "Water",
                                "zMovePower": 175,
                                "contestType": "Tough"
                            },
                            "multiattack": {
                                "num": 718,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Physical",
                                "desc": "This move's type depends on the user's held Memory.",
                                "shortDesc": "Type varies based on the held Memory.",
                                "id": "multiattack",
                                "isViable": True,
                                "name": "Multi-Attack",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 185,
                                "contestType": "Tough"
                            },
                            "mysticalfire": {
                                "num": 595,
                                "accuracy": 100,
                                "basePower": 75,
                                "category": "Special",
                                "desc": "Has a 100% chance to lower the target's Special Attack by 1 stage.",
                                "shortDesc": "100% chance to lower the target's Sp. Atk by 1.",
                                "id": "mysticalfire",
                                "name": "Mystical Fire",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 100,
                                    "boosts": {
                                        "spa": -1,
                                    },
                                },
                                "target": "normal",
                                "type": "Fire",
                                "zMovePower": 140,
                                "contestType": "Beautiful"
                            },
                            "nastyplot": {
                                "num": 417,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Raises the user's Special Attack by 2 stages.",
                                "shortDesc": "Raises the user's Sp. Atk by 2.",
                                "id": "nastyplot",
                                "isViable": True,
                                "name": "Nasty Plot",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1
                                },
                                "boosts": {
                                    "spa": 2,
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Dark",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Clever"
                            },
                            "naturalgift": {
                                "num": 363,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Physical",
                                "desc": "The type and power of this move depend on the user's held Berry, and the Berry is lost. Fails if the user is not holding a Berry, if the user has the Klutz Ability, or if Embargo or Magic Room is in effect for the user.",
                                "shortDesc": "Power and type depends on the user's Berry.",
                                "id": "naturalgift",
                                "name": "Natural Gift",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 160,
                                "contestType": "Clever"
                            },
                            "naturepower": {
                                "num": 267,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "This move calls another move for use based on the battle terrain. Tri Attack on the regular Wi-Fi terrain, Thunderbolt during Electric Terrain, Moonblast during Misty Terrain, Energy Ball during Grassy Terrain, and Psychic during Psychic Terrain.",
                                "shortDesc": "Attack depends on terrain (default Tri Attack).",
                                "id": "naturepower",
                                "isViable": True,
                                "name": "Nature Power",
                                "pp": 20,
                                "priority": 0,
                                "flags": {},
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "contestType": "Beautiful"
                            },
                            "naturesmadness": {
                                "num": 717,
                                "accuracy": 90,
                                "basePower": 0,
                                "category": "Special",
                                "desc": "Deals damage to the target equal to half of its current HP, rounded down, but not less than 1 HP.",
                                "shortDesc": "Does damage equal to 1/2 target's current HP.",
                                "id": "naturesmadness",
                                "isViable": True,
                                "name": "Nature's Madness ",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Fairy",
                                "zMovePower": 100,
                                "contestType": "Tough"
                            },
                            "needlearm": {
                                "num": 302,
                                "accuracy": 100,
                                "basePower": 60,
                                "category": "Physical",
                                "desc": "Has a 30% chance to flinch the target.",
                                "shortDesc": "30% chance to flinch the target.",
                                "id": "needlearm",
                                "name": "Needle Arm",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "volatileStatus": "flinch"
                                },
                                "target": "normal",
                                "type": "Grass",
                                "zMovePower": 120,
                                "contestType": "Clever"
                            },
                            "neverendingnightmare": {
                                "num": 636,
                                "accuracy": True,
                                "basePower": 1,
                                "category": "Physical",
                                "shortDesc": "Power is equal to the base move's Z-Power.",
                                "id": "neverendingnightmare",
                                "isViable": True,
                                "name": "Never-Ending Nightmare",
                                "pp": 1,
                                "priority": 0,
                                "flags": {},
                                "isZ": "ghostiumz",
                                "secondary": None,
                                "target": "normal",
                                "type": "Ghost",
                                "contestType": "Cool"
                            },
                            "nightdaze": {
                                "num": 539,
                                "accuracy": 95,
                                "basePower": 85,
                                "category": "Special",
                                "desc": "Has a 40% chance to lower the target's 'accuracy' by 1 stage.",
                                "shortDesc": "40% chance to lower the target's 'accuracy' by 1. ",
                                "id": "nightdaze",
                                "name": "Night Daze",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 40,
                                    "boosts": {
                                        "accuracy": -1,
                                    },
                                },
                                "target": "normal",
                                "type": "Dark",
                                "zMovePower": 160,
                                "contestType": "Cool"
                            },
                            "nightmare": {
                                "num": 171,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Causes the target to lose 1/4 of its maximum HP, rounded down, at the end of each turn as long as it is asleep. This move does not affect the target unless it is asleep. The effect ends when the target wakes up, even if it falls asleep again in the same turn.",
                                "shortDesc": "A sleeping target is hurt by 1/4 max HP per turn.",
                                "id": "nightmare",
                                "name": "Nightmare",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "volatileStatus": "nightmare",
                                "secondary": None,
                                "target": "normal",
                                "type": "Ghost",
                                "zMoveBoost": {
                                    "spa": 1
                                },
                                "contestType": "Clever"
                            },
                            "nightshade": {
                                "num": 101,
                                "accuracy": 100,
                                "basePower": 0,
                                "damage": "level",
                                "category": "Special",
                                "desc": "Deals damage to the target equal to the user's level.",
                                "shortDesc": "Does damage equal to the user's level.",
                                "id": "nightshade",
                                "isViable": True,
                                "name": "Night Shade",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Ghost",
                                "zMovePower": 100,
                                "contestType": "Clever"
                            },
                            "nightslash": {
                                "num": 400,
                                "accuracy": 100,
                                "basePower": 70,
                                "category": "Physical",
                                "desc": "Has a higher chance for a critical hit.",
                                "shortDesc": "High critical hit ratio.",
                                "id": "nightslash",
                                "isViable": True,
                                "name": "Night Slash",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "critRatio": 2,
                                "secondary": None,
                                "target": "normal",
                                "type": "Dark",
                                "zMovePower": 140,
                                "contestType": "Cool"
                            },
                            "nobleroar": {
                                "num": 568,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Lowers the target's Attack and Special Attack by 1 stage.",
                                "shortDesc": "Lowers the target's Attack and Sp. Atk by 1.",
                                "id": "nobleroar",
                                "name": "Noble Roar",
                                "pp": 30,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "sound": 1,
                                    "authentic": 1
                                },
                                "boosts": {
                                    "atk": -1,
                                    "spa": -1,
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "def": 1
                                },
                                "contestType": "Tough"
                            },
                            "nuzzle": {
                                "num": 609,
                                "accuracy": 100,
                                "basePower": 20,
                                "category": "Physical",
                                "desc": "Has a 100% chance to paralyze the target.",
                                "shortDesc": "100% chance to paralyze the target.",
                                "id": "nuzzle",
                                "isViable": True,
                                "name": "Nuzzle",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 100,
                                    "status": "par",
                                },
                                "target": "normal",
                                "type": "Electric",
                                "zMovePower": 100,
                                "contestType": "Cute"
                            },
                            "oblivionwing": {
                                "num": 613,
                                "accuracy": 100,
                                "basePower": 80,
                                "category": "Special",
                                "desc": "The user recovers 3/4 the HP lost by the target, rounded half up. If Big Root is held by the user, the HP recovered is 1.3x normal, rounded half down.",
                                "shortDesc": "User recovers 75% of the damage dealt.",
                                "id": "oblivionwing",
                                "isViable": True,
                                "name": "Oblivion Wing",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "distance": 1,
                                    "heal": 1
                                },
                                "drain": [
                                    3,
                                    4
                                ],
                                "secondary": None,
                                "target": "any",
                                "type": "Flying",
                                "zMovePower": 160,
                                "contestType": "Cool"
                            },
                            "oceanicoperetta": {
                                "num": 697,
                                "accuracy": True,
                                "basePower": 195,
                                "category": "Special",
                                "shortDesc": "No additional effect.",
                                "id": "oceanicoperetta",
                                "name": "Oceanic Operetta",
                                "pp": 1,
                                "priority": 0,
                                "flags": {},
                                "isZ": "primariumz",
                                "secondary": None,
                                "target": "normal",
                                "type": "Water",
                                "contestType": "Cool"
                            },
                            "octazooka": {
                                "num": 190,
                                "accuracy": 85,
                                "basePower": 65,
                                "category": "Special",
                                "desc": "Has a 50% chance to lower the target's 'accuracy' by 1 stage.",
                                "shortDesc": "50% chance to lower the target's 'accuracy' by 1. ",
                                "id": "octazooka",
                                "name": "Octazooka",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "bullet": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 50,
                                    "boosts": {
                                        "accuracy": -1,
                                    },
                                },
                                "target": "normal",
                                "type": "Water",
                                "zMovePower": 120,
                                "contestType": "Tough"
                            },
                            "odorsleuth": {
                                "num": 316,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "As long as the target remains active, its evasiveness stat stage is ignored during 'accuracy' checks against it if it is greater than 0, and Normal - and Fighting - type attacks can hit the target if it is a Ghost type.Fails if the target is already affected, or affected by Foresight or Miracle Eye.",
                                "shortDesc": "Fighting, Normal hit Ghost. Evasiveness ignored.",
                                "id": "odorsleuth",
                                "name": "Odor Sleuth",
                                "pp": 40,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "authentic": 1,
                                    "mystery": 1
                                },
                                "volatileStatus": "foresight",
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "atk": 1
                                },
                                "contestType": "Clever"
                            },
                            "ominouswind": {
                                "num": 466,
                                "accuracy": 100,
                                "basePower": 60,
                                "category": "Special",
                                "desc": "Has a 10% chance to raise the user's Attack, Defense, Special Attack, Special Defense, and Speed by 1 stage.",
                                "shortDesc": "10% chance to raise all stats by 1 (not acc/eva).",
                                "id": "ominouswind",
                                "name": "Ominous Wind",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 10,
                                    "self": {
                                        "boosts": {
                                            "atk": 1,
                                            "def": 1,
                                            "spa": 1,
                                            "spd": 1,
                                            "spe": 1
                                        },
                                    },
                                },
                                "target": "normal",
                                "type": "Ghost",
                                "zMovePower": 120,
                                "contestType": "Beautiful"
                            },
                            "originpulse": {
                                "num": 618,
                                "accuracy": 85,
                                "basePower": 110,
                                "category": "Special",
                                "desc": "No additional effect.",
                                "shortDesc": "No additional effect. Hits adjacent foes.",
                                "id": "originpulse",
                                "isViable": True,
                                "name": "Origin Pulse",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "pulse": 1,
                                    "mirror": 1
                                },
                                "target": "allAdjacentFoes",
                                "type": "Water",
                                "zMovePower": 185,
                                "contestType": "Beautiful"
                            },
                            "outrage": {
                                "num": 200,
                                "accuracy": 100,
                                "basePower": 120,
                                "category": "Physical",
                                "desc": "The user spends two or three turns locked into this move and becomes confused immediately after its move on the last turn of the effect if it is not already. This move targets an opposing Pokemon at random on each turn. If the user is prevented from moving, is asleep at the beginning of a turn, or the attack is not successful against the target on the first turn of the effect or the second turn of a three-turn effect, the effect ends without causing confusion. If this move is called by Sleep Talk and the user is asleep, the move is used for one turn and does not confuse the user.",
                                "shortDesc": "Lasts 2-3 turns. Confuses the user afterwards.",
                                "id": "outrage",
                                "isViable": True,
                                "name": "Outrage",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "self": {
                                    "volatileStatus": "lockedmove",
                                },
                                "secondary": None,
                                "target": "randomNormal",
                                "type": "Dragon",
                                "zMovePower": 190,
                                "contestType": "Cool"
                            },
                            "overheat": {
                                "num": 315,
                                "accuracy": 90,
                                "basePower": 130,
                                "category": "Special",
                                "desc": "Lowers the user's Special Attack by 2 stages.",
                                "shortDesc": "Lowers the user's Sp. Atk by 2.",
                                "id": "overheat",
                                "isViable": True,
                                "name": "Overheat",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "self": {
                                    "boosts": {
                                        "spa": -2,
                                    },
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Fire",
                                "zMovePower": 195,
                                "contestType": "Beautiful"
                            },
                            "painsplit": {
                                "num": 220,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user and the target's HP become the average of their current HP, rounded down, but not more than the maximum HP of either one.",
                                "shortDesc": "Shares HP of user and target equally.",
                                "id": "painsplit",
                                "isViable": True,
                                "name": "Pain Split",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "mystery": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "def": 1
                                },
                                "contestType": "Clever"
                            },
                            "paleowave": {
                                "num": 0,
                                "accuracy": 100,
                                "basePower": 85,
                                "category": "Special",
                                "desc": "Has a 20% chance to lower the target's Attack by 1 stage.",
                                "shortDesc": "20% chance to lower the target's Attack by 1.",
                                "id": "paleowave",
                                "isNonstandard": "CAP",
                                "isViable": True,
                                "name": "Paleo Wave",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 20,
                                    "boosts": {
                                        "atk": -1
                                    },
                                },
                                "target": "normal",
                                "type": "Rock",
                                "zMovePower": 160,
                                "contestType": "Beautiful"
                            },
                            "paraboliccharge": {
                                "num": 570,
                                "accuracy": 100,
                                "basePower": 65,
                                "category": "Special",
                                "desc": "The user recovers 1/2 the HP lost by the target, rounded half up. If Big Root is held by the user, the HP recovered is 1.3x normal, rounded half down.",
                                "shortDesc": "User recovers 50% of the damage dealt.",
                                "id": "paraboliccharge",
                                "name": "Parabolic Charge",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "heal": 1
                                },
                                "drain": [
                                    1,
                                    2
                                ],
                                "secondary": None,
                                "target": "allAdjacent",
                                "type": "Electric",
                                "zMovePower": 120,
                                "contestType": "Clever"
                            },
                            "partingshot": {
                                "num": 575,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Lowers the target's Attack and Special Attack by 1 stage. If this move is successful, the user switches out even if it is trapped and is replaced immediately by a selected party member. The user does not switch out if the target's Attack and Special Attack stat stages were both unchanged, or if there are no unfainted party members.",
                                "shortDesc": "Lowers target's Atk, Sp. Atk by 1. User switches.",
                                "id": "partingshot",
                                "isViable": True,
                                "name": "Parting Shot",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "sound": 1,
                                    "authentic": 1
                                },
                                "selfSwitch": True,
                                "boosts": {
                                    "atk": -1,
                                    "spa": -1,
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Dark",
                                "zMoveEffect": "healreplacement",
                                "contestType": "Cool"
                            },
                            "payback": {
                                "num": 371,
                                "accuracy": 100,
                                "basePower": 50,
                                "category": "Physical",
                                "desc": "Power doubles if the user moves after the target this turn, including actions taken through Instruct or the Dancer Ability. Switching in does not count as an action.",
                                "shortDesc": "Power doubles if the user moves after the target.",
                                "id": "payback",
                                "name": "Payback",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Dark",
                                "zMovePower": 100,
                                "contestType": "Tough"
                            },
                            "payday": {
                                "num": 6,
                                "accuracy": 100,
                                "basePower": 40,
                                "category": "Physical",
                                "desc": "No additional effect.",
                                "shortDesc": "Scatters coins.",
                                "id": "payday",
                                "name": "Pay Day",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 100,
                                "contestType": "Clever"
                            },
                            "peck": {
                                "num": 64,
                                "accuracy": 100,
                                "basePower": 35,
                                "category": "Physical",
                                "shortDesc": "No additional effect.",
                                "id": "peck",
                                "name": "Peck",
                                "pp": 35,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "distance": 1
                                },
                                "secondary": None,
                                "target": "any",
                                "type": "Flying",
                                "zMovePower": 100,
                                "contestType": "Cool"
                            },
                            "perishsong": {
                                "num": 195,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Each active Pokemon receives a perish count of 4 if it doesn't already have a perish count.At the end of each turn including the turn used, the perish count of all active Pokemon lowers by 1 and Pokemon faint if the number reaches 0. The perish count is removed from Pokemon that switch out.If a Pokemon uses Baton Pass while it has a perish count, the replacement will gain the perish count and continue to count down.",
                                "shortDesc": "All active Pokemon will faint in 3 turns.",
                                "id": "perishsong",
                                "isViable": True,
                                "name": "Perish Song",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "sound": 1,
                                    "distance": 1,
                                    "authentic": 1
                                },
                                "secondary": None,
                                "target": "all",
                                "type": "Normal",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Beautiful"
                            },
                            "petalblizzard": {
                                "num": 572,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Physical",
                                "desc": "No additional effect.",
                                "shortDesc": "No additional effect. Hits adjacent Pokemon.",
                                "id": "petalblizzard",
                                "isViable": True,
                                "name": "Petal Blizzard",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "allAdjacent",
                                "type": "Grass",
                                "zMovePower": 175,
                                "contestType": "Beautiful"
                            },
                            "petaldance": {
                                "num": 80,
                                "accuracy": 100,
                                "basePower": 120,
                                "category": "Special",
                                "desc": "The user spends two or three turns locked into this move and becomes confused immediately after its move on the last turn of the effect if it is not already. This move targets an opposing Pokemon at random on each turn. If the user is prevented from moving, is asleep at the beginning of a turn, or the attack is not successful against the target on the first turn of the effect or the second turn of a three-turn effect, the effect ends without causing confusion. If this move is called by Sleep Talk and the user is asleep, the move is used for one turn and does not confuse the user.",
                                "shortDesc": "Lasts 2-3 turns. Confuses the user afterwards.",
                                "id": "petaldance",
                                "name": "Petal Dance",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "dance": 1
                                },
                                "self": {
                                    "volatileStatus": "lockedmove",
                                },
                                "secondary": None,
                                "target": "randomNormal",
                                "type": "Grass",
                                "zMovePower": 190,
                                "contestType": "Beautiful"
                            },
                            "phantomforce": {
                                "num": 566,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Physical",
                                "desc": "If this move is successful, it breaks through the target's Baneful Bunker, Detect, King's Shield, Protect, or Spiky Shield for this turn, allowing other Pokemon to attack the target normally.If the target 's side is protected by Crafty Shield, Mat Block, Quick Guard, or Wide Guard, that protection is also broken for this turn and other Pokemon may attack the target's side normally.This attack charges on the first turn and executes on the second.On the first turn, the user avoids all attacks.If the user is holding a Power Herb, the move completes in one turn.",
                                "shortDesc": "Disappears turn 1. Hits turn 2. Breaks protection.",
                                "id": "phantomforce",
                                "name": "Phantom Force",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "charge": 1,
                                    "mirror": 1
                                },
                                "breaksProtect": True,
                                "secondary": None,
                                "target": "normal",
                                "type": "Ghost",
                                "zMovePower": 175,
                                "contestType": "Cool"
                            },
                            "photongeyser": {
                                "num": 722,
                                "accuracy": 100,
                                "basePower": 100,
                                "category": "Special",
                                "desc": "This move becomes a physical attack if the user's Attack is greater than its Special Attack, including stat stage changes. This move and its effects ignore the Abilities of other Pokemon.",
                                "shortDesc": "Physical if user's Atk > Sp. Atk. Ignores Abilities.",
                                "id": "photongeyser",
                                "isViable": True,
                                "name": "Photon Geyser",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "ignoreAbility": True,
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "zMovePower": 180,
                                "contestType": "Cool"
                            },
                            "pikapapow": {
                                "num": 732,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Special",
                                "desc": "Power is equal to the greater of (user's Happiness * 2/5), rounded down, or 1.",
                                "shortDesc": "Max happiness: 102 power. Can't miss.",
                                "id": "pikapapow",
                                "isNonstandard": "LGPE",
                                "isUnreleased": True,
                                "isViable": True,
                                "name": "Pika Papow",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Electric",
                                "contestType": "Cute"
                            },
                            "pinmissile": {
                                "num": 42,
                                "accuracy": 95,
                                "basePower": 25,
                                "category": "Physical",
                                "desc": "Hits two to five times. Has a 1/3 chance to hit two or three times, and a 1/6 chance to hit four or five times. If one of the hits breaks the target's substitute, it will take damage for the remaining hits. If the user has the Skill Link Ability, this move will always hit five times.",
                                "shortDesc": "Hits 2-5 times in one turn.",
                                "id": "pinmissile",
                                "name": "Pin Missile",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "multihit": [
                                    2,
                                    5
                                ],
                                "secondary": None,
                                "target": "normal",
                                "type": "Bug",
                                "zMovePower": 140,
                                "contestType": "Cool"
                            },
                            "plasmafists": {
                                "num": 721,
                                "accuracy": 100,
                                "basePower": 100,
                                "category": "Physical",
                                "desc": "If this move is successful, causes Normal-type moves to become Electric type this turn.",
                                "shortDesc": "Normal moves become Electric type this turn.",
                                "id": "plasmafists",
                                "isViable": True,
                                "name": "Plasma Fists",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "powder": 1
                                },
                                "pseudoWeather": "iondeluge",
                                "secondary": None,
                                "target": "normal",
                                "type": "Electric",
                                "zMovePower": 180,
                                "contestType": "Cool"
                            },
                            "playnice": {
                                "num": 589,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Lowers the target's Attack by 1 stage.",
                                "shortDesc": "Lowers the target's Attack by 1.",
                                "id": "playnice",
                                "name": "Play Nice",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "authentic": 1
                                },
                                "boosts": {
                                    "atk": -1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "def": 1
                                },
                                "contestType": "Cute"
                            },
                            "playrough": {
                                "num": 583,
                                "accuracy": 90,
                                "basePower": 90,
                                "category": "Physical",
                                "desc": "Has a 10% chance to lower the target's Attack by 1 stage.",
                                "shortDesc": "10% chance to lower the target's Attack by 1.",
                                "id": "playrough",
                                "isViable": True,
                                "name": "Play Rough",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 10,
                                    "boosts": {
                                        "atk": -1
                                    },
                                },
                                "target": "normal",
                                "type": "Fairy",
                                "zMovePower": 175,
                                "contestType": "Cute"
                            },
                            "pluck": {
                                "num": 365,
                                "accuracy": 100,
                                "basePower": 60,
                                "category": "Physical",
                                "desc": "If this move is successful and the user has not fainted, it steals the target's held Berry if it is holding one and eats it immediately, gaining its effects even if the user's item is being ignored. Items lost to this move cannot be regained with Recycle or the Harvest Ability.",
                                "shortDesc": "User steals and eats the target's Berry.",
                                "id": "pluck",
                                "name": "Pluck",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "distance": 1
                                },
                                "secondary": None,
                                "target": "any",
                                "type": "Flying",
                                "zMovePower": 120,
                                "contestType": "Cute"
                            },
                            "poisonfang": {
                                "num": 305,
                                "accuracy": 100,
                                "basePower": 50,
                                "category": "Physical",
                                "desc": "Has a 50% chance to badly poison the target.",
                                "shortDesc": "50% chance to badly poison the target.",
                                "id": "poisonfang",
                                "name": "Poison Fang",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "bite": 1,
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 50,
                                    "status": "tox",
                                },
                                "target": "normal",
                                "type": "Poison",
                                "zMovePower": 100,
                                "contestType": "Clever"
                            },
                            "poisongas": {
                                "num": 139,
                                "accuracy": 90,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Poisons the target.",
                                "shortDesc": "Poisons the foe(s).",
                                "id": "poisongas",
                                "name": "Poison Gas",
                                "pp": 40,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "status": "psn",
                                "secondary": None,
                                "target": "allAdjacentFoes",
                                "type": "Poison",
                                "zMoveBoost": {
                                    "def": 1
                                },
                                "contestType": "Clever"
                            },
                            "poisonjab": {
                                "num": 398,
                                "accuracy": 100,
                                "basePower": 80,
                                "category": "Physical",
                                "desc": "Has a 30% chance to poison the target.",
                                "shortDesc": "30% chance to poison the target.",
                                "id": "poisonjab",
                                "isViable": True,
                                "name": "Poison Jab",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "status": "psn",
                                },
                                "target": "normal",
                                "type": "Poison",
                                "zMovePower": 160,
                                "contestType": "Tough"
                            },
                            "poisonpowder": {
                                "num": 77,
                                "accuracy": 75,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Poisons the target.",
                                "shortDesc": "Poisons the target.",
                                "id": "poisonpowder",
                                "name": "Poison Powder",
                                "pp": 35,
                                "priority": 0,
                                "flags": {
                                    "powder": 1,
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "status": "psn",
                                "secondary": None,
                                "target": "normal",
                                "type": "Poison",
                                "zMoveBoost": {
                                    "def": 1
                                },
                                "contestType": "Clever"
                            },
                            "poisonsting": {
                                "num": 40,
                                "accuracy": 100,
                                "basePower": 15,
                                "category": "Physical",
                                "desc": "Has a 30% chance to poison the target.",
                                "shortDesc": "30% chance to poison the target.",
                                "id": "poisonsting",
                                "name": "Poison Sting",
                                "pp": 35,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "status": "psn",
                                },
                                "target": "normal",
                                "type": "Poison",
                                "zMovePower": 100,
                                "contestType": "Clever"
                            },
                            "poisontail": {
                                "num": 342,
                                "accuracy": 100,
                                "basePower": 50,
                                "category": "Physical",
                                "desc": "Has a 10% chance to poison the target and a higher chance for a critical hit.",
                                "shortDesc": "High critical hit ratio. 10% chance to poison.",
                                "id": "poisontail",
                                "name": "Poison Tail",
                                "pp": 25,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "critRatio": 2,
                                "secondary": {
                                    "chance": 10,
                                    "status": "psn",
                                },
                                "target": "normal",
                                "type": "Poison",
                                "zMovePower": 100,
                                "contestType": "Clever"
                            },
                            "pollenpuff": {
                                "num": 676,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Special",
                                "desc": "If the target is an ally, this move restores 1/2 of its maximum HP, rounded down, instead of dealing damage.",
                                "shortDesc": "If the target is an ally, heals 50% of its max HP.",
                                "id": "pollenpuff",
                                "name": "Pollen Puff",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "bullet": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Bug",
                                "zMovePower": 175,
                                "contestType": "Cute"
                            },
                            "pound": {
                                "num": 1,
                                "accuracy": 100,
                                "basePower": 40,
                                "category": "Physical",
                                "shortDesc": "No additional effect.",
                                "id": "pound",
                                "name": "Pound",
                                "pp": 35,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 100,
                                "contestType": "Tough"
                            },
                            "powder": {
                                "num": 600,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "If the target uses a Fire-type move this turn, it is prevented from executing and the target loses 1/4 of its maximum HP, rounded half up. This effect does not happen if the Fire-type move is prevented by Primordial Sea.",
                                "shortDesc": "If using a Fire move, target loses 1/4 max HP.",
                                "id": "powder",
                                "name": "Powder",
                                "pp": 20,
                                "priority": 1,
                                "flags": {
                                    "powder": 1,
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "authentic": 1
                                },
                                "volatileStatus": "powder",
                                "secondary": None,
                                "target": "normal",
                                "type": "Bug",
                                "zMoveBoost": {
                                    "spd": 2
                                },
                                "contestType": "Clever"
                            },
                            "powdersnow": {
                                "num": 181,
                                "accuracy": 100,
                                "basePower": 40,
                                "category": "Special",
                                "desc": "Has a 10% chance to freeze the target.",
                                "shortDesc": "10% chance to freeze the foe(s).",
                                "id": "powdersnow",
                                "name": "Powder Snow",
                                "pp": 25,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 10,
                                    "status": "frz",
                                },
                                "target": "allAdjacentFoes",
                                "type": "Ice",
                                "zMovePower": 100,
                                "contestType": "Beautiful"
                            },
                            "powergem": {
                                "num": 408,
                                "accuracy": 100,
                                "basePower": 80,
                                "category": "Special",
                                "shortDesc": "No additional effect.",
                                "id": "powergem",
                                "isViable": True,
                                "name": "Power Gem",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Rock",
                                "zMovePower": 160,
                                "contestType": "Beautiful"
                            },
                            "powersplit": {
                                "num": 471,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user and the target have their Attack and Special Attack stats set to be equal to the average of the user and the target's Attack and Special Attack stats, respectively, rounded down. Stat stage changes are unaffected.",
                                "shortDesc": "Averages Attack and Sp. Atk stats with target.",
                                "id": "powersplit",
                                "name": "Power Split",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mystery": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "zMoveBoost": {
                                    "spe": 1
                                },
                                "contestType": "Clever"
                            },
                            "powerswap": {
                                "num": 384,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user swaps its Attack and Special Attack stat stage changes with the target.",
                                "shortDesc": "Swaps Attack and Sp. Atk stat stages with target.",
                                "id": "powerswap",
                                "name": "Power Swap",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "authentic": 1,
                                    "mystery": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "zMoveBoost": {
                                    "spe": 1
                                },
                                "contestType": "Clever"
                            },
                            "powertrick": {
                                "num": 379,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user swaps its Attack and Defense stats, and stat stage changes remain on their respective stats. This move can be used again to swap the stats back. If the user uses Baton Pass, the replacement will have its Attack and Defense stats swapped if the effect is active. If the user has its stats recalculated by changing forme while its stats are swapped, this effect is ignored but is still active for the purposes of Baton Pass.",
                                "shortDesc": "Switches user's Attack and Defense stats.",
                                "id": "powertrick",
                                "name": "Power Trick",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1
                                },
                                "volatileStatus": "powertrick",
                                "secondary": None,
                                "target": "self",
                                "type": "Psychic",
                                "zMoveBoost": {
                                    "atk": 1
                                },
                                "contestType": "Clever"
                            },
                            "powertrip": {
                                "num": 681,
                                "accuracy": 100,
                                "basePower": 20,
                                "category": "Physical",
                                "desc": "Power is equal to 20+(X*20), where X is the user's total stat stage changes that are greater than 0.",
                                "shortDesc": " + 20 power for each of the user's stat boosts.",
                                "id": "powertrip",
                                "name": "Power Trip",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Dark",
                                "zMovePower": 160,
                                "contestType": "Clever"
                            },
                            "poweruppunch": {
                                "num": 612,
                                "accuracy": 100,
                                "basePower": 40,
                                "category": "Physical",
                                "desc": "Has a 100% chance to raise the user's Attack by 1 stage.",
                                "shortDesc": "100% chance to raise the user's Attack by 1.",
                                "id": "poweruppunch",
                                "isViable": True,
                                "name": "Power-Up Punch",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "powder": 1
                                },
                                "secondary": {
                                    "chance": 100,
                                    "self": {
                                        "boosts": {
                                            "atk": 1,
                                        },
                                    },
                                },
                                "target": "normal",
                                "type": "Fighting",
                                "zMovePower": 100,
                                "contestType": "Tough"
                            },
                            "powerwhip": {
                                "num": 438,
                                "accuracy": 85,
                                "basePower": 120,
                                "category": "Physical",
                                "shortDesc": "No additional effect.",
                                "id": "powerwhip",
                                "isViable": True,
                                "name": "Power Whip",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Grass",
                                "zMovePower": 190,
                                "contestType": "Tough"
                            },
                            "precipiceblades": {
                                "num": 619,
                                "accuracy": 85,
                                "basePower": 120,
                                "category": "Physical",
                                "desc": "No additional effect.",
                                "shortDesc": "No additional effect. Hits adjacent foes.",
                                "id": "precipiceblades",
                                "isViable": True,
                                "name": "Precipice Blades",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "nonsky": 1
                                },
                                "target": "allAdjacentFoes",
                                "type": "Ground",
                                "zMovePower": 190,
                                "contestType": "Cool"
                            },
                            "present": {
                                "num": 217,
                                "accuracy": 90,
                                "basePower": 0,
                                "category": "Physical",
                                "desc": "If this move is successful, it deals damage or heals the target. 40% chance for 40 power, 30% chance for 80 power, 10% chance for 120 power, and 20% chance to heal the target by 1/4 of its maximum HP, rounded down.",
                                "shortDesc": "40, 80, 120 power, or heals target 1/4 max HP.",
                                "id": "present",
                                "name": "Present",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 100,
                                "contestType": "Cute"
                            },
                            "prismaticlaser": {
                                "num": 711,
                                "accuracy": 100,
                                "basePower": 160,
                                "category": "Special",
                                "desc": "If this move is successful, the user must recharge on the following turn and cannot select a move.",
                                "shortDesc": "User cannot move next turn.",
                                "id": "prismaticlaser",
                                "name": "Prismatic Laser",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "recharge": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "self": {
                                    "volatileStatus": "mustrecharge",
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "zMovePower": 200,
                                "contestType": "Cool"
                            },
                            "protect": {
                                "num": 182,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user is protected from most attacks made by other Pokemon during this turn. This move has a 1/X chance of being successful, where X starts at 1 and triples each time this move is successfully used. X resets to 1 if this move fails, if the user's last move used is not Baneful Bunker, Detect, Endure, King's Shield, Protect, Quick Guard, Spiky Shield, or Wide Guard, o if it was one of those moves and the user 's protection was broken. Fails if the user moves last this turn.",
                                "shortDesc": "Prevents moves from affecting the user this turn.",
                                "id": "protect",
                                "isViable": True,
                                "name": "Protect",
                                "pp": 10,
                                "priority": 4,
                                "flags": {},
                                "stallingMove": True,
                                "volatileStatus": "protect",
                                "secondary": None,
                                "target": "self",
                                "type": "Normal",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Cute"
                            },
                            "psybeam": {
                                "num": 60,
                                "accuracy": 100,
                                "basePower": 65,
                                "category": "Special",
                                "desc": "Has a 10% chance to confuse the target.",
                                "shortDesc": "10% chance to confuse the target.",
                                "id": "psybeam",
                                "name": "Psybeam",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 10,
                                    "volatileStatus": "confusion",
                                },
                                "target": "normal",
                                "type": "Psychic",
                                "zMovePower": 120,
                                "contestType": "Beautiful"
                            },
                            "psychup": {
                                "num": 244,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user copies all of the target's current stat stage changes.",
                                "shortDesc": "Copies the target's current stat stages.",
                                "id": "psychup",
                                "name": "Psych Up",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "authentic": 1,
                                    "mystery": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveEffect": "heal",
                                "contestType": "Clever"
                            },
                            "psychic": {
                                "num": 94,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Special",
                                "desc": "Has a 10% chance to lower the target's Special Defense by 1 stage.",
                                "shortDesc": "10% chance to lower the target's Sp. Def by 1.",
                                "id": "psychic",
                                "isViable": True,
                                "name": "Psychic",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 10,
                                    "boosts": {
                                        "spd": -1
                                    },
                                },
                                "target": "normal",
                                "type": "Psychic",
                                "zMovePower": 175,
                                "contestType": "Clever"
                            },
                            "psychicfangs": {
                                "num": 706,
                                "accuracy": 100,
                                "basePower": 85,
                                "category": "Physical",
                                "desc": "If this attack does not miss, the effects of Reflect, Light Screen, and Aurora Veil end for the target's side of the field before damage is calculated.",
                                "shortDesc": "Destroys screens, unless the target is immune.",
                                "id": "psychicfangs",
                                "isViable": True,
                                "name": "Psychic Fangs",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "bite": 1,
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "zMovePower": 160,
                                "contestType": "Clever"
                            },
                            "psychicterrain": {
                                "num": 678,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "For 5 turns, the terrain becomes Psychic Terrain. During the effect, the power of Psychic-type attacks made by grounded Pokemon is multiplied by 1.5 and grounded Pokemon cannot be hit by moves with priority greater than 0, unless the target is an ally. Camouflage transforms the user into a Psychic type, Nature Power becomes Psychic, and Secret Power has a 30% chance to lower the target's Speed by 1 stage. Fails if the current terrain is Psychic Terrain.",
                                "shortDesc": "5 turns. Grounded: +Psychic power, priority-safe.",
                                "id": "psychicterrain",
                                "name": "Psychic Terrain",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "nonsky": 1
                                },
                                "terrain": "psychicterrain",
                                "secondary": None,
                                "target": "all",
                                "type": "Psychic",
                                "zMoveBoost": {
                                    "spa": 1
                                },
                                "contestType": "Clever"
                            },
                            "psychoboost": {
                                "num": 354,
                                "accuracy": 90,
                                "basePower": 140,
                                "category": "Special",
                                "desc": "Lowers the user's Special Attack by 2 stages.",
                                "shortDesc": "Lowers the user's Sp. Atk by 2.",
                                "id": "psychoboost",
                                "isViable": True,
                                "name": "Psycho Boost",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "self": {
                                    "boosts": {
                                        "spa": -2,
                                    },
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "zMovePower": 200,
                                "contestType": "Clever"
                            },
                            "psychocut": {
                                "num": 427,
                                "accuracy": 100,
                                "basePower": 70,
                                "category": "Physical",
                                "desc": "Has a higher chance for a critical hit.",
                                "shortDesc": "High critical hit ratio.",
                                "id": "psychocut",
                                "isViable": True,
                                "name": "Psycho Cut",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "critRatio": 2,
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "zMovePower": 140,
                                "contestType": "Cool"
                            },
                            "psychoshift": {
                                "num": 375,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user's major status condition is transferred to the target, and the user is then cured. Fails if the user has no major status condition or if the target already has one.",
                                "shortDesc": "Transfers the user's status ailment to the target.",
                                "id": "psychoshift",
                                "name": "Psycho Shift",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "zMoveBoost": {
                                    "spa": 2
                                },
                                "contestType": "Clever"
                            },
                            "psyshock": {
                                "num": 473,
                                "accuracy": 100,
                                "basePower": 80,
                                "category": "Special",
                                "defensivecategory": "Physical",
                                "desc": "Deals damage to the target based on its Defense instead of Special Defense.",
                                "shortDesc": "Damages target based on Defense, not Sp. Def.",
                                "id": "psyshock",
                                "isViable": True,
                                "name": "Psyshock",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "zMovePower": 160,
                                "contestType": "Beautiful"
                            },
                            "psystrike": {
                                "num": 540,
                                "accuracy": 100,
                                "basePower": 100,
                                "category": "Special",
                                "defensivecategory": "Physical",
                                "desc": "Deals damage to the target based on its Defense instead of Special Defense.",
                                "shortDesc": "Damages target based on Defense, not Sp. Def.",
                                "id": "psystrike",
                                "isViable": True,
                                "name": "Psystrike",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "zMovePower": 180,
                                "contestType": "Cool"
                            },
                            "psywave": {
                                "num": 149,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Special",
                                "desc": "Deals damage to the target equal to (user's level) * (X + 50) / 100, where X is a random number from 0 to 100, rounded down, but not less than 1 HP.",
                                "shortDesc": "Random damage equal to 0.5x-1.5x user's level.",
                                "id": "psywave",
                                "name": "Psywave",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "zMovePower": 100,
                                "contestType": "Clever"
                            },
                            "pulverizingpancake": {
                                "num": 701,
                                "accuracy": True,
                                "basePower": 210,
                                "category": "Physical",
                                "shortDesc": "No additional effect.",
                                "id": "pulverizingpancake",
                                "name": "Pulverizing Pancake",
                                "pp": 1,
                                "priority": 0,
                                "flags": {
                                    "contact": 1
                                },
                                "isZ": "snorliumz",
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "contestType": "Cool"
                            },
                            "punishment": {
                                "num": 386,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Physical",
                                "desc": "Power is equal to 60+(X*20), where X is the target's total stat stage changes that are greater than 0, but not more than 200 power.",
                                "shortDesc": "60 power +20 for each of the target's stat boosts.",
                                "id": "punishment",
                                "name": "Punishment",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Dark",
                                "zMovePower": 160,
                                "contestType": "Cool"
                            },
                            "purify": {
                                "num": 685,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The target is cured if it has a major status condition. If the target was cured, the user restores 1/2 of its maximum HP, rounded half up.",
                                "shortDesc": "Cures target's status; heals user 1/2 max HP if so.",
                                "id": "purify",
                                "name": "Purify",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "heal": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Poison",
                                "zMoveBoost": {
                                    "atk": 1,
                                    "def": 1,
                                    "spa": 1,
                                    "spd": 1,
                                    "spe": 1
                                },
                                "contestType": "Beautiful"
                            },
                            "pursuit": {
                                "num": 228,
                                "accuracy": 100,
                                "basePower": 40,
                                "category": "Physical",
                                "desc": "If an opposing Pokemon switches out this turn, this move hits that Pokemon before it leaves the field, even if it was not the original target. If the user moves after an opponent using Parting Shot, U-turn, or Volt Switch, but not Baton Pass, it will hit that opponent before it leaves the field. Power doubles and no check is done if the user hits an opponent switching out, and the user 's turn is over; if an opponent faints from this, the replacement Pokemon does not become active until the end of the turn.",
                                "shortDesc": "Power doubles if a foe is switching out.",
                                "id": "pursuit",
                                "isViable": True,
                                "name": "Pursuit",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Dark",
                                "zMovePower": 100,
                                "contestType": "Clever"
                            },
                            "quash": {
                                "num": 511,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Causes the target to take its turn after all other Pokemon this turn, no matter the priority of its selected move. Fails if the target already moved this turn.",
                                "shortDesc": "Forces the target to move last this turn.",
                                "id": "quash",
                                "name": "Quash",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Dark",
                                "zMoveBoost": {
                                    "spe": 1
                                },
                                "contestType": "Clever"
                            },
                            "quickattack": {
                                "num": 98,
                                "accuracy": 100,
                                "basePower": 40,
                                "category": "Physical",
                                "desc": "No additional effect.",
                                "shortDesc": "Usually goes first.",
                                "id": "quickattack",
                                "isViable": True,
                                "name": "Quick Attack",
                                "pp": 30,
                                "priority": 1,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 100,
                                "contestType": "Cool"
                            },
                            "quickguard": {
                                "num": 501,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user and its party members are protected from attacks with original or altered priority greater than 0 made by other Pokemon, including allies, during this turn. This move modifies the same 1/X chance of being successful used by other protection moves, where X starts at 1 and triples each time this move is successfully used, but does not use the chance to check for failure. X resets to 1 if this move fails, if the user's last move used is not Baneful Bunker, Detect, Endure, King's Shield, Protect, Quick Guard, Spiky Shield, or Wide Guard, or if it was one of those moves and the user 's protection was broken. Fails if the user moves last this turn or if this move is already in effect for the user's side.",
                                "shortDesc": "Protects allies from priority attacks this turn.",
                                "id": "quickguard",
                                "name": "Quick Guard",
                                "pp": 15,
                                "priority": 3,
                                "flags": {
                                    "snatch": 1
                                },
                                "sideCondition": "quickguard",
                                "secondary": None,
                                "target": "allySide",
                                "type": "Fighting",
                                "zMoveBoost": {
                                    "def": 1
                                },
                                "contestType": "Cool"
                            },
                            "quiverdance": {
                                "num": 483,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Raises the user's Special Attack, Special Defense, and Speed by 1 stage.",
                                "shortDesc": "Raises the user's Sp. Atk, Sp. Def, Speed by 1.",
                                "id": "quiverdance",
                                "isViable": True,
                                "name": "Quiver Dance",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1,
                                    "dance": 1
                                },
                                "boosts": {
                                    "spa": 1,
                                    "spd": 1,
                                    "spe": 1
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Bug",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Beautiful"
                            },
                            "rage": {
                                "num": 99,
                                "accuracy": 100,
                                "basePower": 20,
                                "category": "Physical",
                                "desc": "Once this move is successfully used, the user's Attack is raised by 1 stage every time it is hit by another Pokemon's attack as long as this move is chosen for use.",
                                "shortDesc": "Raises the user's Attack by 1 if hit during use.",
                                "id": "rage",
                                "name": "Rage",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "self": {
                                    "volatileStatus": "rage",
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 100,
                                "contestType": "Tough"
                            },
                            "ragepowder": {
                                "num": 476,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Until the end of the turn, all single-target attacks from the opposing side are redirected to the user. Such attacks are redirected to the user before they can be reflected by Magic Coat or the Magic Bounce Ability, or drawn in by the Lightning Rod or Storm drain Abilities. Fails if it is not a Double Battle or Battle Royal. This effect is ignored while the user is under the effect of Sky Drop.",
                                "shortDesc": "The foes moves target the user on the turn used.",
                                "id": "ragepowder",
                                "name": "Rage Powder",
                                "pp": 20,
                                "priority": 2,
                                "flags": {
                                    "powder": 1
                                },
                                "volatileStatus": "ragepowder",
                                "secondary": None,
                                "target": "self",
                                "type": "Bug",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Clever"
                            },
                            "raindance": {
                                "num": 240,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "For 5 turns, the weather becomes Rain Dance. The damage of Water-type attacks is multiplied by 1.5 and the damage of Fire-type attacks is multiplied by 0.5 during the effect. Lasts for 8 turns if the user is holding Damp Rock. Fails if the current weather is Rain Dance.",
                                "shortDesc": "For 5 turns, heavy rain powers Water moves.",
                                "id": "raindance",
                                "name": "Rain Dance",
                                "pp": 5,
                                "priority": 0,
                                "flags": {},
                                "weather": "RainDance",
                                "secondary": None,
                                "target": "all",
                                "type": "Water",
                                "zMoveBoost": {
                                    "spe": 1
                                },
                                "contestType": "Beautiful"
                            },
                            "rapidspin": {
                                "num": 229,
                                "accuracy": 100,
                                "basePower": 20,
                                "category": "Physical",
                                "desc": "If this move is successful and the user has not fainted, the effects of Leech Seed and binding moves end for the user, and all hazards are removed from the user's side of the field.",
                                "shortDesc": "Frees user from hazards, binding, Leech Seed.",
                                "id": "rapidspin",
                                "isViable": True,
                                "name": "Rapid Spin",
                                "pp": 40,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 100,
                                "contestType": "Cool"
                            },
                            "razorleaf": {
                                "num": 75,
                                "accuracy": 95,
                                "basePower": 55,
                                "category": "Physical",
                                "desc": "Has a higher chance for a critical hit.",
                                "shortDesc": "High critical hit ratio. Hits adjacent foes.",
                                "id": "razorleaf",
                                "name": "Razor Leaf",
                                "pp": 25,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "critRatio": 2,
                                "secondary": None,
                                "target": "allAdjacentFoes",
                                "type": "Grass",
                                "zMovePower": 100,
                                "contestType": "Cool"
                            },
                            "razorshell": {
                                "num": 534,
                                "accuracy": 95,
                                "basePower": 75,
                                "category": "Physical",
                                "desc": "Has a 50% chance to lower the target's Defense by 1 stage.",
                                "shortDesc": "50% chance to lower the target's Defense by 1.",
                                "id": "razorshell",
                                "isViable": True,
                                "name": "Razor Shell",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 50,
                                    "boosts": {
                                        "def": -1,
                                    },
                                },
                                "target": "normal",
                                "type": "Water",
                                "zMovePower": 140,
                                "contestType": "Cool"
                            },
                            "razorwind": {
                                "num": 13,
                                "accuracy": 100,
                                "basePower": 80,
                                "category": "Special",
                                "desc": "Has a higher chance for a critical hit. This attack charges on the first turn and executes on the second. If the user is holding a Power Herb, the move completes in one turn.",
                                "shortDesc": "Charges, then hits foe(s) turn 2. High crit ratio.",
                                "id": "razorwind",
                                "name": "Razor Wind",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "charge": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "critRatio": 2,
                                "secondary": None,
                                "target": "allAdjacentFoes",
                                "type": "Normal",
                                "zMovePower": 160,
                                "contestType": "Cool"
                            },
                            "recover": {
                                "num": 105,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user restores 1/2 of its maximum HP, rounded half up.",
                                "shortDesc": "Heals the user by 50% of its max HP.",
                                "id": "recover",
                                "isViable": True,
                                "name": "Recover",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1,
                                    "heal": 1
                                },
                                "heal": [
                                    1,
                                    2
                                ],
                                "secondary": None,
                                "target": "self",
                                "type": "Normal",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Clever"
                            },
                            "recycle": {
                                "num": 278,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user regains the item it last used. Fails if the user is holding an item, if the user has not held an item, if the item was a popped Air Balloon, if the item was picked up by a Pokemon with the Pickup Ability, or if the item was lost to Bug Bite, Covet, Incinerate, Knock Off, Pluck, or Thief. Items thrown with Fling can be regained.",
                                "shortDesc": "Restores the item the user last used.",
                                "id": "recycle",
                                "name": "Recycle",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "spe": 2
                                },
                                "contestType": "Clever"
                            },
                            "reflect": {
                                "num": 115,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "For 5 turns, the user and its party members take 0.5x damage from physical attacks, or 0.66x damage if in a Double Battle. Damage is not reduced further with Aurora Veil. Critical hits ignore this effect. It is removed from the user's side if the user or an ally is successfully hit by Brick Break, Psychic Fangs, or Defog. Lasts for 8 turns if the user is holding Light Clay. Fails if the effect is already active on the user's side.",
                                "shortDesc": "For 5 turns, physical damage to allies is halved.",
                                "id": "reflect",
                                "isViable": True,
                                "name": "Reflect",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1
                                },
                                "sideCondition": "reflect",
                                "secondary": None,
                                "target": "allySide",
                                "type": "Psychic",
                                "zMoveBoost": {
                                    "def": 1
                                },
                                "contestType": "Clever"
                            },
                            "reflecttype": {
                                "num": 513,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Causes the user's types to become the same as the current types of the target. If the target's current types include typeless and a non-added type, typeless is ignored. If the target's current types include typeless and an added type from Forest's Curse or Trick - or - Treat, typeless is copied as the Normal type instead.Fails if the user is an Arceus or a Silvally, or if the target 's current type is typeless alone.",
                                "shortDesc": "User becomes the same type as the target.",
                                "id": "reflecttype",
                                "name": "Reflect Type",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "authentic": 1,
                                    "mystery": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "spa": 1
                                },
                                "contestType": "Clever"
                            },
                            "refresh": {
                                "num": 287,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user cures its burn, poison, or paralysis. Fails if the user is not burned, poisoned, or paralyzed.",
                                "shortDesc": "User cures its burn, poison, or paralysis.",
                                "id": "refresh",
                                "isViable": True,
                                "name": "Refresh",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Normal",
                                "zMoveEffect": "heal",
                                "contestType": "Cute"
                            },
                            "relicsong": {
                                "num": 547,
                                "accuracy": 100,
                                "basePower": 75,
                                "category": "Special",
                                "desc": "Has a 10% chance to cause the target to fall asleep. If this move is successful on at least one target and the user is a Meloetta, it changes to Pirouette Forme if it is currently in Aria Forme, or changes to Aria Forme if it is currently in Pirouette Forme. This forme change does not happen if the Meloetta has the Sheer Force Ability. The Pirouette Forme reverts to Aria Forme when Meloetta is not active.",
                                "shortDesc": "10% chance to sleep foe(s). Meloetta transforms.",
                                "id": "relicsong",
                                "isViable": True,
                                "name": "Relic Song",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "sound": 1,
                                    "authentic": 1
                                },
                                "secondary": {
                                    "chance": 10,
                                    "status": "slp",
                                },
                                "target": "allAdjacentFoes",
                                "type": "Normal",
                                "zMovePower": 140,
                                "contestType": "Beautiful"
                            },
                            "rest": {
                                "num": 156,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user falls asleep for the next two turns and restores all of its HP, curing itself of any major status condition in the process. Fails if the user has full HP, is already asleep, or if another effect is preventing sleep.",
                                "shortDesc": "User sleeps 2 turns and restores HP and status.",
                                "id": "rest",
                                "isViable": True,
                                "name": "Rest",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1,
                                    "heal": 1
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Psychic",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Cute"
                            },
                            "retaliate": {
                                "num": 514,
                                "accuracy": 100,
                                "basePower": 70,
                                "category": "Physical",
                                "desc": "Power doubles if one of the user's party members fainted last turn.",
                                "shortDesc": "Power doubles if an ally fainted last turn.",
                                "id": "retaliate",
                                "name": "Retaliate",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 140,
                                "contestType": "Cool"
                            },
                            "return": {
                                "num": 216,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Physical",
                                "desc": "Power is equal to the greater of (user's Happiness * 2/5), rounded down, or 1.",
                                "shortDesc": "Max 102 power at maximum Happiness.",
                                "id": "return",
                                "isViable": True,
                                "name": "Return",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 160,
                                "contestType": "Cute"
                            },
                            "revelationdance": {
                                "num": 686,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Special",
                                "desc": "This move's type depends on the user's primary type. If the user's primary type is typeless, this move's type is the user's secondary type if it has one, otherwise the added type from Forest's Curse or Trick - or - Treat.This move is typeless if the user 's type is typeless alone.",
                                "shortDesc": "Type varies based on the user's primary type.",
                                "id": "revelationdance",
                                "isViable": True,
                                "name": "Revelation Dance",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "dance": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 175,
                                "contestType": "Beautiful"
                            },
                            "revenge": {
                                "num": 279,
                                "accuracy": 100,
                                "basePower": 60,
                                "category": "Physical",
                                "desc": "Power doubles if the user was hit by the target this turn.",
                                "shortDesc": "Power doubles if user is damaged by the target.",
                                "id": "revenge",
                                "name": "Revenge",
                                "pp": 10,
                                "priority": -4,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Fighting",
                                "zMovePower": 120,
                                "contestType": "Tough"
                            },
                            "reversal": {
                                "num": 179,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Physical",
                                "desc": "The power of this move is 20 if X is 33 to 48, 40 if X is 17 to 32, 80 if X is 10 to 16, 100 if X is 5 to 9, 150 if X is 2 to 4, and 200 if X is 0 or 1, where X is equal to (user's current HP * 48 / user's maximum HP), rounded down.",
                                "shortDesc": "More power the less HP the user has left.",
                                "id": "reversal",
                                "name": "Reversal",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Fighting",
                                "zMovePower": 160,
                                "contestType": "Cool"
                            },
                            "roar": {
                                "num": 46,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The target is forced to switch out and be replaced with a random unfainted ally. Fails if the target is the last unfainted Pokemon in its party, or if the target used Ingrain previously or has the Suction Cups Ability.",
                                "shortDesc": "Forces the target to switch to a random ally.",
                                "id": "roar",
                                "isViable": True,
                                "name": "Roar",
                                "pp": 20,
                                "priority": -6,
                                "flags": {
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "sound": 1,
                                    "authentic": 1,
                                    "mystery": 1
                                },
                                "forceSwitch": True,
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "def": 1
                                },
                                "contestType": "Cool"
                            },
                            "roaroftime": {
                                "num": 459,
                                "accuracy": 90,
                                "basePower": 150,
                                "category": "Special",
                                "desc": "If this move is successful, the user must recharge on the following turn and cannot select a move.",
                                "shortDesc": "User cannot move next turn.",
                                "id": "roaroftime",
                                "name": "Roar of Time",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "recharge": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "self": {
                                    "volatileStatus": "mustrecharge",
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Dragon",
                                "zMovePower": 200,
                                "contestType": "Beautiful"
                            },
                            "rockblast": {
                                "num": 350,
                                "accuracy": 90,
                                "basePower": 25,
                                "category": "Physical",
                                "desc": "Hits two to five times. Has a 1/3 chance to hit two or three times, and a 1/6 chance to hit four or five times. If one of the hits breaks the target's substitute, it will take damage for the remaining hits. If the user has the Skill Link Ability, this move will always hit five times.",
                                "shortDesc": "Hits 2-5 times in one turn.",
                                "id": "rockblast",
                                "isViable": True,
                                "name": "Rock Blast",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "bullet": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "multihit": [
                                    2,
                                    5
                                ],
                                "secondary": None,
                                "target": "normal",
                                "type": "Rock",
                                "zMovePower": 140,
                                "contestType": "Tough"
                            },
                            "rockclimb": {
                                "num": 431,
                                "accuracy": 85,
                                "basePower": 90,
                                "category": "Physical",
                                "desc": "Has a 20% chance to confuse the target.",
                                "shortDesc": "20% chance to confuse the target.",
                                "id": "rockclimb",
                                "name": "Rock Climb",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 20,
                                    "volatileStatus": "confusion",
                                },
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 175,
                                "contestType": "Tough"
                            },
                            "rockpolish": {
                                "num": 397,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Raises the user's Speed by 2 stages.",
                                "shortDesc": "Raises the user's Speed by 2.",
                                "id": "rockpolish",
                                "isViable": True,
                                "name": "Rock Polish",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1
                                },
                                "boosts": {
                                    "spe": 2
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Rock",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Tough"
                            },
                            "rockslide": {
                                "num": 157,
                                "accuracy": 90,
                                "basePower": 75,
                                "category": "Physical",
                                "desc": "Has a 30% chance to flinch the target.",
                                "shortDesc": "30% chance to flinch the foe(s).",
                                "id": "rockslide",
                                "isViable": True,
                                "name": "Rock Slide",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "volatileStatus": "flinch"
                                },
                                "target": "allAdjacentFoes",
                                "type": "Rock",
                                "zMovePower": 140,
                                "contestType": "Tough"
                            },
                            "rocksmash": {
                                "num": 249,
                                "accuracy": 100,
                                "basePower": 40,
                                "category": "Physical",
                                "desc": "Has a 50% chance to lower the target's Defense by 1 stage.",
                                "shortDesc": "50% chance to lower the target's Defense by 1.",
                                "id": "rocksmash",
                                "name": "Rock Smash",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 50,
                                    "boosts": {
                                        "def": -1,
                                    },
                                },
                                "target": "normal",
                                "type": "Fighting",
                                "zMovePower": 100,
                                "contestType": "Tough"
                            },
                            "rockthrow": {
                                "num": 88,
                                "accuracy": 90,
                                "basePower": 50,
                                "category": "Physical",
                                "shortDesc": "No additional effect.",
                                "id": "rockthrow",
                                "name": "Rock Throw",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Rock",
                                "zMovePower": 100,
                                "contestType": "Tough"
                            },
                            "rocktomb": {
                                "num": 317,
                                "accuracy": 95,
                                "basePower": 60,
                                "category": "Physical",
                                "desc": "Has a 100% chance to lower the target's Speed by 1 stage.",
                                "shortDesc": "100% chance to lower the target's Speed by 1.",
                                "id": "rocktomb",
                                "name": "Rock Tomb",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 100,
                                    "boosts": {
                                        "spe": -1,
                                    },
                                },
                                "target": "normal",
                                "type": "Rock",
                                "zMovePower": 120,
                                "contestType": "Clever"
                            },
                            "rockwrecker": {
                                "num": 439,
                                "accuracy": 90,
                                "basePower": 150,
                                "category": "Physical",
                                "desc": "If this move is successful, the user must recharge on the following turn and cannot select a move.",
                                "shortDesc": "User cannot move next turn.",
                                "id": "rockwrecker",
                                "name": "Rock Wrecker",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "bullet": 1,
                                    "recharge": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "self": {
                                    "volatileStatus": "mustrecharge",
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Rock",
                                "zMovePower": 200,
                                "contestType": "Tough"
                            },
                            "roleplay": {
                                "num": 272,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user's Ability changes to match the target's Ability. Fails if the user's Ability is Battle Bond, Comatose, Disguise, Multitype, Power Construct, RKS System, Schooling, Shields Down, Stance Change, or already matches the target, or if the target's Ability is Battle Bond, Comatose, Disguise, Flower Gift, Forecast, Illusion, Imposter, Multitype, Power Construct, Power of Alchemy, Receiver, RKS System, Schooling, Shields Down, Stance Change, Trace, Wonder Guard, or Zen Mode.",
                                "shortDesc": "User replaces its Ability with the target's.",
                                "id": "roleplay",
                                "name": "Role Play",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "authentic": 1,
                                    "mystery": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "zMoveBoost": {
                                    "spe": 1
                                },
                                "contestType": "Cute"
                            },
                            "rollingkick": {
                                "num": 27,
                                "accuracy": 85,
                                "basePower": 60,
                                "category": "Physical",
                                "desc": "Has a 30% chance to flinch the target.",
                                "shortDesc": "30% chance to flinch the target.",
                                "id": "rollingkick",
                                "name": "Rolling Kick",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "volatileStatus": "flinch"
                                },
                                "target": "normal",
                                "type": "Fighting",
                                "zMovePower": 120,
                                "contestType": "Cool"
                            },
                            "rollout": {
                                "num": 205,
                                "accuracy": 90,
                                "basePower": 30,
                                "category": "Physical",
                                "desc": "If this move is successful, the user is locked into this move and cannot make another move until it misses, 5 turns have passed, or the attack cannot be used. Power doubles with each successful hit of this move and doubles again if Defense Curl was used previously by the user. If this move is called by Sleep Talk, the move is used for one turn. If this move hits an active Disguise during the effect, the power multiplier is paused but the turn counter is not, potentially allowing the multiplier to be used on the user's next move after this effect ends.",
                                "shortDesc": "Power doubles with each hit. Repeats for 5 turns.",
                                "id": "rollout",
                                "name": "Rollout",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Rock",
                                "zMovePower": 100,
                                "contestType": "Cute"
                            },
                            "roost": {
                                "num": 355,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user restores 1/2 of its maximum HP, rounded half up. Until the end of the turn, Flying-type users lose their Flying type and pure Flying-type users become Normal type. Does nothing if the user's HP is full.",
                                "shortDesc": "Heals 50% HP. Flying-type removed until turn ends.",
                                "id": "roost",
                                "isViable": True,
                                "name": "Roost",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1,
                                    "heal": 1
                                },
                                "heal": [
                                    1,
                                    2
                                ],
                                "self": {
                                    "volatileStatus": "roost",
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Flying",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Clever"
                            },
                            "rototiller": {
                                "num": 563,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Raises the Attack and Special Attack of all grounded Grass-type Pokemon on the field by 1 stage.",
                                "shortDesc": "Raises Atk/Sp. Atk of grounded Grass types by 1.",
                                "id": "rototiller",
                                "name": "Rototiller",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "distance": 1,
                                    "nonsky": 1
                                },
                                "secondary": None,
                                "target": "all",
                                "type": "Ground",
                                "zMoveBoost": {
                                    "atk": 1
                                },
                                "contestType": "Tough"
                            },
                            "round": {
                                "num": 496,
                                "accuracy": 100,
                                "basePower": 60,
                                "category": "Special",
                                "desc": "If there are other active Pokemon that chose this move for use this turn, those Pokemon take their turn immediately after the user, in Speed order, and this move's power is 120 for each other user.",
                                "shortDesc": "Power doubles if others used Round this turn.",
                                "id": "round",
                                "name": "Round",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "sound": 1,
                                    "authentic": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 120,
                                "contestType": "Beautiful"
                            },
                            "sacredfire": {
                                "num": 221,
                                "accuracy": 95,
                                "basePower": 100,
                                "category": "Physical",
                                "desc": "Has a 50% chance to burn the target.",
                                "shortDesc": "50% chance to burn the target. Thaws user.",
                                "id": "sacredfire",
                                "isViable": True,
                                "name": "Sacred Fire",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "defrost": 1
                                },
                                "secondary": {
                                    "chance": 50,
                                    "status": "brn",
                                },
                                "target": "normal",
                                "type": "Fire",
                                "zMovePower": 180,
                                "contestType": "Beautiful"
                            },
                            "sacredsword": {
                                "num": 533,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Physical",
                                "desc": "Ignores the target's stat stage changes, including evasiveness.",
                                "shortDesc": "Ignores the target's stat stage changes.",
                                "id": "sacredsword",
                                "isViable": True,
                                "name": "Sacred Sword",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "ignoreEvasion": True,
                                "ignoreDefensive": True,
                                "secondary": None,
                                "target": "normal",
                                "type": "Fighting",
                                "zMovePower": 175,
                                "contestType": "Cool"
                            },
                            "safeguard": {
                                "num": 219,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "For 5 turns, the user and its party members cannot have major status conditions or confusion inflicted on them by other Pokemon. It is removed from the user's side if the user or an ally is successfully hit by Defog. Fails if the effect is already active on the user's side.",
                                "shortDesc": "For 5 turns, protects user's party from status.",
                                "id": "safeguard",
                                "name": "Safeguard",
                                "pp": 25,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1
                                },
                                "sideCondition": "safeguard",
                                "secondary": None,
                                "target": "allySide",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "spe": 1
                                },
                                "contestType": "Beautiful"
                            },
                            "sandattack": {
                                "num": 28,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Lowers the target's 'accuracy' by 1 stage.",
                                "shortDesc": "Lowers the target's 'accuracy' by 1. ",
                                "id": "sandattack",
                                "name": "Sand Attack",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "boosts": {
                                    "accuracy": -1,
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Ground",
                                "zMoveBoost": {
                                    "evasion": 1
                                },
                                "contestType": "Cute"
                            },
                            "sandstorm": {
                                "num": 201,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "For 5 turns, the weather becomes Sandstorm. At the end of each turn except the last, all active Pokemon lose 1/16 of their maximum HP, rounded down, unless they are a Ground, Rock, or Steel type, or have the Magic Guard, Overcoat, Sand Force, Sand Rush, or Sand Veil Abilities. During the effect, the Special Defense of Rock-type Pokemon is multiplied by 1.5 when taking damage from a special attack. Lasts for 8 turns if the user is holding Smooth Rock. Fails if the current weather is Sandstorm.",
                                "shortDesc": "For 5 turns, a sandstorm rages.",
                                "id": "sandstorm",
                                "name": "Sandstorm",
                                "pp": 10,
                                "priority": 0,
                                "flags": {},
                                "weather": "Sandstorm",
                                "secondary": None,
                                "target": "all",
                                "type": "Rock",
                                "zMoveBoost": {
                                    "spe": 1
                                },
                                "contestType": "Tough"
                            },
                            "sandtomb": {
                                "num": 328,
                                "accuracy": 85,
                                "basePower": 35,
                                "category": "Physical",
                                "desc": "Prevents the target from switching for four or five turns (seven turns if the user is holding Grip Claw). Causes damage to the target equal to 1/8 of its maximum HP (1/6 if the user is holding Binding Band), rounded down, at the end of each turn during effect. The target can still switch out if it is holding Shed Shell or uses Baton Pass, Parting Shot, U-turn, or Volt Switch. The effect ends if either the user or the target leaves the field, or if the target uses Rapid Spin or Substitute successfully. This effect is not stackable or reset by using this or another binding move.",
                                "shortDesc": "Traps and damages the target for 4-5 turns.",
                                "id": "sandtomb",
                                "name": "Sand Tomb",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "volatileStatus": "partiallytrapped",
                                "secondary": None,
                                "target": "normal",
                                "type": "Ground",
                                "zMovePower": 100,
                                "contestType": "Clever"
                            },
                            "sappyseed": {
                                "num": 738,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Physical",
                                "desc": "This move summons Leech Seed on the foe.",
                                "shortDesc": "Summons Leech Seed.",
                                "id": "sappyseed",
                                "isNonstandard": "LGPE",
                                "isUnreleased": True,
                                "isViable": True,
                                "name": "Sappy Seed",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Grass",
                                "contestType": "Clever"
                            },
                            "savagespinout": {
                                "num": 634,
                                "accuracy": True,
                                "basePower": 1,
                                "category": "Physical",
                                "shortDesc": "Power is equal to the base move's Z-Power.",
                                "id": "savagespinout",
                                "name": "Savage Spin-Out",
                                "pp": 1,
                                "priority": 0,
                                "flags": {},
                                "isZ": "buginiumz",
                                "secondary": None,
                                "target": "normal",
                                "type": "Bug",
                                "contestType": "Cool"
                            },
                            "scald": {
                                "num": 503,
                                "accuracy": 100,
                                "basePower": 80,
                                "category": "Special",
                                "desc": "Has a 30% chance to burn the target. The target thaws out if it is frozen.",
                                "shortDesc": "30% chance to burn the target. Thaws target.",
                                "id": "scald",
                                "isViable": True,
                                "name": "Scald",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "defrost": 1
                                },
                                "thawsTarget": True,
                                "secondary": {
                                    "chance": 30,
                                    "status": "brn",
                                },
                                "target": "normal",
                                "type": "Water",
                                "zMovePower": 160,
                                "contestType": "Tough"
                            },
                            "scaryface": {
                                "num": 184,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Lowers the target's Speed by 2 stages.",
                                "shortDesc": "Lowers the target's Speed by 2.",
                                "id": "scaryface",
                                "name": "Scary Face",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "mystery": 1
                                },
                                "boosts": {
                                    "spe": -2,
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "spe": 1
                                },
                                "contestType": "Tough"
                            },
                            "scratch": {
                                "num": 10,
                                "accuracy": 100,
                                "basePower": 40,
                                "category": "Physical",
                                "shortDesc": "No additional effect.",
                                "id": "scratch",
                                "name": "Scratch",
                                "pp": 35,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 100,
                                "contestType": "Tough"
                            },
                            "screech": {
                                "num": 103,
                                "accuracy": 85,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Lowers the target's Defense by 2 stages.",
                                "shortDesc": "Lowers the target's Defense by 2.",
                                "id": "screech",
                                "name": "Screech",
                                "pp": 40,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "sound": 1,
                                    "authentic": 1,
                                    "mystery": 1
                                },
                                "boosts": {
                                    "def": -2,
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "atk": 1
                                },
                                "contestType": "Clever"
                            },
                            "searingshot": {
                                "num": 545,
                                "accuracy": 100,
                                "basePower": 100,
                                "category": "Special",
                                "desc": "Has a 30% chance to burn the target.",
                                "shortDesc": "30% chance to burn adjacent Pokemon.",
                                "id": "searingshot",
                                "isViable": True,
                                "name": "Searing Shot",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "bullet": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "status": "brn",
                                },
                                "target": "allAdjacent",
                                "type": "Fire",
                                "zMovePower": 180,
                                "contestType": "Cool"
                            },
                            "searingsunrazesmash": {
                                "num": 724,
                                "accuracy": True,
                                "basePower": 200,
                                "category": "Physical",
                                "desc": "This move and its effects ignore the Abilities of other Pokemon.",
                                "shortDesc": "Ignores the Abilities of other Pokemon.",
                                "id": "searingsunrazesmash",
                                "name": "Searing Sunraze Smash",
                                "pp": 1,
                                "priority": 0,
                                "flags": {
                                    "contact": 1
                                },
                                "isZ": "solganiumz",
                                "ignoreAbility": True,
                                "secondary": None,
                                "target": "normal",
                                "type": "Steel",
                                "contestType": "Cool"
                            },
                            "secretpower": {
                                "num": 290,
                                "accuracy": 100,
                                "basePower": 70,
                                "category": "Physical",
                                "desc": "Has a 30% chance to cause a secondary effect on the target based on the battle terrain. Causes paralysis on the regular Wi-Fi terrain, causes paralysis during Electric Terrain, lowers Special Attack by 1 stage during Misty Terrain, causes sleep during Grassy Terrain and lowers Speed by 1 stage during Psychic Terrain.",
                                "shortDesc": "Effect varies with terrain. (30% paralysis chance)",
                                "id": "secretpower",
                                "name": "Secret Power",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "status": "par",
                                },
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 140,
                                "contestType": "Clever"
                            },
                            "secretsword": {
                                "num": 548,
                                "accuracy": 100,
                                "basePower": 85,
                                "category": "Special",
                                "defensivecategory": "Physical",
                                "desc": "Deals damage to the target based on its Defense instead of Special Defense.",
                                "shortDesc": "Damages target based on Defense, not Sp. Def.",
                                "id": "secretsword",
                                "isViable": True,
                                "name": "Secret Sword",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Fighting",
                                "zMovePower": 160,
                                "contestType": "Beautiful"
                            },
                            "seedbomb": {
                                "num": 402,
                                "accuracy": 100,
                                "basePower": 80,
                                "category": "Physical",
                                "shortDesc": "No additional effect.",
                                "id": "seedbomb",
                                "isViable": True,
                                "name": "Seed Bomb",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "bullet": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Grass",
                                "zMovePower": 160,
                                "contestType": "Tough"
                            },
                            "seedflare": {
                                "num": 465,
                                "accuracy": 85,
                                "basePower": 120,
                                "category": "Special",
                                "desc": "Has a 40% chance to lower the target's Special Defense by 2 stages.",
                                "shortDesc": "40% chance to lower the target's Sp. Def by 2.",
                                "id": "seedflare",
                                "isViable": True,
                                "name": "Seed Flare",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 40,
                                    "boosts": {
                                        "spd": -2
                                    },
                                },
                                "target": "normal",
                                "type": "Grass",
                                "zMovePower": 190,
                                "contestType": "Beautiful"
                            },
                            "seismictoss": {
                                "num": 69,
                                "accuracy": 100,
                                "basePower": 0,
                                "damage": "level",
                                "category": "Physical",
                                "desc": "Deals damage to the target equal to the user's level.",
                                "shortDesc": "Does damage equal to the user's level.",
                                "id": "seismictoss",
                                "isViable": True,
                                "name": "Seismic Toss",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "nonsky": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Fighting",
                                "zMovePower": 100,
                                "contestType": "Tough"
                            },
                            "selfdestruct": {
                                "num": 120,
                                "accuracy": 100,
                                "basePower": 200,
                                "category": "Physical",
                                "desc": "The user faints after using this move, even if this move fails for having no target. This move is prevented from executing if any active Pokemon has the Damp Ability.",
                                "shortDesc": "Hits adjacent Pokemon. The user faints.",
                                "id": "selfdestruct",
                                "name": "Self-Destruct",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "selfdestruct": "always",
                                "secondary": None,
                                "target": "allAdjacent",
                                "type": "Normal",
                                "zMovePower": 200,
                                "contestType": "Beautiful"
                            },
                            "shadowball": {
                                "num": 247,
                                "accuracy": 100,
                                "basePower": 80,
                                "category": "Special",
                                "desc": "Has a 20% chance to lower the target's Special Defense by 1 stage.",
                                "shortDesc": "20% chance to lower the target's Sp. Def by 1.",
                                "id": "shadowball",
                                "isViable": True,
                                "name": "Shadow Ball",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "bullet": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 20,
                                    "boosts": {
                                        "spd": -1
                                    },
                                },
                                "target": "normal",
                                "type": "Ghost",
                                "zMovePower": 160,
                                "contestType": "Clever"
                            },
                            "shadowbone": {
                                "num": 708,
                                "accuracy": 100,
                                "basePower": 85,
                                "category": "Physical",
                                "desc": "Has a 20% chance to lower the target's Defense by 1 stage.",
                                "shortDesc": "20% chance to lower the target's Defense by 1.",
                                "id": "shadowbone",
                                "isViable": True,
                                "name": "Shadow Bone",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 20,
                                    "boosts": {
                                        "def": -1,
                                    },
                                },
                                "target": "normal",
                                "type": "Ghost",
                                "zMovePower": 160,
                                "contestType": "Cool"
                            },
                            "shadowclaw": {
                                "num": 421,
                                "accuracy": 100,
                                "basePower": 70,
                                "category": "Physical",
                                "desc": "Has a higher chance for a critical hit.",
                                "shortDesc": "High critical hit ratio.",
                                "id": "shadowclaw",
                                "isViable": True,
                                "name": "Shadow Claw",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "critRatio": 2,
                                "secondary": None,
                                "target": "normal",
                                "type": "Ghost",
                                "zMovePower": 140,
                                "contestType": "Cool"
                            },
                            "shadowforce": {
                                "num": 467,
                                "accuracy": 100,
                                "basePower": 120,
                                "category": "Physical",
                                "desc": "If this move is successful, it breaks through the target's Baneful Bunker, Detect, King's Shield, Protect, or Spiky Shield for this turn, allowing other Pokemon to attack the target normally.If the target 's side is protected by Crafty Shield, Mat Block, Quick Guard, or Wide Guard, that protection is also broken for this turn and other Pokemon may attack the target' s side normally.This attack charges on the first turn and executes on the second.On the first turn, the user avoids all attacks.If the user is holding a Power Herb, the move completes in one turn.",
                                "shortDesc": "Disappears turn 1. Hits turn 2. Breaks protection.",
                                "id": "shadowforce",
                                "isViable": True,
                                "name": "Shadow Force",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "charge": 1,
                                    "mirror": 1
                                },
                                "breaksProtect": True,
                                "secondary": None,
                                "target": "normal",
                                "type": "Ghost",
                                "zMovePower": 190,
                                "contestType": "Cool"
                            },
                            "shadowpunch": {
                                "num": 325,
                                "accuracy": True,
                                "basePower": 60,
                                "category": "Physical",
                                "shortDesc": "This move does not check 'accuracy'.",
                                "id": "shadowpunch",
                                "isViable": True,
                                "name": "Shadow Punch",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "powder": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Ghost",
                                "zMovePower": 120,
                                "contestType": "Clever"
                            },
                            "shadowsneak": {
                                "num": 425,
                                "accuracy": 100,
                                "basePower": 40,
                                "category": "Physical",
                                "desc": "No additional effect.",
                                "shortDesc": "Usually goes first.",
                                "id": "shadowsneak",
                                "isViable": True,
                                "name": "Shadow Sneak",
                                "pp": 30,
                                "priority": 1,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Ghost",
                                "zMovePower": 100,
                                "contestType": "Clever"
                            },
                            "shadowstrike": {
                                "num": 0,
                                "accuracy": 95,
                                "basePower": 80,
                                "category": "Physical",
                                "desc": "Has a 50% chance to lower the target's Defense by 1 stage.",
                                "shortDesc": "50% chance to lower the target's Defense by 1.",
                                "id": "shadowstrike",
                                "isNonstandard": "CAP",
                                "isViable": True,
                                "name": "Shadow Strike",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 50,
                                    "boosts": {
                                        "def": -1,
                                    },
                                },
                                "target": "normal",
                                "type": "Ghost",
                                "zMovePower": 160,
                                "contestType": "Clever"
                            },
                            "sharpen": {
                                "num": 159,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Raises the user's Attack by 1 stage.",
                                "shortDesc": "Raises the user's Attack by 1.",
                                "id": "sharpen",
                                "name": "Sharpen",
                                "pp": 30,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1
                                },
                                "boosts": {
                                    "atk": 1,
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "atk": 1
                                },
                                "contestType": "Cute"
                            },
                            "shatteredpsyche": {
                                "num": 648,
                                "accuracy": True,
                                "basePower": 1,
                                "category": "Physical",
                                "shortDesc": "Power is equal to the base move's Z-Power.",
                                "id": "shatteredpsyche",
                                "isViable": True,
                                "name": "Shattered Psyche",
                                "pp": 1,
                                "priority": 0,
                                "flags": {},
                                "isZ": "psychiumz",
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "contestType": "Cool"
                            },
                            "sheercold": {
                                "num": 329,
                                "accuracy": 30,
                                "basePower": 0,
                                "category": "Special",
                                "desc": "Deals damage to the target equal to the target's maximum HP. Ignores 'accuracy' and evasiveness modifiers. This attack's 'accuracy' is equal to (user 's level - target's level + X) % , where X is 30 if the user is an Ice type and 20 otherwise, and fails if the target is at a higher level.Ice - type Pokemon and Pokemon with the Sturdy Ability are immune.",
                                "shortDesc": "OHKOs non-Ice targets. Fails if user's lower level.",
                                "id": "sheercold",
                                "name": "Sheer Cold",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "ohko": "Ice",
                                "target": "normal",
                                "type": "Ice",
                                "zMovePower": 180,
                                "contestType": "Beautiful"
                            },
                            "shellsmash": {
                                "num": 504,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Lowers the user's Defense and Special Defense by 1 stage. Raises the user's Attack, Special Attack, and Speed by 2 stages.",
                                "shortDesc": "Lowers Def, SpD by 1; raises Atk, SpA, Spe by 2.",
                                "id": "shellsmash",
                                "isViable": True,
                                "name": "Shell Smash",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1
                                },
                                "boosts": {
                                    "def": -1,
                                    "spd": -1,
                                    "atk": 2,
                                    "spa": 2,
                                    "spe": 2
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Normal",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Tough"
                            },
                            "shelltrap": {
                                "num": 704,
                                "accuracy": 100,
                                "basePower": 150,
                                "category": "Special",
                                "desc": "Fails unless the user is hit by a physical attack from an opponent this turn before it can execute the move. If the user was hit and has not fainted, it attacks immediately after being hit, and the effect ends. If the opponent's physical attack had a secondary effect removed by the Sheer Force Ability, it does not count for the purposes of this effect.",
                                "shortDesc": "User must take physical damage before moving.",
                                "id": "shelltrap",
                                "name": "Shell Trap",
                                "pp": 5,
                                "priority": -3,
                                "flags": {
                                    "protect": 1
                                },
                                "secondary": None,
                                "target": "allAdjacentFoes",
                                "type": "Fire",
                                "zMovePower": 200,
                                "contestType": "Tough"
                            },
                            "shiftgear": {
                                "num": 508,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Raises the user's Speed by 2 stages and its Attack by 1 stage.",
                                "shortDesc": "Raises the user's Speed by 2 and Attack by 1.",
                                "id": "shiftgear",
                                "isViable": True,
                                "name": "Shift Gear",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1
                                },
                                "boosts": {
                                    "spe": 2,
                                    "atk": 1,
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Steel",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Clever"
                            },
                            "shockwave": {
                                "num": 351,
                                "accuracy": True,
                                "basePower": 60,
                                "category": "Special",
                                "shortDesc": "This move does not check 'accuracy'",
                                "id": "shockwave",
                                "name": "Shock Wave",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Electric",
                                "zMovePower": 120,
                                "contestType": "Cool"
                            },
                            "shoreup": {
                                "num": 659,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user restores 1/2 of its maximum HP, rounded half down. If the weather is Sandstorm, the user instead restores 2/3 of its maximum HP, rounded half down.",
                                "shortDesc": "User restores 1/2 its max HP; 2/3 in Sandstorm.",
                                "id": "shoreup",
                                "isViable": True,
                                "name": "Shore Up",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1,
                                    "heal": 1
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Ground",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Beautiful"
                            },
                            "signalbeam": {
                                "num": 324,
                                "accuracy": 100,
                                "basePower": 75,
                                "category": "Special",
                                "desc": "Has a 10% chance to confuse the target.",
                                "shortDesc": "10% chance to confuse the target.",
                                "id": "signalbeam",
                                "isViable": True,
                                "name": "Signal Beam",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 10,
                                    "volatileStatus": "confusion",
                                },
                                "target": "normal",
                                "type": "Bug",
                                "zMovePower": 140,
                                "contestType": "Beautiful"
                            },
                            "silverwind": {
                                "num": 318,
                                "accuracy": 100,
                                "basePower": 60,
                                "category": "Special",
                                "desc": "Has a 10% chance to raise the user's Attack, Defense, Special Attack, Special Defense, and Speed by 1 stage.",
                                "shortDesc": "10% chance to raise all stats by 1 (not acc/eva).",
                                "id": "silverwind",
                                "name": "Silver Wind",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 10,
                                    "self": {
                                        "boosts": {
                                            "atk": 1,
                                            "def": 1,
                                            "spa": 1,
                                            "spd": 1,
                                            "spe": 1
                                        },
                                    },
                                },
                                "target": "normal",
                                "type": "Bug",
                                "zMovePower": 120,
                                "contestType": "Beautiful"
                            },
                            "simplebeam": {
                                "num": 493,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Causes the target's Ability to become Simple. Fails if the target's Ability is Battle Bond, Comatose, Disguise, Multitype, Power Construct, RKS System, Schooling, Shields Down, Simple, Stance Change, Truant, or Zen Mode.",
                                "shortDesc": "The target's Ability becomes Simple.",
                                "id": "simplebeam",
                                "name": "Simple Beam",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "mystery": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "spa": 1
                                },
                                "contestType": "Cute"
                            },
                            "sing": {
                                "num": 47,
                                "accuracy": 55,
                                "basePower": 0,
                                "category": "Status",
                                "shortDesc": "Causes the target to fall asleep.",
                                "id": "sing",
                                "name": "Sing",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "sound": 1,
                                    "authentic": 1
                                },
                                "status": "slp",
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "spe": 1
                                },
                                "contestType": "Cute"
                            },
                            "sinisterarrowraid": {
                                "num": 695,
                                "accuracy": True,
                                "basePower": 180,
                                "category": "Physical",
                                "shortDesc": "No additional effect.",
                                "id": "sinisterarrowraid",
                                "name": "Sinister Arrow Raid",
                                "pp": 1,
                                "priority": 0,
                                "flags": {},
                                "isZ": "decidiumz",
                                "secondary": None,
                                "target": "normal",
                                "type": "Ghost",
                                "contestType": "Cool"
                            },
                            "sizzlyslide": {
                                "num": 735,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Physical",
                                "desc": "Has a 100% chance to burn the foe.",
                                "shortDesc": "100% chance to burn the foe.",
                                "id": "sizzlyslide",
                                "isNonstandard": "LGPE",
                                "isUnreleased": True,
                                "isViable": True,
                                "name": "Sizzly Slide",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "defrost": 1
                                },
                                "secondary": {
                                    "chance": 100,
                                    "status": "brn",
                                },
                                "target": "normal",
                                "type": "Fire",
                                "contestType": "Clever"
                            },
                            "sketch": {
                                "num": 166,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "This move is permanently replaced by the last move used by the target. The copied move has the maximum PP for that move. Fails if the target has not made a move, if the user has Transformed, or if the move is Chatter, Sketch, Struggle, or any move the user knows.",
                                "shortDesc": "Permanently copies the last move target used.",
                                "id": "sketch",
                                "name": "Sketch",
                                "pp": 1,
                                "noPPBoosts": True,
                                "priority": 0,
                                "flags": {
                                    "authentic": 1,
                                    "mystery": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "atk": 1,
                                    "def": 1,
                                    "spa": 1,
                                    "spd": 1,
                                    "spe": 1
                                },
                                "contestType": "Clever"
                            },
                            "skillswap": {
                                "num": 285,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user swaps its Ability with the target's Ability. Fails if either the user or the target's Ability is Battle Bond, Comatose, Disguise, Illusion, Multitype, Power Construct, RKS System, Schooling, Shields Down, Stance Change, Wonder Guard, or Zen Mode.",
                                "shortDesc": "The user and the target trade Abilities.",
                                "id": "skillswap",
                                "name": "Skill Swap",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "authentic": 1,
                                    "mystery": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "zMoveBoost": {
                                    "spe": 1
                                },
                                "contestType": "Clever"
                            },
                            "skullbash": {
                                "num": 130,
                                "accuracy": 100,
                                "basePower": 130,
                                "category": "Physical",
                                "desc": "This attack charges on the first turn and executes on the second. Raises the user's Defense by 1 stage on the first turn. If the user is holding a Power Herb, the move completes in one turn.",
                                "shortDesc": "Raises user's Defense by 1 on turn 1. Hits turn 2.",
                                "id": "skullbash",
                                "name": "Skull Bash",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "charge": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 195,
                                "contestType": "Tough"
                            },
                            "skyattack": {
                                "num": 143,
                                "accuracy": 90,
                                "basePower": 140,
                                "category": "Physical",
                                "desc": "Has a 30% chance to flinch the target and a higher chance for a critical hit. This attack charges on the first turn and executes on the second. If the user is holding a Power Herb, the move completes in one turn.",
                                "shortDesc": "Charges, then hits turn 2. 30% flinch. High crit.",
                                "id": "skyattack",
                                "name": "Sky Attack",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "charge": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "distance": 1
                                },
                                "critRatio": 2,
                                "secondary": {
                                    "chance": 30,
                                    "volatileStatus": "flinch"
                                },
                                "target": "any",
                                "type": "Flying",
                                "zMovePower": 200,
                                "contestType": "Cool"
                            },
                            "skydrop": {
                                "num": 507,
                                "accuracy": 100,
                                "basePower": 60,
                                "category": "Physical",
                                "desc": "This attack takes the target into the air with the user on the first turn and executes on the second. Pokemon weighing 200 kg or more cannot be lifted. On the first turn, the user and the target avoid all attacks other than Gust, Hurricane, Sky Uppercut, Smack Down, Thousand Arrows, Thunder, and Twister. The user and the target cannot make a move between turns, but the target can select a move to use. This move cannot damage Flying-type Pokemon. Fails on the first turn if the target is an ally, if the target has a substitute, or if the target is using Bounce, Dig, Dive, Fly, Phantom Force, Shadow Force, or Sky Drop.",
                                "shortDesc": "User and foe fly up turn 1. Damages on turn 2.",
                                "id": "skydrop",
                                "name": "Sky Drop",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "charge": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "gravity": 1,
                                    "distance": 1
                                },
                                "secondary": None,
                                "target": "any",
                                "type": "Flying",
                                "zMovePower": 120,
                                "contestType": "Tough"
                            },
                            "skyuppercut": {
                                "num": 327,
                                "accuracy": 90,
                                "basePower": 85,
                                "category": "Physical",
                                "desc": "This move can hit a target using Bounce, Fly, or Sky Drop, or is under the effect of Sky Drop.",
                                "shortDesc": "Can hit Pokemon using Bounce, Fly, or Sky Drop.",
                                "id": "skyuppercut",
                                "name": "Sky Uppercut",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "powder": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Fighting",
                                "zMovePower": 160,
                                "contestType": "Cool"
                            },
                            "slackoff": {
                                "num": 303,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user restores 1/2 of its maximum HP, rounded half up.",
                                "shortDesc": "Heals the user by 50% of its max HP.",
                                "id": "slackoff",
                                "isViable": True,
                                "name": "Slack Off",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1,
                                    "heal": 1
                                },
                                "heal": [
                                    1,
                                    2
                                ],
                                "secondary": None,
                                "target": "self",
                                "type": "Normal",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Cute"
                            },
                            "slam": {
                                "num": 21,
                                "accuracy": 75,
                                "basePower": 80,
                                "category": "Physical",
                                "shortDesc": "No additional effect.",
                                "id": "slam",
                                "name": "Slam",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "nonsky": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 160,
                                "contestType": "Tough"
                            },
                            "slash": {
                                "num": 163,
                                "accuracy": 100,
                                "basePower": 70,
                                "category": "Physical",
                                "desc": "Has a higher chance for a critical hit.",
                                "shortDesc": "High critical hit ratio.",
                                "id": "slash",
                                "name": "Slash",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "critRatio": 2,
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 140,
                                "contestType": "Cool"
                            },
                            "sleeppowder": {
                                "num": 79,
                                "accuracy": 75,
                                "basePower": 0,
                                "category": "Status",
                                "shortDesc": "Causes the target to fall asleep.",
                                "id": "sleeppowder",
                                "isViable": True,
                                "name": "Sleep Powder",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "powder": 1,
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "status": "slp",
                                "secondary": None,
                                "target": "normal",
                                "type": "Grass",
                                "zMoveBoost": {
                                    "spe": 1
                                },
                                "contestType": "Clever"
                            },
                            "sleeptalk": {
                                "num": 214,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "One of the user's known moves, besides this move, is selected for use at random. Fails if the user is not asleep. The selected move does not have PP deducted from it, and can currently have 0 PP. This move cannot select Assist, Beak Blast, Belch, Bide, Celebrate, Chatter, Copycat, Focus Punch, Hold Hands, Me First, Metronome, Mimic, Mirror Move, Nature Power, Shell Trap, Sketch, Sleep Talk, Struggle, Uproar, any two-turn move, or any Z-Move.",
                                "shortDesc": "User must be asleep. Uses another known move.",
                                "id": "sleeptalk",
                                "isViable": True,
                                "name": "Sleep Talk",
                                "pp": 10,
                                "priority": 0,
                                "flags": {},
                                "sleepUsable": True,
                                "secondary": None,
                                "target": "self",
                                "type": "Normal",
                                "zMoveEffect": "crit2",
                                "contestType": "Cute"
                            },
                            "sludge": {
                                "num": 124,
                                "accuracy": 100,
                                "basePower": 65,
                                "category": "Special",
                                "desc": "Has a 30% chance to poison the target.",
                                "shortDesc": "30% chance to poison the target.",
                                "id": "sludge",
                                "name": "Sludge",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "status": "psn",
                                },
                                "target": "normal",
                                "type": "Poison",
                                "zMovePower": 120,
                                "contestType": "Tough"
                            },
                            "sludgebomb": {
                                "num": 188,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Special",
                                "desc": "Has a 30% chance to poison the target.",
                                "shortDesc": "30% chance to poison the target.",
                                "id": "sludgebomb",
                                "isViable": True,
                                "name": "Sludge Bomb",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "bullet": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "status": "psn",
                                },
                                "target": "normal",
                                "type": "Poison",
                                "zMovePower": 175,
                                "contestType": "Tough"
                            },
                            "sludgewave": {
                                "num": 482,
                                "accuracy": 100,
                                "basePower": 95,
                                "category": "Special",
                                "desc": "Has a 10% chance to poison the target.",
                                "shortDesc": "10% chance to poison adjacent Pokemon.",
                                "id": "sludgewave",
                                "isViable": True,
                                "name": "Sludge Wave",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 10,
                                    "status": "psn",
                                },
                                "target": "allAdjacent",
                                "type": "Poison",
                                "zMovePower": 175,
                                "contestType": "Tough"
                            },
                            "smackdown": {
                                "num": 479,
                                "accuracy": 100,
                                "basePower": 50,
                                "category": "Physical",
                                "desc": "This move can hit a target using Bounce, Fly, or Sky Drop, or is under the effect of Sky Drop. If this move hits a target under the effect of Bounce, Fly, Magnet Rise, or Telekinesis, the effect ends. If the target is a Flying type that has not used Roost this turn or a Pokemon with the Levitate Ability, it loses its immunity to Ground-type attacks and the Arena Trap Ability as long as it remains active. During the effect, Magnet Rise fails for the target and Telekinesis fails against the target.",
                                "shortDesc": "Removes the target's Ground immunity.",
                                "id": "smackdown",
                                "name": "Smack Down",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "nonsky": 1
                                },
                                "volatileStatus": "smackdown",
                                "secondary": None,
                                "target": "normal",
                                "type": "Rock",
                                "zMovePower": 100,
                                "contestType": "Tough"
                            },
                            "smartstrike": {
                                "num": 684,
                                "accuracy": True,
                                "basePower": 70,
                                "category": "Physical",
                                "shortDesc": "This move does not check accuracy'",
                                "id": "smartstrike",
                                "name": "Smart Strike",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Steel",
                                "zMovePower": 140,
                                "contestType": "Cool"
                            },
                            "smellingsalts": {
                                "num": 265,
                                "accuracy": 100,
                                "basePower": 70,
                                "category": "Physical",
                                "desc": "Power doubles if the target is paralyzed. If the user has not fainted, the target is cured of paralysis.",
                                "shortDesc": "Power doubles if target is paralyzed, and cures it.",
                                "id": "smellingsalts",
                                "name": "Smelling Salts",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 140,
                                "contestType": "Tough"
                            },
                            "smog": {
                                "num": 123,
                                "accuracy": 70,
                                "basePower": 30,
                                "category": "Special",
                                "desc": "Has a 40% chance to poison the target.",
                                "shortDesc": "40% chance to poison the target.",
                                "id": "smog",
                                "name": "Smog",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 40,
                                    "status": "psn",
                                },
                                "target": "normal",
                                "type": "Poison",
                                "zMovePower": 100,
                                "contestType": "Tough"
                            },
                            "smokescreen": {
                                "num": 108,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status,by 1 stage.",
                                "shortDesc": "Lowers the target's by 1. ",
                                "id": "smokescreen",
                                "name": "Smokescreen",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "boosts": {
                                    "accuracy": -1,
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "evasion": 1
                                },
                                "contestType": "Clever"
                            },
                            "snarl": {
                                "num": 555,
                                "accuracy": 95,
                                "basePower": 55,
                                "category": "Special",
                                "desc": "Has a 100% chance to lower the target's Special Attack by 1 stage.",
                                "shortDesc": "100% chance to lower the foe(s) Sp. Atk by 1.",
                                "id": "snarl",
                                "name": "Snarl",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "sound": 1,
                                    "authentic": 1
                                },
                                "secondary": {
                                    "chance": 100,
                                    "boosts": {
                                        "spa": -1,
                                    },
                                },
                                "target": "allAdjacentFoes",
                                "type": "Dark",
                                "zMovePower": 100,
                                "contestType": "Tough"
                            },
                            "snatch": {
                                "num": 289,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "If another Pokemon uses certain non-damaging moves this turn, the user steals that move to use itself. If multiple Pokemon use one of those moves this turn, the applicable moves are all stolen by the first Pokemon in turn order that used this move this turn. This effect is ignored while the user is under the effect of Sky Drop.",
                                "shortDesc": "User steals certain support moves to use itself.",
                                "id": "snatch",
                                "name": "Snatch",
                                "pp": 10,
                                "priority": 4,
                                "flags": {
                                    "authentic": 1
                                },
                                "volatileStatus": "snatch",
                                "secondary": None,
                                "pressureTarget": "foeSide",
                                "target": "self",
                                "type": "Dark",
                                "zMoveBoost": {
                                    "spe": 2
                                },
                                "contestType": "Clever"
                            },
                            "snore": {
                                "num": 173,
                                "accuracy": 100,
                                "basePower": 50,
                                "category": "Special",
                                "desc": "Has a 30% chance to flinch the target. Fails if the user is not asleep.",
                                "shortDesc": "User must be asleep. 30% chance to flinch target.",
                                "id": "snore",
                                "name": "Snore",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "sound": 1,
                                    "authentic": 1
                                },
                                "sleepUsable": True,
                                "secondary": {
                                    "chance": 30,
                                    "volatileStatus": "flinch"
                                },
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 100,
                                "contestType": "Cute"
                            },
                            "soak": {
                                "num": 487,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Causes the target to become a Water type. Fails if the target is an Arceus or a Silvally, or if the target is already purely Water type.",
                                "shortDesc": "Changes the target's type to Water.",
                                "id": "soak",
                                "name": "Soak",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "mystery": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Water",
                                "zMoveBoost": {
                                    "spa": 1
                                },
                                "contestType": "Cute"
                            },
                            "softboiled": {
                                "num": 135,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user restores 1/2 of its maximum HP, rounded half up.",
                                "shortDesc": "Heals the user by 50% of its max HP.",
                                "id": "softboiled",
                                "isViable": True,
                                "name": "Soft-Boiled",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1,
                                    "heal": 1
                                },
                                "heal": [
                                    1,
                                    2
                                ],
                                "secondary": None,
                                "target": "self",
                                "type": "Normal",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Cute"
                            },
                            "solarbeam": {
                                "num": 76,
                                "accuracy": 100,
                                "basePower": 120,
                                "category": "Special",
                                "desc": "This attack charges on the first turn and executes on the second. Power is halved if the weather is Hail, Primordial Sea, Rain Dance, or Sandstorm. If the user is holding a Power Herb or the weather is Desolate Land or Sunny Day, the move completes in one turn.",
                                "shortDesc": "Charges turn 1. Hits turn 2. No charge in sunlight.",
                                "id": "solarbeam",
                                "name": "Solar Beam",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "charge": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Grass",
                                "zMovePower": 190,
                                "contestType": "Cool"
                            },
                            "solarblade": {
                                "num": 669,
                                "accuracy": 100,
                                "basePower": 125,
                                "category": "Physical",
                                "desc": "This attack charges on the first turn and executes on the second. Power is halved if the weather is Hail, Primordial Sea, Rain Dance, or Sandstorm. If the user is holding a Power Herb or the weather is Desolate Land or Sunny Day, the move completes in one turn.",
                                "shortDesc": "Charges turn 1. Hits turn 2. No charge in sunlight.",
                                "id": "solarblade",
                                "name": "Solar Blade",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "charge": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Grass",
                                "zMovePower": 190,
                                "contestType": "Cool"
                            },
                            "sonicboom": {
                                "num": 49,
                                "accuracy": 90,
                                "basePower": 0,
                                "damage": 20,
                                "category": "Special",
                                "desc": "Deals 20 HP of damage to the target.",
                                "shortDesc": "Always does 20 HP of damage.",
                                "id": "sonicboom",
                                "name": "Sonic Boom",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 100,
                                "contestType": "Cool"
                            },
                            "soulstealing7starstrike": {
                                "num": 699,
                                "accuracy": True,
                                "basePower": 195,
                                "category": "Physical",
                                "shortDesc": "No additional effect.",
                                "id": "soulstealing7starstrike",
                                "name": "Soul-Stealing 7-Star Strike",
                                "pp": 1,
                                "priority": 0,
                                "flags": {
                                    "contact": 1
                                },
                                "isZ": "marshadiumz",
                                "secondary": None,
                                "target": "normal",
                                "type": "Ghost",
                                "contestType": "Cool"
                            },
                            "spacialrend": {
                                "num": 460,
                                "accuracy": 95,
                                "basePower": 100,
                                "category": "Special",
                                "desc": "Has a higher chance for a critical hit.",
                                "shortDesc": "High critical hit ratio.",
                                "id": "spacialrend",
                                "isViable": True,
                                "name": "Spacial Rend",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "critRatio": 2,
                                "secondary": None,
                                "target": "normal",
                                "type": "Dragon",
                                "zMovePower": 180,
                                "contestType": "Beautiful"
                            },
                            "spark": {
                                "num": 209,
                                "accuracy": 100,
                                "basePower": 65,
                                "category": "Physical",
                                "desc": "Has a 30% chance to paralyze the target.",
                                "shortDesc": "30% chance to paralyze the target.",
                                "id": "spark",
                                "name": "Spark",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "status": "par",
                                },
                                "target": "normal",
                                "type": "Electric",
                                "zMovePower": 120,
                                "contestType": "Cool"
                            },
                            "sparklingaria": {
                                "num": 664,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Special",
                                "desc": "If the user has not fainted, the target is cured of its burn.",
                                "shortDesc": "The target is cured of its burn.",
                                "id": "sparklingaria",
                                "name": "Sparkling Aria",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "sound": 1,
                                    "authentic": 1
                                },
                                "target": "allAdjacent",
                                "type": "Water",
                                "zMovePower": 175,
                                "contestType": "Tough"
                            },
                            "sparklyswirl": {
                                "num": 740,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Special",
                                "desc": "Every Pokemon in the user's party is cured of its major status condition.",
                                "shortDesc": "Cures the user's party of all status conditions.",
                                "id": "sparklyswirl",
                                "isNonstandard": "LGPE",
                                "isUnreleased": True,
                                "isViable": True,
                                "name": "Sparkly Swirl",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Fairy",
                                "contestType": "Clever"
                            },
                            "spectralthief": {
                                "num": 712,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Physical",
                                "desc": "The target's stat stages greater than 0 are stolen from it and applied to the user before dealing damage.",
                                "shortDesc": "Steals target's boosts before dealing damage.",
                                "id": "spectralthief",
                                "isViable": True,
                                "name": "Spectral Thief",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "authentic": 1
                                },
                                "stealsBoosts": True,
                                "secondary": None,
                                "target": "normal",
                                "type": "Ghost",
                                "zMovePower": 175,
                                "contestType": "Cool"
                            },
                            "speedswap": {
                                "num": 683,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user swaps its Speed stat with the target. Stat stage changes are unaffected.",
                                "shortDesc": "Swaps Speed stat with target.",
                                "id": "speedswap",
                                "name": "Speed Swap",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "authentic": 1,
                                    "mystery": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "zMoveBoost": {
                                    "spe": 1
                                },
                                "contestType": "Clever"
                            },
                            "spiderweb": {
                                "num": 169,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Prevents the target from switching out. The target can still switch out if it is holding Shed Shell or uses Baton Pass, Parting Shot, U-turn, or Volt Switch. If the target leaves the field using Baton Pass, the replacement will remain trapped. The effect ends if the user leaves the field.",
                                "shortDesc": "Prevents the target from switching out.",
                                "id": "spiderweb",
                                "name": "Spider Web",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Bug",
                                "zMoveBoost": {
                                    "def": 1
                                },
                                "contestType": "Clever"
                            },
                            "spikecannon": {
                                "num": 131,
                                "accuracy": 100,
                                "basePower": 20,
                                "category": "Physical",
                                "desc": "Hits two to five times. Has a 1/3 chance to hit two or three times, and a 1/6 chance to hit four or five times. If one of the hits breaks the target's substitute, it will take damage for the remaining hits. If the user has the Skill Link Ability, this move will always hit five times.",
                                "shortDesc": "Hits 2-5 times in one turn.",
                                "id": "spikecannon",
                                "name": "Spike Cannon",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "multihit": [
                                    2,
                                    5
                                ],
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 100,
                                "contestType": "Cool"
                            },
                            "spikes": {
                                "num": 191,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Sets up a hazard on the opposing side of the field, damaging each opposing Pokemon that switches in, unless it is a Flying-type Pokemon or has the Levitate Ability. Can be used up to three times before failing. Opponents lose 1/8 of their maximum HP with one layer, 1/6 of their maximum HP with two layers, and 1/4 of their maximum HP with three layers, all rounded down. Can be removed from the opposing side if any opposing Pokemon uses Rapid Spin or Defog successfully, or is hit by Defog.",
                                "shortDesc": "Hurts grounded foes on switch-in. Max 3 layers.",
                                "id": "spikes",
                                "isViable": True,
                                "name": "Spikes",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "reflectable": 1,
                                    "nonsky": 1
                                },
                                "sideCondition": "spikes",
                                "secondary": None,
                                "target": "foeSide",
                                "type": "Ground",
                                "zMoveBoost": {
                                    "def": 1
                                },
                                "contestType": "Clever"
                            },
                            "spikyshield": {
                                "num": 596,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user is protected from most attacks made by other Pokemon during this turn, and Pokemon making contact with the user lose 1/8 of their maximum HP, rounded down. This move has a 1/X chance of being successful, where X starts at 1 and triples each time this move is successfully used. X resets to 1 if this move fails, if the user's last move used is not Baneful Bunker, Detect, Endure, King's Shield, Protect, Quick Guard, Spiky Shield, or Wide Guard, or if it was one of those moves and the user 's protection was broken. Fails if the user moves last this turn.",
                                "shortDesc": "Protects from moves contact  loses 1/8 max HP.",
                                "id": "spikyshield",
                                "isViable": True,
                                "name": "Spiky Shield",
                                "pp": 10,
                                "priority": 4,
                                "flags": {},
                                "stallingMove": True,
                                "volatileStatus": "spikyshield",
                                "secondary": None,
                                "target": "self",
                                "type": "Grass",
                                "zMoveBoost": {
                                    "def": 1
                                },
                                "contestType": "Tough"
                            },
                            "spiritshackle": {
                                "num": 662,
                                "accuracy": 100,
                                "basePower": 80,
                                "category": "Physical",
                                "desc": "Prevents the target from switching out. The target can still switch out if it is holding Shed Shell or uses Baton Pass, Parting Shot, U-turn, or Volt Switch. If the target leaves the field using Baton Pass, the replacement will remain trapped. The effect ends if the user leaves the field.",
                                "shortDesc": "Prevents the target from switching out.",
                                "id": "spiritshackle",
                                "isViable": True,
                                "name": "Spirit Shackle",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "target": "normal",
                                "type": "Ghost",
                                "zMovePower": 160,
                                "contestType": "Tough"
                            },
                            "spitup": {
                                "num": 255,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Special",
                                "desc": "Power is equal to 100 times the user's Stockpile count. Fails if the user's Stockpile count is 0. Whether or not this move is successful, the user's Defense and Special Defense decrease by as many stages as Stockpile had increased them, and the user's Stockpile count resets to 0.",
                                "shortDesc": "More power with more uses of Stockpile.",
                                "id": "spitup",
                                "name": "Spit Up",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 100,
                                "contestType": "Tough"
                            },
                            "spite": {
                                "num": 180,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Causes the target's last move used to lose 4 PP. Fails if the target has not made a move, if the move has 0 PP, or if it no longer knows the move.",
                                "shortDesc": "Lowers the PP of the target's last move by 4.",
                                "id": "spite",
                                "name": "Spite",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "authentic": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Ghost",
                                "zMoveEffect": "heal",
                                "contestType": "Tough"
                            },
                            "splash": {
                                "num": 150,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "shortDesc": "No competitive use.",
                                "id": "splash",
                                "name": "Splash",
                                "pp": 40,
                                "priority": 0,
                                "flags": {
                                    "gravity": 1
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "atk": 3
                                },
                                "contestType": "Cute"
                            },
                            "splinteredstormshards": {
                                "num": 727,
                                "accuracy": True,
                                "basePower": 190,
                                "category": "Physical",
                                "desc": "Ends the effects of Electric Terrain, Grassy Terrain, Misty Terrain, and Psychic Terrain.",
                                "shortDesc": "Ends the effects of Terrain.",
                                "id": "splinteredstormshards",
                                "name": "Splintered Stormshards",
                                "pp": 1,
                                "priority": 0,
                                "flags": {},
                                "isZ": "lycaniumz",
                                "secondary": None,
                                "target": "normal",
                                "type": "Rock",
                                "contestType": "Cool"
                            },
                            "splishysplash": {
                                "num": 730,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Special",
                                "desc": "Has a 30% chance to paralyze the target.",
                                "shortDesc": "30% chance to paralyze the target.",
                                "id": "splishysplash",
                                "isNonstandard": "LGPE",
                                "isUnreleased": True,
                                "isViable": True,
                                "name": "Splishy Splash",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "status": "par",
                                },
                                "target": "allAdjacentFoes",
                                "type": "Water",
                                "contestType": "Cool"
                            },
                            "spore": {
                                "num": 147,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "shortDesc": "Causes the target to fall asleep.",
                                "id": "spore",
                                "isViable": True,
                                "name": "Spore",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "powder": 1,
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "status": "slp",
                                "secondary": None,
                                "target": "normal",
                                "type": "Grass",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Beautiful"
                            },
                            "spotlight": {
                                "num": 671,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Until the end of the turn, all single-target attacks from opponents of the target are redirected to the target. Such attacks are redirected to the target before they can be reflected by Magic Coat or the Magic Bounce Ability, or drawn in by the Lightning Rod or Storm drain Abilities. Fails if it is not a Double Battle or Battle Royal.",
                                "shortDesc": "target's foes moves are redirected to it this turn.",
                                "id": "spotlight",
                                "name": "Spotlight",
                                "pp": 15,
                                "priority": 3,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mystery": 1
                                },
                                "volatileStatus": "spotlight",
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "spd": 1
                                },
                                "contestType": "Cute"
                            },
                            "stealthrock": {
                                "num": 446,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Sets up a hazard on the opposing side of the field, damaging each opposing Pokemon that switches in. Fails if the effect is already active on the opposing side. Foes lose 1/32, 1/16, 1/8, 1/4, or 1/2 of their maximum HP, rounded down, based on their weakness to the Rock type; 0.25x, 0.5x, neutral, 2x, or 4x, respectively. Can be removed from the opposing side if any opposing Pokemon uses Rapid Spin or Defog successfully, or is hit by Defog.",
                                "shortDesc": "Hurts foes on switch-in. Factors Rock weakness.",
                                "id": "stealthrock",
                                "isViable": True,
                                "name": "Stealth Rock",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "reflectable": 1
                                },
                                "sideCondition": "stealthrock",
                                "secondary": None,
                                "target": "foeSide",
                                "type": "Rock",
                                "zMoveBoost": {
                                    "def": 1
                                },
                                "contestType": "Cool"
                            },
                            "steameruption": {
                                "num": 592,
                                "accuracy": 95,
                                "basePower": 110,
                                "category": "Special",
                                "desc": "Has a 30% chance to burn the target. The target thaws out if it is frozen.",
                                "shortDesc": "30% chance to burn the target.",
                                "id": "steameruption",
                                "isViable": True,
                                "name": "Steam Eruption",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "defrost": 1
                                },
                                "thawsTarget": True,
                                "secondary": {
                                    "chance": 30,
                                    "status": "brn",
                                },
                                "target": "normal",
                                "type": "Water",
                                "zMovePower": 185,
                                "contestType": "Beautiful"
                            },
                            "steamroller": {
                                "num": 537,
                                "accuracy": 100,
                                "basePower": 65,
                                "category": "Physical",
                                "desc": "Has a 30% chance to flinch the target. Damage doubles and no 'accuracy' check is done if the target has used Minimize while active.",
                                "shortDesc": "30% chance to flinch the target.",
                                "id": "steamroller",
                                "name": "Steamroller",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "volatileStatus": "flinch"
                                },
                                "target": "normal",
                                "type": "Bug",
                                "zMovePower": 120,
                                "contestType": "Tough"
                            },
                            "steelwing": {
                                "num": 211,
                                "accuracy": 90,
                                "basePower": 70,
                                "category": "Physical",
                                "desc": "Has a 10% chance to raise the user's Defense by 1 stage.",
                                "shortDesc": "10% chance to raise the user's Defense by 1.",
                                "id": "steelwing",
                                "name": "Steel Wing",
                                "pp": 25,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 10,
                                    "self": {
                                        "boosts": {
                                            "def": 1,
                                        },
                                    },
                                },
                                "target": "normal",
                                "type": "Steel",
                                "zMovePower": 140,
                                "contestType": "Cool"
                            },
                            "stickyweb": {
                                "num": 564,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Sets up a hazard on the opposing side of the field, lowering the Speed by 1 stage of each opposing Pokemon that switches in, unless it is a Flying-type Pokemon or has the Levitate Ability. Fails if the effect is already active on the opposing side. Can be removed from the opposing side if any opposing Pokemon uses Rapid Spin or Defog successfully, or is hit by Defog.",
                                "shortDesc": "Lowers Speed of grounded foes by 1 on switch-in.",
                                "id": "stickyweb",
                                "isViable": True,
                                "name": "Sticky Web",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "reflectable": 1
                                },
                                "sideCondition": "stickyweb",
                                "secondary": None,
                                "target": "foeSide",
                                "type": "Bug",
                                "zMoveBoost": {
                                    "spe": 1
                                },
                                "contestType": "Tough"
                            },
                            "stockpile": {
                                "num": 254,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Raises the user's Defense and Special Defense by 1 stage. The user's Stockpile count increases by 1. Fails if the user's Stockpile count is 3. The user's Stockpile count is reset to 0 when it is no longer active.",
                                "shortDesc": "Raises user's Defense, Sp. Def by 1. Max 3 uses.",
                                "id": "stockpile",
                                "name": "Stockpile",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1
                                },
                                "volatileStatus": "stockpile",
                                "secondary": None,
                                "target": "self",
                                "type": "Normal",
                                "zMoveEffect": "heal",
                                "contestType": "Tough"
                            },
                            "stokedsparksurfer": {
                                "num": 700,
                                "accuracy": True,
                                "basePower": 175,
                                "category": "Special",
                                "desc": "Has a 100% chance to paralyze the target.",
                                "shortDesc": "100% chance to paralyze the target.",
                                "id": "stokedsparksurfer",
                                "name": "Stoked Sparksurfer",
                                "pp": 1,
                                "priority": 0,
                                "flags": {},
                                "isZ": "aloraichiumz",
                                "secondary": {
                                    "chance": 100,
                                    "status": "par",
                                },
                                "target": "normal",
                                "type": "Electric",
                                "contestType": "Cool"
                            },
                            "stomp": {
                                "num": 23,
                                "accuracy": 100,
                                "basePower": 65,
                                "category": "Physical",
                                "desc": "Has a 30% chance to flinch the target. Damage doubles and no 'accuracy' check is done if the target has used Minimize while active. ",
                                "shortDesc": "30% chance to flinch the target.",
                                "id": "stomp",
                                "name": "Stomp",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "nonsky": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "volatileStatus": "flinch"
                                },
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 120,
                                "contestType": "Tough"
                            },
                            "stompingtantrum": {
                                "num": 707,
                                "accuracy": 100,
                                "basePower": 75,
                                "category": "Physical",
                                "desc": "Power doubles if the user's last move on the previous turn, including moves called by other moves or those used through Instruct, Magic Coat, Snatch, or the Dancer or Magic Bounce Abilities, failed to do any of its normal effects, not including damage from an unsuccessful High Jump Kick, Jump Kick, or Mind Blown, or if the user was prevented from moving by any effect other than recharging or Sky Drop. A move that was blocked by Baneful Bunker, Detect, King's Shield, Protect, Spiky Shield, Crafty Shield, Mat Block, Quick Guard, or Wide Guard will not double this move 's power, nor will Bounce or Fly ending early due to the effect of Gravity, Smack Down, or Thousand Arrows.",
                                "shortDesc": "Power doubles if the user's last move failed.",
                                "id": "stompingtantrum",
                                "name": "Stomping Tantrum",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Ground",
                                "zMovePower": 140,
                                "contestType": "Tough"
                            },
                            "stoneedge": {
                                "num": 444,
                                "accuracy": 80,
                                "basePower": 100,
                                "category": "Physical",
                                "desc": "Has a higher chance for a critical hit.",
                                "shortDesc": "High critical hit ratio.",
                                "id": "stoneedge",
                                "isViable": True,
                                "name": "Stone Edge",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "critRatio": 2,
                                "secondary": None,
                                "target": "normal",
                                "type": "Rock",
                                "zMovePower": 180,
                                "contestType": "Tough"
                            },
                            "storedpower": {
                                "num": 500,
                                "accuracy": 100,
                                "basePower": 20,
                                "category": "Special",
                                "desc": "Power is equal to 20+(X*20), where X is the user's total stat stage changes that are greater than 0.",
                                "shortDesc": " + 20 power for each of the user's stat boosts.",
                                "id": "storedpower",
                                "name": "Stored Power",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "zMovePower": 160,
                                "contestType": "Clever"
                            },
                            "stormthrow": {
                                "num": 480,
                                "accuracy": 100,
                                "basePower": 60,
                                "category": "Physical",
                                "desc": "This move is always a critical hit unless the target is under the effect of Lucky Chant or has the Battle Armor or Shell Armor Abilities.",
                                "shortDesc": "Always results in a critical hit.",
                                "id": "stormthrow",
                                "isViable": True,
                                "name": "Storm Throw",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "willCrit": True,
                                "secondary": None,
                                "target": "normal",
                                "type": "Fighting",
                                "zMovePower": 120,
                                "contestType": "Cool"
                            },
                            "strength": {
                                "num": 70,
                                "accuracy": 100,
                                "basePower": 80,
                                "category": "Physical",
                                "shortDesc": "No additional effect.",
                                "id": "strength",
                                "name": "Strength",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 160,
                                "contestType": "Tough"
                            },
                            "strengthsap": {
                                "num": 668,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Lowers the target's Attack by 1 stage. The user restores its HP equal to the target's Attack stat calculated with its stat stage before this move was used. If Big Root is held by the user, the HP recovered is 1.3x normal, rounded half down. Fails if the target's Attack stat stage is -6.",
                                "shortDesc": "User heals HP=target's Atk stat. Lowers Atk by 1.",
                                "id": "strengthsap",
                                "isViable": True,
                                "name": "Strength Sap",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "heal": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Grass",
                                "zMoveBoost": {
                                    "def": 1
                                },
                                "contestType": "Cute"
                            },
                            "stringshot": {
                                "num": 81,
                                "accuracy": 95,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Lowers the target's Speed by 2 stages.",
                                "shortDesc": "Lowers the foe(s) Speed by 2.",
                                "id": "stringshot",
                                "name": "String Shot",
                                "pp": 40,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "boosts": {
                                    "spe": -2,
                                },
                                "secondary": None,
                                "target": "allAdjacentFoes",
                                "type": "Bug",
                                "zMoveBoost": {
                                    "spe": 1
                                },
                                "contestType": "Clever"
                            },
                            "struggle": {
                                "num": 165,
                                "accuracy": True,
                                "basePower": 50,
                                "category": "Physical",
                                "desc": "Deals typeless damage to a random opposing Pokemon. If this move was successful, the user loses 1/4 of its maximum HP, rounded half up, and the Rock Head Ability does not prevent this. This move is automatically used if none of the user's known moves can be selected.",
                                "shortDesc": "User loses 1/4 of its max HP.",
                                "id": "struggle",
                                "name": "Struggle",
                                "pp": 1,
                                "noPPBoosts": True,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1
                                },
                                "noSketch": True,
                                "struggleRecoil": True,
                                "secondary": None,
                                "target": "randomNormal",
                                "type": "Normal",
                                "zMovePower": 1,
                                "contestType": "Tough"
                            },
                            "strugglebug": {
                                "num": 522,
                                "accuracy": 100,
                                "basePower": 50,
                                "category": "Special",
                                "desc": "Has a 100% chance to lower the target's Special Attack by 1 stage.",
                                "shortDesc": "100% chance to lower the foe(s) Sp. Atk by 1.",
                                "id": "strugglebug",
                                "name": "Struggle Bug",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 100,
                                    "boosts": {
                                        "spa": -1,
                                    },
                                },
                                "target": "allAdjacentFoes",
                                "type": "Bug",
                                "zMovePower": 100,
                                "contestType": "Cute"
                            },
                            "stunspore": {
                                "num": 78,
                                "accuracy": 75,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Paralyzes the target.",
                                "shortDesc": "Paralyzes the target.",
                                "id": "stunspore",
                                "name": "Stun Spore",
                                "pp": 30,
                                "priority": 0,
                                "flags": {
                                    "powder": 1,
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "status": "par",
                                "secondary": None,
                                "target": "normal",
                                "type": "Grass",
                                "zMoveBoost": {
                                    "spd": 1
                                },
                                "contestType": "Clever"
                            },
                            "submission": {
                                "num": 66,
                                "accuracy": 80,
                                "basePower": 80,
                                "category": "Physical",
                                "desc": "If the target lost HP, the user takes recoil damage equal to 1/4 the HP lost by the target, rounded half up, but not less than 1 HP.",
                                "shortDesc": "Has 1/4 recoil.",
                                "id": "submission",
                                "name": "Submission",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "recoil": [
                                    1,
                                    4
                                ],
                                "secondary": None,
                                "target": "normal",
                                "type": "Fighting",
                                "zMovePower": 160,
                                "contestType": "Cool"
                            },
                            "substitute": {
                                "num": 164,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user takes 1/4 of its maximum HP, rounded down, and puts it into a substitute to take its place in battle. The substitute is removed once enough damage is inflicted on it, or if the user switches out or faints. Baton Pass can be used to transfer the substitute to an ally, and the substitute will keep its remaining HP. Until the substitute is broken, it receives damage from all attacks made by other Pokemon and shields the user from status effects and stat stage changes caused by other Pokemon. Sound-based moves and Pokemon with the Infiltrator Ability ignore substitutes. The user still takes normal damage from weather and status effects while behind its substitute. If the substitute breaks during a multi-hit attack, the user will take damage from any remaining hits. If a substitute is created while the user is trapped by a binding move, the binding effect ends immediately. Fails if the user does not have enough HP remaining to create a substitute without fainting, or if it already has a substitute.",
                                "shortDesc": "User takes 1/4 its max HP to put in a substitute.",
                                "id": "substitute",
                                "isViable": True,
                                "name": "Substitute",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1,
                                    "nonsky": 1
                                },
                                "volatileStatus": "substitute",
                                "secondary": None,
                                "target": "self",
                                "type": "Normal",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Cute"
                            },
                            "subzeroslammer": {
                                "num": 650,
                                "accuracy": True,
                                "basePower": 1,
                                "category": "Physical",
                                "shortDesc": "Power is equal to the base move's Z-Power.",
                                "id": "subzeroslammer",
                                "isViable": True,
                                "name": "Subzero Slammer",
                                "pp": 1,
                                "priority": 0,
                                "flags": {},
                                "isZ": "iciumz",
                                "secondary": None,
                                "target": "normal",
                                "type": "Ice",
                                "contestType": "Cool"
                            },
                            "suckerpunch": {
                                "num": 389,
                                "accuracy": 100,
                                "basePower": 70,
                                "category": "Physical",
                                "desc": "Fails if the target did not select a physical attack, special attack, or Me First for use this turn, or if the target moves before the user.",
                                "shortDesc": "Usually goes first. Fails if target is not attacking.",
                                "id": "suckerpunch",
                                "isViable": True,
                                "name": "Sucker Punch",
                                "pp": 5,
                                "priority": 1,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Dark",
                                "zMovePower": 140,
                                "contestType": "Clever"
                            },
                            "sunnyday": {
                                "num": 241,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "For 5 turns, the weather becomes Sunny Day. The damage of Fire-type attacks is multiplied by 1.5 and the damage of Water-type attacks is multiplied by 0.5 during the effect. Lasts for 8 turns if the user is holding Heat Rock. Fails if the current weather is Sunny Day.",
                                "shortDesc": "For 5 turns, intense sunlight powers Fire moves.",
                                "id": "sunnyday",
                                "name": "Sunny Day",
                                "pp": 5,
                                "priority": 0,
                                "flags": {},
                                "weather": "sunnyday",
                                "secondary": None,
                                "target": "all",
                                "type": "Fire",
                                "zMoveBoost": {
                                    "spe": 1
                                },
                                "contestType": "Beautiful"
                            },
                            "sunsteelstrike": {
                                "num": 713,
                                "accuracy": 100,
                                "basePower": 100,
                                "category": "Physical",
                                "desc": "This move and its effects ignore the Abilities of other Pokemon.",
                                "shortDesc": "Ignores the Abilities of other Pokemon.",
                                "id": "sunsteelstrike",
                                "isViable": True,
                                "name": "Sunsteel Strike",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "ignoreAbility": True,
                                "secondary": None,
                                "target": "normal",
                                "type": "Steel",
                                "zMovePower": 180,
                                "contestType": "Cool"
                            },
                            "superfang": {
                                "num": 162,
                                "accuracy": 90,
                                "category": "Physical",
                                "desc": "Deals damage to the target equal to half of its current HP, rounded down, but not less than 1 HP.",
                                "shortDesc": "Does damage equal to 1/2 target's current HP.",
                                "id": "superfang",
                                "isViable": True,
                                "name": "Super Fang",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 100,
                                "contestType": "Tough"
                            },
                            "superpower": {
                                "num": 276,
                                "accuracy": 100,
                                "basePower": 120,
                                "category": "Physical",
                                "desc": "Lowers the user's Attack and Defense by 1 stage.",
                                "shortDesc": "Lowers the user's Attack and Defense by 1.",
                                "id": "superpower",
                                "isViable": True,
                                "name": "Superpower",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "self": {
                                    "boosts": {
                                        "atk": -1,
                                        "def": -1,
                                    },
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Fighting",
                                "zMovePower": 190,
                                "contestType": "Tough"
                            },
                            "supersonic": {
                                "num": 48,
                                "accuracy": 55,
                                "basePower": 0,
                                "category": "Status",
                                "shortDesc": "Causes the target to become confused.",
                                "id": "supersonic",
                                "name": "Supersonic",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "sound": 1,
                                    "authentic": 1
                                },
                                "volatileStatus": "confusion",
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "spe": 1
                                },
                                "contestType": "Clever"
                            },
                            "supersonicskystrike": {
                                "num": 626,
                                "accuracy": True,
                                "basePower": 1,
                                "category": "Physical",
                                "shortDesc": "Power is equal to the base move's Z-Power.",
                                "id": "supersonicskystrike",
                                "isViable": True,
                                "name": "Supersonic Skystrike",
                                "pp": 1,
                                "priority": 0,
                                "flags": {},
                                "isZ": "flyiniumz",
                                "secondary": None,
                                "target": "normal",
                                "type": "Flying",
                                "contestType": "Cool"
                            },
                            "surf": {
                                "num": 57,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Special",
                                "desc": "Damage doubles if the target is using Dive.",
                                "shortDesc": "Hits adjacent Pokemon. Double damage on Dive.",
                                "id": "surf",
                                "isViable": True,
                                "name": "Surf",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "nonsky": 1
                                },
                                "secondary": None,
                                "target": "allAdjacent",
                                "type": "Water",
                                "zMovePower": 175,
                                "contestType": "Beautiful"
                            },
                            "swagger": {
                                "num": 207,
                                "accuracy": 85,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Raises the target's Attack by 2 stages and confuses it.",
                                "shortDesc": "Raises the target's Attack by 2 and confuses it.",
                                "id": "swagger",
                                "name": "Swagger",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "mystery": 1
                                },
                                "volatileStatus": "confusion",
                                "boosts": {
                                    "atk": 2,
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Cute"
                            },
                            "swallow": {
                                "num": 256,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user restores its HP based on its Stockpile count. Restores 1/4 of its maximum HP if it's 1, 1 / 2 of its maximum HP if it's 2, both rounded half down, and all of its HP if it's 3. Fails if the user 's Stockpile count is 0. The user's Defense and Special Defense decrease by as many stages as Stockpile had increased them, and the user 's Stockpile count resets to 0.",
                                "shortDesc": "Heals the user based on uses of Stockpile.",
                                "id": "swallow",
                                "name": "Swallow",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1,
                                    "heal": 1
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Normal",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Tough"
                            },
                            "sweetkiss": {
                                "num": 186,
                                "accuracy": 75,
                                "basePower": 0,
                                "category": "Status",
                                "shortDesc": "Causes the target to become confused.",
                                "id": "sweetkiss",
                                "name": "Sweet Kiss",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "volatileStatus": "confusion",
                                "secondary": None,
                                "target": "normal",
                                "type": "Fairy",
                                "zMoveBoost": {
                                    "spa": 1
                                },
                                "contestType": "Cute"
                            },
                            "sweetscent": {
                                "num": 230,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Lowers the target's evasiveness by 2 stages.",
                                "shortDesc": "Lowers the foe(s) evasiveness by 2.",
                                "id": "sweetscent",
                                "name": "Sweet Scent",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "boosts": {
                                    "evasion": -2,
                                },
                                "secondary": None,
                                "target": "allAdjacentFoes",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "accuracy": 1
                                },
                                "contestType": "Cute"
                            },
                            "swift": {
                                "num": 129,
                                "accuracy": True,
                                "basePower": 60,
                                "category": "Special",
                                "desc": "This move does not check 'accuracy'.",
                                "shortDesc": "This move does not check 'accuracy'. Hits foes.",
                                "id": "swift",
                                "name": "Swift",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "allAdjacentFoes",
                                "type": "Normal",
                                "zMovePower": 120,
                                "contestType": "Cool"
                            },
                            "switcheroo": {
                                "num": 415,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user swaps its held item with the target's held item. Fails if either the user or the target is holding a Mail or Z-Crystal, if neither is holding an item, if the user is trying to give or take a Mega Stone to or from the species that can Mega Evolve with it, or if the user is trying to give or take a Blue Orb, a Red Orb, a Griseous Orb, a Plate, a Drive, or a Memory to or from a Kyogre, a Groudon, a Giratina, an Arceus, a Genesect, or a Silvally, respectively. The target is immune to this move if it has the Sticky Hold Ability.",
                                "shortDesc": "User switches its held item with the target's.",
                                "id": "switcheroo",
                                "isViable": True,
                                "name": "Switcheroo",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "mystery": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Dark",
                                "zMoveBoost": {
                                    "spe": 2
                                },
                                "contestType": "Clever"
                            },
                            "swordsdance": {
                                "num": 14,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Raises the user's Attack by 2 stages.",
                                "shortDesc": "Raises the user's Attack by 2.",
                                "id": "swordsdance",
                                "isViable": True,
                                "name": "Swords Dance",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1,
                                    "dance": 1
                                },
                                "boosts": {
                                    "atk": 2,
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Normal",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Beautiful"
                            },
                            "synchronoise": {
                                "num": 485,
                                "accuracy": 100,
                                "basePower": 120,
                                "category": "Special",
                                "desc": "The target is immune if it does not share a type with the user.",
                                "shortDesc": "Hits adjacent Pokemon sharing the user's type.",
                                "id": "synchronoise",
                                "name": "Synchronoise",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "allAdjacent",
                                "type": "Psychic",
                                "zMovePower": 190,
                                "contestType": "Clever"
                            },
                            "synthesis": {
                                "num": 235,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user restores 1/2 of its maximum HP if Delta Stream or no weather conditions are in effect, 2/3 of its maximum HP if the weather is Desolate Land or Sunny Day, and 1/4 of its maximum HP if the weather is Hail, Primordial Sea, Rain Dance, or Sandstorm, all rounded half down.",
                                "shortDesc": "Heals the user by a weather-dependent amount.",
                                "id": "synthesis",
                                "isViable": True,
                                "name": "Synthesis",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1,
                                    "heal": 1
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Grass",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Clever"
                            },
                            "tackle": {
                                "num": 33,
                                "accuracy": 100,
                                "basePower": 40,
                                "category": "Physical",
                                "shortDesc": "No additional effect.",
                                "id": "tackle",
                                "name": "Tackle",
                                "pp": 35,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 100,
                                "contestType": "Tough"
                            },
                            "tailglow": {
                                "num": 294,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Raises the user's Special Attack by 3 stages.",
                                "shortDesc": "Raises the user's Sp. Atk by 3.",
                                "id": "tailglow",
                                "isViable": True,
                                "name": "Tail Glow",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1
                                },
                                "boosts": {
                                    "spa": 3,
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Bug",
                                "zMoveEffect": "clearnegativeboost",
                                "contestType": "Beautiful"
                            },
                            "tailslap": {
                                "num": 541,
                                "accuracy": 85,
                                "basePower": 25,
                                "category": "Physical",
                                "desc": "Hits two to five times. Has a 1/3 chance to hit two or three times, and a 1/6 chance to hit four or five times. If one of the hits breaks the target's substitute, it will take damage for the remaining hits. If the user has the Skill Link Ability, this move will always hit five times.",
                                "shortDesc": "Hits 2-5 times in one turn.",
                                "id": "tailslap",
                                "isViable": True,
                                "name": "Tail Slap",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "multihit": [
                                    2,
                                    5
                                ],
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 140,
                                "contestType": "Cute"
                            },
                            "tailwhip": {
                                "num": 39,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Lowers the target's Defense by 1 stage.",
                                "shortDesc": "Lowers the foe(s) Defense by 1.",
                                "id": "tailwhip",
                                "name": "Tail Whip",
                                "pp": 30,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "boosts": {
                                    "def": -1,
                                },
                                "secondary": None,
                                "target": "allAdjacentFoes",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "atk": 1
                                },
                                "contestType": "Cute"
                            },
                            "tailwind": {
                                "num": 366,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "For 4 turns, the user and its party members have their Speed doubled. Fails if this move is already in effect for the user's side.",
                                "shortDesc": "For 4 turns, alliesSpeed is doubled.",
                                "id": "tailwind",
                                "isViable": True,
                                "name": "Tailwind",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1
                                },
                                "sideCondition": "tailwind",
                                "secondary": None,
                                "target": "allySide",
                                "type": "Flying",
                                "zMoveEffect": "crit2",
                                "contestType": "Cool"
                            },
                            "takedown": {
                                "num": 36,
                                "accuracy": 85,
                                "basePower": 90,
                                "category": "Physical",
                                "desc": "If the target lost HP, the user takes recoil damage equal to 1/4 the HP lost by the target, rounded half up, but not less than 1 HP.",
                                "shortDesc": "Has 1/4 recoil.",
                                "id": "takedown",
                                "name": "Take Down",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "recoil": [
                                    1,
                                    4
                                ],
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 175,
                                "contestType": "Tough"
                            },
                            "taunt": {
                                "num": 269,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Prevents the target from using non-damaging moves for its next three turns. Pokemon with the Oblivious Ability or protected by the Aroma Veil Ability are immune.",
                                "shortDesc": "Target can't use status moves its next 3 turns",
                                "id": "taunt",
                                "isViable": True,
                                "name": "Taunt",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "authentic": 1
                                },
                                "volatileStatus": "taunt",
                                "secondary": None,
                                "target": "normal",
                                "type": "Dark",
                                "zMoveBoost": {
                                    "atk": 1
                                },
                                "contestType": "Clever"
                            },
                            "tearfullook": {
                                "num": 715,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Lowers the target's Attack and Special Attack by 1 stage.",
                                "shortDesc": "Lowers the target's Attack and Sp. Atk by 1.",
                                "id": "tearfullook",
                                "name": "Tearful Look",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "boosts": {
                                    "atk": -1,
                                    "spa": -1,
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "def": 1
                                },
                                "contestType": "Cute"
                            },
                            "technoblast": {
                                "num": 546,
                                "accuracy": 100,
                                "basePower": 120,
                                "category": "Special",
                                "desc": "This move's type depends on the user's held Drive.",
                                "shortDesc": "Type varies based on the held Drive.",
                                "id": "technoblast",
                                "isViable": True,
                                "name": "Techno Blast",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 190,
                                "contestType": "Cool"
                            },
                            "tectonicrage": {
                                "num": 630,
                                "accuracy": True,
                                "basePower": 1,
                                "category": "Physical",
                                "shortDesc": "Power is equal to the base move's Z-Power.",
                                "id": "tectonicrage",
                                "isViable": True,
                                "name": "Tectonic Rage",
                                "pp": 1,
                                "priority": 0,
                                "flags": {},
                                "isZ": "groundiumz",
                                "secondary": None,
                                "target": "normal",
                                "type": "Ground",
                                "contestType": "Cool"
                            },
                            "teeterdance": {
                                "num": 298,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Causes the target to become confused.",
                                "shortDesc": "Confuses adjacent Pokemon.",
                                "id": "teeterdance",
                                "name": "Teeter Dance",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "dance": 1
                                },
                                "volatileStatus": "confusion",
                                "secondary": None,
                                "target": "allAdjacent",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "spa": 1
                                },
                                "contestType": "Cute"
                            },
                            "telekinesis": {
                                "num": 477,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "For 3 turns, the target cannot avoid any attacks made against it, other than OHKO moves, as long as it remains active. During the effect, the target is immune to Ground-type attacks and the effects of Spikes, Toxic Spikes, Sticky Web, and the Arena Trap Ability as long as it remains active. If the target uses Baton Pass, the replacement will gain the effect. Ingrain, Smack Down, Thousand Arrows, and Iron Ball override this move if the target is under any of their effects. Fails if the target is already under this effect or the effects of Ingrain, Smack Down, or Thousand Arrows. The target is immune to this move on use if its species is Diglett, Dugtrio, Alolan Diglett, Alolan Dugtrio, Sandygast, Palossand, or Gengar while Mega-Evolved. Mega Gengar cannot be under this effect by any means.",
                                "shortDesc": "For 3 turns, target floats but moves can't miss it.",
                                "id": "telekinesis",
                                "name": "Telekinesis",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "gravity": 1,
                                    "mystery": 1
                                },
                                "volatileStatus": "telekinesis",
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "zMoveBoost": {
                                    "spa": 1
                                },
                                "contestType": "Clever"
                            },
                            "teleport": {
                                "num": 100,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "shortDesc": "Fails when used.",
                                "id": "teleport",
                                "name": "Teleport",
                                "pp": 20,
                                "priority": 0,
                                "flags": {},
                                "onTryHit": False,
                                "secondary": None,
                                "target": "self",
                                "type": "Psychic",
                                "zMoveEffect": "heal",
                                "contestType": "Cool"
                            },
                            "thief": {
                                "num": 168,
                                "accuracy": 100,
                                "basePower": 60,
                                "category": "Physical",
                                "desc": "If this attack was successful and the user has not fainted, it steals the target's held item if the user is not holding one. The target's item is not stolen if it is a Mail or Z-Crystal, or if the target is a Kyogre holding a Blue Orb, a Groudon holding a Red Orb, a Giratina holding a Griseous Orb, an Arceus holding a Plate, a Genesect holding a Drive, a Silvally holding a Memory, or a Pokemon that can Mega Evolve holding the Mega Stone for its species. Items lost to this move cannot be regained with Recycle or the Harvest Ability.",
                                "shortDesc": "If the user has no item, it steals the target's.",
                                "id": "thief",
                                "name": "Thief",
                                "pp": 25,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Dark",
                                "zMovePower": 120,
                                "contestType": "Tough"
                            },
                            "thousandarrows": {
                                "num": 614,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Physical",
                                "desc": "This move can hit airborne Pokemon, which includes Flying-type Pokemon, Pokemon with the Levitate Ability, Pokemon holding an Air Balloon, and Pokemon under the effect of Magnet Rise or Telekinesis. If the target is a Flying type and is not already grounded, this move deals neutral damage regardless of its other type(s). This move can hit a target using Bounce, Fly, or Sky Drop. If this move hits a target under the effect of Bounce, Fly, Magnet Rise, or Telekinesis, the effect ends. If the target is a Flying type that has not used Roost this turn or a Pokemon with the Levitate Ability, it loses its immunity to Ground-type attacks and the Arena Trap Ability as long as it remains active. During the effect, Magnet Rise fails for the target and Telekinesis fails against the target.",
                                "shortDesc": "Grounds adjacent foes. First hit neutral on Flying.",
                                "id": "thousandarrows",
                                "isViable": True,
                                "name": "Thousand Arrows",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "nonsky": 1
                                },
                                "volatileStatus": "smackdown",
                                "ignoreImmunity": {
                                    "Ground": True
                                },
                                "secondary": None,
                                "target": "allAdjacentFoes",
                                "type": "Ground",
                                "zMovePower": 180,
                                "contestType": "Beautiful"
                            },
                            "thousandwaves": {
                                "num": 615,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Physical",
                                "desc": "Prevents the target from switching out. The target can still switch out if it is holding Shed Shell or uses Baton Pass, Parting Shot, U-turn, or Volt Switch. If the target leaves the field using Baton Pass, the replacement will remain trapped. The effect ends if the user leaves the field.",
                                "shortDesc": "Hits adjacent foes. Prevents them from switching.",
                                "id": "thousandwaves",
                                "name": "Thousand Waves",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "nonsky": 1
                                },
                                "secondary": None,
                                "target": "allAdjacentFoes",
                                "type": "Ground",
                                "zMovePower": 175,
                                "contestType": "Tough"
                            },
                            "thrash": {
                                "num": 37,
                                "accuracy": 100,
                                "basePower": 120,
                                "category": "Physical",
                                "desc": "The user spends two or three turns locked into this move and becomes confused immediately after its move on the last turn of the effect if it is not already. This move targets an opposing Pokemon at random on each turn. If the user is prevented from moving, is asleep at the beginning of a turn, or the attack is not successful against the target on the first turn of the effect or the second turn of a three-turn effect, the effect ends without causing confusion. If this move is called by Sleep Talk and the user is asleep, the move is used for one turn and does not confuse the user.",
                                "shortDesc": "Lasts 2-3 turns. Confuses the user afterwards.",
                                "id": "thrash",
                                "name": "Thrash",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "self": {
                                    "volatileStatus": "lockedmove",
                                },
                                "secondary": None,
                                "target": "randomNormal",
                                "type": "Normal",
                                "zMovePower": 190,
                                "contestType": "Tough"
                            },
                            "throatchop": {
                                "num": 675,
                                "accuracy": 100,
                                "basePower": 80,
                                "category": "Physical",
                                "desc": "For 2 turns, the target cannot use sound-based moves.",
                                "shortDesc": "For 2 turns, the target cannot use sound moves.",
                                "id": "throatchop",
                                "name": "Throat Chop",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "target": "normal",
                                "type": "Dark",
                                "zMovePower": 160,
                                "contestType": "Clever"
                            },
                            "thunder": {
                                "num": 87,
                                "accuracy": 70,
                                "basePower": 110,
                                "category": "Special",
                                "desc": "Has a 30% chance to paralyze the target. This move can hit a target using Bounce, Fly, or Sky Drop, or is under the effect of Sky Drop. If the weather is Primordial Sea or Rain Dance, this move does not check. If the weather is Desolate Land or Sunny Day, this move's is 50 % .",
                                "shortDesc": "30% chance to paralyze. Can't miss in rain.",
                                "id": "thunder",
                                "isViable": True,
                                "name": "Thunder",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 30,
                                    "status": "par",
                                },
                                "target": "normal",
                                "type": "Electric",
                                "zMovePower": 185,
                                "contestType": "Cool"
                            },
                            "thunderbolt": {
                                "num": 85,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Special",
                                "desc": "Has a 10% chance to paralyze the target.",
                                "shortDesc": "10% chance to paralyze the target.",
                                "id": "thunderbolt",
                                "isViable": True,
                                "name": "Thunderbolt",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 10,
                                    "status": "par",
                                },
                                "target": "normal",
                                "type": "Electric",
                                "zMovePower": 175,
                                "contestType": "Cool"
                            },
                            "thunderfang": {
                                "num": 422,
                                "accuracy": 95,
                                "basePower": 65,
                                "category": "Physical",
                                "desc": "Has a 10% chance to paralyze the target and a 10% chance to flinch it.",
                                "shortDesc": "10% chance to paralyze. 10% chance to flinch.",
                                "id": "thunderfang",
                                "name": "Thunder Fang",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "bite": 1,
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondaries": [{
                                        "chance": 10,
                                        "status": "par",
                                    },
                                    {
                                        "chance": 10,
                                        "volatileStatus": "flinch"
                                    },
                                ],
                                "target": "normal",
                                "type": "Electric",
                                "zMovePower": 120,
                                "contestType": "Cool"
                            },
                            "thunderpunch": {
                                "num": 9,
                                "accuracy": 100,
                                "basePower": 75,
                                "category": "Physical",
                                "desc": "Has a 10% chance to paralyze the target.",
                                "shortDesc": "10% chance to paralyze the target.",
                                "id": "thunderpunch",
                                "isViable": True,
                                "name": "Thunder Punch",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "powder": 1
                                },
                                "secondary": {
                                    "chance": 10,
                                    "status": "par",
                                },
                                "target": "normal",
                                "type": "Electric",
                                "zMovePower": 140,
                                "contestType": "Cool"
                            },
                            "thundershock": {
                                "num": 84,
                                "accuracy": 100,
                                "basePower": 40,
                                "category": "Special",
                                "desc": "Has a 10% chance to paralyze the target.",
                                "shortDesc": "10% chance to paralyze the target.",
                                "id": "thundershock",
                                "name": "Thunder Shock",
                                "pp": 30,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 10,
                                    "status": "par",
                                },
                                "target": "normal",
                                "type": "Electric",
                                "zMovePower": 100,
                                "contestType": "Cool"
                            },
                            "thunderwave": {
                                "num": 86,
                                "accuracy": 90,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Paralyzes the target. This move does not ignore type immunity.",
                                "shortDesc": "Paralyzes the target.",
                                "id": "thunderwave",
                                "isViable": True,
                                "name": "Thunder Wave",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "status": "par",
                                "ignoreImmunity": False,
                                "secondary": None,
                                "target": "normal",
                                "type": "Electric",
                                "zMoveBoost": {
                                    "spd": 1
                                },
                                "contestType": "Cool"
                            },
                            "tickle": {
                                "num": 321,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Lowers the target's Attack and Defense by 1 stage.",
                                "shortDesc": "Lowers the target's Attack and Defense by 1.",
                                "id": "tickle",
                                "name": "Tickle",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "mystery": 1
                                },
                                "boosts": {
                                    "atk": -1,
                                    "def": -1,
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "def": 1
                                },
                                "contestType": "Cute"
                            },
                            "topsyturvy": {
                                "num": 576,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The target's positive stat stages become negative and vice versa. Fails if all of the target's stat stages are 0.",
                                "shortDesc": "Inverts the target's stat stages.",
                                "id": "topsyturvy",
                                "name": "Topsy-Turvy",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "mystery": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Dark",
                                "zMoveBoost": {
                                    "atk": 1
                                },
                                "contestType": "Clever"
                            },
                            "torment": {
                                "num": 259,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Prevents the target from selecting the same move for use two turns in a row. This effect ends when the target is no longer active.",
                                "shortDesc": "Target can't select the same move twice in a row.",
                                "id": "torment",
                                "name": "Torment",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "authentic": 1
                                },
                                "volatileStatus": "torment",
                                "secondary": None,
                                "target": "normal",
                                "type": "Dark",
                                "zMoveBoost": {
                                    "def": 1
                                },
                                "contestType": "Tough"
                            },
                            "toxic": {
                                "num": 92,
                                "accuracy": 90,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Badly poisons the target. If a Poison-type Pokemon uses this move, the target cannot avoid the attack, even if the target is in the middle of a two-turn move.",
                                "shortDesc": "Badly poisons the target. Poison types can't miss.",
                                "id": "toxic",
                                "isViable": True,
                                "name": "Toxic",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "status": "tox",
                                "secondary": None,
                                "target": "normal",
                                "type": "Poison",
                                "zMoveBoost": {
                                    "def": 1
                                },
                                "contestType": "Clever"
                            },
                            "toxicspikes": {
                                "num": 390,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Sets up a hazard on the opposing side of the field, poisoning each opposing Pokemon that switches in, unless it is a Flying-type Pokemon or has the Levitate Ability. Can be used up to two times before failing. Opposing Pokemon become poisoned with one layer and badly poisoned with two layers. Can be removed from the opposing side if any opposing Pokemon uses Rapid Spin or Defog successfully, is hit by Defog, or a grounded Poison-type Pokemon switches in. Safeguard prevents the opposing party from being poisoned on switch-in, but a substitute does not.",
                                "shortDesc": "Poisons grounded foes on switch-in. Max 2 layers.",
                                "id": "toxicspikes",
                                "isViable": True,
                                "name": "Toxic Spikes",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "reflectable": 1,
                                    "nonsky": 1
                                },
                                "sideCondition": "toxicspikes",
                                "secondary": None,
                                "target": "foeSide",
                                "type": "Poison",
                                "zMoveBoost": {
                                    "def": 1
                                },
                                "contestType": "Clever"
                            },
                            "toxicthread": {
                                "num": 672,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Lowers the target's Speed by 1 stage and poisons it.",
                                "shortDesc": "Lowers the target's Speed by 1 and poisons it.",
                                "id": "toxicthread",
                                "isViable": True,
                                "name": "Toxic Thread",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "status": "psn",
                                "boosts": {
                                    "spe": -1,
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Poison",
                                "zMoveBoost": {
                                    "spe": 1
                                },
                                "contestType": "Tough"
                            },
                            "transform": {
                                "num": 144,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user transforms into the target. The target's current stats, stat stages, types, moves, Ability, weight, gender, and sprite are copied. The user's level and HP remain the same and each copied move receives only 5 PP, with a maximum of 5 PP each. The user can no longer change formes if it would have the ability to do so. This move fails if it hits a substitute, if either the user or the target is already transformed, or if either is behind an Illusion.",
                                "shortDesc": "Copies target's stats, moves, types, and Ability.",
                                "id": "transform",
                                "name": "Transform",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "mystery": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveEffect": "heal",
                                "contestType": "Clever"
                            },
                            "triattack": {
                                "num": 161,
                                "accuracy": 100,
                                "basePower": 80,
                                "category": "Special",
                                "desc": "Has a 20% chance to either burn, freeze, or paralyze the target.",
                                "shortDesc": "20% chance to paralyze or burn or freeze target.",
                                "id": "triattack",
                                "isViable": True,
                                "name": "Tri Attack",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 20
                                },
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 160,
                                "contestType": "Beautiful"
                            },
                            "trick": {
                                "num": 271,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user swaps its held item with the target's held item. Fails if either the user or the target is holding a Mail or Z-Crystal, if neither is holding an item, if the user is trying to give or take a Mega Stone to or from the species that can Mega Evolve with it, or if the user is trying to give or take a Blue Orb, a Red Orb, a Griseous Orb, a Plate, a Drive, or a Memory to or from a Kyogre, a Groudon, a Giratina, an Arceus, a Genesect, or a Silvally, respectively. The target is immune to this move if it has the Sticky Hold Ability.",
                                "shortDesc": "User switches its held item with the target's.",
                                "id": "trick",
                                "isViable": True,
                                "name": "Trick",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "mystery": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Psychic",
                                "zMoveBoost": {
                                    "spe": 2
                                },
                                "contestType": "Clever"
                            },
                            "trickortreat": {
                                "num": 567,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Causes the Ghost type to be added to the target, effectively making it have two or three types. Fails if the target is already a Ghost type. If Forest's Curse adds a type to the target,it replaces the type added by this move and vice versa.",
                                "shortDesc": "Adds Ghost to the target's type(s).",
                                "id": "trickortreat",
                                "name": "Trick-or-Treat",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "mystery": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Ghost",
                                "zMoveBoost": {
                                    "atk": 1,
                                    "def": 1,
                                    "spa": 1,
                                    "spd": 1,
                                    "spe": 1
                                },
                                "contestType": "Cute"
                            },
                            "trickroom": {
                                "num": 433,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "For 5 turns, the Speed of every Pokemon is recalculated for the purposes of determining turn order. During the effect, each Pokemon's Speed is considered to be(10000 - its normal Speed), and if this value is greater than 8191, 8192 is subtracted from it.If this move is used during the effect, the effect ends. ",
                                "shortDesc": "Goes last. For 5 turns, turn order is reversed.",
                                "id": "trickroom",
                                "name": "Trick Room",
                                "pp": 5,
                                "priority": -7,
                                "flags": {
                                    "mirror": 1
                                },
                                "pseudoWeather": "trickroom",
                                "secondary": None,
                                "target": "all",
                                "type": "Psychic",
                                "zMoveBoost": {
                                    "accuracy": 1
                                },
                                "contestType": "Clever"
                            },
                            "triplekick": {
                                "num": 167,
                                "accuracy": 90,
                                "basePower": 10,
                                "category": "Physical",
                                "desc": "Hits three times. Power increases to 20 for the second hit and 30 for the third. This move checks for each hit, and the attack ends if the target avoids a hit.If one of the hits breaks the target 's substitute, it will take damage for the remaining hits. If the user has the Skill Link Ability, this move will always hit three times.",
                                "shortDesc": "Hits 3 times. Each hit can miss, but power rises.",
                                "id": "triplekick",
                                "name": "Triple Kick",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "multihit": 3,
                                "multiaccuracy": True,
                                "secondary": None,
                                "target": "normal",
                                "type": "Fighting",
                                "zMovePower": 120,
                                "contestType": "Cool"
                            },
                            "tropkick": {
                                "num": 688,
                                "accuracy": 100,
                                "basePower": 70,
                                "category": "Physical",
                                "desc": "Has a 100% chance to lower the target's Attack by 1 stage.",
                                "shortDesc": "100% chance to lower the target's Attack by 1.",
                                "id": "tropkick",
                                "name": "Trop Kick",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 100,
                                    "boosts": {
                                        "atk": -1
                                    },
                                },
                                "target": "normal",
                                "type": "Grass",
                                "zMovePower": 140,
                                "contestType": "Cute"
                            },
                            "trumpcard": {
                                "num": 376,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Special",
                                "desc": "The power of this move is based on the amount of PP remaining after normal PP reduction and the Pressure Ability resolve. 200 power for 0 PP, 80 power for 1 PP, 60 power for 2 PP, 50 power for 3 PP, and 40 power for 4 or more PP.",
                                "shortDesc": "More power the fewer PP this move has left.",
                                "id": "trumpcard",
                                "name": "Trump Card",
                                "pp": 5,
                                "noPPBoosts": True,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 160,
                                "contestType": "Cool"
                            },
                            "twineedle": {
                                "num": 41,
                                "accuracy": 100,
                                "basePower": 25,
                                "category": "Physical",
                                "desc": "Hits twice, with each hit having a 20% chance to poison the target. If the first hit breaks the target's substitute, it will take damage for the second hit.",
                                "shortDesc": "Hits 2 times. Each hit has 20% chance to poison.",
                                "id": "twineedle",
                                "name": "Twineedle",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "multihit": 2,
                                "secondary": {
                                    "chance": 20,
                                    "status": "psn",
                                },
                                "target": "normal",
                                "type": "Bug",
                                "zMovePower": 100,
                                "contestType": "Cool"
                            },
                            "twinkletackle": {
                                "num": 656,
                                "accuracy": True,
                                "basePower": 1,
                                "category": "Physical",
                                "shortDesc": "Power is equal to the base move's Z-Power.",
                                "id": "twinkletackle",
                                "isViable": True,
                                "name": "Twinkle Tackle",
                                "pp": 1,
                                "priority": 0,
                                "flags": {},
                                "isZ": "fairiumz",
                                "secondary": None,
                                "target": "normal",
                                "type": "Fairy",
                                "contestType": "Cool"
                            },
                            "twister": {
                                "num": 239,
                                "accuracy": 100,
                                "basePower": 40,
                                "category": "Special",
                                "desc": "Has a 20% chance to flinch the target. Power doubles if the target is using Bounce, Fly, or Sky Drop, or is under the effect of Sky Drop.",
                                "shortDesc": "20% chance to flinch the foe(s).",
                                "id": "twister",
                                "name": "Twister",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 20,
                                    "volatileStatus": "flinch"
                                },
                                "target": "allAdjacentFoes",
                                "type": "Dragon",
                                "zMovePower": 100,
                                "contestType": "Cool"
                            },
                            "uturn": {
                                "num": 369,
                                "accuracy": 100,
                                "basePower": 70,
                                "category": "Physical",
                                "desc": "If this move is successful and the user has not fainted, the user switches out even if it is trapped and is replaced immediately by a selected party member. The user does not switch out if there are no unfainted party members, or if the target switched out using an Eject Button or through the effect of the Emergency Exit or Wimp Out Abilities.",
                                "shortDesc": "User switches out after damaging the target.",
                                "id": "uturn",
                                "isViable": True,
                                "name": "U-turn",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "selfSwitch": True,
                                "secondary": None,
                                "target": "normal",
                                "type": "Bug",
                                "zMovePower": 140,
                                "contestType": "Cute"
                            },
                            "uproar": {
                                "num": 253,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Special",
                                "desc": "The user spends three turns locked into this move. This move targets an opponent at random on each turn. On the first of the three turns, all sleeping active Pokemon wake up. During the three turns, no active Pokemon can fall asleep by any means, and Pokemon switched in during the effect do not wake up. If the user is prevented from moving or the attack is not successful against the target during one of the turns, the effect ends.",
                                "shortDesc": "Lasts 3 turns. Active Pokemon cannot fall asleep.",
                                "id": "uproar",
                                "name": "Uproar",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "sound": 1,
                                    "authentic": 1
                                },
                                "self": {
                                    "volatileStatus": "uproar",
                                },
                                "secondary": None,
                                "target": "randomNormal",
                                "type": "Normal",
                                "zMovePower": 175,
                                "contestType": "Cute"
                            },
                            "vacuumwave": {
                                "num": 410,
                                "accuracy": 100,
                                "basePower": 40,
                                "category": "Special",
                                "desc": "No additional effect.",
                                "shortDesc": "Usually goes first.",
                                "id": "vacuumwave",
                                "name": "Vacuum Wave",
                                "pp": 30,
                                "priority": 1,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Fighting",
                                "zMovePower": 100,
                                "contestType": "Cool"
                            },
                            "vcreate": {
                                "num": 557,
                                "accuracy": 95,
                                "basePower": 180,
                                "category": "Physical",
                                "desc": "Lowers the user's Speed, Defense, and Special Defense by 1 stage.",
                                "shortDesc": "Lowers the user's Defense, Sp. Def, Speed by 1.",
                                "id": "vcreate",
                                "isViable": True,
                                "name": "V-create",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "self": {
                                    "boosts": {
                                        "spe": -1,
                                        "def": -1,
                                        "spd": -1
                                    },
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Fire",
                                "zMovePower": 220,
                                "contestType": "Cool"
                            },
                            "veeveevolley": {
                                "num": 741,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Physical",
                                "desc": "Power is equal to the greater of (user's Happiness * 2/5), rounded down, or 1.",
                                "shortDesc": "Max happiness: 102 power. Can't miss.",
                                "id": "veeveevolley",
                                "isNonstandard": "LGPE",
                                "isUnreleased": True,
                                "isViable": True,
                                "name": "Veevee Volley",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "contestType": "Cute"
                            },
                            "venomdrench": {
                                "num": 599,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Lowers the target's Attack, Special Attack, and Speed by 1 stage if the target is poisoned. Fails if the target is not poisoned.",
                                "shortDesc": "Lowers Atk/Sp. Atk/Speed of poisoned foes by 1.",
                                "id": "venomdrench",
                                "name": "Venom Drench",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "allAdjacentFoes",
                                "type": "Poison",
                                "zMoveBoost": {
                                    "def": 1
                                },
                                "contestType": "Clever"
                            },
                            "venoshock": {
                                "num": 474,
                                "accuracy": 100,
                                "basePower": 65,
                                "category": "Special",
                                "desc": "Power doubles if the target is poisoned.",
                                "shortDesc": "Power doubles if the target is poisoned.",
                                "id": "venoshock",
                                "name": "Venoshock",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Poison",
                                "zMovePower": 120,
                                "contestType": "Beautiful"
                            },
                            "vicegrip": {
                                "num": 11,
                                "accuracy": 100,
                                "basePower": 55,
                                "category": "Physical",
                                "shortDesc": "No additional effect.",
                                "id": "vicegrip",
                                "name": "Vice Grip",
                                "pp": 30,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 100,
                                "contestType": "Tough"
                            },
                            "vinewhip": {
                                "num": 22,
                                "accuracy": 100,
                                "basePower": 45,
                                "category": "Physical",
                                "shortDesc": "No additional effect.",
                                "id": "vinewhip",
                                "name": "Vine Whip",
                                "pp": 25,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Grass",
                                "zMovePower": 100,
                                "contestType": "Cool"
                            },
                            "vitalthrow": {
                                "num": 233,
                                "accuracy": True,
                                "basePower": 70,
                                "category": "Physical",
                                "desc": "This move does not check 'accuracy'",
                                "shortDesc": "This move does not check 'accuracy'.Goes last.",
                                "id": "vitalthrow",
                                "name": "Vital Throw",
                                "pp": 10,
                                "priority": -1,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Fighting",
                                "zMovePower": 140,
                                "contestType": "Cool"
                            },
                            "voltswitch": {
                                "num": 521,
                                "accuracy": 100,
                                "basePower": 70,
                                "category": "Special",
                                "desc": "If this move is successful and the user has not fainted, the user switches out even if it is trapped and is replaced immediately by a selected party member. The user does not switch out if there are no unfainted party members, or if the target switched out using an Eject Button or through the effect of the Emergency Exit or Wimp Out Abilities.",
                                "shortDesc": "User switches out after damaging the target.",
                                "id": "voltswitch",
                                "isViable": True,
                                "name": "Volt Switch",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "selfSwitch": True,
                                "secondary": None,
                                "target": "normal",
                                "type": "Electric",
                                "zMovePower": 140,
                                "contestType": "Cool"
                            },
                            "volttackle": {
                                "num": 344,
                                "accuracy": 100,
                                "basePower": 120,
                                "category": "Physical",
                                "desc": "Has a 10% chance to paralyze the target. If the target lost HP, the user takes recoil damage equal to 33% the HP lost by the target, rounded half up, but not less than 1 HP.",
                                "shortDesc": "Has 33% recoil. 10% chance to paralyze target.",
                                "id": "volttackle",
                                "isViable": True,
                                "name": "Volt Tackle",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "recoil": [
                                    33,
                                    100
                                ],
                                "secondary": {
                                    "chance": 10,
                                    "status": "par",
                                },
                                "target": "normal",
                                "type": "Electric",
                                "zMovePower": 190,
                                "contestType": "Cool"
                            },
                            "wakeupslap": {
                                "num": 358,
                                "accuracy": 100,
                                "basePower": 70,
                                "category": "Physical",
                                "desc": "Power doubles if the target is asleep. If the user has not fainted, the target wakes up.",
                                "shortDesc": "Power doubles if target is asleep, and wakes it.",
                                "id": "wakeupslap",
                                "name": "Wake-Up Slap",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Fighting",
                                "zMovePower": 140,
                                "contestType": "Tough"
                            },
                            "waterfall": {
                                "num": 127,
                                "accuracy": 100,
                                "basePower": 80,
                                "category": "Physical",
                                "desc": "Has a 20% chance to flinch the target.",
                                "shortDesc": "20% chance to flinch the target.",
                                "id": "waterfall",
                                "isViable": True,
                                "name": "Waterfall",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": {
                                    "chance": 20,
                                    "volatileStatus": "flinch"
                                },
                                "target": "normal",
                                "type": "Water",
                                "zMovePower": 160,
                                "contestType": "Tough"
                            },
                            "watergun": {
                                "num": 55,
                                "accuracy": 100,
                                "basePower": 40,
                                "category": "Special",
                                "shortDesc": "No additional effect.",
                                "id": "watergun",
                                "name": "Water Gun",
                                "pp": 25,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Water",
                                "zMovePower": 100,
                                "contestType": "Cute"
                            },
                            "waterpledge": {
                                "num": 518,
                                "accuracy": 100,
                                "basePower": 80,
                                "category": "Special",
                                "desc": "If one of the user's allies chose to use Fire Pledge or Grass Pledge this turn and has not moved yet, it takes its turn immediately after the user and the user's move does nothing. If combined with Fire Pledge, the ally uses Water Pledge with 150 power and a rainbow appears on the user's side for 4 turns, which doubles secondary effect chances but does not stack with the Serene Grace Ability. If combined with Grass Pledge, the ally uses Grass Pledge with 150 power and a swamp appears on the target's side for 4 turns, which quarters the Speed of each Pokemon on that side. When used as a combined move, this move gains STAB no matter what the user's type is. This move does not consume the user's Water Gem, and cannot be redirected by the Storm drain Ability.",
                                "shortDesc": "Use with Grass or Fire Pledge for added effect.",
                                "id": "waterpledge",
                                "name": "Water Pledge",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1,
                                    "nonsky": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Water",
                                "zMovePower": 160,
                                "contestType": "Beautiful"
                            },
                            "waterpulse": {
                                "num": 352,
                                "accuracy": 100,
                                "basePower": 60,
                                "category": "Special",
                                "desc": "Has a 20% chance to confuse the target.",
                                "shortDesc": "20% chance to confuse the target.",
                                "id": "waterpulse",
                                "name": "Water Pulse",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "pulse": 1,
                                    "mirror": 1,
                                    "distance": 1
                                },
                                "secondary": {
                                    "chance": 20,
                                    "volatileStatus": "confusion",
                                },
                                "target": "any",
                                "type": "Water",
                                "zMovePower": 120,
                                "contestType": "Beautiful"
                            },
                            "watershuriken": {
                                "num": 594,
                                "accuracy": 100,
                                "basePower": 15,
                                "category": "Special",
                                "desc": "Hits two to five times. Has a 1/3 chance to hit two or three times, and a 1/6 chance to hit four or five times. If one of the hits breaks the target's substitute, it will take damage for the remaining hits. If the user has the Skill Link Ability, this move will always hit five times. If the user is an Ash-Greninja with the Battle Bond Ability, this move has a power of 20 and always hits three times.",
                                "shortDesc": "Usually goes first. Hits 2-5 times in one turn.",
                                "id": "watershuriken",
                                "isViable": True,
                                "name": "Water Shuriken",
                                "pp": 20,
                                "priority": 1,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "multihit": [
                                    2,
                                    5
                                ],
                                "secondary": None,
                                "target": "normal",
                                "type": "Water",
                                "zMovePower": 100,
                                "contestType": "Cool"
                            },
                            "watersport": {
                                "num": 346,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "For 5 turns, all Fire-type attacks used by any active Pokemon have their power multiplied by 0.33. Fails if this effect is already active.",
                                "shortDesc": "For 5 turns, Fire-type attacks have 1/3 power.",
                                "id": "watersport",
                                "name": "Water Sport",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "nonsky": 1
                                },
                                "pseudoWeather": "watersport",
                                "secondary": None,
                                "target": "all",
                                "type": "Water",
                                "zMoveBoost": {
                                    "spd": 1
                                },
                                "contestType": "Cute"
                            },
                            "waterspout": {
                                "num": 323,
                                "accuracy": 100,
                                "basePower": 150,
                                "category": "Special",
                                "desc": "Power is equal to (user's current HP * 150 / user's maximum HP), rounded down, but not less than 1.",
                                "shortDesc": "Less power as user's HP decreases. Hits foe(s).",
                                "id": "waterspout",
                                "isViable": True,
                                "name": "Water Spout",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "allAdjacentFoes",
                                "type": "Water",
                                "zMovePower": 200,
                                "contestType": "Beautiful"
                            },
                            "weatherball": {
                                "num": 311,
                                "accuracy": 100,
                                "basePower": 50,
                                "category": "Special",
                                "desc": "Power doubles if a weather condition other than Delta Stream is active, and this move's type changes to match. Ice type during Hail, Water type during Primordial Sea or Rain Dance, Rock type during Sandstorm, and Fire type during Desolate Land or Sunny Day.",
                                "shortDesc": "Power doubles and type varies in each weather.",
                                "id": "weatherball",
                                "name": "Weather Ball",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "bullet": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 160,
                                "contestType": "Beautiful"
                            },
                            "whirlpool": {
                                "num": 250,
                                "accuracy": 85,
                                "basePower": 35,
                                "category": "Special",
                                "desc": "Prevents the target from switching for four or five turns (seven turns if the user is holding Grip Claw). Causes damage to the target equal to 1/8 of its maximum HP (1/6 if the user is holding Binding Band), rounded down, at the end of each turn during effect. The target can still switch out if it is holding Shed Shell or uses Baton Pass, Parting Shot, U-turn, or Volt Switch. The effect ends if either the user or the target leaves the field, or if the target uses Rapid Spin or Substitute successfully. This effect is not stackable or reset by using this or another binding move.",
                                "shortDesc": "Traps and damages the target for 4-5 turns.",
                                "id": "whirlpool",
                                "name": "Whirlpool",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "volatileStatus": "partiallytrapped",
                                "secondary": None,
                                "target": "normal",
                                "type": "Water",
                                "zMovePower": 100,
                                "contestType": "Beautiful"
                            },
                            "whirlwind": {
                                "num": 18,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The target is forced to switch out and be replaced with a random unfainted ally. Fails if the target is the last unfainted Pokemon in its party, or if the target used Ingrain previously or has the Suction Cups Ability.",
                                "shortDesc": "Forces the target to switch to a random ally.",
                                "id": "whirlwind",
                                "isViable": True,
                                "name": "Whirlwind",
                                "pp": 20,
                                "priority": -6,
                                "flags": {
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "authentic": 1,
                                    "mystery": 1
                                },
                                "forceSwitch": True,
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "spd": 1
                                },
                                "contestType": "Clever"
                            },
                            "wideguard": {
                                "num": 469,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "The user and its party members are protected from moves made by other Pokemon, including allies, during this turn that target all adjacent foes or all adjacent Pokemon. This move modifies the same 1/X chance of being successful used by other protection moves, where X starts at 1 and triples each time this move is successfully used, but does not use the chance to check for failure. X resets to 1 if this move fails, if the user's last move used is not Baneful Bunker, Detect, Endure, King's Shield, Protect, Quick Guard, Spiky Shield, or Wide Guard, or if it was one of those moves and the user 's protection was broken. Fails if the user moves last this turn or if this move is already in effect for the user's side.",
                                "shortDesc": "Protects allies from multi-target moves this turn.",
                                "id": "wideguard",
                                "name": "Wide Guard",
                                "pp": 10,
                                "priority": 3,
                                "flags": {
                                    "snatch": 1
                                },
                                "sideCondition": "wideguard",
                                "secondary": None,
                                "target": "allySide",
                                "type": "Rock",
                                "zMoveBoost": {
                                    "def": 1
                                },
                                "contestType": "Tough"
                            },
                            "wildcharge": {
                                "num": 528,
                                "accuracy": 100,
                                "basePower": 90,
                                "category": "Physical",
                                "desc": "If the target lost HP, the user takes recoil damage equal to 1/4 the HP lost by the target, rounded half up, but not less than 1 HP.",
                                "shortDesc": "Has 1/4 recoil.",
                                "id": "wildcharge",
                                "isViable": True,
                                "name": "Wild Charge",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "recoil": [
                                    1,
                                    4
                                ],
                                "secondary": None,
                                "target": "normal",
                                "type": "Electric",
                                "zMovePower": 175,
                                "contestType": "Tough"
                            },
                            "willowisp": {
                                "num": 261,
                                "accuracy": 85,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Burns the target.",
                                "shortDesc": "Burns the target.",
                                "id": "willowisp",
                                "isViable": True,
                                "name": "Will-O-Wisp",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "status": "brn",
                                "secondary": None,
                                "target": "normal",
                                "type": "Fire",
                                "zMoveBoost": {
                                    "atk": 1
                                },
                                "contestType": "Beautiful"
                            },
                            "wingattack": {
                                "num": 17,
                                "accuracy": 100,
                                "basePower": 60,
                                "category": "Physical",
                                "shortDesc": "No additional effect.",
                                "id": "wingattack",
                                "name": "Wing Attack",
                                "pp": 35,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1,
                                    "distance": 1
                                },
                                "secondary": None,
                                "target": "any",
                                "type": "Flying",
                                "zMovePower": 120,
                                "contestType": "Cool"
                            },
                            "wish": {
                                "num": 273,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "At the end of the next turn, the Pokemon at the user's position has 1/2 of the user's maximum HP restored to it, rounded half up. Fails if this move is already in effect for the user's position.",
                                "shortDesc": "Next turn, 50% of the user's max HP is restored.",
                                "id": "wish",
                                "isViable": True,
                                "name": "Wish",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1,
                                    "heal": 1
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "spd": 1
                                },
                                "contestType": "Cute"
                            },
                            "withdraw": {
                                "num": 110,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Raises the user's Defense by 1 stage.",
                                "shortDesc": "Raises the user's Defense by 1.",
                                "id": "withdraw",
                                "name": "Withdraw",
                                "pp": 40,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1
                                },
                                "boosts": {
                                    "def": 1,
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Water",
                                "zMoveBoost": {
                                    "def": 1
                                },
                                "contestType": "Cute"
                            },
                            "wonderroom": {
                                "num": 472,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "For 5 turns, all active Pokemon have their Defense and Special Defense stats swapped. Stat stage changes are unaffected. If this move is used during the effect, the effect ends.",
                                "shortDesc": "For 5 turns, all Defense and Sp. Def stats switch.",
                                "id": "wonderroom",
                                "name": "Wonder Room",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "all",
                                "type": "Psychic",
                                "zMoveBoost": {
                                    "spd": 1
                                },
                                "contestType": "Clever"
                            },
                            "woodhammer": {
                                "num": 452,
                                "accuracy": 100,
                                "basePower": 120,
                                "category": "Physical",
                                "desc": "If the target lost HP, the user takes recoil damage equal to 33% the HP lost by the target, rounded half up, but not less than 1 HP.",
                                "shortDesc": "Has 33% recoil.",
                                "id": "woodhammer",
                                "isViable": True,
                                "name": "Wood Hammer",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "recoil": [
                                    33,
                                    100
                                ],
                                "secondary": None,
                                "target": "normal",
                                "type": "Grass",
                                "zMovePower": 190,
                                "contestType": "Tough"
                            },
                            "workup": {
                                "num": 526,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Raises the user's Attack and Special Attack by 1 stage.",
                                "shortDesc": "Raises the user's Attack and Sp. Atk by 1.",
                                "id": "workup",
                                "name": "Work Up",
                                "pp": 30,
                                "priority": 0,
                                "flags": {
                                    "snatch": 1
                                },
                                "boosts": {
                                    "atk": 1,
                                    "spa": 1,
                                },
                                "secondary": None,
                                "target": "self",
                                "type": "Normal",
                                "zMoveBoost": {
                                    "atk": 1
                                },
                                "contestType": "Tough"
                            },
                            "worryseed": {
                                "num": 388,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Causes the target's Ability to become Insomnia. Fails if the target's Ability is Battle Bond, Comatose, Disguise, Insomnia, Multitype, Power Construct, RKS System, Schooling, Shields Down, Stance Change, Truant, or Zen Mode.",
                                "shortDesc": "The target's Ability becomes Insomnia.",
                                "id": "worryseed",
                                "name": "Worry Seed",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1,
                                    "mystery": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Grass",
                                "zMoveBoost": {
                                    "spe": 1
                                },
                                "contestType": "Clever"
                            },
                            "wrap": {
                                "num": 35,
                                "accuracy": 90,
                                "basePower": 15,
                                "category": "Physical",
                                "desc": "Prevents the target from switching for four or five turns (seven turns if the user is holding Grip Claw). Causes damage to the target equal to 1/8 of its maximum HP (1/6 if the user is holding Binding Band), rounded down, at the end of each turn during effect. The target can still switch out if it is holding Shed Shell or uses Baton Pass, Parting Shot, U-turn, or Volt Switch. The effect ends if either the user or the target leaves the field, or if the target uses Rapid Spin or Substitute successfully. This effect is not stackable or reset by using this or another binding move.",
                                "shortDesc": "Traps and damages the target for 4-5 turns.",
                                "id": "wrap",
                                "name": "Wrap",
                                "pp": 20,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "volatileStatus": "partiallytrapped",
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 100,
                                "contestType": "Tough"
                            },
                            "wringout": {
                                "num": 378,
                                "accuracy": 100,
                                "basePower": 0,
                                "category": "Special",
                                "desc": "Power is equal to 120 * (target's current HP / target's maximum HP), rounded half down, but not less than 1.",
                                "shortDesc": "More power the more HP the target has left.",
                                "id": "wringout",
                                "name": "Wring Out",
                                "pp": 5,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Normal",
                                "zMovePower": 190,
                                "contestType": "Tough"
                            },
                            "xscissor": {
                                "num": 404,
                                "accuracy": 100,
                                "basePower": 80,
                                "category": "Physical",
                                "shortDesc": "No additional effect.",
                                "id": "xscissor",
                                "isViable": True,
                                "name": "X-Scissor",
                                "pp": 15,
                                "priority": 0,
                                "flags": {
                                    "contact": 1,
                                    "protect": 1,
                                    "mirror": 1
                                },
                                "secondary": None,
                                "target": "normal",
                                "type": "Bug",
                                "zMovePower": 160,
                                "contestType": "Cool"
                            },
                            "yawn": {
                                "num": 281,
                                "accuracy": True,
                                "basePower": 0,
                                "category": "Status",
                                "desc": "Causes the target to fall asleep at the end of the next turn. Fails when used if the target cannot fall asleep or if it already has a major status condition. At the end of the next turn, if the target is still active, does not have a major status condition, and can fall asleep, it falls asleep. If the target becomes affected, this effect cannot be prevented by Safeguard or a substitute, or by falling asleep and waking up during the effect.",
                                "shortDesc": "Puts the target to sleep after 1 turn.",
                                "id": "yawn",
                                "name": "Yawn",
                                "pp": 10,
                                "priority": 0,
                                "flags": {
                                    "protect": 1,
                                    "reflectable": 1,
                                    "mirror": 1
                                },
                                "volatileStatus": "yawn",
                            },
                            "secondary": None,
                            "target": "normal",
                            "type": "Normal",
                            "zMoveBoost": {
                                "spe": 1
                            },
                            "contestType": "Cute"
                        },
                        "zapcannon": {
                            "num": 192,
                            "accuracy": 50,
                            "basePower": 120,
                            "category": "Special",
                            "desc": "Has a 100% chance to paralyze the target.",
                            "shortDesc": "100% chance to paralyze the target.",
                            "id": "zapcannon",
                            "name": "Zap Cannon",
                            "pp": 5,
                            "priority": 0,
                            "flags": {
                                "bullet": 1,
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": {
                                "chance": 100,
                                "status": "par",
                            },
                            "target": "normal",
                            "type": "Electric",
                            "zMovePower": 190,
                            "contestType": "Cool"
                        },
                        "zenheadbutt": {
                            "num": 428,
                            "accuracy": 90,
                            "basePower": 80,
                            "category": "Physical",
                            "desc": "Has a 20% chance to flinch the target.",
                            "shortDesc": "20% chance to flinch the target.",
                            "id": "zenheadbutt",
                            "isViable": True,
                            "name": "Zen Headbutt",
                            "pp": 15,
                            "priority": 0,
                            "flags": {
                                "contact": 1,
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": {
                                "chance": 20,
                                "volatileStatus": "flinch"
                            },
                            "target": "normal",
                            "type": "Psychic",
                            "zMovePower": 160,
                            "contestType": "Clever"
                        },
                        "zingzap": {
                            "num": 716,
                            "accuracy": 100,
                            "basePower": 80,
                            "category": "Physical",
                            "desc": "Has a 30% chance to flinch the target.",
                            "shortDesc": "30% chance to flinch the target.",
                            "id": "zingzap",
                            "isViable": True,
                            "name": "Zing Zap",
                            "pp": 10,
                            "priority": 0,
                            "flags": {
                                "contact": 1,
                                "protect": 1,
                                "mirror": 1
                            },
                            "secondary": {
                                "chance": 30,
                                "volatileStatus": "flinch"
                            },
                            "target": "normal",
                            "type": "Electric",
                            "zMovePower": 160,
                            "contestType": "Cool"
                        },
                        "zippyzap": {
                            "num": 729,
                            "accuracy": 100,
                            "basePower": 50,
                            "category": "Physical",
                            "desc": "Will always result in a critical hit.",
                            "shortDesc": "Nearly always goes first. Always crits.",
                            "id": "zippyzap",
                            "isNonstandard": "LGPE",
                            "isUnreleased": True,
                            "isViable": True,
                            "name": "Zippy Zap",
                            "pp": 15,
                            "priority": 2,
                            "flags": {
                                "contact": 1,
                                "protect": 1
                            },
                            "willCrit": True,
                            "secondary": None,
                            "target": "normal",
                            "type": "Electric",
                            "contestType": "Cool"
                        },
                    }
    return moves[move]
print(get_move('zippyzap'))
