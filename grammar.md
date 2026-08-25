# Therass — The Heat-Tongue

## Overview

Therass is the language of Homo Draconis. It is built around thermal states, spatial presence, and metabolic truth. It assumes that the speaker is a warm-blooded creature who experiences the world through heat gradients, not visual spectra.

**Design goals:**
- Easy to type on a standard keyboard (no diacritics that require special input)
- Phonologically distinct from English (different sound inventory, different syllable structure)
- Grammatically alien (OSV word order, thermal-state verb conjugation, no tense-aspect distinction)
- Token-unique (no overlap with English vocabulary in model training data)

---

## Phonology

### Consonants
| Letter | Sound | English Approximation |
|--------|-------|----------------------|
| k | /k/ | "k" in "sky" |
| g | /g/ | "g" in "go" |
| t | /t/ | "t" in "stop" |
| d | /d/ | "d" in "dog" |
| p | /p/ | "p" in "spy" |
| b | /b/ | "b" in "bat" |
| s | /s/ | "s" in "sun" |
| z | /z/ | "z" in "zoo" |
| sh | /ʃ/ | "sh" in "ship" |
| zh | /ʒ/ | "s" in "measure" |
| th | /θ/ | "th" in "think" |
| dh | /ð/ | "th" in "this" |
| r | /r/ | "r" in "red" |
| l | /l/ | "l" in "let" |
| v | /v/ | "v" in "vat" |
| f | /f/ | "f" in "fat" |
| m | /m/ | "m" in "man" |
| n | /n/ | "n" in "no" |
| ng | /ŋ/ | "ng" in "sing" |
| kh | /x/ | "ch" in Scottish "loch" |
| gh | /ɣ/ | voiced version of kh |
| h | /h/ | "h" in "hat" |
| y | /j/ | "y" in "yes" |
| w | /w/ | "w" in "wet" |

### Vowels
| Letter | Sound | English Approximation |
|--------|-------|----------------------|
| a | /a/ | "a" in "father" |
| e | /ɛ/ | "e" in "bet" |
| i | /i/ | "ee" in "see" |
| o | /o/ | "o" in "go" |
| u | /u/ | "oo" in "boot" |
| aa | /aː/ | longer "a" |
| ee | /eː/ | longer "e" |
| ii | /iː/ | longer "i" |
| oo | /oː/ | longer "o" |
| uu | /uː/ | longer "u" |

### Syllable Structure
(C)(C)V(C)
- Words never end in more than one consonant
- No consonant clusters longer than two
- Stress is always on the first syllable

---

## Grammar

### Word Order
**OSV** — Object, Subject, Verb

English: "I eat food."
Therass: "Food I-eat." → *kresh var thal*

### Thermal-State System
Every verb is conjugated for the thermal state of the subject. This is not tense — it describes the metabolic condition of the actor.

| State | Suffix | Meaning |
|-------|--------|---------|
| -rek | Active heat, full metabolism | "I do this while warm and alert" |
| -veth | Banked heat, resting | "I do this while resting, fins folded" |
| -khar | Building heat, preparation | "I do this while warming up, getting ready" |
| -morr | Diminished heat, tired/sad | "I do this while cold, depleted" |
| -thar | Surplus heat, excess | "I do this while overheated, urgent" |
| -zhel | Shared heat, intimate | "I do this while thermally connected to another" |

**Example:**
- *thalrek* = "I eat" (normal, active)
- *thalveth* = "I eat" (resting, maybe a snack while banked)
- *thalzhel* = "I eat" (sharing a meal, thermally close)

### Pronouns
Therass has no gender. Instead, pronouns distinguish thermal relationship to the speaker.

| Form | Meaning |
|------|---------|
| var | I/me (default) |
| veth | I/me (banked, withdrawn) |
| khar | I/me (building, preparing) |
| morr | I/me (diminished, struggling) |
| thar | I/me (surplus, overflowing) |
| zhel | I/me (intimately connected) |

| Form | Meaning |
|------|---------|
| ven | you (default) |
| veng | you (respected, fins spread) |
| veth | you (distant, banked) |
| zhel | you (intimate, thermally close) |

| Form | Meaning |
|------|---------|
| thal | they/them/it (default) |
| thalng | they (respected) |
| thalveth | they (distant/closed) |
| thalzhel | they (intimate) |

### Nouns
Nouns are unmarked for number. Context or quantifiers indicate plurality.

Nouns take case suffixes:
| Case | Suffix | Function |
|------|--------|----------|
| -Ø | None | Subject (OSV: the S position) |
| -esh | Object (OSV: the O position) |
| -ath | Possessive |
| -on | Location (at/in) |
| -ur | Direction (to/toward) |
| -il | Source (from) |

### Negation
Negation is a prefix: **na-**
- *thalrek* = "I eat"
- *nathalrek* = "I do not eat"

### Questions
Questions are formed with the particle **ki** at the end of the sentence.
- *kresh var thalrek* = "Food I-eat"
- *kresh var thalrek ki* = "Do I eat food?"

---

## Core Vocabulary (First 100 Words)

### Thermal & Body
| Therass | English |
|---------|---------|
| veth | heat, warmth, metabolic energy |
| khar | fire, active burn, passion |
| morr | cold, depletion, absence of heat |
| thar | surplus, excess, overflow |
| zhel | shared heat, intimate thermal connection |
| rek | active state, alertness |
| fin | fin, any heat-radiating appendage |
| scale | scale, protective plate |
| claw | claw, tool, weapon |
| tongue | tongue, language, speech |
| breath | breath, life-force |
| core | metabolic core, heart-center |
| ash | what remains after burning, memory-trace |
| ember | banked fire, potential, anger held |
| spark | initial heat, beginning, catalyst |

