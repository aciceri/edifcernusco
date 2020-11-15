from datetime import date
from os import environ
from inspect import cleandoc
from itertools import chain
from functools import reduce

assets_path = 'assets'
generated_path = '_dist'
images_path = 'images'
houses_path = 'houses.yaml'
img_width = 1000
who = cleandoc('''
La Cooperativa Edificatrice Cernuschese “Bruno Ciceri” è una società a responsabilità limitata “senza scopo di lucro”. Questa scelta statutaria ci consente di essere presente sul mercato immobiliare di Cernusco sul Naviglio con la prerogativa di riuscire a consegnare ai soci appartamenti a prezzi calmierati. La nostra ormai decennale esperienza in questo settore (il Consiglio di Amministrazione è composto quasi esclusivamente di pensionati volontari) continua a soddisfare le esigenze di giovani coppie che vogliono continuare a risiedere a Cernusco o di chi vuole una nuova casa per esigenze familiari.
''')
history = cleandoc('''
La Cooperativa ha una lunga storia alle spalle. Il primo consiglio di Amministrazione rogitava la fondazione il 2 agosto 1908 e da allora la società ha perseguito diverse funzioni passando da punto di riferimento delle prime associazioni socialiste/democratiche fino all’avvento del regime fascista che trasformò la sede in sala cinematografica. All’indomani della Liberazione si diede vita ad un CRAL, ad una cooperativa di consumo e a varie attività culturali (cinema, sala da ballo, bar e sedi di partito).
''')
commitment = cleandoc('''
Alla fine degli anni Ottanta l’Edificatrice Cernuschese attuava per la prima volta un altro dei mandati statutari e iniziava a costruire case iniziando a ristrutturare la sede di via Balconi e proseguendo con la costruzione in via Penati 2, in via Ada Negri, in via Boccccio 6, in via De Amicis e in via Monza 132. Oggi (gennaio 2019) è aperto un nuovo cantiere in via Monza. Nell’attuale sede hanno ospitalità varie sedi di partiti di Cernusco e un salone a disposizione di varie associazioni culturali e organizzazioni no-profit.
''')
realizations = cleandoc('''
Le seguenti sono solo alcune delle nostre realizzazioni.
''')
address = cleandoc('''
Cooperativa Edificatrice Cernuschese "Bruno Ciceri"</br>
Via Fatebenefratelli, 9</br>
Cernusco sul Naviglio
''')
email = 'coop.edif.cern@tiscali.it'
facebook_page = 'https://fb.me/cineforumlunik'
telephone = '(+39) 02 49 433 102 (segreteria telefonica)'
contacts = cleandoc(f"""
La sede della Cooperativa è aperta tutti i Martedì dalle 21:00 alle 23:00, è possibile contattarci telefonicamente in tale orario. Per qualsiasi informazione non esitate a contattarci per e-mail o tramite il modulo presente su questo sito.
""")
footer = cleandoc("""
<ul class="copyright">
  <li>© Cooperativa Edificatrice Cernuschese "Bruno Ciceri" All rights reserved.</li>
  <li><a href="privacy-policy.txt">Informativa sulla privacy</a></li>
  <li>Design: <a href="http://html5up.net">HTML5 UP</a></li></ul>
""")

houses = {
    'VIA DE AMICIS': ['amicis1.jpg', 'amicis2.jpg', 'amicis3.jpg', 'amicis4.jpg'],
    'VIA ADA NEGRI': ['negri.jpg'],
    'VIA PENATI': ['penati.jpg']
} 


values = {'gmaps_place_id': 'ChIJ3b1qkdK3hkcRe7llxcKzCvM',
          'gmaps_key': environ['GMAPS_KEY'],
          'who': who,
          'history': history,
          'commitment': commitment,
          'realizations': realizations,
          'address': address,
          'email': email,
          'facebook_page': facebook_page,
          'telephone': telephone,
          'houses':  [(list(filter(lambda kv: url in kv[1], houses.items()))[0][0], url) for url in reduce(chain, houses.values())],
          'contacts': contacts,
          'footer': footer}
