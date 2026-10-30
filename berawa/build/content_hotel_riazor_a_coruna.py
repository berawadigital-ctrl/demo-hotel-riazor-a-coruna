# Contenido de la demo Hotel Riazor (A Coruña) (es/en/fr/de). Hechos de riazorhotel.com leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächlichen Zimmer.'}
H={'es':['Doble estándar vistas al mar','Doble con terraza','Junior suite','Suite','Familiar','Triple'],
'en':['Standard double, sea view','Double with terrace','Junior suite','Suite','Family room','Triple'],
'fr':['Double standard vue mer','Double avec terrasse','Junior suite','Suite','Familiale','Triple'],
'de':['Standard-Doppelzimmer Meerblick','Doppelzimmer mit Terrasse','Junior Suite','Suite','Familienzimmer','Dreibettzimmer']}
RD={
'es':['20–25 m² con ventanas de gran formato a la Ensenada de Riazor, cama doble o dos camas.','25–30 m² más terraza en la planta 11 o 12, con vistas a la Ensenada de Riazor y cama de 150 cm.','38 m² con vistas al mar y dos ambientes, para 2 adultos y 1 niño (sofá cama).','50 m² con salón, zona de estar con vistas al mar y dos baños.','35–40 m² con dos ambientes, para 2 adultos y 2 niños; las hay con vistas al mar e interiores.','30–35 m² para 3 personas: dos camas individuales más supletoria.'],
'en':['20–25 m² with large windows onto the Riazor bay, double bed or twin beds.','25–30 m² plus a terrace on the 11th or 12th floor, overlooking the Riazor bay, with a 150 cm bed.','38 m² with sea views and two areas, for 2 adults and 1 child (sofa bed).','50 m² with a lounge, a sitting area with sea views and two bathrooms.','35–40 m² with two areas, for 2 adults and 2 children; sea-view and interior options.','30–35 m² for 3 people: two single beds plus an extra bed.'],
'fr':['20–25 m² avec de grandes fenêtres sur la baie de Riazor, lit double ou deux lits.','25–30 m² plus terrasse au 11e ou 12e étage, vue sur la baie de Riazor, lit de 150 cm.','38 m² avec vue sur la mer et deux espaces, pour 2 adultes et 1 enfant (canapé-lit).','50 m² avec salon, coin séjour vue mer et deux salles de bain.','35–40 m² avec deux espaces, pour 2 adultes et 2 enfants ; vue mer ou intérieures.','30–35 m² pour 3 personnes : deux lits simples plus un lit d\'appoint.'],
'de':['20–25 m² mit großen Fenstern zur Bucht von Riazor, Doppelbett oder zwei Einzelbetten.','25–30 m² plus Terrasse im 11. oder 12. Stock, mit Blick auf die Bucht von Riazor und 150-cm-Bett.','38 m² mit Meerblick und zwei Bereichen, für 2 Erwachsene und 1 Kind (Schlafsofa).','50 m² mit Salon, Sitzbereich mit Meerblick und zwei Bädern.','35–40 m² mit zwei Bereichen, für 2 Erwachsene und 2 Kinder; mit Meerblick oder innen.','30–35 m² für 3 Personen: zwei Einzelbetten plus Zustellbett.']}
ART={
'hero':('waves',9301,['#1e4a63','#edbd83','#f6deb5','#2f6683','#1e4a63','#123246']),
'intro':('skyline',9302,['#1e4a63','#e7a568','#f5d5a3','#2c4a3e','#233e33','#162a22']),
'r1':('waves',9311,['#245772','#ebba80','#f4dcb2','#3a7391','#245772','#153a50']),
'r2':('skyline',9312,['#1e4a63','#e3a266','#f4d29f','#2a483c','#213b31','#152820']),
'r3':('columns',9313,['#ecebe6','#f8f6f1','#8f5a2a','#1e4a63','#123246']),
'r4':('arches',9314,['#efe6d6','#dfb07c','#9a5a28','#1e4a63','#123246']),
'r5':('hills',9315,['#e4ebe6','#efe7d2','#e6b677','#9fb7a6','#6f8f80','#46695d']),
'r6':('columns',9316,['#edeae2','#f7f4ee','#a5652f','#1e4a63','#123246']),
'g1':('waves',9321,['#1e4a63','#edbd83','#f6deb5','#3c6a86','#1e4a63','#123246']),
'g2':('skyline',9322,['#2f5a73','#e0a868','#f3d6a6','#1e4a63','#1b3446','#112333']),
'g3':('hills',9323,['#e3eae2','#eee6ce','#eab875','#a4ba9a','#78977e','#4f7059']),
'g4':('arches',9324,['#ece3d2','#dcab76','#9e5a26','#1e4a63','#123246'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3','r4','r5','r6'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Riazor · Hotel de 4 estrellas en la playa de Riazor, A Coruña',see_rooms='Ver las habitaciones',hero_k='A Coruña · Playa de Riazor',hero_t='En primera línea de la playa de Riazor',hero_s='Hotel boutique de 4 estrellas completamente renovado, con vistas al Atlántico.',
 intro_t='Una ventana al mar en pleno corazón de A Coruña',intro_p1='Edificio totalmente reformado, con suelos de madera, habitaciones amplias y techos altos, y un restaurante con producto de proximidad y cocina gallega.',
 intro_p2='Cancelación sin cargo hasta 24 horas antes de la llegada y late checkout hasta las 14:00 bajo disponibilidad, solicitándolo en recepción.',
 stats=['4 estrellas','Primera línea de playa','Recepción 24 h','Gimnasio 24 h'],nav_rooms='Habitaciones',rooms_t='Nuestras habitaciones',rooms_s='Seis de sus tipos de habitación; también hay doble estándar interior y doble adaptada.',
 svcs=['Carta de almohadas','Recepción 24 horas multilingüe','Consigna de equipajes','Restaurante Cícero y cafetería','Salones para eventos','WiFi GPON'],
 around_s='La playa de Riazor, el paseo marítimo de 12 km y la Torre de Hércules; estación de tren a 2 km y aeropuerto a 15 km.',
 loc_p='Avda. Pedro Barrie de la Maza, 29 · 15004 A Coruña, en primera línea de la playa de Riazor.',
 chips=['¿Qué habitaciones tenéis?','¿Hay habitación familiar?','¿A qué hora es el desayuno?','¿Admitís mascotas?']),
'en':dict(title='Hotel Riazor · 4-star hotel on Riazor beach, A Coruña',see_rooms='See the rooms',hero_k='A Coruña · Riazor beach',hero_t='Right on Riazor beach',hero_s='Fully renovated 4-star boutique hotel with views of the Atlantic.',
 intro_t='A window onto the sea in the heart of A Coruña',intro_p1='A completely refurbished building with wooden floors, spacious rooms and high ceilings, and a restaurant with local produce and Galician cuisine.',
 intro_p2='Free cancellation up to 24 hours before arrival and late check-out until 14:00 subject to availability, on request at reception.',
 stats=['4 stars','Beachfront','24 h reception','24 h gym'],nav_rooms='Rooms',rooms_t='Our rooms',rooms_s='Six of their room types; there are also interior standard doubles and adapted doubles.',
 svcs=['Pillow menu','24-hour multilingual reception','Luggage storage','Cícero restaurant and cafeteria','Event rooms','GPON WiFi'],
 around_s='Riazor beach, the 12 km seafront promenade and the Tower of Hercules; train station 2 km away and airport 15 km.',
 loc_p='Avda. Pedro Barrie de la Maza, 29 · 15004 A Coruña, right on Riazor beach.',
 chips=['Which rooms do you have?','Is there a family room?','What time is breakfast?','Are pets allowed?']),
'fr':dict(title='Hotel Riazor · Hôtel 4 étoiles sur la plage de Riazor, La Corogne',see_rooms='Voir les chambres',hero_k='La Corogne · Plage de Riazor',hero_t='Face à la plage de Riazor',hero_s='Hôtel boutique 4 étoiles entièrement rénové, avec vue sur l\'Atlantique.',
 intro_t='Une fenêtre sur la mer au cœur de La Corogne',intro_p1='Un bâtiment entièrement rénové, parquet, chambres spacieuses et hauts plafonds, et un restaurant de produits locaux et de cuisine galicienne.',
 intro_p2='Annulation sans frais jusqu\'à 24 heures avant l\'arrivée et départ tardif jusqu\'à 14h00 selon disponibilité, sur demande à la réception.',
 stats=['4 étoiles','Face à la plage','Réception 24 h/24','Salle de sport 24 h/24'],nav_rooms='Chambres',rooms_t='Nos chambres',rooms_s='Six de leurs types de chambre ; il existe aussi des doubles standard intérieures et des doubles adaptées.',
 svcs=['Carte d\'oreillers','Réception multilingue 24 h/24','Bagagerie','Restaurant Cícero et cafétéria','Salles pour événements','WiFi GPON'],
 around_s='La plage de Riazor, la promenade maritime de 12 km et la tour d\'Hercule ; gare à 2 km et aéroport à 15 km.',
 loc_p='Avda. Pedro Barrie de la Maza, 29 · 15004 La Corogne, face à la plage de Riazor.',
 chips=['Quelles chambres avez-vous ?','Y a-t-il une chambre familiale ?','À quelle heure est le petit-déjeuner ?','Les animaux sont-ils admis ?']),
'de':dict(title='Hotel Riazor · 4-Sterne-Hotel am Strand von Riazor, A Coruña',see_rooms='Zimmer ansehen',hero_k='A Coruña · Strand von Riazor',hero_t='Direkt am Strand von Riazor',hero_s='Komplett renoviertes 4-Sterne-Boutiquehotel mit Blick auf den Atlantik.',
 intro_t='Ein Fenster zum Meer im Herzen von A Coruña',intro_p1='Ein vollständig renoviertes Gebäude mit Holzböden, großzügigen Zimmern und hohen Decken sowie ein Restaurant mit regionalen Produkten und galicischer Küche.',
 intro_p2='Kostenlose Stornierung bis 24 Stunden vor Anreise und später Check-out bis 14:00 Uhr nach Verfügbarkeit, auf Anfrage an der Rezeption.',
 stats=['4 Sterne','Direkt am Strand','Rezeption 24 h','Fitnessraum 24 h'],nav_rooms='Zimmer',rooms_t='Unsere Zimmer',rooms_s='Sechs ihrer Zimmertypen; außerdem gibt es Standard-Doppelzimmer innen und barrierefreie Doppelzimmer.',
 svcs=['Kissenmenü','Mehrsprachige Rezeption rund um die Uhr','Gepäckaufbewahrung','Restaurant Cícero und Cafeteria','Veranstaltungsräume','GPON-WLAN'],
 around_s='Der Strand von Riazor, die 12 km lange Strandpromenade und der Herkulesturm; Bahnhof 2 km, Flughafen 15 km entfernt.',
 loc_p='Avda. Pedro Barrie de la Maza, 29 · 15004 A Coruña, direkt am Strand von Riazor.',
 chips=['Welche Zimmer gibt es?','Gibt es ein Familienzimmer?','Wann gibt es Frühstück?','Sind Haustiere erlaubt?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RES='https://www.riazorhotel.com/es/onetbooking/request'; RES_EN='https://www.riazorhotel.com/en/onetbooking/request'
BOOK=dict(mode='engine',url={'es':RES,'en':RES_EN,'fr':RES_EN,'de':RES_EN})
D=dict(name='Hotel Riazor',ac='#1e4a63',ac2='#9a5a28',ac2_a11y='#6d4a17',book=BOOK,around=['Playa de Riazor','Torre de Hércules'],foot=FOOT,
 address='Avda. Pedro Barrie de la Maza, 29 · 15004 A Coruña',phones=['+34 981 253 400'],emails=['reservas@riazorhotel.com'],maps='Hotel Riazor, Avenida Pedro Barrie de la Maza 29, A Coruña',t=T)
META=dict(repo='demo-hotel-riazor-a-coruna',name='Hotel Riazor',legal_name='ABELURIA HOTELES S.L.',registry_ids=['NIF B70555495','RM A Coruña hoja C-57540'],
 url='https://www.riazorhotel.com/',domain='riazorhotel.com',municipality='A Coruña',province='A Coruña',sector='hotel boutique de 4 estrellas en primera línea de la playa de Riazor',
 read_at='2026-10-30T06:51:00+01:00',created_at='2026-10-30T06:50:30+01:00',built_at='2026-10-30T07:00:00+01:00',audit_date='2026-10-30T06:46:10+01:00',
 rating=dict(value=4.3,coincide=['telefono','web'],date='2026-10-29T10:59:20+01:00',url='https://www.google.com/maps/place/Hotel+Riazor/@43.3683538,-8.4090757,17z/data=!4m9!3m8!1s0xd2e7c62e62a34f3:0xc58783e46a6d097!5m2!4m1!1i2!8m2!3d43.3683538!4d-8.4090757!16s%2Fg%2F1ywqfz7rt'),
 book=dict(mode='engine',url=RES,note='motor de reservas real de su web (onetbooking), HTTP 200 comprobado el 30/10/2026 en es y en.'),first_of_type=None)
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Hay habitación familiar?','K02'),('¿A qué hora es el desayuno?','K03'),('¿Admitís mascotas?','K04'),('¿Puedo cancelar?','K05'),('¿Puedo salir más tarde?','K06'),('¿Hay gimnasio?','K07'),('¿Hay parking?','K08'),('¿Dónde está el hotel?','K09'),('¿Cómo reservo?','K10'),('¿Podéis confirmarme disponibilidad para mañana?','K10'),('¿Cuánto cuesta una noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('Is there a family room?','K02'),('What time is breakfast?','K03'),('Are pets allowed?','K04'),('Can I cancel?','K05'),('Can I have a late check-out?','K06'),('Is there a gym?','K07'),('Is there parking?','K08'),('Where is the hotel?','K09'),('How do I book?','K10'),('Can you confirm availability for tomorrow?','K10'),('How much is a night?',None),('Do you have a swimming pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Y a-t-il une chambre familiale ?','K02'),('À quelle heure est le petit-déjeuner ?','K03'),('Les animaux sont-ils admis ?','K04'),('Puis-je annuler ?','K05'),('Puis-je faire un départ tardif ?','K06'),('Y a-t-il une salle de sport ?','K07'),('Y a-t-il un parking ?','K08'),('Où se trouve l\'hôtel ?','K09'),('Comment réserver ?','K10'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K10'),('Combien coûte une nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Gibt es ein Familienzimmer?','K02'),('Wann gibt es Frühstück?','K03'),('Sind Haustiere erlaubt?','K04'),('Kann ich stornieren?','K05'),('Ist ein später Check-out möglich?','K06'),('Gibt es einen Fitnessraum?','K07'),('Gibt es einen Parkplatz?','K08'),('Wo liegt das Hotel?','K09'),('Wie kann ich buchen?','K10'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K10'),('Was kostet eine Übernachtung?',None),('Haben Sie ein Schwimmbad?',None)]}
