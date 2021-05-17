

# Basic techniques
Kihonwaza = (
			'Abisetaoshi',
			'Oshidashi',
			'Oshitaoshi',
			'Tsukidashi',
			'Tsukitaoshi',
			'Yorikiri',
			'Yoritaoshi'
			)


# Throwing techniques
Nagete = (
		'Ipponzeoi',
		'Kakenage',
		'Koshinage',
		'Kotenage',
		'Kubinage',
		'Nichonage',
		'Shitatedashinage',
		'Shitatenage',
		'Sukuinage',
		'Tsukaminage',
		'Uwatedashinage',
		'Uwatenage',
		'Yaguranage'
		)


# Leg tripping techniques
Kakete = (
		'Ashitori',
		'Chongake',
		'Kawazugake',
		'Kekaeshi',
		'Ketaguri',
		'Kirikaeshi',
		'Komatasukui',
		'Kozumatori',
		'Mitokorozeme',
		'Nimaigeri',
		'Omata',
		'Sotogake',
		'Sotokomata',
		'Susoharai',
		'Susotori',
		'Tsumatori',
		'Uchigake',
		'Watashikomi'
		)


# Twist down techniques
Hinerite = (
			'Amiuchi',
			'Gasshohineri',
			'Harimanage',
			'Kainahineri',
			'Katasukashi',
			'Kotehineri',
			'Kubihineri',
			'Makiotoshi',
			'Osakate',
			'Sabaori',
			'Sakatottari',
			'Shitatehineri',
			'Sotomuso',
			'Tokkurinage',
			'Tottari',
			'Tsukiotoshi',
			'Uchimuso',
			'Uwatehineri',
			'Zubuneri'
			)


# Backwards body drop
Sorite = (
		'Izori',
		'Kakezori',
		'Shumokuzori',
		'Sototasukizori',
		'Tasukizori',
		'Tsutaezori'
		)


# Special techniques
Tokushuwaza = (
				'Hatakikomi',
				'Hikiotoshi',
				'Hikkake',
				'Kimedashi',
				'Kimetaoshi',
				'Okuridashi',
				'Okurigake',
				'Okurihikiotoshi',
				'Okurinage',
				'Okuritaoshi',
				'Okuritsuridashi',
				'Okuritsuriotoshi',
				'Sokubiotoshi',
				'Tsuridashi',
				'Tsuriotoshi',
				'Ushiromotare',
				'Utchari',
				'Waridashi',
				'Yobimodoshi'
			)


# Non-techniques
Higi = (
	'Fumidashi',
	'Isamiashi',
	'Koshikudake',
	'Tsukihiza',
	'Tsukite',
	)


Others = (
	'Fusen',
	'Hansoku'
	)



classes = 	{
				'Kihonwaza: Basic technique': Kihonwaza,
				'Nagete: Throwing technique': Nagete,
				'Kakete: Leg tripping technique': Kakete,
				'Hinerite: Twist down technique': Hinerite,
				'Sorite: Backwards body drop': Sorite,
				'Tokushuwaza: Special technique': Tokushuwaza,
				'Higi: Non-technique': Higi,
				'Others': Others
			}



# get the class for a certain kimarite
def classify(kimarite):
	kimarite = kimarite.lower().capitalize()
	for class_ in classes.keys():
		if kimarite in classes[class_]:
			return class_


def is_oshi(kimarite):
	kimarite = kimarite.lower().capitalize()
	return kimarite in ('Oshidashi', 'Hatakikomi', 'Tsukidashi', 'Tsukiotoshi', 'Oshitaoshi', 'Waridashi', 'Okurdashi')
