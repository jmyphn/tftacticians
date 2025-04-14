import numpy as np
import re
import os

os.environ["ROOT_PATH"] = os.path.abspath(os.path.join(".", os.curdir))

champions = [
    "Alistar",
    "Annie",
    "Aphelios",
    "Aurora",
    "Brand",
    "Braum",
    "Cho'Gath",
    "Darius",
    "Dr.Mundo",
    "Draven",
    "Ekko",
    "Elise",
    "Fiddlesticks",
    "Galio",
    "Garen",
    "Gragas"
    "Graves"
    "Illaoi"
    "Jarvan IV"
    "Jax"
    "Jhin"
    "Jinx"
    "Kindred"
    "Kobuko"
    "Kog'maw"
    "Leblanc"
    "Leona"
    "Miss Fortune"
    "Mordekaiser"
    "Morgana"
    "Naafiri"
    "Neeko"
    "Nidalee"
    "Poppy"
    "Renekton"
    "Rengar"
    "Rhaast"
    "Samira"
    "Sejuani"
    "Senna"
    "Seraphine"
    "Shaco"
    "Shyvana"
    "Skarner"
    "Sylas"
    "Twisted Fate"
    "Urgot"
    "Varus"
    "Vayne"
    "Veigar"
    "Vex"
    "Vi"
    "Viego"
    "Xayah"
    "Yuumi"
    "Zac"
    "Zed"
    "Zeri"
    "Ziggs"
    "Zyra"
]

