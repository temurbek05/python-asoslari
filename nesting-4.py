countries = {
    'USA': {
        'capital': 'Washington, D.C.',
        'population': 331002651,
        'official_language': 'English',
        'currency': 'United States Dollar (USD)'
    },
    'India': {
        'capital': 'New Delhi',
        'population': 1380004385,
        'official_language': 'Hindi, English',
        'currency': 'Indian Rupee (INR)'
    },
    'China': {
        'capital': 'Beijing',
        'population': 1444216107,
        'official_language': 'Mandarin',
        'currency': 'Renminbi (CNY)'
    },
    'Brazil': {
        'capital': 'Brasília',
        'population': 212559417,
        'official_language': 'Portuguese',
        'currency': 'Brazilian Real (BRL)'
    }
}
for country, info in countries.items():
    print(f"The capital of {country} is {info['capital']}, {info['population']} people live in it,  ",
          f"they speak {info['official_language']}")
    
    #f"The capital of {country} is {info['capital']}, {info['population']} live in it,  ",
       #   f"they speak {info['official_language']}
#print(countries.items())
    
    