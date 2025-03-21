DROP TABLE IF EXISTS champ_info;
DROP TABLE IF EXISTS trait_info;
CREATE TABLE IF NOT EXISTS champ_info (
    name VARCHAR(64) PRIMARY KEY,
    cost INT,
    traits VARCHAR(255)
);
CREATE TABLE IF NOT EXISTS trait_info (
    name VARCHAR(64) PRIMARY KEY,
    description VARCHAR(512)
);

INSERT INTO champ_info (name, cost, traits) VALUES ("Ahri", 2, "Star Guardian,Sorcerer");
INSERT INTO champ_info (name, cost, traits) VALUES ("Annie", 2, "Mech-Pilot,Sorcerer");
INSERT INTO champ_info (name, cost, traits) VALUES ("Ashe", 3, "Celestial,Sniper");
INSERT INTO champ_info (name, cost, traits) VALUES ("Aurelion Sol", 5, "Rebel,Starship");
INSERT INTO champ_info (name, cost, traits) VALUES ("Blitzcrank", 2, "Chrono,Brawler");
INSERT INTO champ_info (name, cost, traits) VALUES ("Caitlyn", 1, "Chrono,Sniper");
INSERT INTO champ_info (name, cost, traits) VALUES ("Cho'Gath", 4, "Void,Brawler");
INSERT INTO champ_info (name, cost, traits) VALUES ("Darius", 2, "Space Pirate,Mana-Reaver");
INSERT INTO champ_info (name, cost, traits) VALUES ("Ekko", 5, "Cybernetic,Infiltrato");
INSERT INTO champ_info (name, cost, traits) VALUES ("Ezreal", 3, "Chrono,Blaster");
INSERT INTO champ_info (name, cost, traits) VALUES ("Fiora", 1, "Cybernetic,Blademaster");
INSERT INTO champ_info (name, cost, traits) VALUES ("Fizz", 4, "Mech-Pilot,Infiltrator");
INSERT INTO champ_info (name, cost, traits) VALUES ("Gangplank", 5, "Space Pirate,Mercenary,Demolitionist");
INSERT INTO champ_info (name, cost, traits) VALUES ("Graves", 1, "Space Pirate,Blaster");
INSERT INTO champ_info (name, cost, traits) VALUES ("Irelia", 4, "Cybernetic,Mana-Reaver,Blademaster");
INSERT INTO champ_info (name, cost, traits) VALUES ("Jarvan IV", 1, "Dark Star,Protector");
INSERT INTO champ_info (name, cost, traits) VALUES ("Jayce", 3, "Space Pirate,Vanguard");
INSERT INTO champ_info (name, cost, traits) VALUES ("Jhin", 4, "Dark Star,Sniper");
INSERT INTO champ_info (name, cost, traits) VALUES ("Jinx", 4, "Rebel,Blaster");
INSERT INTO champ_info (name, cost, traits) VALUES ("Kai'Sa", 2, "Valkyrie,Infiltrator");
INSERT INTO champ_info (name, cost, traits) VALUES ("Karma", 3, "Dark Star,Mystic");
INSERT INTO champ_info (name, cost, traits) VALUES ("Kassadin", 3, "Celestial,Mana-Reaver");
INSERT INTO champ_info (name, cost, traits) VALUES ("Kayle", 4, "Valkyrie,Blademaster");
INSERT INTO champ_info (name, cost, traits) VALUES ("Kha'Zix", 1, "Void,Infiltrator");
INSERT INTO champ_info (name, cost, traits) VALUES ("Leona", 1, "Cybernetic,Vanguard");
INSERT INTO champ_info (name, cost, traits) VALUES ("Lucian", 2, "Cybernetic,Blaster");
INSERT INTO champ_info (name, cost, traits) VALUES ("Lulu", 5, "Celestial,Mystic");
INSERT INTO champ_info (name, cost, traits) VALUES ("Lux", 3, "Dark Star,Sorcerer");
INSERT INTO champ_info (name, cost, traits) VALUES ("Malphite", 1, "Rebel,Brawler");
INSERT INTO champ_info (name, cost, traits) VALUES ("Master Yi", 3, "Rebel,Blademaster");
INSERT INTO champ_info (name, cost, traits) VALUES ("Miss Fortune", 5, "Valkyrie,Mercenary,Blaster");
INSERT INTO champ_info (name, cost, traits) VALUES ("Mordekaiser", 2, "Dark Star,Vanguard");
INSERT INTO champ_info (name, cost, traits) VALUES ("Neeko", 3, "Star Guardian,Protector");
INSERT INTO champ_info (name, cost, traits) VALUES ("Poppy", 1, "Star Guardian,Vanguard");
INSERT INTO champ_info (name, cost, traits) VALUES ("Rakan", 2, "Celestial,Protector");
INSERT INTO champ_info (name, cost, traits) VALUES ("Rumble", 3, "Mech-Pilot,Demolitionist");
INSERT INTO champ_info (name, cost, traits) VALUES ("Shaco", 3, "Dark Star,Infiltrator");
INSERT INTO champ_info (name, cost, traits) VALUES ("Shen", 2, "Chrono,Blademaster");
INSERT INTO champ_info (name, cost, traits) VALUES ("Sona", 2, "Rebel,Mystic");
INSERT INTO champ_info (name, cost, traits) VALUES ("Soraka", 4, "Star Guardian,Mystic");
INSERT INTO champ_info (name, cost, traits) VALUES ("Syndra", 3, "Star Guardian,Sorcerer");
INSERT INTO champ_info (name, cost, traits) VALUES ("Thresh", 5, "Chrono,Mana-Reaver");
INSERT INTO champ_info (name, cost, traits) VALUES ("Twisted Fate", 1, "Chrono,Sorcerer");
INSERT INTO champ_info (name, cost, traits) VALUES ("Vel'Koz", 4, "Void,Sorcerer");
INSERT INTO champ_info (name, cost, traits) VALUES ("Vi", 3, "Cybernetic,Brawler");
INSERT INTO champ_info (name, cost, traits) VALUES ("Wukong", 4, "Chrono,Vanguard");
INSERT INTO champ_info (name, cost, traits) VALUES ("Xayah", 1, "Celestial,Blademaster");
INSERT INTO champ_info (name, cost, traits) VALUES ("Xerath", 5, "Dark Star,Sorcerer");
INSERT INTO champ_info (name, cost, traits) VALUES ("Xin Zhao", 2, "Celestial,Protector");
INSERT INTO champ_info (name, cost, traits) VALUES ("Yasuo", 2, "Rebel,Blademaster");
INSERT INTO champ_info (name, cost, traits) VALUES ("Ziggs", 1, "Rebel,Demolitionist");
INSERT INTO champ_info (name, cost, traits) VALUES ("Zoe", 1, "Star Guardian,Sorcerer");