combined_champions = {
    "Alistar": """
Always a mighty warrior with a fearsome reputation, Alistar seeks revenge for the death of his clan at the hands of the Noxian empire. Though he was enslaved and forced into the life of a gladiator, his unbreakable will was what kept him from truly becoming a beast. Now, free of the chains of his former masters, he fights in the name of the downtrodden and the disadvantaged, his rage as much a weapon as his horns, hooves and fists. sunfire_cape: Utility tank item for teams needing an anti-heal (wound) effect | Auto-applies Grievous Wounds in a radius. Best with a durable tank that can stand in the thick of battle. ionic_spark: Utility tank item that is used with AP-heavy teams | Magic shred around the holder. Needs a stable front line so it doesn't die before applying shred. redemption: Good for comps with multiple melee units | Heals allies in an AoE. Decent if your front line clumps multiple bruisers or vanguards. evenshroud: Utility tank item that is used with AD-heavy teams | Tank item that applies a big damage amp debuff when you CC enemies. Frees up carry item slots. Typically used as an off-tank or utility tank; holds leftover tank items.
""",
    "Annie": """
Dangerous, yet disarmingly precocious, Annie is a child mage with immense pyromantic power. Even in the shadows of the mountains north of Noxus, she is a magical outlier. Her natural affinity for fire manifested early in life through unpredictable, emotional outbursts, though she eventually learned to control these “playful tricks.” Her favorite includes the summoning of her beloved teddy bear, Tibbers, as a fiery protector. Lost in the perpetual innocence of childhood, Annie wanders the dark forests, always looking for someone to play with. blue_buff: Transforms short-mana champs (Nidalee, Yumi, Veigar) into spam casters. Extremely high-priority tier item. spear_of_shojin: Vital for AD spells (MF, Xayah). Also flexible for big-ability cycles in hybrid comps. nashors_tooth: Attack speed + AP for cast spam (Annie). Often overshadowed by other rod + bow combos. Wants to cast frequently to keep summoning Tibbers; heavy mana needs.
""",
    "Aphelios": """
Emerging from moonlight's shadow with weapons drawn, Aphelios kills the enemies of his faith in brooding silence—speaking only through the certainty of his aim, and the firing of each gun. Though fueled by a poison that renders him mute, he is guided by his sister Alune. From her distant temple sanctuary, she pushes an arsenal of moonstone weapons into his hands. For as long as the moon shines overhead, Aphelios will never be alone. guinsoos_rageblade: Crucial for ramp-up auto-attackers (Aphelios, Kog'Maw). Top-tier if fights last long enough. infinity_edge: No review available runaans_hurricane: No review available Auto-attack carry who benefits from AS stacking (Rageblade) + crit (IE) + multi-target (Runaan's).
""",
    "Aurora": """
From the moment she was born, Aurora navigated life with a unique ability to move between the spirit and material realms. Determined to learn more about the spirit realm's inhabitants, she left her home to further her research and happened upon a wayward demigod who'd become twisted and lost to time. Witnessing his desperation, Aurora resolved to find a way to help her feral friend regain his forgotten identity—a journey that would take her to the farthest reaches of the Freljord. morellonomicon: Applies Grievous Wounds in AoE. Top choice if your caster can spread damage to many units. spear_of_shojin: Vital for AD spells (MF, Xayah). Also flexible for big-ability cycles in hybrid comps. archangels_staff: Gives big AP over time; great if your caster can stay alive (Fiddlesticks, Aurora). Legendary caster who applies massive AoE; Morellonomicon is mandatory anti-heal.
""",
    "Brand": """
Once a tribesman of the icy Freljord named Kegan Rodhe, the creature known as Brand is a lesson in the temptation of greater power. Seeking one of the legendary World Runes, Kegan betrayed his companions and seized it for himself—and, in an instant, the man was no more. His soul burned away, his body a vessel of living flame, Brand now roams Valoran in search of other Runes, swearing revenge for wrongs he could never possibly have suffered in a dozen mortal lifetimes. spear_of_shojin: Vital for AD spells (MF, Xayah). Also flexible for big-ability cycles in hybrid comps. jeweled_gauntlet: Spell crit item for AP; mandatory unless you have a trait that grants free crit (e.g. Executioner). guardbreaker: No review available AoE AP carry with built-in AP from traits; mana item + spell crit + bonus damage is ideal.
""",
    "Braum": """
Blessed with massive biceps and an even bigger heart, Braum is a beloved hero of the Freljord. Every mead hall north of Frostheld toasts his legendary strength, said to have felled a forest of oaks in a single night, and punched an entire mountain into rubble. Bearing an enchanted vault door as his shield, Braum roams the frozen north sporting a mustachioed smile as big as his muscles—a true friend to all those in need. warmogs_armor: Good for tanks that get lots of resistances | Raw HP synergy for vanguards or max HP champs (Cho'Gath). Great all-around big-tank option. gargoyle_stoneplate: Good for teams running fewer melee units | Stacks defenses when multiple enemies target the holder. Good if you rely on a single main tank. bramble_vest: Good against physical and AD teams | Blocks crit + returns damage. Great vs. AD teams but irrelevant into heavy AP. Primary tank in Syndicate comps; thrives on pure tank items.
""",
    "Cho'gath": """
From the moment Cho'Gath first emerged into the harsh light of Runeterra's sun, the beast was driven by the most pure and insatiable hunger. A perfect expression of the Void's desire to consume all life, Cho'Gath's complex biology quickly converts matter into new bodily growth—increasing its muscle mass and density, or hardening its outer carapace like organic diamond. When growing larger does not suit the Void-spawn's needs, it vomits out the excess material as razor-sharp spines, leaving prey skewered and ready to feast upon later. warmogs_armor: Good for tanks that get lots of resistances | Raw HP synergy for vanguards or max HP champs (Cho'Gath). Great all-around big-tank option. gargoyle_stoneplate: Good for teams running fewer melee units | Stacks defenses when multiple enemies target the holder. Good if you rely on a single main tank. ionic_spark: Utility tank item that is used with AP-heavy teams | Magic shred around the holder. Needs a stable front line so it doesn't die before applying shred. Very flexible tank; can hold pure tank or partial AP utility items.
""",
    "Darius": """
There is no greater symbol of Noxian might than Darius, the nation's most feared and battle-hardened commander. Rising from humble origins to become the Hand of Noxus, he cleaves through the empire's enemies—many of them Noxians themselves. Knowing that he never doubts his cause is just, and never hesitates once his axe is raised, those who stand against the leader of the Trifarian Legion can expect no mercy. gargoyle_stoneplate: Good for teams running fewer melee units | Stacks defenses when multiple enemies target the holder. Good if you rely on a single main tank. redemption: Good for comps with multiple melee units | Heals allies in an AoE. Decent if your front line clumps multiple bruisers or vanguards. sunfire_cape: Utility tank item for teams needing an anti-heal (wound) effect | Auto-applies Grievous Wounds in a radius. Best with a durable tank that can stand in the thick of battle. Main front-liner in some Syndicate builds; AoE spin benefits from tank + utility.
""",
    "Dr.Mundo": """
Utterly mad, tragically homicidal, and horrifyingly purple, Dr. Mundo is what keeps many of Zaun's citizens indoors on particularly dark nights. Now a self-proclaimed physician, he was once a patient of Zaun's most infamous asylum. After curing the entire staff, Dr. Mundo established his practice in the empty wards that once treated him and began mimicking the highly unethical procedures he had so often experienced himself. With a full cabinet of medicines and zero medical knowledge, he now makes himself more monstrous with each injection and terrifies the hapless patients who wander near his office. warmogs_armor: Good for tanks that get lots of resistances | Raw HP synergy for vanguards or max HP champs (Cho'Gath). Great all-around big-tank option. Gains extra % max HP from traits; raw health (Warmog's) scales especially well.
""",
    "Draven": """
In Noxus, warriors known as Reckoners face one another in arenas where blood is spilled and strength tested—but none has ever been as celebrated as Draven. A former soldier, he found that the crowds uniquely appreciated his flair for the dramatic, and his unparalleled skill with his spinning axes. Addicted to the spectacle of his own brash perfection, Draven has sworn to defeat whomever he must to ensure that his name is chanted throughout the empire forever more. spear_of_shojin: Vital for AD spells (MF, Xayah). Also flexible for big-ability cycles in hybrid comps. infinity_edge: No review available last_whisper: Armor shred for AD teams. Often overshadowed if you run Evenshroud, but still strong for multi-target. Spell-based AD carry who hits multiple enemies; needs mana + crit + shred/amp.
""",
    "Ekko": """
A prodigy from the rough streets of Zaun, Ekko is able to manipulate time to twist any situation to his advantage. He uses his own invention, the Z-Drive, to explore the branching possibilities of reality, crafting the perfect moment to seemingly achieve the impossible the first time, every time. Though Ekko revels in this freedom, when there's a threat to those he cares about, he and the Firelights will do anything to defend them. (no_recommended_items): No review available Not typically itemized as a main carry; often just a secondary or leftover-tank unit.
""",
    "Elise": """
Elise is a deadly predator who dwells in a shuttered, lightless palace, deep within the oldest city of Noxus. Once mortal, she was the mistress of a powerful house, but the bite of a vile demigod transformed her into something beautiful, yet utterly inhuman—a spider-like creature, drawing unsuspecting prey into her web. To maintain her eternal youth, Elise now prefers to feed upon the naive and the faithless, and there are few who can resist her seductions. (generic_ap): No review available Low priority for 3-star or main items; usually just a leftover AP holder if needed.
""",
    "Fiddlesticks": """
Something has awoken in Runeterra. Something ancient. Something terrible. The ageless horror known as Fiddlesticks stalks the edges of mortal society, drawn to areas thick with paranoia where it feeds upon terrorized victims. Wielding a jagged scythe, the haggard, makeshift creature reaps fear itself, shattering the minds of those unlucky enough to survive in its wake. Beware the sounding of the crow, or the whispering of the shape that appears almost human… Fiddlesticks has returned. archangels_staff: Gives big AP over time; great if your caster can stay alive (Fiddlesticks, Aurora). archangels_staff: Gives big AP over time; great if your caster can stay alive (Fiddlesticks, Aurora). hextech_gunblade: Heals the lowest HP ally for percent of damage dealt. Best if you have infinite-scaling AP (e.g. Archangels). Short-range AP with built-in omnivamp; double Archangel’s scales well in longer fights.
""",
    "Galio": """
Outside the gleaming city of Demacia, the stone colossus Galio keeps vigilant watch. Built as a bulwark against enemy mages, he often stands motionless for decades until the presence of powerful magic stirs him to life. Once activated, Galio makes the most of his time, savoring the thrill of a fight and the rare honor of defending his countrymen. But his triumphs are always bittersweet, for the magic he destroys is also his source of reanimation, and each victory leaves him dormant once again. sunfire_cape: Utility tank item for teams needing an anti-heal (wound) effect | Auto-applies Grievous Wounds in a radius. Best with a durable tank that can stand in the thick of battle. redemption: Good for comps with multiple melee units | Heals allies in an AoE. Decent if your front line clumps multiple bruisers or vanguards. evenshroud: Utility tank item that is used with AD-heavy teams | Tank item that applies a big damage amp debuff when you CC enemies. Frees up carry item slots. Utility front-liner who provides AoE knockup; any leftover tank/utility items are fine.
""",
    "Garen": """
A proud and noble warrior, Garen fights as one of the Dauntless Vanguard. He is popular among his fellows, and respected well enough by his enemies—not least as a scion of the prestigious Crownguard family, entrusted with defending Demacia and its ideals. Clad in magic-resistant armor and bearing a mighty broadsword, Garen stands ready to confront mages and sorcerers on the field of battle, in a veritable whirlwind of righteous steel. titans_resolve: Use on a tank that also deals significant damage | Hybrid stacking item for front-liners who do damage. Usually overshadowed except on strong melee bruisers. bloodthirster: Build on melee AD champs who need a shield + lifesteal (e.g. Zed, Rengar). Less common set-wide. steraks_gage: Scales with both HP & AD, but underperforms in a set with fewer AD bruisers. Potentially okay on Renekton. 5-cost bruiser with flexible damage/tank potential; typical AD-melee item mix.
""",
    "Gragas": """
Equal parts jolly and imposing, Gragas is a massive, rowdy brewmaster on his own quest for the perfect pint of ale. Hailing from parts unknown, he now searches for rare ingredients among the unblemished wastes of the Freljord, trying each recipe as he goes. Often intoxicated and extremely impulsive, he is legendary for the brawls he starts, which often end in all-night parties and widespread property damage. Any appearance from Gragas must surely foreshadow drinking and destruction—in that order. archangels_staff: Gives big AP over time; great if your caster can stay alive (Fiddlesticks, Aurora). bloodthirster: Build on melee AD champs who need a shield + lifesteal (e.g. Zed, Rengar). Less common set-wide. titans_resolve: Use on a tank that also deals significant damage | Hybrid stacking item for front-liners who do damage. Usually overshadowed except on strong melee bruisers. Hero-augment bruiser who can do surprising AP damage while staying alive.
""",
    "Graves": """
Malcolm Graves is a renowned mercenary, gambler, and thief—a wanted man in every city and empire he has visited. Even though he has an explosive temper, he possesses a strict sense of criminal honor, often enforced at the business end of his double-barreled shotgun Destiny. In recent years, he has reconciled a troubled partnership with Twisted Fate, and together they have prospered once more in the turmoil of Bilgewater's criminal underbelly. edge_of_night: Removes aggro at low HP. Solid for melee carries (Rengar, Graves) but narrow in this set. hand_of_justice: Adds crit, healing, or raw damage. Often a third item for melee front-liners or short-range DPS. titans_resolve: Use on a tank that also deals significant damage | Hybrid stacking item for front-liners who do damage. Usually overshadowed except on strong melee bruisers. Short-range Executioner with innate crit; needs survivability + healing + mixed stats.
""",
    "Illaoi": """
Illaoi's powerful physique is dwarfed only by her indomitable faith. As the prophet of the Great Kraken, she uses a huge, golden idol to rip her foes' spirits from their bodies and shatter their perception of reality. All who challenge the “Truth Bearer of Nagakabouros” soon discover Illaoi never battles alone—the god of the Serpent Isles fights by her side. (no_recommended_items): No review available Overshadowed in Anima Squad; rarely itemized heavily.
""",
    "Jarvan IV": """
Prince Jarvan, scion of the Lightshield dynasty, is heir apparent to the throne of Demacia. Raised to be a paragon of his nation's greatest virtues, he is forced to balance the heavy expectations placed upon him with his own desire to fight on the front lines. Jarvan inspires his troops with his fearsome courage and selfless determination, raising his family's colors high and revealing his true strength as a future leader of his people. sunfire_cape: Utility tank item for teams needing an anti-heal (wound) effect | Auto-applies Grievous Wounds in a radius. Best with a durable tank that can stand in the thick of battle. ionic_spark: Utility tank item that is used with AP-heavy teams | Magic shred around the holder. Needs a stable front line so it doesn't die before applying shred. evenshroud: Utility tank item that is used with AD-heavy teams | Tank item that applies a big damage amp debuff when you CC enemies. Frees up carry item slots. Usually a utility tank in Slayers; frees main carries to build pure damage.
""",
    "Jax": """
Unmatched in both his skill with unique armaments and his biting sarcasm, Jax is the last known weapons master of Icathia. After his homeland was laid low by its own hubris in unleashing the Void, Jax and his kind vowed to protect what little remained. As magic now rises in the world, this slumbering threat stirs once more, and Jax roams Valoran, wielding the last light of Icathia and testing all warriors he meets to see if any are strong enough to stand beside him... bloodthirster: Build on melee AD champs who need a shield + lifesteal (e.g. Zed, Rengar). Less common set-wide. titans_resolve: Use on a tank that also deals significant damage | Hybrid stacking item for front-liners who do damage. Usually overshadowed except on strong melee bruisers. quicksilver: Prevents CC but rarely vital. Can be useful on unstoppable auto-attackers (Zed, Aphelios). Hero-augment melee auto-attacker who hates downtime (prefers QSS over Edge of Night).
""",
    "Jhin": """
Jhin is a meticulous criminal psychopath who believes murder is art. Once an Ionian prisoner, but freed by shadowy elements within Ionia's ruling council, the serial killer now works as their cabal's assassin. Using his gun as his paintbrush, Jhin creates works of artistic brutality, horrifying victims and onlookers. He gains a cruel pleasure from putting on his gruesome theater, making him the ideal choice to send the most powerful of messages: terror. spear_of_shojin: Vital for AD spells (MF, Xayah). Also flexible for big-ability cycles in hybrid comps. infinity_edge: No review available guardbreaker: No review available AD caster with Executioner synergy; needs mana + crit; sometimes pairs with exotech item.
""",
    "Jinx": """
An unhinged and impulsive criminal from the undercity, Jinx is haunted by the consequences of her past—but that doesn't stop her from bringing her own chaotic brand of pandemonium to Piltover and Zaun. She uses her arsenal of DIY weapons to devastating effect, unleashing torrents of colorful explosions and gunfire, inspiring the disenfranchised to rebellion and resistance with the mayhem she leaves in her wake. spear_of_shojin: Vital for AD spells (MF, Xayah). Also flexible for big-ability cycles in hybrid comps. infinity_edge: No review available last_whisper: Armor shred for AD teams. Often overshadowed if you run Evenshroud, but still strong for multi-target. AoE rockets; Shojin for repeated casts, plus crit + shred for wide damage.
""",
    "Kindred": """
Separate, but never parted, Kindred represents the twin essences of death. Lamb's bow offers a swift release from the mortal realm for those who accept their fate. Wolf hunts down those who run from their end, delivering violent finality within his crushing jaws. Though interpretations of Kindred's nature vary across Runeterra, every mortal must choose the true face of their death. spear_of_shojin: Vital for AD spells (MF, Xayah). Also flexible for big-ability cycles in hybrid comps. infinity_edge: No review available Mostly an early- or mid-game carry holder; overshadowed by bigger late-game units.
""",
    "Kobuko": """
A jolly yordle from Bandle City, Kobuko spent years exploring the world and discovered that it is often harsh and unfair. And his search to understand this led him to Ionia, where he fell in love with the culture, the people, the environment, and the philosophies, and then added his own brand of yordle eccentricity to the mix. Now he travels across Runeterra, seeking to help others find joy and value in life, even through adversity, and encouraging those he meets to pursue their dreams, do what they love, and explore new possibilities. (any_items): No review available Highly flexible 5-cost; can use almost any leftover or powerful items effectively.
""",
    "Kog'maw": """
Belched forth from a rotting Void incursion deep in the wastelands of Icathia, Kog'Maw is an inquisitive yet putrid creature with a caustic, gaping mouth. This particular Void-spawn needs to gnaw and drool on anything within reach to truly understand it. Though not inherently evil, Kog'Maw's beguiling naiveté is dangerous, as it often precedes a feeding frenzy—not for sustenance, but to satisfy its unending curiosity. guinsoos_rageblade: Crucial for ramp-up auto-attackers (Aphelios, Kog'Maw). Top-tier if fights last long enough. runaans_hurricane: No review available deathblade: Raw AD for your main carry (e.g. Draven, Aphelios). Often overshadowed by Infinity Edge + others. Auto-attack champion that scales well with AS and multi-target hits; Gunblade also viable.
""",
    "Leblanc": """
Mysterious even to other members of the Black Rose cabal, LeBlanc is but one of many names for a pale woman who has manipulated people and events since the earliest days of Noxus. Using her magic to mirror herself, the sorceress can appear to anyone, anywhere, and even be in many places at once. Always plotting just out of sight, LeBlanc's true motives are as inscrutable as her shifting identity. blue_buff: Transforms short-mana champs (Nidalee, Yumi, Veigar) into spam casters. Extremely high-priority tier item. archangels_staff: Gives big AP over time; great if your caster can stay alive (Fiddlesticks, Aurora). jeweled_gauntlet: Spell crit item for AP; mandatory unless you have a trait that grants free crit (e.g. Executioner). Strategist AP caster; cast frequency (mana) + raw AP or crit synergy.
""",
    "Leona": """
Imbued with the fire of the sun, Leona is a holy warrior of the Solari who defends Mount Targon with her Zenith Blade and the Shield of Daybreak. Her skin shimmers with starfire while her eyes burn with the power of the celestial Aspect within her. Armored in gold and bearing a terrible burden of ancient knowledge, Leona brings enlightenment to some, death to others. warmogs_armor: Good for tanks that get lots of resistances | Raw HP synergy for vanguards or max HP champs (Cho'Gath). Great all-around big-tank option. gargoyle_stoneplate: Good for teams running fewer melee units | Stacks defenses when multiple enemies target the holder. Good if you rely on a single main tank. bramble_vest: Good against physical and AD teams | Blocks crit + returns damage. Great vs. AD teams but irrelevant into heavy AP. Main tank for Anima Squad; typical big-tank items.
""",
    "Miss Fortune": """
A Bilgewater captain famed for her looks but feared for her ruthlessness, Sarah Fortune paints a stark figure among the hardened criminals of the port city. As a child, she witnessed the reaver king Gangplank murder her family—an act she brutally avenged years later, blowing up his flagship while he was still aboard. Those who underestimate her will face a beguiling and unpredictable opponent… and, likely, a bullet or two in their guts. spear_of_shojin: Vital for AD spells (MF, Xayah). Also flexible for big-ability cycles in hybrid comps. infinity_edge: No review available giant_slayer: %HP damage. Great when lobbies stack bruisers or bastions with huge health pools. Spell-based AD carry who channels her ult; needs mana + crit for damage, plus bonus amp.
""",
    "Mordekaiser": """
Twice slain and thrice born, Mordekaiser is a brutal warlord from a foregone epoch who uses his necromantic sorcery to bind souls into an eternity of servitude. Few now remain who remember his earlier conquests, or know the true extent of his powers—but there are some ancient souls that do, and they fear the day when he may return to claim dominion over both the living and the dead. sunfire_cape: Utility tank item for teams needing an anti-heal (wound) effect | Auto-applies Grievous Wounds in a radius. Best with a durable tank that can stand in the thick of battle. redemption: Good for comps with multiple melee units | Heals allies in an AoE. Decent if your front line clumps multiple bruisers or vanguards. crownguard: A defensive item that grants a large shield when HP drops. Decent if you survive initial burst. 3-cost exotech with shielding/CC; benefits from AoE utility tank items.
""",
    "Morgana": """
Conflicted between her celestial and mortal natures, Morgana bound her wings to embrace humanity, and inflicts her pain and bitterness upon the dishonest and the corrupt. She rejects laws and traditions she believes are unjust, and fights for truth from the shadows of Demacia—even as others seek to repress it—by casting shields and chains of dark fire. More than anything else, Morgana truly believes that even the banished and outcast may one day rise again. blue_buff: Transforms short-mana champs (Nidalee, Yumi, Veigar) into spam casters. Extremely high-priority tier item. (leftover_ap): No review available Early-game AP item holder with low mana; not a main late-game carry.
""",
    "Naafiri": """
Across the sands of Shurima, a chorus of howls rings out. It is the call of the dune hounds, voracious predators who form packs and compete for the right to hunt in these barren lands. Among them, one pack stands above all, for they are driven not only by canine instincts, but by the ancient power of the Darkin. (no_recommended_items): No review available Rarely itemized in Nitro comps; overshadowed by other DPS/tank options.
""",
    "Neeko": """
Hailing from a long lost tribe of vastaya, Neeko can blend into any crowd by borrowing the appearances of others, even absorbing something of their emotional state to tell friend from foe in an instant. No one is ever sure where—or who—Neeko might be, but those who intend to do her harm will soon witness her true colors revealed, and feel the full power of her primordial spirit magic unleashed upon them. ionic_spark: Utility tank item that is used with AP-heavy teams | Magic shred around the holder. Needs a stable front line so it doesn't die before applying shred. warmogs_armor: Good for tanks that get lots of resistances | Raw HP synergy for vanguards or max HP champs (Cho'Gath). Great all-around big-tank option. gargoyle_stoneplate: Good for teams running fewer melee units | Stacks defenses when multiple enemies target the holder. Good if you rely on a single main tank. Strategist/Street Demon tank with plenty of durability; Spark shreds MR for AP team.
""",
    "Nidalee": """
Raised in the deepest jungle, Nidalee is a master tracker who can shapeshift into a ferocious cougar at will. Neither wholly woman nor beast, she viciously defends her territory from any and all trespassers, with carefully placed traps and deft spear throws. She cripples her quarry before pouncing on them in feline form—the lucky few who survive tell tales of a wild woman with razor-sharp instincts, and even sharper claws... (no_recommended_items): No review available Usually not itemized; overshadowed by the Nitro robot or bigger carries.
""",
    "Poppy": """
Runeterra has no shortage of valiant champions, but few are as tenacious as Poppy. Bearing the legendary hammer of Orlon, a weapon twice her size, this determined yordle has spent untold years searching in secret for the fabled “Hero of Demacia,” said to be its rightful wielder. Until then, she dutifully charges into battle, pushing back the kingdom's enemies with every whirling strike. archangels_staff: Gives big AP over time; great if your caster can stay alive (Fiddlesticks, Aurora). titans_resolve: Use on a tank that also deals significant damage | Hybrid stacking item for front-liners who do damage. Usually overshadowed except on strong melee bruisers. bloodthirster: Build on melee AD champs who need a shield + lifesteal (e.g. Zed, Rengar). Less common set-wide. Hero-augment tank-carry; can also do Titan’s + HoJ + Jeweled Gauntlet for burst.
""",
    "Renekton": """
Renekton is a terrifying, rage-fueled Ascended being from the scorched deserts of Shurima. Once, he was his empire's most esteemed warrior, leading the nation's armies to countless victories. However, after the empire's fall, Renekton was entombed beneath the sands, and slowly, as the world turned and changed, he succumbed to insanity. Now free once more, he is utterly consumed with finding and killing his brother, Nasus, who he blames, in his madness, for the centuries he spent in darkness. bloodthirster: Build on melee AD champs who need a shield + lifesteal (e.g. Zed, Rengar). Less common set-wide. titans_resolve: Use on a tank that also deals significant damage | Hybrid stacking item for front-liners who do damage. Usually overshadowed except on strong melee bruisers. steraks_gage: Scales with both HP & AD, but underperforms in a set with fewer AD bruisers. Potentially okay on Renekton. 5-cost bastion bruiser who steals AD; standard AD-melee item suite.
""",
    "Rengar": """
Rengar is a ferocious vastayan trophy hunter who lives for the thrill of tracking down and killing dangerous creatures. He scours the world for the most fearsome beasts he can find, especially seeking any trace of Kha'Zix, the void creature who scratched out his eye. Rengar stalks his prey neither for food nor glory, but for the sheer beauty of the pursuit. bloodthirster: Build on melee AD champs who need a shield + lifesteal (e.g. Zed, Rengar). Less common set-wide. titans_resolve: Use on a tank that also deals significant damage | Hybrid stacking item for front-liners who do damage. Usually overshadowed except on strong melee bruisers. guardbreaker: No review available 3-cost assassin who jumps to targets; sustain + stacking damage is vital.
""",
    "Rhaast": """
A sentient Darkin scythe, Rhaast is wielded by Shieda Kayn, Master Zed's second-in-command to the Order of Shadows. Slowly corrupting the young Kayn from within his prison, Rhaast hopes to one day become powerful enough to take over Kayn's body and become the malevolent overlord he was always meant to be. bloodthirster: Build on melee AD champs who need a shield + lifesteal (e.g. Zed, Rengar). Less common set-wide. infinity_edge: No review available hand_of_justice: Adds crit, healing, or raw damage. Often a third item for melee front-liners or short-range DPS. Vanguard synergy; likes the shield from BT plus damage + healing for frontline DPS.
""",
    "Samira": """
Samira stares death in the eye with unyielding confidence, seeking thrill wherever she goes. After her Shuriman home was destroyed as a child, Samira found her true calling in Noxus, where she built a reputation as a stylish daredevil taking on dangerous missions of the highest caliber. Wielding black-powder pistols and a custom-engineered blade, Samira thrives in life-or-death circumstances, eliminating any who stand in her way with flash and flair. infinity_edge: No review available hand_of_justice: Adds crit, healing, or raw damage. Often a third item for melee front-liners or short-range DPS. giant_slayer: %HP damage. Great when lobbies stack bruisers or bastions with huge health pools. AD caster who leaps in; needs crit + healing + bonus damage or shred.
""",
    "Sejuani": """
Sejuani is the brutal, unforgiving Iceborn warmother of the Winter's Claw, one of the most feared tribes of the Freljord. Her people's survival is a constant, desperate battle against the elements, forcing them to raid Noxians, Demacians, and Avarosans alike to survive the harsh winters. Sejuani herself spearheads the most dangerous of these attacks from the saddle of her drüvask boar Bristle, using her True Ice flail to freeze and shatter her enemies. protectors_vow: Good for tanks that need to cast their first ability as soon as possible adaptive_helm: Good for tanks with impactful abilities that cast multiple times per fight | Helps high-mana champions (e.g. Sejuani) cast again by gaining mana from taking hits. redemption: Good for comps with multiple melee units | Heals allies in an AoE. Decent if your front line clumps multiple bruisers or vanguards. Massive AoE stun; quick-cast tank items are best to ensure early ult.
""",
    "Senna": """
Cursed from childhood to be haunted by the supernatural Black Mist, Senna joined a sacred order known as the Sentinels of Light, and fiercely fought back—only to be killed, her soul imprisoned in a lantern by the cruel wraith Thresh. But refusing to lose hope, within the lantern Senna learned to use the Mist, and reemerged to new life, forever changed. Now wielding darkness along with light, Senna seeks to end the Black Mist by turning it against itself—with every blast of her relic weapon, redeeming the souls lost within. guinsoos_rageblade: Crucial for ramp-up auto-attackers (Aphelios, Kog'Maw). Top-tier if fights last long enough. runaans_hurricane: No review available giant_slayer: %HP damage. Great when lobbies stack bruisers or bastions with huge health pools. AoE auto-attacker; wants attack speed + multi-target hits + bonus AD.
""",
    "Seraphine": """
Born in Piltover to Zaunite parents, Seraphine can hear the souls of others—the world sings to her, and she sings back. Though these sounds overwhelmed her in her youth, she now draws on them for inspiration, turning the chaos into a symphony. She performs for the sister cities to remind their citizens that they're not alone, that they're stronger together, and that, in her eyes, their potential is limitless. spear_of_shojin: Vital for AD spells (MF, Xayah). Also flexible for big-ability cycles in hybrid comps. jeweled_gauntlet: Spell crit item for AP; mandatory unless you have a trait that grants free crit (e.g. Executioner). guardbreaker: No review available Backline AoE caster; synergy from Techies requires mana + spell crit + damage amp.
""",
    "Shaco": """
Crafted long ago as a plaything for a lonely prince, the enchanted marionette Shaco now delights in murder and mayhem. Corrupted by dark magic and the loss of his beloved charge, the once-kind puppet finds pleasure only in the misery of the poor souls he torments. He uses toys and simple tricks to deadly effect, finding the results of his bloody “games” hilarious—and for those who hear a dark chuckle in the dead of night, the Demon Jester may have marked them as his next plaything. edge_of_night: Removes aggro at low HP. Solid for melee carries (Rengar, Graves) but narrow in this set. infinity_edge: No review available hand_of_justice: Adds crit, healing, or raw damage. Often a third item for melee front-liners or short-range DPS. Melee assassin/spellcaster; EoN for survival, IE + HoJ for crit + lifesteal.
""",
    "Shyvana": """
Shyvana is a creature with the magic of a rune shard burning within her heart. Though she often appears humanoid, she can take her true form as a fearsome dragon, incinerating her foes with fiery breath. Having saved the life of the crown prince Jarvan IV, Shyvana now serves uneasily in his royal guard, struggling to find acceptance among the suspicious people of Demacia. crownguard: A defensive item that grants a large shield when HP drops. Decent if you survive initial burst. redemption: Good for comps with multiple melee units | Heals allies in an AoE. Decent if your front line clumps multiple bruisers or vanguards. ionic_spark: Utility tank item that is used with AP-heavy teams | Magic shred around the holder. Needs a stable front line so it doesn't die before applying shred. ‘Off-tank’ in Nitro comps; not tanky enough for pure items, so uses partial utility.
""",
    "Skarner": """
The ancient, colossal brackern Skarner is revered in Ixtal as one of the founding members of its ruling caste, the Yun Tal. Devoted to keeping his nation safe from the rest of the world, Skarner dwells in a chamber beneath Ixaocan where he can hear the vibrations of the earth and detect potential threats. As more members of the Yun Tal begin questioning Ixtal's self-isolation, Skarner grows increasingly paranoid and will do anything to keep Ixtal and its people safe—no matter the cost. (no_recommended_items): No review available Not a major 3-star or synergy carry; overshadowed in most comps.
""",
    "Sylas": """
Raised in one of Demacia's lesser quarters, Sylas of Dregbourne has come to symbolize the darker side of the Great City. As a boy, his ability to root out hidden sorcery caught the attention of the notorious mageseekers, who eventually imprisoned him for turning those same powers against them. Having now broken free, Sylas lives as a hardened revolutionary, using the magic of those around him to destroy the kingdom he once served… and his band of outcast mage followers seems to grow by the day. bloodthirster: Build on melee AD champs who need a shield + lifesteal (e.g. Zed, Rengar). Less common set-wide. titans_resolve: Use on a tank that also deals significant damage | Hybrid stacking item for front-liners who do damage. Usually overshadowed except on strong melee bruisers. steraks_gage: Scales with both HP & AD, but underperforms in a set with fewer AD bruisers. Potentially okay on Renekton. Hero-augment bruiser; standard melee + sustain combo.
""",
    "Twisted Fate": """
Twisted Fate is an infamous cardsharp and swindler who has gambled and charmed his way across much of the known world, earning the enmity and admiration of the rich and foolish alike. He rarely takes things seriously, greeting each day with a mocking smile and an insouciant swagger. In every possible way, Twisted Fate always has an ace up his sleeve. guinsoos_rageblade: Crucial for ramp-up auto-attackers (Aphelios, Kog'Maw). Top-tier if fights last long enough. guinsoos_rageblade: Crucial for ramp-up auto-attackers (Aphelios, Kog'Maw). Top-tier if fights last long enough. hextech_gunblade: Heals the lowest HP ally for % of damage dealt. Best if you have infinite-scaling AP (e.g. Archangels). Stacks AP each auto; double Rageblade + healing can ‘go infinite.’
""",
    "Urgot": """
Once a powerful Noxian headsman, Urgot was betrayed by the empire for which he had killed so many. Bound in iron chains, he was forced to learn the true meaning of strength in the Dredge—a prison mine deep beneath Zaun. Emerging in a disaster that spread chaos throughout the city, he now casts an imposing shadow over its criminal underworld. Raising his victims on the very chains that once enslaved him, he will purge his new home of the unworthy, making it a crucible of pain. guinsoos_rageblade: Crucial for ramp-up auto-attackers (Aphelios, Kog'Maw). Top-tier if fights last long enough. infinity_edge: No review available last_whisper: Armor shred for AD teams. Often overshadowed if you run Evenshroud, but still strong for multi-target. Hybrid DPS/spell champion; gains from attack-speed stacking + crit + shred.
""",
    "Varus": """
One of the ancient darkin, Varus was a deadly killer who loved to torment his foes, driving them almost to insanity before delivering the killing arrow. He was imprisoned at the end of the Great Darkin War, but escaped centuries later in the remade flesh of two Ionian hunters—they had unwittingly released him, cursed to bear the bow containing his bound essence. Varus now seeks out those who trapped him, in order to enact his brutal vengeance, but the mortal souls within still resist him every step of the way. spear_of_shojin: Vital for AD spells (MF, Xayah). Also flexible for big-ability cycles in hybrid comps. rabadons_deathcap: Maximizes flat AP. Great if not stacking Archangels or you have enough time to ramp. guardbreaker: No review available Executioner trait provides crit, so raw AP + quick casting is key.
""",
    "Vayne": """
Shauna Vayne is a deadly, remorseless Demacian monster hunter, who has dedicated her life to finding and destroying the demon that murdered her family. Armed with a wrist-mounted crossbow and a heart full of vengeance, she is only truly happy when slaying practitioners or creations of the dark arts, striking from the shadows with a flurry of silver bolts. guinsoos_rageblade: Crucial for ramp-up auto-attackers (Aphelios, Kog'Maw). Top-tier if fights last long enough. runaans_hurricane: No review available hextech_gunblade: Heals the lowest HP ally for % of damage dealt. Best if you have infinite-scaling AP (e.g. Archangels). Slayer synergy; heavy auto-attacks with multi-target via Runaan’s + sustain.
""",
    "Veigar": """
An enthusiastic master of dark sorcery, Veigar has embraced powers that few mortals dare approach. As a free-spirited inhabitant of Bandle City, he longed to push beyond the limitations of yordle magic, and turned instead to arcane texts that had been hidden away for thousands of years. Now a stubborn creature with an endless fascination for the mysteries of the universe, Veigar is often underestimated by others—but even though he believes himself truly evil, he possesses an inner morality that leads some to question his deeper motivations. blue_buff: Transforms short-mana champs (Nidalee, Yumi, Veigar) into spam casters. Extremely high-priority tier item. nashors_tooth: Attack speed + AP for cast spam (Annie). Often overshadowed by other rod + bow combos. hextech_gunblade: Heals the lowest HP ally for % of damage dealt. Best if you have infinite-scaling AP (e.g. Archangels). Short-range AP carry in Techies; spams spells quickly (low mana), deals high damage.
""",
    "Vex": """
In the black heart of the Shadow Isles, a lone yordle trudges through the spectral fog, content in its murky misery. With an endless supply of teen angst and a powerful shadow in tow, Vex lives in her own self-made slice of gloom, far from the revolting cheer of the “normie” world. Though she lacks ambition, she is quick to strike down color and happiness, stopping all would-be interlopers with her magical malaise. blue_buff: Transforms short-mana champs (Nidalee, Yumi, Veigar) into spam casters. Extremely high-priority tier item. rabadons_deathcap: Maximizes flat AP. Great if not stacking Archangels or you have enough time to ramp. guardbreaker: No review available Executioner trait means built-in crit; needs raw AP + fast casts.
""",
    "Vi": """
Raised on the mean streets of Zaun, Vi is a hotheaded, impulsive, and fearsome woman with very little respect for authority. She has always been a shrewd survivor, both from her youthful troublemaking topside and an unfairly long stint in Stillwater Hold. Now working with the Piltover Enforcers to keep the peace instead of breaking it, she wields mighty hextech gauntlets that can punch through walls—and criminals—with equal ease. steraks_gage: Scales with both HP & AD, but underperforms in a set with fewer AD bruisers. Potentially okay on Renekton. bloodthirster: Build on melee AD champs who need a shield + lifesteal (e.g. Zed, Rengar). Less common set-wide. titans_resolve: Use on a tank that also deals significant damage | Hybrid stacking item for front-liners who do damage. Usually overshadowed except on strong melee bruisers. Hero-augment bruiser scaling with HP + typical frontliner damage items.
""",
    "Viego": """
Once ruler of a long-lost kingdom, Viego perished over a thousand years ago when his attempt to bring his wife back from the dead triggered the magical catastrophe known as the Ruination. Transformed into a powerful, unliving wraith tortured by an obsessive longing for his centuries-dead queen, Viego now stands as the Ruined King, controlling the deadly Harrowings as he scours Runeterra for anything that might one day restore her, and destroying all in his path as the Black Mist pours endlessly from his cruel, broken heart. edge_of_night: Removes aggro at low HP. Solid for melee carries (Rengar, Graves) but narrow in this set. jeweled_gauntlet: Spell crit item for AP; mandatory unless you have a trait that grants free crit (e.g. Executioner). hand_of_justice: Adds crit, healing, or raw damage. Often a third item for melee front-liners or short-range DPS. If Techies-based: gets AP from trait, so focus on crit + lifesteal. In Golden Ox builds, replace JG/HoJ with archangels_staff or rabadons_deathcap.
""",
    "Xayah": """
Deadly and precise, Xayah is a vastayan revolutionary waging a personal war to save her people. She uses her speed, guile, and razor-sharp feather blades to cut down anyone who stands in her way. Xayah fights alongside her partner and lover, Rakan, to protect their dwindling tribe, and restore their race to her vision of its former glory. spear_of_shojin: Vital for AD spells (MF, Xayah). Also flexible for big-ability cycles in hybrid comps. infinity_edge: No review available last_whisper: Armor shred for AD teams. Often overshadowed if you run Evenshroud, but still strong for multi-target. Spell-focused AD carry who still needs auto damage; needs mana + crit + shred.
""",
    "Yuumi": """
A magical cat from Bandle City, Yuumi was once the familiar of a yordle enchantress, Norra. When her master mysteriously disappeared, Yuumi became the Keeper of Norra's sentient Book of Thresholds, traveling through portals in its pages to search for her. Yearning for affection, Yuumi seeks friendly companions to partner with on her journey, protecting them with luminous shields and fierce resolve. While Book strives to keep her on task, Yuumi is often drawn to worldly comforts, such as naps and fish. In the end, however, she always returns to her quest to find her friend. blue_buff: Transforms short-mana champs (Nidalee, Yumi, Veigar) into spam casters. Extremely high-priority tier item. statikk_shiv: Backline lightning + MR shred. Great for hybrid AP boards or quick AoE anti-heal synergy. morellonomicon: Applies Grievous Wounds in AoE. Top choice if your caster can spread damage to many units. Usually leftover items if forced; can poke from range, but not a main carry.
""",
    "Zac": """
Zac is the product of a toxic spill that ran through a chemtech seam and pooled in an isolated cavern deep in Zaun's Sump. Despite such humble origins, Zac has grown from primordial ooze into a thinking being who dwells in the city's pipes, occasionally emerging to help those who cannot help themselves or to rebuild the broken infrastructure of Zaun. ionic_spark: Utility tank item that is used with AP-heavy teams | Magic shred around the holder. Needs a stable front line so it doesn't die before applying shred. sunfire_cape: Utility tank item for teams needing an anti-heal (wound) effect | Auto-applies Grievous Wounds in a radius. Best with a durable tank that can stand in the thick of battle. protectors_vow: Good for tanks that need to cast their first ability as soon as possible Splits into multiple blobs each applying AoE effects; accelerate first cast.
""",
    "Zed": """
Utterly ruthless and without mercy, Zed is the leader of the Order of Shadow, an organization he created with the intent of militarizing Ionia's magical and martial traditions to drive out Noxian invaders. During the war, desperation led him to unlock the secret shadow form—a malevolent spirit magic as dangerous and corrupting as it is powerful. Zed has mastered all of these forbidden techniques to destroy anything he sees as a threat to his nation, or his new order. edge_of_night: Removes aggro at low HP. Solid for melee carries (Rengar, Graves) but narrow in this set. infinity_edge: No review available hand_of_justice: Adds crit, healing, or raw damage. Often a third item for melee front-liners or short-range DPS. Main melee AD caster at 4-cost; needs strong survival + crit + healing.
""",
    "Zeri": """
A headstrong, spirited young woman from Zaun's working-class, Zeri channels her electric magic to charge herself and her custom-crafted gun. Her volatile power mirrors her emotions, its sparks reflecting her lightning-fast approach to life. Deeply compassionate toward others, Zeri carries the love of her family and her home into every fight. Though her eagerness to help can sometimes backfire, Zeri believes one truth to be certain: stand up for your community, and it will stand up with you. guinsoos_rageblade: Crucial for ramp-up auto-attackers (Aphelios, Kog'Maw). Top-tier if fights last long enough. hextech_gunblade: Heals the lowest HP ally for % of damage dealt. Best if you have infinite-scaling AP (e.g. Archangels). runaans_hurricane: No review available Auto-attack synergy with echo shots; stacking AS + healing + multi-target.
""",
    "Ziggs": """
With a love of big bombs and short fuses, the yordle Ziggs is an explosive force of nature. As an inventor's assistant in Piltover, he was bored by his predictable life and befriended a mad, blue-haired bomber named Jinx. After a wild night on the town, Ziggs took her advice and moved to Zaun, where he now explores his fascinations more freely, terrorizing the chem-barons and regular citizens alike in his never ending quest to blow stuff up. blue_buff: Transforms short-mana champs (Nidalee, Yumi, Veigar) into spam casters. Extremely high-priority tier item. morellonomicon: Applies Grievous Wounds in AoE. Top choice if your caster can spread damage to many units. statikk_shiv: Backline lightning + MR shred. Great for hybrid AP boards or quick AoE anti-heal synergy. AoE bombard from backline; repeated casts applying utility or anti-heal.
""",
    "Zyra": """
Born in an ancient, sorcerous catastrophe, Zyra is the wrath of nature given form—an alluring hybrid of plant and human, kindling new life with every step. She views the many mortals of Valoran as little more than prey for her seeded progeny, and thinks nothing of slaying them with flurries of deadly spines. Though her true purpose has not been revealed, Zyra wanders the world, indulging her most primal urges to colonize, and strangle all other life from it. spear_of_shojin: Vital for AD spells (MF, Xayah). Also flexible for big-ability cycles in hybrid comps. morellonomicon: Applies Grievous Wounds in AoE. Top choice if your caster can spread damage to many units. statikk_shiv: Backline lightning + MR shred. Great for hybrid AP boards or quick AoE anti-heal synergy. Generally used for CC; repeated casts for stuns or anti-heal.
""",
}

