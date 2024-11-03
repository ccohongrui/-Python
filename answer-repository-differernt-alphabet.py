from itertools import combinations
# 題目
alice =['fire', 'rome', 'pecs', 'owse', 'warn', 'apse', 'yore', 'sith', 'hake', 'iota', 'laic', 'grat', 'fist', 'limb', 'airs', 'baby', 'darn', 'ryke', 'pulk', 'hasp', 'balk', 'stay', 'bibb', 'step', 'cero', 'aped', 'sunk', 'dray', 'bank', 'keno', 'hods', 'beat', 'cays', 'kelt', 'reps', 'taus', 'dibs', 'reft', 'ribs', 'lich', 'anoa', 'secs', 'vans', 'defi', 'rums', 'lati', 'herl', 'berm', 'shod', 'conk', 'pont', 'muon', 'gibs', 'eyry', 'elks', 'pate', 'dews', 'past', 'unit', 'amis', 'dove', 'woks', 'coot', 'fuss', 'mary', 'biga', 'wane', 'nuke', 'scum', 'lent', 'dolt', 'ants', 'doxy', 'anas', 'jupe', 'vasa', 'nuns', 'brut', 'gods', 'sura', 'vlei', 'alto', 'spry', 'eggy', 'guar', 'kobo', 'roes', 'rami', 'gift', 'soma', 'peel', 'mart', 'jehu', 'tiny', 'anis', 'mors', 'brow', 'teal', 'swat', 'grot', 'eros', 'acts', 'mare', 'semi', 'toll', 'pint', 'segs', 'etas', 'hazy', 'afar', 'roan', 'teen', 'sols', 'gulp', 'pope', 'titi', 'tuns', 'weer', 'jack', 'germ', 'skin', 'cuif', 'jute', 'tees', 'lags', 'razz', 'wigs', 'halm', 'flex', 'eats', 'nans', 'shoo', 'zona', 'mode', 'supe', 'keck', 'none', 'tabs', 'pant', 'baba', 'clot', 'cels', 'soca', 'apps', 'murr', 'site', 'cake', 'yews', 'thud', 'leaf', 'bolo', 'rolf', 'kith', 'omit', 'exed', 'maps', 'espy', 'plum', 'diol', 'twee', 'gila', 'hong', 'tavs', 'rein', 'foys', 'wilt', 'wise', 'lear', 'mike', 'seif', 'jube', 'mots', 'hame', 'gull', 'taut', 'lava', 'samp', 'prim', 'skee', 'puja', 'qats', 'fard', 'grue', 'back', 'idol', 'barf', 'tung', 'kier', 'reif', 'seas', 'bush', 'temp', 'shes', 'raga', 'coil', 'burb', 'open', 'chis', 'city', 'trip', 'feet', 'deme', 'arks', 'crus', 'swad', 'curs', 'fore', 'diel', 'lade', 'maul', 'well', 'yods', 'rake', 'gnaw', 'dhak', 'ajar', 'wits', 'gore', 'your', 'bien', 'hets', 'oles', 'bile', 'tirl', 'safe', 'teff', 'leku', 'drip', 'coft', 'ably', 'tech', 'cobs', 'jive', 'oval', 'prex', 'cedi', 'elds', 'ripe', 'oryx', 'disk', 'gnus', 'hoya', 'tune', 'bris', 'tele', 'ghee', 'hams', 'yaup', 'stum', 'lunt', 'alit', 'chin', 'cede', 'tops', 'java', 'tain', 'blab', 'apos', 'copy', 'limp', 'odic', 'lutz', 'bent', 'gets', 'pawl', 'aims', 'cion', 'hath', 'tapa', 'carb', 'brie', 'gaum', 'koji', 'dura', 'agee', 'wabs', 'keef', 'glad', 'leal', 'herd', 'cane', 'puck', 'brag', 'cuss', 'lion', 'beer', 'cepe', 'lota', 'rock', 'bumf', 'dung', 'beep', 'kino', 'vets', 'spur', 'tews', 'niff', 'duns', 'sone', 'gaze', 'gasp', 'moas', 'tyes', 'coff', 'mast', 'gals', 'lues', 'envy', 'bidi', 'husk', 'sole', 'psis', 'ouph', 'star', 'bren', 'muso', 'noel', 'puns', 'duce', 'doty', 'raps', 'isba', 'lawn', 'lipe', 'waly', 'souk', 'rote', 'roam', 'imps', 'haed', 'dexy', 'ruse', 'ties', 'golf', 'mace', 'taxi', 'dame', 'ires', 'quay', 'celt', 'tufa', 'doat', 'ritz', 'mein', 'guls', 'saga', 'ball', 'lime', 'sine', 'lied', 'gamb', 'logy', 'runt', 'tack', 'nide', 'barn', 'camp', 'wool', 'spat', 'lorn', 'pave', 'lown', 'vary', 'pups', 'wild', 'fall', 'writ', 'weed', 'punt', 'vase', 'ocas', 'spin', 'fake', 'pact', 'fabs', 'sulu', 'sell', 'vale', 'soja', 'ashy', 'moan', 'onto', 'ride', 'apes', 'hubs', 'vext', 'fids', 'quin', 'list', 'pogo', 'gain', 'fail', 'albs', 'bibs', 'vamp', 'burs', 'syli', 'kues', 'unco', 'smog', 'kaki', 'prig', 'flak', 'orby', 'burr', 'tilt', 'bise', 'roto', 'plew', 'amus', 'swop', 'mods', 'glop', 'dele', 'whey', 'tent', 'leis', 'beth', 'pain', 'sows', 'duke', 'tell', 'hobo', 'nose', 'nite', 'piny', 'find', 'bark', 'jinx', 'alls', 'dead', 'bled', 'sike', 'axel', 'vows', 'gama', 'load', 'ruff', 'poet', 'foil', 'leer', 'tile', 'yeps', 'size', 'biro', 'pend', 'tens', 'eaux', 'fins', 'nixe', 'ghat', 'magi', 'goop', 'giga', 'oxid', 'gosh', 'dock', 'rick', 'gude', 'frow', 'jell', 'fess', 'phew', 'said', 'fair', 'riot', 'sirs', 'tubs', 'self', 'puke', 'gyre', 'alae', 'djin', 'laws', 'toit', 'loft', 'toon', 'away', 'chez', 'band', 'carn', 'avos', 'bout', 'pice', 'tore', 'wark', 'hops', 'agma', 'agar', 'data', 'minx', 'gala', 'slid', 'vibe', 'soot', 'mogs', 'kips', 'rift', 'redo', 'sign', 'peon', 'wyes', 'bill', 'dang', 'tump', 'hoed', 'wair', 'able', 'cell', 'idyl', 'yows', 'bate', 'kune', 'boos', 'cant', 'lakh', 'holm', 'wont', 'inti', 'foal', 'flus', 'weka', 'pfft', 'gelt', 'oaks', 'tail', 'juke', 'sups', 'drow', 'cark', 'busy', 'koan', 'bufo', 'grow', 'wand', 'mail', 'beys', 'pods', 'biff', 'obey', 'wyte', 'ante', 'fits', 'warm', 'oink', 'vent', 'axes', 'suit', 'bulb', 'ughs', 'come', 'nipa', 'lint', 'soft', 'kaka', 'luma', 'kemp', 'moon', 'ward', 'woad', 'curn', 'wind', 'this', 'yous', 'ones', 'alec', 'shut', 'rung', 'mile', 'agin', 'joey', 'lats', 'when', 'cons', 'prey', 'nils', 'aahs', 'tone', 'naff', 'pats', 'puma', 'wolf', 'coof', 'chap', 'yuca', 'lehr', 'hang', 'rite', 'spue', 'chub', 'cigs', 'feds', 'cans', 'gage', 'frap', 'milt', 'euro', 'burd', 'otic', 'sett', 'toys', 'bide', 'sink', 'eely', 'masa', 'vend', 'keep', 'sima', 'whys', 'sloe', 'hart', 'fens', 'camo', 'opes', 'guck', 'hull', 'peas', 'real', 'bods', 'skew', 'shri', 'peag', 'quip', 'pula', 'fila', 'gaen', 'sots', 'silo', 'sect', 'howl', 'jete', 'baps', 'coed', 'prat', 'peer', 'utah', 'odea', 'cube', 'hero', 'opus', 'slip', 'murk', 'wive', 'pray', 'fare', 'dals', 'migg', 'carr', 'neap', 'tanh', 'ilea', 'poll', 'kook', 'gent', 'read', 'uvea', 'caph', 'kilt', 'chop', 'lums', 'prep', 'bima', 'film', 'tost', 'ains', 'clod', 'rete', 'pond', 'yeti', 'orts', 'sure', 'sent', 'iron', 'jeed', 'loll', 'stud', 'thir', 'nick', 'gyms', 'dore', 'wens', 'pony', 'gied', 'beef', 'trey', 'holt', 'slim', 'kuru', 'pipe', 'volt', 'lune', 'toro', 'oots', 'rhus', 'mong', 'gled', 'give', 'shah', 'seme', 'fell', 'room', 'clew', 'veer', 'dols', 'caky', 'jato', 'soph', 'lych', 'kafs', 'coni', 'khat', 'rede', 'pyic', 'wonk', 'meow', 'tall', 'smit', 'staw', 'lyes', 'sard', 'seen', 'toad', 'amok', 'fern', 'putt', 'hins', 'jeep', 'dino', 'tole', 'turf', 'culm', 'ways', 'nori', 'stir', 'save', 'sass', 'cist', 'whim', 'rips', 'bath', 'oses', 'crag', 'hold', 'emir', 'fink', 'eths', 'fora', 'mini', 'trug', 'rove', 'pyin', 'pois', 'waft', 'whet', 'dons', 'dose', 'kiln', 'dost', 'luxe', 'teed', 'user', 'fogs', 'thaw', 'chid', 'torn', 'blow', 'chat', 'dyer', 'gats', 'lost', 'scow', 'fere', 'hyle', 'egad', 'tire', 'guvs', 'vara', 'cads', 'drab', 'sice', 'nays', 'whig', 'quai', 'raft', 'pack', 'clog', 'guff', 'cagy', 'maun', 'zonk', 'zebu', 'awls', 'mola', 'halo', 'dreg', 'keps', 'blip', 'rubs', 'auto', 'torr', 'pols', 'zing', 'talk', 'watt', 'cobb', 'gaol', 'leys', 'trio', 'emeu', 'wack', 'were', 'dell', 'rise', 'swab', 'ewer', 'vile', 'pass', 'bigs', 'kerb', 'gips', 'tank', 'inks', 'moot', 'buys', 'dyad', 'phot', 'zags', 'acyl', 'immy', 'cult', 'hast', 'dows', 'glut', 'lets', 'expo', 'mote', 'cole', 'jibs', 'glug', 'pyes', 'okas', 'scad', 'lulu', 'nary', 'boys', 'mutt', 'guid', 'coif', 'womb', 'horn', 'vine', 'bird', 'deil', 'sees', 'apod', 'wipe', 'fane', 'lief', 'sons', 'repo', 'fino', 'flax', 'alba', 'guru', 'pegs', 'nogs', 'bass', 'upby', 'geed', 'sump', 'yeas', 'sock', 'alan', 'moll', 'ogre', 'viga', 'hint', 'echo', 'rebs', 'cuke', 'oaky', 'posh', 'hyla', 'lowe', 'hunk', 'nims', 'slew', 'aced', 'skis', 'does', 'limo', 'deft', 'caws', 'pugs', 'idem', 'bork', 'shad', 'peal', 'mony', 'koto', 'skat', 'zeds', 'slub', 'nota', 'gory', 'lieu', 'rich', 'lard', 'pike', 'flam', 'shiv', 'move', 'pews', 'guys', 'coke', 'fade', 'joke', 'coss', 'gout', 'shot', 'buns', 'jugs', 'ibis', 'jake', 'gien', 'gorm', 'gads', 'bead', 'pans', 'viol', 'mums', 'aver', 'rids', 'dent', 'spay', 'view', 'rows', 'jobs', 'urps', 'juga', 'oily', 'buds', 'even', 'fobs', 'bola', 'imid', 'into', 'sods', 'efts', 'hums', 'tree', 'hewn', 'lass', 'ogam', 'tels', 'loch', 'gape', 'mity', 'weld', 'utas', 'naps', 'gird', 'deni', 'gimp', 'kirs', 'vade', 'grin', 'bals', 'funs', 'perp', 'jure', 'jiao', 'yagi', 'wads', 'bong', 'cask', 'aves', 'ilks', 'yens', 'like', 'mask', 'fuci', 'fats', 'nags', 'zinc', 'lido', 'aril', 'heil', 'trog', 'waif', 'derm', 'jeon', 'naan', 'marl', 'wary', 'bios', 'doby', 'both', 'lips', 'frit']
bob = ['girt', 'year', 'daff', 'dors', 'dorp', 'boho', 'deys', 'gown', 'glia', 'drip', 'rick', 'hoax', 'hulk', 'exes', 'jiff', 'lept', 'gaps', 'soya', 'keto', 'koji', 'huns', 'lums', 'ropy', 'rest', 'serf', 'hems', 'dote', 'rash', 'cleg', 'whew', 'ammo', 'yods', 'nowt', 'brie', 'brad', 'pean', 'defi', 'ably', 'sice', 'reed', 'rids', 'gout', 'thew', 'fuse', 'lear', 'foul', 'sloe', 'roar', 'vacs', 'whys', 'oles', 'babu', 'lira', 'doll', 'yeld', 'loan', 'oust', 'memo', 'sett', 'ergs', 'atop', 'wows', 'kain', 'wyte', 'negs', 'lady', 'yeas', 'buss', 'kefs', 'nogs', 'hall', 'birk', 'fays', 'judy', 'feet', 'hath', 'zouk', 'baas', 'glue', 'staw', 'weer', 'neif', 'pray', 'aero', 'tyes', 'task', 'tomb', 'ibis', 'sack', 'rush', 'rood', 'poke', 'nide', 'sari', 'faro', 'fibs', 'gilt', 'buoy', 'nosh', 'caws', 'fash', 'deaf', 'kafs', 'iris', 'late', 'rifs', 'flat', 'vees', 'slog', 'gees', 'ripe', 'bumf', 'step', 'keel', 'filo', 'nene', 'zaps', 'kerb', 'sook', 'sati', 'wags', 'went', 'veto', 'area', 'saul', 'tars', 'prom', 'exon', 'nets', 'flak', 'club', 'warp', 'bugs', 'ante', 'hair', 'cash', 'reef', 'sour', 'amah', 'polo', 'pine', 'repp', 'kune', 'rues', 'fain', 'mitt', 'tact', 'yips', 'bene', 'moan', 'drek', 'jake', 'hype', 'trio', 'peag', 'boas', 'blur', 'burd', 'wash', 'gulf', 'didy', 'tuba', 'floc', 'paps', 'snub', 'pane', 'sers', 'thou', 'drat', 'okes', 'worm', 'gala', 'cade', 'ulva', 'pony', 'guid', 'ryes', 'flub', 'roto', 'ogre', 'otic', 'balk', 'joes', 'gelt', 'geek', 'pyes', 'esne', 'upon', 'seta', 'yaps', 'blue', 'tsar', 'chia', 'bola', 'ride', 'enow', 'haws', 'mist', 'fore', 'sofa', 'sing', 'neem', 'rear', 'away', 'wise', 'kyte', 'gene', 'izar', 'ulus', 'gaud', 'romp', 'silo', 'skag', 'pale', 'laws', 'rang', 'wave', 'loaf', 'tuns', 'gite', 'gill', 'feme', 'sacs', 'mate', 'slue', 'sump', 'tahr', 'myna', 'yard', 'mixt', 'kaph', 'owed', 'kops', 'yaff', 'bree', 'hank', 'yule', 'hake', 'mopy', 'seem', 'palp', 'wons', 'duly', 'gyms', 'idol', 'spiv', 'dupe', 'toyo', 'half', 'koss', 'hili', 'wans', 'yays', 'hard', 'ball', 'opus', 'tier', 'skim', 'moll', 'gets', 'ilka', 'wear', 'hypo', 'pish', 'weds', 'gins', 'pall', 'nerd', 'swob', 'nite', 'yawl', 'roam', 'bels', 'banc', 'pope', 'duff', 'alow', 'wack', 'blog', 'soke', 'earl', 'bung', 'pegs', 'lost', 'fuss', 'wees', 'coup', 'mozo', 'flaw', 'hadj', 'hots', 'syph', 'snow', 'mars', 'soph', 'luke', 'fuze', 'urge', 'tels', 'clap', 'tees', 'game', 'idem', 'orle', 'hand', 'shmo', 'berg', 'zees', 'tech', 'suer', 'ears', 'cete', 'lash', 'birr', 'lynx', 'bath', 'mary', 'muso', 'team', 'rope', 'yuke', 'wall', 'spud', 'peck', 'poco', 'soma', 'hind', 'wimp', 'yodh', 'hove', 'come', 'sear', 'nubs', 'bust', 'lima', 'diol', 'yawp', 'curb', 'bred', 'grig', 'mobs', 'bump', 'watt', 'take', 'mans', 'puka', 'trip', 'lars', 'airt', 'free', 'atom', 'rins', 'peri', 'orra', 'harl', 'inks', 'taxi', 'emmy', 'typy', 'tell', 'dite', 'tics', 'yipe', 'blah', 'snag', 'flus', 'shed', 'pion', 'bent', 'gids', 'toit', 'sled', 'math', 'mots', 'tort', 'gave', 'weld', 'pint', 'ossa', 'coos', 'umbo', 'bone', 'dhow', 'dirl', 'join', 'rule', 'judo', 'surf', 'ogam', 'rime', 'deed', 'flog', 'goth', 'yird', 'sold', 'pams', 'limn', 'kyak', 'jefe', 'duci', 'deli', 'pail', 'dahl', 'coho', 'nobs', 'yore', 'ulna', 'weft', 'guns', 'yelk', 'logo', 'tepa', 'achy', 'sike', 'weir', 'sima', 'taos', 'info', 'corf', 'ides', 'mugs', 'raja', 'cyma', 'gits', 'agar', 'sugh', 'dorm', 'meow', 'rasp', 'abut', 'mara', 'husk', 'skeg', 'raze', 'prep', 'turf', 'samp', 'only', 'head', 'brin', 'glug', 'ends', 'nibs', 'oxer', 'peat', 'bomb', 'teat', 'tala', 'eggy', 'foxy', 'avow', 'pipe', 'scan', 'haed', 'pool', 'waff', 'able', 'will', 'slub', 'rank', 'zona', 'temp', 'pule', 'mack', 'lour', 'kelt', 'sial', 'gest', 'ahed', 'pome', 'cell', 'slob', 'cyme', 'cogs', 'fuji', 'duce', 'move', 'quip', 'hits', 'shot', 'togs', 'jinx', 'luau', 'dyes', 'tuck', 'tamp', 'bowl', 'yech', 'devs', 'tout', 'fall', 'rath', 'bott', 'push', 'xyst', 'jade', 'gast', 'secs', 'sash', 'tufa', 'zoom', 'gaby', 'wark', 'tied', 'tuff', 'fiar', 'knar', 'nurl', 'cage', 'slug', 'dung', 'phew', 'culm', 'rung', 'beau', 'coir', 'pain', 'mess', 'lowe', 'bean', 'sate', 'fete', 'chat', 'dows', 'hats', 'gain', 'naan', 'waes', 'abri', 'fury', 'ates', 'smug', 'kick', 'sods', 'bold', 'prof', 'noms', 'mung', 'flic', 'napa', 'neat', 'geed', 'haik', 'cast', 'loop', 'eggs', 'maar', 'alef', 'bins', 'faze', 'piki', 'eric', 'snog', 'loto', 'puce', 'scry', 'hyla', 'cart', 'grum', 'mice', 'rale', 'boos', 'leet', 'obol', 'wept', 'dyad', 'fabs', 'oven', 'base', 'deva', 'wolf', 'migs', 'sirs', 'mewl', 'agio', 'shea', 'maes', 'fend', 'cobb', 'tors', 'redd', 'purl', 'mity', 'wild', 'rack', 'oily', 'ires', 'egad', 'hewn', 'kiln', 'puke', 'womb', 'slip', 'hare', 'gies', 'berm', 'okas', 'dhak', 'axes', 'maps', 'sans', 'wits', 'tund', 'nipa', 'qats', 'reis', 'jack', 'oldy', 'naif', 'subs', 'jota', 'aver', 'gait', 'feod', 'kith', 'next', 'cozy', 'fact', 'lilt', 'goer', 'icky', 'chid', 'doux', 'tats', 'ruga', 'blip', 'clad', 'wost', 'gorp', 'amin', 'soms', 'haut', 'alma', 'fiat', 'mall', 'sols', 'bads', 'size', 'felt', 'ados', 'lute', 'plot', 'hams', 'lush', 'slit', 'genu', 'ulan', 'emic', 'cuif', 'rend', 'bias', 'veal', 'ritz', 'hero', 'rain', 'near', 'doth', 'bibs', 'obes', 'urea', 'ants', 'heal', 'gams', 'lard', 'zoos', 'sera', 'jell', 'mony', 'yous', 'tyin', 'wyes', 'gone', 'fads', 'loon', 'meld', 'haku', 'vole', 'gore', 'cows', 'atap', 'core', 'ayes', 'dont', 'boor', 'rote', 'naik', 'proa', 'lakh', 'tyee', 'lure', 'pole', 'herl', 'fest', 'quit', 'cate', 'opes', 'euro', 'folk', 'tyer', 'olid', 'grew', 'kors', 'nori', 'sidh', 'ices', 'duds', 'chaw', 'done', 'opts', 'swum', 'mini', 'ruin', 'yang', 'dies', 'sibs', 'celt', 'tube', 'gray', 'dada', 'buns', 'hews', 'mano', 'paul', 'gibs', 'farm', 'tads', 'foam', 'toll', 'pima', 'howe', 'trug', 'dews', 'cess', 'bard', 'mort', 'sard', 'keta', 'bros', 'dust', 'oats', 'caky', 'wast', 'pupa', 'dels', 'cere', 'kegs', 'agee', 'dune', 'cuds', 'neon', 'awry', 'jigs', 'kibe', 'eath', 'qadi', 'pity', 'gamp', 'sone', 'tans', 'goas', 'lamb', 'yews', 'gaol', 'sips', 'snob', 'ness', 'vena', 'wyns', 'rede', 'elms', 'udos', 'cane', 'pout', 'jouk', 'ions', 'baff', 'zeks', 'prey', 'this', 'ogle', 'sewn', 'rube', 'plea', 'kays', 'pfui', 'guvs', 'dozy', 'recs', 'blet', 'leke', 'wink', 'rocs', 'mail', 'scar', 'wipe', 'lugs', 'mosk', 'good', 'byrl', 'mako', 'sorb', 'pong', 'duke', 'sees', 'stew', 'digs', 'nips', 'oast', 'nala', 'dark', 'eras', 'cred', 'geds', 'also', 'dojo', 'cosy', 'hens', 'slop', 'taco', 'copy', 'mote', 'emyd', 'tele', 'bise', 'jean', 'suns', 'resh', 'gyri', 'keps', 'soul', 'john', 'flux', 'whig', 'lain', 'kudu', 'toke', 'imam', 'heat', 'teel', 'brat', 'rani', 'aces', 'ache', 'edit', 'reel', 'abbe', 'fief', 'dona', 'mair', 'flam', 'ghee', 'sexy', 'rail', 'tote', 'guck', 'hack', 'waur', 'epha', 'honk', 'ones', 'hays', 'auto', 'ally', 'noel', 'wage', 'hied', 'dubs', 'film', 'dump', 'mumu', 'fido', 'rugs', 'lilo', 'pood', 'smit', 'teen', 'dure', 'wych', 'kaka', 'haps', 'roof', 'ordo', 'gate', 'nope', 'diva', 'cors', 'miss', 'delf', 'gals', 'lino', 'hook', 'rays', 'eked', 'dime', 'male', 'dahs', 'prez', 'hins', 'peek', 'sabe', 'fehs', 'crus', 'ruff', 'stoa', 'wain', 'suks', 'pawn', 'fila', 'jato', 'gods', 'wary', 'okra', 'rind', 'spay', 'bams', 'rate', 'anna', 'sibb', 'ouch', 'frog', 'segs', 'prop', 'guru', 'cepe', 'rebs', 'moxa', 'khan', 'cyst', 'wavy', 'expo', 'cusp', 'mold', 'sots', 'feed', 'hint', 'skit', 'weed', 'fugs', 'bort', 'gied', 'irid', 'shri', 'hock', 'kant', 'part', 'poxy', 'lari', 'keys', 'koas', 'sims', 'coop', 'dine', 'alga', 'vote', 'orcs', 'whit', 'gong', 'muni', 'owse', 'lich', 'clod', 'flit', 'swam', 'hums', 'zags', 'jilt', 'deft', 'pulp', 'imps', 'chai', 'rode', 'jill', 'bids', 'tule', 'sola', 'curf', 'mope', 'iglu', 'lean', 'dols', 'gums', 'sway', 'darb', 'elds', 'khaf', 'roan', 'hull', 'jeux', 'supe', 'liny', 'gran', 'ager', 'eide', 'bode', 'boon', 'airy', 'town', 'naff', 'load', 'nape']
word="dols"
first=1
# 組成字母必須不同
for Alice in alice:
    if (Alice[0]==Alice[2] or Alice[0]==Alice[1] or Alice[0]==Alice[3] or Alice[1]==Alice[2] or Alice[1]==Alice[3] or Alice[2]==Alice[3]):
        alice.remove(Alice)