INSERT INTO trait_info (name, description) VALUES ("Blademaster", "Blademasters' Basic Attacks have a chance to trigger two additional attacks against their target. These additional attacks deal damage like Basic Attacks and trigger on-hit effects.");
INSERT INTO trait_info (name, description) VALUES ("Blaster", "Every fourth Basic Attack from a Blaster fires additional attacks at random enemies. These additional attacks deal damage like Basic Attacks, trigger on-hit effects, and can critically hit.");
INSERT INTO trait_info (name, description) VALUES ("Brawler", "Brawlers gain bonus Maximum Health.");
INSERT INTO trait_info (name, description) VALUES ("Celestial", "All allies heal for some of the damage they deal with spells and attacks.");
INSERT INTO trait_info (name, description) VALUES ("Chrono", "All allies gain attack speed every few seconds.");
INSERT INTO trait_info (name, description) VALUES ("Cybernetic", "Cybernetic champions with at least one item gain Health and Attack Damage.");
INSERT INTO trait_info (name, description) VALUES ("Dark Star", "When a Dark Star champion dies they give increased damage, plus any previous stacks of this effect, to the nearest ally Dark Star champion.");
INSERT INTO trait_info (name, description) VALUES ("Demolitionist", "Damage from Demolitionists' spellcasts stuns their targets for a few seconds. (Once per spellcast)");
INSERT INTO trait_info (name, description) VALUES ("Infiltrator", "Infiltrators gain Attack Speed for a few seconds at the start of combat.");
INSERT INTO trait_info (name, description) VALUES ("Mana-Reaver", "Mana-Reavers' Basic Attacks increase the mana cost of their target's next spellcast by a percentage.");
INSERT INTO trait_info (name, description) VALUES ("Mech-Pilot", "At the start of combat, three random Mech-Pilots are teleported into a Super-Mech. The Super-Mech has the combined Health, Attack Damage, and Traits of its pilots, as well as 3 random items from among them. When the Super-Mech dies the Pilots are ejected, granted Mana, and continue to fight.");
INSERT INTO trait_info (name, description) VALUES ("Mercenary", "Upgrades for Mercenaries' spells have a chance to appear in the shop.");
INSERT INTO trait_info (name, description) VALUES ("Mystic", "All allies gain Magic Resistance.");
INSERT INTO trait_info (name, description) VALUES ("Protector", "Protectors shield themselves for a few seconds whenever they cast a spell. This shield doesn't stack.");
INSERT INTO trait_info (name, description) VALUES ("Rebel", "At the start of combat, Rebels gain a shield and bonus damage for each adjacent Rebel. The shield lasts for a few seconds.");
INSERT INTO trait_info (name, description) VALUES ("Sniper", "Snipers deal percentage increased damage for each hex between themselves and their target.");
INSERT INTO trait_info (name, description) VALUES ("Sorcerer", "All allies have increased Spell Power.");
INSERT INTO trait_info (name, description) VALUES ("Space Pirate", "Whenever a Space Pirate lands a killing blow on a Champion there is a chance to drop extra loot.");
INSERT INTO trait_info (name, description) VALUES ("Star Guardian", "Star Guardians' spellcasts grant Mana to other Star Guardians, spread among them.");
INSERT INTO trait_info (name, description) VALUES ("Starship", "Starships gain mana per second, maneuver around the board, and are immune to movement impairing effects, but can't make Basic Attacks.");
INSERT INTO trait_info (name, description) VALUES ("Valkyrie", "Valkyrie attacks and spells always critically hit targets below a percentage health.");
INSERT INTO trait_info (name, description) VALUES ("Vanguard", "Vanguard champions gain bonus Armor.");
INSERT INTO trait_info (name, description) VALUES ("Void", "Attacks and spells from Void champions deal true damage.");