combined_champions = [f"{k} : {v}" for k, v in combined_champions.items()]

# Create a mapping of champion names to their indices for easy access
champions_lower_dict = {champions[i].lower(): i for i in range(len(champions))}  

comatrix_normalized = np.load(os.path.join(os.environ['ROOT_PATH'], 'data', 'comatrix_normalized.npy'))
comatrix = np.load(os.path.join(os.environ['ROOT_PATH'], 'data', 'comatrix.npy'))

# Tokenize method which can be passed into various methods.
def tokenize(text):
    """Returns a list of words that make up the text.    

    Parameters
    ----------
    text : str
        The input text string

    Returns
    -------
    list
        A list of tokens corresponding to the input string.
    """
    return [x for x in re.findall(r"[a-z]+", text.lower())]


def recommend_next_champion(user_comp_csv, comatrix_normalized, champions, champions_lower_dict):
    """
    Given a comma-separated list of champion names, returns the champion
    with the highest row-normalized co-occurrence sum that is not already
    in the user's comp.

    user_comp_csv: str, e.g. "Ahri, Annie, Ashe"
    comatrix_normalized: np.array (N x N), row-normalized co-occurrence matrix
    champions: list of str, e.g. ["Ahri", "Annie", "Ashe", ...]
    champions_lower_dict: dict, e.g. {"ahri": 0, "annie": 1, "ashe": 2, ...}

    Return: str, name of the recommended champion
    """

    # Parse the user's champions into a list of lowercase names
    user_champ_list = [champ.strip().lower() for champ in user_comp_csv.split(',') if champ.strip()]

    # Convert each champion to its index (skip any name not in the dictionary)
    user_indices = [champions_lower_dict[c] for c in user_champ_list if c in champions_lower_dict]

    # Accumulate row-normalized co-occurrence scores across all champions in the comp
    # This gives us a "likelihood" score for every other champion
    accum_scores = np.zeros(comatrix_normalized.shape[0])
    for idx in user_indices:
        accum_scores += comatrix_normalized[idx]

    # Exclude champions already in the user's comp by setting their scores to a negative number
    for idx in user_indices:
        accum_scores[idx] = -1_000_000  # any large negative value to ensure they're not chosen

    # Get the index of the champion with the highest score
    recommended_idx = np.argmax(accum_scores)

    # Return the champion name
    return champions[recommended_idx]