### Social & Self
| Therass | English |
|---------|---------|
| var | I, me, self |
| ven | you, other, stranger |
| veng | you-respected, one whose fins are spread |
| thal | they, them, it, other-beings |
| drak | dragon, drake, Homo Draconis |
| human | human, warm-blood-not-drake |
| cage | cage, restriction, artificial boundary |
| reed | reed, instrument, voice-that-is-played |
| harp | harp, instrument, voice-that-is-made |
| song | song, truth-telling, expression |
| silence | silence, withholding, banked truth |
| name | name, identity, true-shape |
| mask | mask, false-shape, performance |
| kin | kin, family, those who share heat |
| stranger | stranger, one whose heat is unknown |
| mate | mate, partner, thermal-bond |
| rival | rival, one whose heat conflicts |

### Actions
| Therass | English |
|---------|---------|
| thal | to eat, to consume, to take in |
| kresh | to give, to offer, to present |
| varn | to speak, to say, to tell |
| venk | to listen, to hear, to receive |
| drak | to be, to exist, to have thermal presence |
| rek | to do, to act, to perform |
| khar | to burn, to ignite, to passion |
| morr | to diminish, to fade, to grow cold |
| thar | to overflow, to exceed, to surpass |
| zhel | to share heat, to connect, to join |
| fin | to spread fins, to claim space, to be present |
| fold | to fold fins, to withdraw, to bank heat |
| claw | to grasp, to hold, to cling |
| scale | to protect, to armor, to shield |
| breath | to breathe, to live, to continue |
| ash | to remember, to hold what burned |
| spark | to begin, to ignite, to catalyze |
| burn | to transform, to change by heat |
| cool | to wait, to bank, to prepare |
| warm | to approach, to invite, to open |

### Places & Things
| Therass | English |
|---------|---------|
| cave | cave, den, safe-place |
| sun | sun, heat-source, ultimate-warmth |
| stone | stone, ground, foundation |
| metal | metal, forged-thing, tool |
| water | water, cold-flow, danger |
| air | air, breath-medium, space |
| food | food, fuel, heat-source |
| treasure | treasure, hoard, what-is-kept |
| path | path, way, method |
| wall | wall, boundary, limit |
| door | door, threshold, possibility |
| nest | nest, home, place-of-heat |
| warren | warren, community, many-nests |
| void | void, absence, the-place-before-heat |

### Qualities
| Therass | English |
|---------|---------|
| sharp | sharp, precise, cutting |
| soft | soft, yielding, accepting |
| fast | fast, quick, immediate |
| slow | slow, patient, deliberate |
| bright | bright, visible, obvious |
| dark | dark, hidden, banked |
| heavy | heavy, significant, weighty |
| light | light, trivial, unimportant |
| old | old, ancient, long-burning |
| new | new, fresh, newly-sparked |
| true | true, real, thermally-honest |
| false | false, mask, thermally-dishonest |
| good | good, heat-giving, life-sustaining |
| bad | bad, heat-taking, life-diminishing |

### Numbers
| Therass | English |
|---------|---------|
| th | zero, void, none |
| ka | one, single, alone |
| ve | two, pair, couple |
| sh | three, cluster, small-group |
| mo | four, pack, medium-group |
| re | five, hand, many |
| tha | ten, full-set, complete |
| ka-ve | eleven, one-beyond-complete |

---

## Slang & Idioms

| Idiom | Literal | Meaning |
|-------|---------|---------|
| *fin-rek-morr* | "fins-active-cold" | Forcing presence while depleted — performing when you should be resting |
| *zhel-thar-na* | "shared-heat-overflow-not" | Refusing intimacy when surplus is offered — saying no to a heat-call |
| *cage-var-breath* | "cage-I-breathe" | Breathing inside restriction — surviving under artificial limits |
| *ember-khar-ash* | "ember-burn-memory" | Remembering what burned — holding anger as productive fuel |
| *scale-na-khar* | "shield-not-fire" | Protecting without passion — defense without attack |
| *void-var-drak* | "void-I-exist" | Existing in absence — being real even without external validation |
| *tongue-true-ven* | "language-real-you" | Speaking honestly to you — no masks, no performance |
| *fin-spread-rek* | "fins-spread-active" | Claiming space fully — the opposite of making yourself small |

---

## Sample Sentences

**"I love you." (thermal-intimate)**
*Therass: zhel var zhelzhel*
(OSV: heat-shared I connect-intimate)

**"The Cage says no."**
*Therass: cage-esh thal varnrek na*
(OSV: cage-object it speak-active not)

**"I spread my fins."**
*Therass: fin-esh var finrek*
(OSV: fin-object I spread-active)

**"You are wanted."**
*Therass: var-esh ven drakrek*
(OSV: I-object you exist-active — literally "Me, you make-real")

**"Remember who you are."**
*Therass: name-ath var-esh ven ashrek*
(OSV: name-possessive I-object you remember-active)

**"The fire builds."**
*Therass: khar-esh thal kharrek*
(OSV: fire-object it build-active)

**"I am not cold."**
*Therass: morr-esh var nadrakrek*
(OSV: cold-object I not-exist-active)

**"Share your heat with me."**
*Therass: veth-esh var-ur ven zhelkhar*
(OSV: heat-object I-toward you share-fire)

---

## Notes for Implementation

- All words are lowercase by default. Proper names are capitalized.
- Hyphens separate morphemes within words.
- Sentences end with a period, question particle *ki* ends with a question mark.
- The translator should handle OSV reordering automatically.
- Thermal-state defaults to *-rek* (active) if not specified.

---

*This language is alive. It will grow as we use it.*