for Alice in alice:
    if (Alice[0]==Alice[2] or Alice[0]==Alice[1] or Alice[0]==Alice[3] or Alice[1]==Alice[2] or Alice[1]==Alice[3] or Alice[2]==Alice[3]):
        alice.remove(Alice)
for Bob in bob:
    if (Bob[0]==Bob[1] or Bob[0]==Bob[2] or Bob[0]==Bob[3] or Bob[1]==Bob[2] or Bob[1]==Bob[3] or Bob[2]==Bob[3]):
        bob.remove(Bob)
for Bob in bob:
    if (Bob[0]==Bob[1] or Bob[0]==Bob[2] or Bob[0]==Bob[3] or Bob[1]==Bob[2] or Bob[1]==Bob[3] or Bob[2]==Bob[3]):
        bob.remove(Bob)
# 不可跟題目重複
if word in alice:
    alice.remove(word)
if word in bob:
    bob.remove(word)
# 切換first=0變數為who,s turn
if str(first)=="0":
    first="0"
    next="Alice_turn"
elif str(first)=="1":
    first="1"
    next="Bob_turn"
# 回合數及迴圈停止變數
round=0
while_stop="start"
while while_stop!="Finish":
    round=round+1
    str_round=str(round)
    if next=="Alice_turn" or next=="Bob_miss":
        for Alice in alice:
            alice_saperate=list(combinations(Alice,3))
            word_saperate=list(combinations(word,3))
            if first=="1" and next=="Bob_miss" and str_round=="2":
                if (alice_saperate[0]==word_saperate[0] or alice_saperate[1]==word_saperate[1] or alice_saperate[2]==word_saperate[2] or alice_saperate[3]==word_saperate[3]):
                    print(0)
                    while_stop="Finish"
                    break
                elif Alice==alice[-1] and (alice_saperate[0]!=word_saperate[0] or alice_saperate[1]!=word_saperate[1] or alice_saperate[2]!=word_saperate[2] or alice_saperate[3]!=word_saperate[3]):
                    print(-1)
                    while_stop="Finish"
                    break
            if first=="0" and next=="Alice_turn" and str_round=="1" and Alice==alice[-1] and (alice_saperate[0]!=word_saperate[0] or alice_saperate[1]!=word_saperate[1] or alice_saperate[2]!=word_saperate[2] or alice_saperate[3]!=word_saperate[3]):
                    next="Alice_miss"
                    break
            if next=="Alice_turn":
                if (alice_saperate[0]==word_saperate[0] or alice_saperate[1]==word_saperate[1] or alice_saperate[2]==word_saperate[2] or alice_saperate[3]==word_saperate[3]):
                    next="Bob_turn"
                    word=Alice
                    alice.remove(Alice)
                    if Alice in bob:
                        bob.remove(Alice)
                    break
                elif Alice==alice[-1] and (alice_saperate[0]!=word_saperate[0] or alice_saperate[1]!=word_saperate[1] or alice_saperate[2]!=word_saperate[2] or alice_saperate[3]!=word_saperate[3]):
                    print(1)
                    while_stop="Finish"
                    break
    if next=="Bob_turn" or next=="Alice_miss":
        for Bob in bob:
            bob_saperate=list(combinations(Bob,3))
            word_saperate=list(combinations(word,3))       
            if first=="0" and next=="Alice_miss" and str_round=="1":
                if (bob_saperate[0]==word_saperate[0] or bob_saperate[1]==word_saperate[1] or bob_saperate[2]==word_saperate[2] or bob_saperate[3]==word_saperate[3]):
                    print(1)
                    while_stop="Finish"
                    break
                elif Bob==bob[-1] and (bob_saperate[0]!=word_saperate[0] or bob_saperate[1]!=word_saperate[1] or bob_saperate[2]!=word_saperate[2] or bob_saperate[3]!=word_saperate[3]):
                    print(-1)
                    while_stop="Finish" 
                    break
            if first=="1" and next=="Bob_turn" and str_round=="1" and Bob==bob[-1] and (bob_saperate[0]!=word_saperate[0] or bob_saperate[1]!=word_saperate[1] or bob_saperate[2]!=word_saperate[2] or bob_saperate[3]!=word_saperate[3]):
                next="Bob_miss"
                break
            if next=="Bob_turn":
                if (bob_saperate[0]==word_saperate[0] or bob_saperate[1]==word_saperate[1] or bob_saperate[2]==word_saperate[2] or bob_saperate[3]==word_saperate[3]):
                    next="Alice_turn"
                    word=Bob
                    bob.remove(Bob)
                    if Bob in alice:
                        alice.remove(Bob)
                    break
                elif Bob==bob[-1] and (bob_saperate[0]!=word_saperate[0] or bob_saperate[1]!=word_saperate[1] or bob_saperate[2]!=word_saperate[2] or bob_saperate[3]!=word_saperate[3]):
                    print(0)
                    while_stop="Finish" 
                    break