def recommend_champions(user_comp_csv):
    """
    Given a comma-separated list of champion names, returns accumulated scores
    of all champions' row-normalized co-occurrence sum that are not already
    in the user's comp.

    :param user_comp_csv: str of comma-separated champion names

    :return: accumulated scores of all champions
    """

    # 1) Parse the user's champions into a list of lowercase names
    user_champ_list = [champ.strip().lower() for champ in user_comp_csv.split(',') if champ.strip()]

    # 2) Convert each champion to its index (skip any name not in the dictionary)
    user_indices = [champions_lower_dict[c] for c in user_champ_list if c in champions_lower_dict]

    # 3) Accumulate row-normalized co-occurrence scores across all champions in the comp
    accum_scores = np.zeros(comatrix_normalized.shape[0])
    for idx in user_indices:
        accum_scores += comatrix_normalized[idx]

    # 4) Exclude champions already in the user's comp by setting their scores to negative
    for idx in user_indices:
        accum_scores[idx] = -1_000_000  # ensure they're not chosen

    # 5) Return the accumulated scores for all champions
    return accum_scores

# Example usage:
# recommended = recommend_next_champions("Ahri, Annie, Ashe", comatrix_normalized, champions, champions_lower_dict, k=3)
# print("Recommended champions:", recommended)