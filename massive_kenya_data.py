"""
massive_kenya_data.py
Comprehensive Kenya travel knowledge base with 200+ documents.

Run: python massive_kenya_data.py
"""

from vector_store import add_documents_simple, get_document_count, clear_knowledge_base

# ══════════════════════════════════════════════════════════════════════════════
# MASSIVE KENYA TRAVEL KNOWLEDGE BASE - 200+ Documents
# ══════════════════════════════════════════════════════════════════════════════

MASSIVE_KENYA_DATA = [
    
    # ═══════════════════════════════════════════════════════════════════════════
    # MASAI MARA - Comprehensive Coverage (15 documents)
    # ═══════════════════════════════════════════════════════════════════════════
    
    {"content": "Masai Mara National Reserve is Kenya's most famous safari destination, located in Narok County in southwestern Kenya. It covers 1,510 square kilometers (580 sq mi) of savanna grassland along the Tanzanian border, forming part of the larger Mara-Serengeti ecosystem. The reserve is named after the Maasai people and the Mara River.", "source": "kws.go.ke", "category": "safari", "region": "Rift Valley", "destination": "Masai Mara"},
    
    {"content": "Masai Mara entry fees for 2024-2025: Non-resident adults $80 USD per day, non-resident children (under 12) $45 USD per day. East African residents pay 1,200 KES for adults and 600 KES for children. Kenya citizens pay 1,000 KES for adults and 500 KES for children. Vehicle entry fees: 400 KES for saloon cars, 1,000 KES for minibuses.", "source": "kws.go.ke", "category": "safari", "region": "Rift Valley", "destination": "Masai Mara"},
    
    {"content": "The Great Wildebeest Migration is the world's largest terrestrial animal migration. Between July and October, approximately 1.5 million wildebeest, 400,000 zebras, and 200,000 gazelles migrate from Tanzania's Serengeti to Kenya's Masai Mara following the rains and fresh grass. The migration is driven by rainfall patterns.", "source": "kws.go.ke", "category": "safari", "region": "Rift Valley", "destination": "Masai Mara"},
    
    {"content": "Mara River crossings are the most dramatic part of the wildebeest migration. Crocodiles up to 5 meters long wait in the murky waters. Thousands of wildebeest drown each year during crossings, their bodies feeding crocodiles and vultures. Best viewing spots include Lookout Hill and specific crossing points along the river.", "source": "magicalkenya.com", "category": "safari", "region": "Rift Valley", "destination": "Masai Mara"},
    
    {"content": "Masai Mara has the highest density of lions in Africa, with approximately 850-900 lions. Famous lion prides include the Marsh Pride (featured in Big Cat Diary), Paradise Pride, and Bila Shaka Pride. The Mara is also excellent for seeing leopards, cheetahs, elephants, buffalos, and hyenas.", "source": "kws.go.ke", "category": "safari", "region": "Rift Valley", "destination": "Masai Mara"},
    
    {"content": "Hot air balloon safaris over the Masai Mara offer a unique perspective. Flights depart at dawn (around 6:00 AM), last 1-1.5 hours, and include a champagne bush breakfast. Cost: $450-550 USD per person. Operators include Governor's Balloon Safaris and Skyship Balloon Safaris. Book at least 24 hours in advance.", "source": "magicalkenya.com", "category": "safari", "region": "Rift Valley", "destination": "Masai Mara"},
    
    {"content": "Masai Mara accommodation ranges from budget camping ($30/night) to ultra-luxury lodges ($2,000+/night). Popular luxury camps: Angama Mara, Governors' Camp, &Beyond Bateleur Camp, Mara Plains Camp. Mid-range options: Mara Serena Safari Lodge, Keekorok Lodge, Sarova Mara Game Camp. Budget: public campsites and basic tented camps.", "source": "magicalkenya.com", "category": "safari", "region": "Rift Valley", "destination": "Masai Mara"},
    
    {"content": "Getting to Masai Mara: By road from Nairobi takes 5-6 hours (270 km) via Narok. The road is tarmac until Narok, then murram (dirt). By air: daily flights from Nairobi's Wilson Airport take 45 minutes. Airlines: Safarilink, AirKenya, Mombasa Air Safari. Multiple airstrips: Mara Serena, Keekorok, Ol Kiombo, Musiara.", "source": "magicalkenya.com", "category": "safari", "region": "Rift Valley", "destination": "Masai Mara"},
    
    {"content": "Best time to visit Masai Mara: July-October for the wildebeest migration, especially August-September for river crossings. January-February offers excellent wildlife viewing with fewer tourists and calving season in nearby Serengeti. November and April-May are rainy seasons with fewer visitors and lower rates.", "source": "magicalkenya.com", "category": "safari", "region": "Rift Valley", "destination": "Masai Mara"},
    
    {"content": "Masai Mara game drives: Morning drives start at 6:00 AM when predators are most active. Afternoon drives depart around 4:00 PM and end at sunset (6:30 PM). Night drives are available in the Mara Conservancies outside the main reserve. Full-day drives with packed lunch allow exploration of distant areas.", "source": "kws.go.ke", "category": "safari", "region": "Rift Valley", "destination": "Masai Mara"},
    
    {"content": "Mara Conservancies are private wildlife conservancies bordering the main reserve, offering exclusive safari experiences. Key conservancies: Mara North, Olare Motorogi, Naboisho, and Mara Naboisho. Benefits include night drives, walking safaris, off-road driving, and fewer vehicles. Higher prices but more exclusive experience.", "source": "magicalkenya.com", "category": "safari", "region": "Rift Valley", "destination": "Masai Mara"},
    
    {"content": "Maasai cultural experiences in the Mara include village visits ($20-30 USD), traditional dance performances, learning about Maasai customs, and visiting local markets. Many lodges arrange cultural visits. The Maasai are known for their distinctive red shuka robes, beaded jewelry, and semi-nomadic cattle-herding lifestyle.", "source": "magicalkenya.com", "category": "culture", "region": "Rift Valley", "destination": "Masai Mara"},
    
    {"content": "Photography tips for Masai Mara: Bring a telephoto lens (200-400mm minimum), a wide-angle for landscapes, bean bag for vehicle support, dust covers for equipment. Best light is early morning and late afternoon. Memory cards: bring at least 64GB. Batteries drain faster in heat - bring spares.", "source": "magicalkenya.com", "category": "safari", "region": "Rift Valley", "destination": "Masai Mara"},
    
    {"content": "Masai Mara bird watching: Over 470 bird species recorded. Key species include Secretary Bird, Lilac-breasted Roller (Kenya's national bird candidate), various vulture species, Martial Eagle, and migratory birds from Europe. The Mara River area is excellent for waterbirds. November-April is best for migratory species.", "source": "kws.go.ke", "category": "safari", "region": "Rift Valley", "destination": "Masai Mara"},
    
    {"content": "Safety in Masai Mara: Never exit vehicles in the main reserve. Keep a safe distance from wildlife (minimum 25 meters). Don't feed animals. Follow guide instructions. The Mara is malaria zone - take prophylaxis. Don't walk outside camps at night. Hippos and buffalos are most dangerous - more deaths than lions.", "source": "kws.go.ke", "category": "safari", "region": "Rift Valley", "destination": "Masai Mara"},

    # ═══════════════════════════════════════════════════════════════════════════
    # AMBOSELI NATIONAL PARK (10 documents)
    # ═══════════════════════════════════════════════════════════════════════════
    
    {"content": "Amboseli National Park is located in Kajiado County at the foot of Mount Kilimanjaro, Africa's highest peak. The park covers 392 square kilometers. Its name comes from the Maasai word 'Empusel' meaning 'salty dust'. The park offers the most classic postcard images of elephants with Kilimanjaro in the background.", "source": "kws.go.ke", "category": "safari", "region": "Rift Valley", "destination": "Amboseli"},
    
    {"content": "Amboseli entry fees: Non-resident adults $60 USD per day, children $35 USD. East African citizens: 1,000 KES adults, 500 KES children. Kenya citizens: 500 KES adults, 215 KES children. Smartcard or cash accepted. Park hours: 6:00 AM to 6:00 PM. No night drives in the main park.", "source": "kws.go.ke", "category": "safari", "region": "Rift Valley", "destination": "Amboseli"},
    
    {"content": "Amboseli has over 1,500 elephants, one of the highest densities in Africa. The Amboseli Elephant Research Project, running since 1972, has identified over 3,000 individual elephants. Researchers know many elephants by name. The elephants are remarkably tolerant of vehicles, offering exceptional photography opportunities.", "source": "kws.go.ke", "category": "safari", "region": "Rift Valley", "destination": "Amboseli"},
    
    {"content": "Best views of Mount Kilimanjaro from Amboseli are early morning (6:00-8:00 AM) before clouds form. By mid-morning, the 5,895-meter peak is usually hidden. The mountain is in Tanzania, but Amboseli offers the best views. Observation Hill provides 360-degree panoramic views of the park and mountain.", "source": "magicalkenya.com", "category": "safari", "region": "Rift Valley", "destination": "Amboseli"},
    
    {"content": "Amboseli habitats include dried lake bed, sulfur springs, swamps, savanna, and acacia woodlands. The permanent swamps fed by Kilimanjaro's underground water attract wildlife year-round. Key viewing areas: Enkongo Narok Swamp, Longinye Swamp, and the dry lake bed. The swamps support hippos, buffalo, and waterbirds.", "source": "kws.go.ke", "category": "safari", "region": "Rift Valley", "destination": "Amboseli"},
    
    {"content": "Getting to Amboseli: 240 km from Nairobi (4-5 hours by road) via Namanga. The road is tarmac throughout. Alternative route via Emali (shorter but rougher). Daily flights from Nairobi's Wilson Airport (45 minutes) with AirKenya and Safarilink. Airstrip: Amboseli Airport.", "source": "magicalkenya.com", "category": "safari", "region": "Rift Valley", "destination": "Amboseli"},
    
    {"content": "Amboseli wildlife beyond elephants: lions, cheetahs, leopards, spotted hyenas, buffalos, hippos, zebras, wildebeest, giraffes, and over 400 bird species. The park is one of the best places to see free-ranging cheetahs. Predator sightings are common in the open savanna areas.", "source": "kws.go.ke", "category": "safari", "region": "Rift Valley", "destination": "Amboseli"},
    
    {"content": "Best time to visit Amboseli: Dry season (June-October, January-February) offers best wildlife viewing as animals concentrate around swamps. Kilimanjaro views are clearest December-March. Wet season (March-May, November) has fewer tourists, green landscapes, and migratory birds.", "source": "magicalkenya.com", "category": "safari", "region": "Rift Valley", "destination": "Amboseli"},
    
    {"content": "Amboseli accommodation: Ol Tukai Lodge (inside park, $300-500/night), Amboseli Serena Safari Lodge (park border, $400-600/night), Tortilis Camp (luxury, $700+/night), Kibo Safari Camp (mid-range, $150-250/night). Budget options available in Kimana outside the park.", "source": "magicalkenya.com", "category": "safari", "region": "Rift Valley", "destination": "Amboseli"},
    
    {"content": "Amboseli combines well with Tsavo (3 hours), Chyulu Hills (1.5 hours), and Tanzania's Kilimanjaro National Park (border crossing at Namanga). A classic itinerary: 2 nights Amboseli + 2 nights Tsavo West + 2 nights Tsavo East, or combine with beach holiday in Diani (5 hours).", "source": "magicalkenya.com", "category": "safari", "region": "Rift Valley", "destination": "Amboseli"},

    # ═══════════════════════════════════════════════════════════════════════════
    # TSAVO NATIONAL PARKS (12 documents)
    # ═══════════════════════════════════════════════════════════════════════════
    
    {"content": "Tsavo National Park is Kenya's largest national park, divided into Tsavo East (13,747 sq km) and Tsavo West (9,065 sq km) by the Nairobi-Mombasa highway and railway. Combined, they cover 4% of Kenya's total land area. The parks are named after the Tsavo River.", "source": "kws.go.ke", "category": "safari", "region": "Coast", "destination": "Tsavo"},
    
    {"content": "Tsavo entry fees: Non-resident adults $52 USD per day, children $26 USD. East African citizens: 515 KES adults, 260 KES children. Kenya citizens: 345 KES adults, 175 KES children. Fees are the same for both Tsavo East and Tsavo West, but separate tickets required for each.", "source": "kws.go.ke", "category": "safari", "region": "Coast", "destination": "Tsavo"},
    
    {"content": "Tsavo's red elephants are famous worldwide. The elephants dust themselves with the park's red volcanic soil, giving them their distinctive color. Tsavo has one of Kenya's largest elephant populations - over 12,000. The elephants were nearly wiped out by poaching in the 1970s-80s but have recovered.", "source": "kws.go.ke", "category": "safari", "region": "Coast", "destination": "Tsavo"},
    
    {"content": "The Man-Eaters of Tsavo were two male lions that killed railway workers during the construction of the Kenya-Uganda Railway in 1898. Lieutenant Colonel John Henry Patterson eventually shot both lions. Their story inspired the film 'The Ghost and the Darkness'. Their taxidermied bodies are displayed at Chicago's Field Museum.", "source": "kws.go.ke", "category": "safari", "region": "Coast", "destination": "Tsavo"},
    
    {"content": "Tsavo West attractions: Mzima Springs - crystal-clear water supporting hippos and crocodiles, viewable through an underwater observatory. Shetani Lava Flow - 200-year-old volcanic formation stretching 50 km. Chaimu Crater - extinct volcano offering panoramic views. Ngulia Rhino Sanctuary protects black rhinos.", "source": "kws.go.ke", "category": "safari", "region": "Coast", "destination": "Tsavo West"},
    
    {"content": "Mzima Springs in Tsavo West produces 250 million liters of crystal-clear water daily from underground aquifers fed by Kilimanjaro's snowmelt. The springs support hippos, crocodiles, and various fish species. An underwater viewing chamber allows visitors to watch fish and occasionally hippos from below. Walking is permitted on marked trails.", "source": "kws.go.ke", "category": "safari", "region": "Coast", "destination": "Tsavo West"},
    
    {"content": "Tsavo East attractions: Yatta Plateau - the world's longest lava flow at 290 km. Lugard Falls - series of rapids on the Galana River. Mudanda Rock - natural dam and wildlife gathering point. Aruba Dam - artificial dam attracting wildlife. The park is more open and flatter than Tsavo West.", "source": "kws.go.ke", "category": "safari", "region": "Coast", "destination": "Tsavo East"},
    
    {"content": "Galana River runs through Tsavo East, providing a lifeline for wildlife during dry seasons. The river attracts elephants, hippos, crocodiles, and numerous bird species. Lugard Falls, where the river narrows through colorful rock formations, is a popular viewpoint. Crocodile Point offers excellent crocodile viewing.", "source": "kws.go.ke", "category": "safari", "region": "Coast", "destination": "Tsavo East"},
    
    {"content": "Getting to Tsavo: Tsavo West gates: Mtito Andei (250 km from Nairobi), Tsavo Gate (from Mombasa). Tsavo East gates: Voi (330 km from Nairobi), Buchuma (from Mombasa). The parks are easily accessed from both Nairobi and Mombasa. The SGR train stops at Mtito Andei and Voi stations.", "source": "magicalkenya.com", "category": "safari", "region": "Coast", "destination": "Tsavo"},
    
    {"content": "Tsavo wildlife: elephants, lions, leopards, cheetahs, buffalos, hippos, crocodiles, lesser kudu, gerenuk, oryx, and over 500 bird species. The parks are less crowded than Masai Mara, offering a wilderness experience. Game viewing can be more challenging due to the parks' vast size and thick vegetation.", "source": "kws.go.ke", "category": "safari", "region": "Coast", "destination": "Tsavo"},
    
    {"content": "Tsavo accommodation: Tsavo West - Kilaguni Serena Safari Lodge (first lodge in a Kenyan national park, $200-400/night), Severin Safari Camp, Ngulia Safari Lodge. Tsavo East - Voi Safari Lodge, Ashnil Aruba Lodge, Satao Camp (luxury, $500+/night). Budget camping available.", "source": "magicalkenya.com", "category": "safari", "region": "Coast", "destination": "Tsavo"},
    
    {"content": "Best time to visit Tsavo: Dry seasons (January-February, June-October) when vegetation is sparse and wildlife concentrates around water sources. The parks are hot year-round (30-35°C). Wet seasons (March-May, November-December) have lush scenery but challenging roads and dispersed wildlife.", "source": "magicalkenya.com", "category": "safari", "region": "Coast", "destination": "Tsavo"},

    # ═══════════════════════════════════════════════════════════════════════════
    # LAKE NAKURU NATIONAL PARK (8 documents)
    # ═══════════════════════════════════════════════════════════════════════════
    
    {"content": "Lake Nakuru National Park is located in the Rift Valley, 160 km northwest of Nairobi. The park covers 188 square kilometers around the shallow, alkaline Lake Nakuru. It was established in 1961 and became a national park in 1968. The name 'Nakuru' means 'dusty place' in Maasai.", "source": "kws.go.ke", "category": "safari", "region": "Rift Valley", "destination": "Lake Nakuru"},
    
    {"content": "Lake Nakuru entry fees: Non-resident adults $60 USD per day, children $35 USD. East African citizens: 1,030 KES adults, 515 KES children. Kenya citizens: 860 KES adults, 215 KES children. Park hours: 6:00 AM to 6:00 PM. The park is fully fenced to protect rhinos.", "source": "kws.go.ke", "category": "safari", "region": "Rift Valley", "destination": "Lake Nakuru"},
    
    {"content": "Lake Nakuru flamingos: The lake once hosted up to 2 million lesser flamingos, creating a pink shoreline. Flamingo numbers fluctuate with water levels and algae availability. When water levels rose in 2013, many flamingos moved to Lake Bogoria. Check current conditions before visiting for flamingos.", "source": "kws.go.ke", "category": "safari", "region": "Rift Valley", "destination": "Lake Nakuru"},
    
    {"content": "Lake Nakuru is a rhino sanctuary housing both black and white rhinos - over 70 individuals. It's one of the best places in Kenya to see rhinos. The park is fully fenced with electrified barriers. The sanctuary was established to protect rhinos from poaching during the 1980s-90s crisis.", "source": "kws.go.ke", "category": "safari", "region": "Rift Valley", "destination": "Lake Nakuru"},
    
    {"content": "Lake Nakuru wildlife: Lions, leopards, buffalos, endangered Rothschild's giraffes (about 70), waterbucks, impalas, baboons, and over 450 bird species. The park introduced lions and Rothschild's giraffes for conservation. Pythons are sometimes spotted in fig tree forests.", "source": "kws.go.ke", "category": "safari", "region": "Rift Valley", "destination": "Lake Nakuru"},
    
    {"content": "Baboon Cliff viewpoint offers spectacular panoramic views of Lake Nakuru and the entire park. It's the best spot for photography, especially at sunrise. Out of Africa viewpoint is another excellent spot. The cliff is named after the baboon troops commonly seen there.", "source": "magicalkenya.com", "category": "safari", "region": "Rift Valley", "destination": "Lake Nakuru"},
    
    {"content": "Getting to Lake Nakuru: 160 km from Nairobi (2-2.5 hours) on excellent tarmac road via Naivasha. Main gate is near Nakuru town. The park is perfect for a day trip from Nairobi or en route to Masai Mara. Combine with Lake Naivasha and Hell's Gate for a Rift Valley circuit.", "source": "magicalkenya.com", "category": "safari", "region": "Rift Valley", "destination": "Lake Nakuru"},
    
    {"content": "Lake Nakuru accommodation: Lake Nakuru Lodge (inside park, $250-400/night), Sarova Lion Hill Game Lodge (inside park, $200-350/night), Flamingo Hill Tented Camp. Budget options in Nakuru town include Merica Hotel, Midland Hotel. Naivasha (50 km) has more accommodation options.", "source": "magicalkenya.com", "category": "safari", "region": "Rift Valley", "destination": "Lake Nakuru"},

    # ═══════════════════════════════════════════════════════════════════════════
    # SAMBURU NATIONAL RESERVE (8 documents)
    # ═══════════════════════════════════════════════════════════════════════════
    
    {"content": "Samburu National Reserve is located in northern Kenya's Samburu County, 350 km north of Nairobi. The reserve covers 165 square kilometers along the Ewaso Ng'iro River. Adjacent Buffalo Springs and Shaba reserves form a larger ecosystem of 440 square kilometers.", "source": "kws.go.ke", "category": "safari", "region": "Northern Kenya", "destination": "Samburu"},
    
    {"content": "Samburu entry fees: Non-resident adults $70 USD per day, children $40 USD. East African citizens: 1,030 KES adults, 515 KES children. Kenya citizens: 860 KES adults, 430 KES children. Fees apply separately to Samburu, Buffalo Springs, and Shaba reserves.", "source": "kws.go.ke", "category": "safari", "region": "Northern Kenya", "destination": "Samburu"},
    
    {"content": "The Samburu Special Five are unique northern Kenya species: Grevy's zebra (endangered, larger than common zebra with narrow stripes), reticulated giraffe (distinctive pattern), Somali ostrich (blue-grey neck, not pink), gerenuk (long-necked antelope that stands on hind legs), and beisa oryx (straight horns).", "source": "kws.go.ke", "category": "safari", "region": "Northern Kenya", "destination": "Samburu"},
    
    {"content": "Ewaso Ng'iro River is Samburu's lifeline, flowing from Mount Kenya through the reserve. The riverine forest supports elephants, leopards, crocodiles, and diverse birdlife. Doum palms along the river are distinctive. During dry season, wildlife congregates along the river, offering excellent viewing.", "source": "kws.go.ke", "category": "safari", "region": "Northern Kenya", "destination": "Samburu"},
    
    {"content": "Samburu leopards: The reserve is famous for relaxed leopards often seen during daytime. Some lodges have resident leopards that visit for food scraps. The riverine vegetation provides perfect leopard habitat. Night drives in nearby conservancies offer excellent leopard sightings.", "source": "magicalkenya.com", "category": "safari", "region": "Northern Kenya", "destination": "Samburu"},
    
    {"content": "Elsa the lioness from 'Born Free' was released in Meru National Park but had connections to the Samburu region. Joy Adamson's conservation work highlighted northern Kenya. Samburu and Buffalo Springs offer authentic wilderness with fewer tourists than southern parks.", "source": "magicalkenya.com", "category": "safari", "region": "Northern Kenya", "destination": "Samburu"},
    
    {"content": "Getting to Samburu: 350 km from Nairobi (5-6 hours) via Nanyuki or Isiolo. Roads are tarmac until Isiolo, then good gravel. Daily flights from Nairobi to Samburu's airstrips (1 hour) with Safarilink. The reserve is often combined with Ol Pejeta, Mount Kenya, or Laikipia conservancies.", "source": "magicalkenya.com", "category": "safari", "region": "Northern Kenya", "destination": "Samburu"},
    
    {"content": "Samburu accommodation: Saruni Samburu (luxury, $600-1,000/night with pool overlooking watering hole), Elephant Bedroom Camp ($400-700/night), Samburu Intrepids ($300-500/night), Samburu Sopa Lodge ($200-400/night). Budget camping available at public campsites along the river.", "source": "magicalkenya.com", "category": "safari", "region": "Northern Kenya", "destination": "Samburu"},

    # ═══════════════════════════════════════════════════════════════════════════
    # NAIROBI NATIONAL PARK & ATTRACTIONS (10 documents)
    # ═══════════════════════════════════════════════════════════════════════════
    
    {"content": "Nairobi National Park is the world's only national park within a capital city, just 7 km from Nairobi's city center. Established in 1946, it covers 117 square kilometers. The park has an open southern boundary allowing wildlife to migrate to and from Kitengela plains.", "source": "kws.go.ke", "category": "safari", "region": "Nairobi", "destination": "Nairobi National Park"},
    
    {"content": "Nairobi National Park entry fees: Non-resident adults $43 USD per day, children $22 USD. East African citizens: 430 KES adults, 215 KES children. Kenya citizens: 345 KES adults, 100 KES children. Park hours: 6:00 AM to 6:00 PM. Main gate is at Langata Road entrance.", "source": "kws.go.ke", "category": "safari", "region": "Nairobi", "destination": "Nairobi National Park"},
    
    {"content": "Nairobi National Park wildlife: Lions (about 30), leopards, cheetahs, hyenas, buffalos, giraffes, zebras, gazelles, ostriches, and endangered black rhinos (about 50). The park has no elephants. Over 400 bird species recorded. Wildlife is photographed against Nairobi's skyline - unique in the world.", "source": "kws.go.ke", "category": "safari", "region": "Nairobi", "destination": "Nairobi National Park"},
    
    {"content": "David Sheldrick Wildlife Trust at Nairobi National Park rescues and rehabilitates orphaned elephants and rhinos. Public visiting hour: 11:00 AM - 12:00 PM daily. Entry: $15 USD adults, free for children under 3. Visitors can watch baby elephants being bottle-fed and playing in mud baths. Elephant adoption programs available.", "source": "sheldrickwildlifetrust.org", "category": "safari", "region": "Nairobi", "destination": "Nairobi"},
    
    {"content": "Giraffe Centre in Langata protects endangered Rothschild's giraffes. Visitors can hand-feed giraffes from a raised platform and even get a 'giraffe kiss'. Entry: $15 USD adults, $7.50 USD children. Open 9:00 AM - 5:00 PM daily. The center has successfully bred giraffes for reintroduction to the wild.", "source": "giraffecentre.org", "category": "safari", "region": "Nairobi", "destination": "Nairobi"},
    
    {"content": "Karen Blixen Museum is the former home of 'Out of Africa' author Karen Blixen (Isak Dinesen). Located in the Karen suburb named after her, the museum showcases her life in Kenya from 1914-1931. Entry: $12 USD. Open 9:30 AM - 6:00 PM. The original furniture and coffee farm equipment are displayed.", "source": "museums.or.ke", "category": "culture", "region": "Nairobi", "destination": "Karen"},
    
    {"content": "Nairobi National Museum covers Kenya's cultural and natural heritage. Exhibits include prehistoric human fossils, tribal artifacts, stuffed wildlife, and contemporary Kenyan art. Entry: $12 USD adults. Open 9:30 AM - 5:30 PM. The complex includes Snake Park, botanical gardens, and Nature Trail.", "source": "museums.or.ke", "category": "culture", "region": "Nairobi", "destination": "Nairobi"},
    
    {"content": "Kazuri Beads factory in Karen employs single mothers to create handcrafted ceramic beads and pottery. Visitors can tour the factory and purchase directly. Free entry. Open 8:00 AM - 5:00 PM weekdays, 9:00 AM - 4:00 PM Saturday. 'Kazuri' means 'small and beautiful' in Swahili.", "source": "kazuri.com", "category": "culture", "region": "Nairobi", "destination": "Karen"},
    
    {"content": "Bomas of Kenya showcases traditional Kenyan cultures through daily dance performances and replica traditional villages of Kenya's 42 ethnic groups. Entry: 1,200 KES adults, 600 KES children. Performances at 2:30 PM weekdays, 3:30 PM weekends. Located 10 km from city center near Langata.", "source": "bomasofkenya.co.ke", "category": "culture", "region": "Nairobi", "destination": "Nairobi"},
    
    {"content": "Nairobi Safari Walk at KWS headquarters is an elevated wooden boardwalk through natural habitats. See lions, cheetahs, white rhinos, and bongos in large enclosures. Entry: $20 USD adults, $10 USD children. Combined ticket with Animal Orphanage available. Great introduction to Kenya's wildlife before safari.", "source": "kws.go.ke", "category": "safari", "region": "Nairobi", "destination": "Nairobi"},

    # ═══════════════════════════════════════════════════════════════════════════
    # OTHER NATIONAL PARKS (15 documents)
    # ═══════════════════════════════════════════════════════════════════════════
    
    {"content": "Hell's Gate National Park near Lake Naivasha is unique for allowing walking and cycling through the park. Entry: $26 USD adults. The park features dramatic cliffs, gorges, geothermal steam vents, and Maasai cultural center. Wildlife includes buffalos, zebras, giraffes, and baboons. Inspired Disney's Lion King landscapes.", "source": "kws.go.ke", "category": "adventure", "region": "Rift Valley", "destination": "Hell's Gate"},
    
    {"content": "Hell's Gate gorge walking is a highlight - descend into steep-walled canyons with natural hot springs. Hiring a guide ($20 USD) is recommended for safety. The gorge can be slippery after rain. Fischer's Tower and Central Tower are prominent volcanic plugs. The park is excellent for rock climbing.", "source": "kws.go.ke", "category": "adventure", "region": "Rift Valley", "destination": "Hell's Gate"},
    
    {"content": "Mount Kenya National Park protects Africa's second-highest mountain (5,199m). Entry: $52 USD per day. Three main peaks: Batian, Nelion (technical climbs), and Point Lenana (4,985m, trekkers' peak). The mountain is a UNESCO World Heritage Site with unique Afro-alpine vegetation and glaciers.", "source": "kws.go.ke", "category": "adventure", "region": "Central", "destination": "Mount Kenya"},
    
    {"content": "Mount Kenya trekking routes: Sirimon (easiest, from northwest), Naro Moru (fastest, steepest), Chogoria (most scenic, from east). Trek to Point Lenana takes 4-5 days. Costs: guides $40-60/day, porters $20-30/day, park fees, hut fees ($25-35/night). Best months: January-February, August-September.", "source": "kws.go.ke", "category": "adventure", "region": "Central", "destination": "Mount Kenya"},
    
    {"content": "Aberdare National Park is a forested mountain range 100 km north of Nairobi. Entry: $52 USD. The park offers trout fishing, waterfalls (Karuru Falls is 273m), moorland hikes, and wildlife including elephants, buffalos, giant forest hogs, and bongo antelopes. Famous tree lodges: Treetops and The Ark.", "source": "kws.go.ke", "category": "safari", "region": "Central", "destination": "Aberdares"},
    
    {"content": "Meru National Park is where Joy Adamson released Elsa the lioness ('Born Free'). Entry: $52 USD. Located 350 km northeast of Nairobi, the park has 870 sq km of wilderness with fewer visitors. Wildlife includes elephants, lions, leopards, cheetahs, rhinos (sanctuary), and lesser kudu. Tana River runs through it.", "source": "kws.go.ke", "category": "safari", "region": "Eastern", "destination": "Meru"},
    
    {"content": "Ol Pejeta Conservancy in Laikipia is home to the world's last two northern white rhinos and a chimpanzee sanctuary. Entry: $90 USD adults (includes conservancy fees). The 90,000-acre private conservancy has excellent rhino tracking, Big Five viewing, and night drives. Sweetwaters Tented Camp offers waterhole viewing.", "source": "olpejetaconservancy.org", "category": "safari", "region": "Central", "destination": "Ol Pejeta"},
    
    {"content": "Lake Bogoria National Reserve is famous for hot springs, geysers, and flamingos (especially when they migrate from Nakuru). Entry: $50 USD. The alkaline lake has no swimming. Greater kudu and over 350 bird species present. Lake Bogoria Spa Resort offers natural hot spring baths. Best accessed from Nakuru (60 km).", "source": "kws.go.ke", "category": "lakes", "region": "Rift Valley", "destination": "Lake Bogoria"},
    
    {"content": "Lake Naivasha is a freshwater Rift Valley lake 90 km from Nairobi. No entry fee for the lake itself. Activities: boat rides ($30-40/hour), hippo spotting, birdwatching (400+ species), Crescent Island walking safari ($30 entry). The area has flower farms, Hell's Gate, and luxury retreats. Popular weekend getaway from Nairobi.", "source": "magicalkenya.com", "category": "lakes", "region": "Rift Valley", "destination": "Lake Naivasha"},
    
    {"content": "Crescent Island on Lake Naivasha allows walking among wildlife - zebras, wildebeest, giraffes, waterbucks, and hippos (keep distance). Entry: $30 USD. Access by boat from any Lake Naivasha resort ($10-15 each way). The island was featured in 'Out of Africa' film. Great for photography without vehicle restrictions.", "source": "magicalkenya.com", "category": "safari", "region": "Rift Valley", "destination": "Lake Naivasha"},
    
    {"content": "Chyulu Hills National Park offers stunning volcanic landscapes between Amboseli and Tsavo. Entry: $52 USD. The hills have lush forests, caves (including one of the world's longest lava tubes), and views of Kilimanjaro. Activities: hiking, horseback safaris, and cave exploration. Ol Donyo Lodge is a luxury option.", "source": "kws.go.ke", "category": "adventure", "region": "Rift Valley", "destination": "Chyulu Hills"},
    
    {"content": "Lake Turkana, the 'Jade Sea', is the world's largest permanent desert lake. Entry fees vary by area. Located in remote northern Kenya, the lake is a UNESCO World Heritage Site. Central Island has volcanic crater lakes. The area is home to Turkana, Samburu, and El Molo tribes. Access mainly by flying from Nairobi.", "source": "kws.go.ke", "category": "lakes", "region": "Northern Kenya", "destination": "Lake Turkana"},
    
    {"content": "Kakamega Forest is Kenya's only tropical rainforest and easternmost fragment of the Congo rainforest. Entry: $25 USD. The forest has 330 bird species, colobus monkeys, giant trees, and butterflies. Guided walks, night walks for bushbabies, and birdwatching. Located in western Kenya near Kisumu.", "source": "kws.go.ke", "category": "adventure", "region": "Western", "destination": "Kakamega Forest"},
    
    {"content": "Saiwa Swamp National Park near Kitale is Kenya's smallest national park (3 sq km) and the only place to see the rare sitatunga antelope. Entry: $25 USD. Wooden walkways traverse the swamp. Other wildlife includes de Brazza's monkey, giant forest squirrel, and otters. Best visited combined with Mount Elgon.", "source": "kws.go.ke", "category": "safari", "region": "Western", "destination": "Saiwa Swamp"},
    
    {"content": "Mount Elgon National Park straddles the Kenya-Uganda border, featuring Africa's largest caldera (40 km). Entry: $26 USD. The extinct volcano (4,321m) offers caves with elephant salt-mining activity, waterfalls, hot springs, and Afro-alpine moorland. Popular for hiking and caving. Less visited than Mount Kenya.", "source": "kws.go.ke", "category": "adventure", "region": "Western", "destination": "Mount Elgon"},

    # ═══════════════════════════════════════════════════════════════════════════
    # DIANI BEACH & SOUTH COAST (12 documents)
    # ═══════════════════════════════════════════════════════════════════════════
    
    {"content": "Diani Beach is a 17 km stretch of white sand on Kenya's south coast, 30 km from Mombasa. Voted Africa's Leading Beach Destination multiple times. The beach has palm trees, turquoise water, and coral reefs. Water temperature: 25-29°C year-round. Protected from strong currents by offshore reef.", "source": "magicalkenya.com", "category": "beach", "region": "Coast", "destination": "Diani Beach"},
    
    {"content": "Diani Beach activities: Scuba diving and snorkeling ($50-100), kite surfing (excellent conditions), jet skiing, glass-bottom boat trips, deep-sea fishing (marlin, sailfish), skydiving ($400), day trips to Wasini Island, and dolphin watching tours ($50-80). Multiple water sports operators along the beach.", "source": "magicalkenya.com", "category": "beach", "region": "Coast", "destination": "Diani Beach"},
    
    {"content": "Kisite-Mpunguti Marine National Park is accessible from Diani via Shimoni (1.5 hours south). Entry: $17 USD. The park has pristine coral reefs, dolphins (bottlenose and spinner), sea turtles, whale sharks (seasonal), and 250 fish species. Full-day tours including snorkeling cost $80-120.", "source": "kws.go.ke", "category": "beach", "region": "Coast", "destination": "Kisite Marine Park"},
    
    {"content": "Wasini Island near Shimoni offers Swahili culture, seafood lunch at the Wasini Women's Group, mangrove boardwalk, and snorkeling. Full-day tours from Diani cost $80-120 including boat, lunch, and snorkeling. The island has no cars - transport is by foot or dhow. Ruins of an 18th-century Swahili settlement.", "source": "magicalkenya.com", "category": "beach", "region": "Coast", "destination": "Wasini Island"},
    
    {"content": "Shimoni Caves are slave-era coral caves near Kisite Marine Park. 'Shimoni' means 'place of the hole'. The caves were used to hold slaves before transport to Zanzibar markets. Entry: $5 USD. The caves extend several hundred meters underground. Combine with marine park visit for full-day trip.", "source": "museums.or.ke", "category": "culture", "region": "Coast", "destination": "Shimoni"},
    
    {"content": "Colobus Conservation in Diani protects endangered Angolan colobus monkeys threatened by road accidents and habitat loss. Visitors can tour the rescue center, learn about primates, and support conservation. Entry: $15 USD. Open 8:00 AM - 4:00 PM. They've built rope bridges ('colobridges') across roads.", "source": "colobusconservation.org", "category": "safari", "region": "Coast", "destination": "Diani Beach"},
    
    {"content": "Getting to Diani: From Mombasa, cross Likoni Ferry (free, vehicles queue) then 30-minute drive south. Alternative: fly to Ukunda Airstrip from Nairobi (1 hour) or Masai Mara. Taxis from Mombasa cost 3,000-4,000 KES. Once in Diani, tuk-tuks and boda-bodas (motorbike taxis) are common transport.", "source": "magicalkenya.com", "category": "transport", "region": "Coast", "destination": "Diani Beach"},
    
    {"content": "Diani Beach accommodation ranges from budget ($30/night) to all-inclusive luxury ($500+/night). Popular resorts: Leopard Beach Resort, Diani Sea Resort, Baobab Beach Resort, The Sands at Nomad. Mid-range: Diani Reef Beach Resort, Southern Palms. Budget: Neptune Paradise, Pinewood Village.", "source": "magicalkenya.com", "category": "beach", "region": "Coast", "destination": "Diani Beach"},
    
    {"content": "Best time to visit Diani Beach: December-March (hot, dry, perfect beach weather), June-October (dry, cooler, ideal for activities). April-May is long rains (heavy rain, some closures). November has short rains. Kite surfing is best January-March and July-September with steady winds.", "source": "magicalkenya.com", "category": "beach", "region": "Coast", "destination": "Diani Beach"},
    
    {"content": "Diani nightlife and dining: Forty Thieves Beach Bar (legendary beach bar with seafood), Ali Barbour's Cave Restaurant (fine dining in natural cave), Sails Beach Bar, Nomad Beach Bar. Shopping: Diani Beach Shopping Centre, Nakumatt (groceries). Friday Maasai Market sells crafts and souvenirs.", "source": "magicalkenya.com", "category": "beach", "region": "Coast", "destination": "Diani Beach"},
    
    {"content": "Tiwi Beach is a quieter alternative to Diani, located between Diani and Likoni Ferry. The beach is more secluded with fewer vendors. Good for budget travelers and those seeking tranquility. Accommodation is more limited. Access to Diani beach facilities requires transport.", "source": "magicalkenya.com", "category": "beach", "region": "Coast", "destination": "Tiwi Beach"},
    
    {"content": "Funzi Island is an undeveloped island south of Diani, accessible only by boat. Day trips ($100-150) include mangrove cruises, village visits, seafood lunch, and sandbank swimming. The island has Swahili fishing communities unchanged for centuries. Overnight camping possible. Very few tourists.", "source": "magicalkenya.com", "category": "beach", "region": "Coast", "destination": "Funzi Island"},

    # ═══════════════════════════════════════════════════════════════════════════
    # MOMBASA & NORTH COAST (10 documents)
    # ═══════════════════════════════════════════════════════════════════════════
    
    {"content": "Mombasa is Kenya's second-largest city and oldest, founded by Arab traders over 2,000 years ago. The city blends African, Arab, Indian, and European influences. Key attractions: Fort Jesus, Old Town, Mombasa Tusks, beaches. Population: over 1.2 million. Mombasa Island is connected to mainland by bridges and ferries.", "source": "magicalkenya.com", "category": "culture", "region": "Coast", "destination": "Mombasa"},
    
    {"content": "Fort Jesus in Mombasa is a UNESCO World Heritage Site built by the Portuguese in 1593-1596. Entry: $12 USD adults, $6 USD children. The fort changed hands between Portuguese and Omani Arabs nine times. The museum displays artifacts from Portuguese, Omani, and Swahili periods. Open 8:00 AM - 6:00 PM.", "source": "museums.or.ke", "category": "culture", "region": "Coast", "destination": "Mombasa"},
    
    {"content": "Mombasa Old Town features narrow streets, Swahili architecture with ornately carved doors, mosques, and historic buildings. Key sites: Mandhry Mosque (1570), Basheikh Mosque, Leven Steps, Old Post Office, Uhuru Gardens. Walking tours available ($20-30). The area is safe during daytime. Best explored on foot.", "source": "magicalkenya.com", "category": "culture", "region": "Coast", "destination": "Mombasa"},
    
    {"content": "The Mombasa Tusks are giant aluminum tusks on Moi Avenue, erected in 1952 for Princess (later Queen) Elizabeth's visit. They form the letter 'M' for Mombasa. The tusks are Mombasa's most iconic landmark, featured in every tourist photo. Located in the city center, free to photograph.", "source": "magicalkenya.com", "category": "culture", "region": "Coast", "destination": "Mombasa"},
    
    {"content": "North coast beaches (Nyali, Bamburi, Shanzu) stretch 30 km from Mombasa. These beaches have all-inclusive resorts, water sports, and family-friendly facilities. Water is calmer than south coast. Popular resorts: Sarova Whitesands, Voyager Beach Resort, Severin Sea Lodge, Bamburi Beach Hotel.", "source": "magicalkenya.com", "category": "beach", "region": "Coast", "destination": "Mombasa"},
    
    {"content": "Haller Park (formerly Bamburi Nature Trail) is a rehabilitated cement quarry transformed into an eco-park. Entry: $20 USD adults, $10 USD children. See hippos, giraffes, crocodiles, tortoises, and fish. Feeding times: hippos 4:00 PM, crocodiles 11:00 AM. Great for families. Includes reptile park and butterfly house.", "source": "hallerpark.info", "category": "safari", "region": "Coast", "destination": "Mombasa"},
    
    {"content": "Mombasa Marine National Park covers 10 square kilometers of coral reef and sea grass. Entry: $17 USD. Access by glass-bottom boat from Nyali. Snorkeling and diving reveal colorful coral, tropical fish, dolphins, and sea turtles. Best visibility: October-March. Several operators at Nyali Beach.", "source": "kws.go.ke", "category": "beach", "region": "Coast", "destination": "Mombasa"},
    
    {"content": "Moi International Airport (MBA) handles domestic and international flights. Airlines: Kenya Airways, Ethiopian, Emirates, Fly Dubai, Turkish. Airport is 10 km from city center. Taxis to Mombasa: 2,000 KES, to Diani: 4,000-5,000 KES. Some resorts offer airport transfers.", "source": "kaa.go.ke", "category": "transport", "region": "Coast", "destination": "Mombasa"},
    
    {"content": "Getting to Mombasa from Nairobi: SGR train (4.5 hours, $35 first class, $10 economy), flights (1 hour, $80-150), bus (8-9 hours, 1,200-2,000 KES with Easy Coach, Modern Coast). The SGR train passes through Tsavo - watch for elephants and other wildlife from the window.", "source": "krc.co.ke", "category": "transport", "region": "Coast", "destination": "Mombasa"},
    
    {"content": "Mombasa food: Try Swahili cuisine - pilau (spiced rice), biryani, mishkaki (kebabs), samosas, coconut fish curry, and tamarind juice. Best restaurants: Tamarind (upmarket seafood), Singh Restaurant (Indian), Barka (local Swahili), Jahazi Coffee House (Old Town). Street food available everywhere.", "source": "magicalkenya.com", "category": "culture", "region": "Coast", "destination": "Mombasa"},

    # ═══════════════════════════════════════════════════════════════════════════
    # WATAMU & MALINDI (10 documents)
    # ═══════════════════════════════════════════════════════════════════════════
    
    {"content": "Watamu is a small beach town 105 km north of Mombasa, known for its marine park and laid-back atmosphere. The town has pristine beaches, coral reefs, and Italian-influenced restaurants. Less developed than Diani, Watamu offers a quieter beach experience. Population: about 30,000.", "source": "magicalkenya.com", "category": "beach", "region": "Coast", "destination": "Watamu"},
    
    {"content": "Watamu Marine National Park is one of Kenya's best snorkeling and diving destinations. Entry: $17 USD. The park protects pristine coral gardens with over 600 fish species, sea turtles, dolphins, and whale sharks (seasonal). Glass-bottom boat trips: $30-50. Best visited at low tide.", "source": "kws.go.ke", "category": "beach", "region": "Coast", "destination": "Watamu"},
    
    {"content": "Watamu turtle conservation: Local Oceans Conservation runs a turtle rescue and rehabilitation center. Visitors can watch turtle releases (season: April-August), visit the center ($10), and participate in conservation activities. Green, hawksbill, and olive ridley turtles nest on Watamu beaches.", "source": "localocean.org", "category": "beach", "region": "Coast", "destination": "Watamu"},
    
    {"content": "Bio-Ken Snake Farm in Watamu houses various African snake species for research and antivenin production. Entry: $10 USD. See black mambas, cobras, puff adders, and pythons. Educational tours explain snake ecology and safety. The farm supplies antivenin to hospitals throughout East Africa.", "source": "bio-ken.com", "category": "safari", "region": "Coast", "destination": "Watamu"},
    
    {"content": "Gede Ruins are the remains of a 12th-century Swahili town mysteriously abandoned in the 17th century. Entry: $10 USD. The site includes a palace, mosque, and houses, all carved from coral stone. Adjacent Arabuko-Sokoke Forest is Kenya's largest coastal forest. Hire a guide for best experience.", "source": "museums.or.ke", "category": "culture", "region": "Coast", "destination": "Gede"},
    
    {"content": "Arabuko-Sokoke Forest near Watamu is Kenya's largest remaining coastal forest and a biodiversity hotspot. Entry: $25 USD. Home to rare birds (Sokoke scops owl, Clarke's weaver), Ader's duiker, golden-rumped elephant shrew, and butterflies. Guided walks and night drives available.", "source": "kws.go.ke", "category": "safari", "region": "Coast", "destination": "Arabuko-Sokoke"},
    
    {"content": "Malindi is a historic trading town 30 km north of Watamu. Portuguese explorer Vasco da Gama landed here in 1498 and erected a pillar that still stands. The town has a strong Italian community and excellent Italian restaurants. More developed than Watamu with banks, shops, and nightlife.", "source": "magicalkenya.com", "category": "beach", "region": "Coast", "destination": "Malindi"},
    
    {"content": "Malindi Marine National Park protects coral reefs off Malindi town. Entry: $17 USD. Snorkeling and diving reveal coral gardens, tropical fish, sea turtles, and dolphins. Glass-bottom boat trips available. The park is older than Watamu's and more heavily visited. Best snorkeling: October-March.", "source": "kws.go.ke", "category": "beach", "region": "Coast", "destination": "Malindi"},
    
    {"content": "Getting to Watamu/Malindi: Flights from Nairobi to Malindi Airport (1.5 hours) with Safarilink, Fly 540. By road from Mombasa: 2-2.5 hours (120 km). Matatus and buses available. From Nairobi: 8-10 hours by bus. Many Malindi visitors combine with Tsavo safaris.", "source": "magicalkenya.com", "category": "transport", "region": "Coast", "destination": "Watamu"},
    
    {"content": "Watamu accommodation: Hemingways Watamu (luxury, $400-700/night), Ocean Sports (water sports focused, $200-350/night), Turtle Bay Beach Club (all-inclusive, $300-500/night), Medina Palms (luxury villas), Temple Point Resort. Budget guesthouses available in Watamu village.", "source": "magicalkenya.com", "category": "beach", "region": "Coast", "destination": "Watamu"},

    # ═══════════════════════════════════════════════════════════════════════════
    # LAMU ISLAND (8 documents)
    # ═══════════════════════════════════════════════════════════════════════════
    
    {"content": "Lamu Old Town is a UNESCO World Heritage Site and Kenya's oldest continually inhabited town, founded in the 14th century. The town has no cars - transport is by foot, donkey, or boat. Swahili architecture features coral stone buildings, ornately carved wooden doors, and narrow streets.", "source": "magicalkenya.com", "category": "culture", "region": "Coast", "destination": "Lamu"},
    
    {"content": "Lamu Island is accessed by flight from Nairobi (1.5 hours) or Mombasa (30 minutes) to Manda Island, then boat to Lamu Town. Airlines: Safarilink, Fly 540. Flights cost $100-250. By road is long (8+ hours from Malindi) and security concerns exist. Flying is strongly recommended.", "source": "magicalkenya.com", "category": "transport", "region": "Coast", "destination": "Lamu"},
    
    {"content": "Lamu Museum in the waterfront displays Swahili culture, dhow-building traditions, and Lamu's history. Entry: $5 USD. The museum occupies a grand 19th-century building. Other museums: Swahili House Museum (traditional home), German Post Office Museum, Lamu Fort (1813).", "source": "museums.or.ke", "category": "culture", "region": "Coast", "destination": "Lamu"},
    
    {"content": "Shela Beach is Lamu's main beach, a 12 km stretch of pristine white sand often deserted. The village of Shela has upscale guesthouses, boutique hotels, and the iconic Peponi Hotel. Water is warm year-round. Swimming is safe but watch for strong currents. Dhow trips and fishing available.", "source": "magicalkenya.com", "category": "beach", "region": "Coast", "destination": "Lamu"},
    
    {"content": "Dhow sailing is quintessential Lamu. Traditional wooden dhows offer sunset cruises ($30-50), fishing trips, and transport between islands. Full-day trips to Manda Island, Kiwayu, or Pate Island cost $100-200. Learn to sail, or relax while the crew navigates using traditional skills.", "source": "magicalkenya.com", "category": "beach", "region": "Coast", "destination": "Lamu"},
    
    {"content": "Lamu Cultural Festival is held annually in November, celebrating Swahili heritage with donkey races, dhow races, traditional music, poetry, and henna competitions. The festival attracts visitors from around the world. Book accommodation months in advance. The Maulidi Festival (Prophet's birthday) is another major event.", "source": "lamuheritage.org", "category": "culture", "region": "Coast", "destination": "Lamu"},
    
    {"content": "Lamu accommodation ranges from simple guesthouses ($30/night) to exclusive villas ($1,000+/night). Iconic stays: Peponi Hotel (waterfront, $200-400/night), Lamu House (heritage, $300-500/night), The Majlis (Manda Island luxury, $600+/night). Many properties are restored Swahili houses.", "source": "magicalkenya.com", "category": "beach", "region": "Coast", "destination": "Lamu"},
    
    {"content": "Lamu food: Seafood is exceptional - lobster, crab, fish, octopus. Try Swahili dishes: pilau, biryani, mandazi (fried dough), coconut-based curries, fresh fruit juices. Whispers Coffee House and Peponi Hotel are popular. Alcohol is available but less prevalent due to Muslim culture. Pork is not served.", "source": "magicalkenya.com", "category": "culture", "region": "Coast", "destination": "Lamu"},

    # ═══════════════════════════════════════════════════════════════════════════
    # PRACTICAL TRAVEL INFO (20 documents)
    # ═══════════════════════════════════════════════════════════════════════════
    
    {"content": "Kenya visa requirements: Most nationalities require a visa. eVisa available at evisa.go.ke for $51 USD, processed in 2-3 business days. East African Community citizens don't need visas. Visas are single-entry, valid 90 days. Yellow fever vaccination required if arriving from endemic countries.", "source": "evisa.go.ke", "category": "transport", "region": "General", "destination": "Kenya"},
    
    {"content": "Jomo Kenyatta International Airport (NBO) is Kenya's main gateway, located 18 km from Nairobi city center. Airlines: Kenya Airways, British Airways, Emirates, Ethiopian, KLM, Turkish. Airport to city: Uber/Bolt 800-1,500 KES, taxi 2,500-3,500 KES, shuttle bus 400 KES.", "source": "kaa.go.ke", "category": "transport", "region": "Nairobi", "destination": "Nairobi"},
    
    {"content": "Wilson Airport in Nairobi handles domestic and charter flights, especially to safari destinations. Located 6 km from city center. Airlines: Safarilink, AirKenya, Fly 540. Flights to Masai Mara (45 min), Samburu (1 hour), Lamu (1.5 hours), Mombasa (1 hour), and many lodge airstrips.", "source": "kaa.go.ke", "category": "transport", "region": "Nairobi", "destination": "Nairobi"},
    
    {"content": "Standard Gauge Railway (SGR) connects Nairobi and Mombasa in 4.5 hours. Departures: 8:00 AM and 3:00 PM from both cities. Fares: First Class $35 USD (meals included, 2x2 seating), Economy $10 USD (3x3 seating). Book online at metickets.krc.co.ke. The route passes through Tsavo - watch for elephants!", "source": "krc.co.ke", "category": "transport", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenya currency is the Kenyan Shilling (KES). Exchange rate: approximately 130-155 KES = 1 USD (fluctuates). USD widely accepted at hotels, safari lodges, and national parks. ATMs available in all cities - Equity, KCB, Standard Chartered accept international cards. Visa/Mastercard accepted at hotels and large businesses.", "source": "centralbank.go.ke", "category": "transport", "region": "General", "destination": "Kenya"},
    
    {"content": "Tipping in Kenya: Safari guides $15-25 USD per day per vehicle, camp/lodge staff $10-15 USD per day (pooled), restaurant servers 10% of bill, airport porters 100-200 KES per bag, hotel porters 100 KES per bag. Tips are appreciated but not obligatory. Pay tips directly to individuals when possible.", "source": "magicalkenya.com", "category": "transport", "region": "General", "destination": "Kenya"},
    
    {"content": "Safari packing essentials: Neutral clothing (khaki, olive, brown - avoid bright colors and white), layers for cold mornings/hot afternoons, comfortable walking shoes, hat and sunglasses, sunscreen SPF 30+, insect repellent with DEET, binoculars, camera with telephoto lens (200-400mm+), power bank.", "source": "magicalkenya.com", "category": "transport", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenya climate: Nairobi (altitude 1,795m): temperate, 10-26°C year-round, rainy March-May and October-November. Coast: tropical, 25-32°C, humid, rainy April-June. Safari areas: hot days (30-35°C), cool mornings (10-15°C). Best safari season: June-October (dry). Best beach: December-March.", "source": "meteo.go.ke", "category": "transport", "region": "General", "destination": "Kenya"},
    
    {"content": "Malaria prevention is essential in Kenya. High-risk areas: coast, western Kenya, and regions below 1,800m. Low-risk: Nairobi and highlands above 2,500m. Take antimalarial prophylaxis (consult doctor). Use DEET repellent, sleep under treated nets, wear long sleeves at dusk/dawn.", "source": "cdc.gov", "category": "transport", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenya vaccinations: Yellow fever required if arriving from endemic countries. Recommended: Hepatitis A & B, Typhoid, Tetanus, Polio. Consider Rabies if extended travel or animal contact. Consult travel clinic 4-6 weeks before departure. Bring vaccination card.", "source": "cdc.gov", "category": "transport", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenya safety tips: Kenya is generally safe for tourists but use common sense. Avoid walking alone at night in cities. Use registered taxis or Uber/Bolt. Don't display expensive jewelry or electronics. Keep copies of passport. Register with your embassy. Safari areas are very safe.", "source": "state.gov", "category": "transport", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenya public holidays: New Year (Jan 1), Good Friday & Easter Monday, Labour Day (May 1), Madaraka Day (Jun 1), Mashujaa Day (Oct 20), Jamhuri Day (Dec 12), Christmas (Dec 25-26), Eid al-Fitr and Eid al-Adha (dates vary). Parks and attractions open but may be busy.", "source": "kenya.go.ke", "category": "transport", "region": "General", "destination": "Kenya"},
    
    {"content": "Mobile phones in Kenya: Main networks are Safaricom, Airtel, and Telkom. Safaricom is most reliable and uses M-Pesa mobile money (useful for payments). SIM cards available at airport ($3-5) - bring unlocked phone. 4G coverage in cities and tourist areas. Wi-Fi at most hotels.", "source": "safaricom.co.ke", "category": "transport", "region": "General", "destination": "Kenya"},
    
    {"content": "M-Pesa is Kenya's revolutionary mobile money system, used for almost everything. Tourists can use it for payments at shops, restaurants, and transport. Register at any Safaricom shop (passport required). Useful for avoiding cash. Taxi drivers, markets, and small businesses prefer M-Pesa.", "source": "safaricom.co.ke", "category": "transport", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenya electricity: 240V, 50Hz. Plug type G (British 3-pin). Bring universal adapter. Safari lodges usually have charging facilities but may be limited to certain hours (generator-powered camps). Bring power bank for game drives. Solar charging available at some eco-camps.", "source": "kenya.go.ke", "category": "transport", "region": "General", "destination": "Kenya"},
    
    {"content": "Self-driving in Kenya: Rental cars available from Nairobi and Mombasa. International driving permit recommended. Drive on the left. Roads vary from excellent tarmac to rough dirt. 4x4 essential for national parks and rainy season. Main routes to parks are well-signposted. Watch for wildlife on roads.", "source": "ntsa.go.ke", "category": "transport", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenya language: Official languages are English and Swahili. English widely spoken in tourism industry. Basic Swahili phrases: Jambo (Hello), Habari (How are you?), Asante (Thank you), Karibu (Welcome), Hakuna Matata (No worries), Safari (Journey), Simba (Lion), Tembo (Elephant).", "source": "magicalkenya.com", "category": "culture", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenya time zone: East Africa Time (EAT), UTC+3. No daylight saving time. Kenya is 8 hours ahead of EST, 3 hours ahead of GMT. Safari activities follow sunrise/sunset - game drives typically 6:00 AM - 10:00 AM and 4:00 PM - 6:30 PM.", "source": "kenya.go.ke", "category": "transport", "region": "General", "destination": "Kenya"},
    
    {"content": "Emergency contacts Kenya: Police/Ambulance 999, Tourist Helpline 0800 723 253 (free), KWS Emergency (wildlife) 0800 597 000. Embassy contacts: US +254 20 363 6000, UK +254 20 284 4000. Save local guide's number. Safari lodges have radio contact with flying doctors.", "source": "kenya.go.ke", "category": "transport", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenya internet: Most hotels and safari lodges have Wi-Fi, though it may be slow or limited in remote areas. Cafes in cities have free Wi-Fi. Mobile data with local SIM is reliable in tourist areas. Download offline maps (Google Maps, Maps.me) before safari. Starlink available at some upscale lodges.", "source": "magicalkenya.com", "category": "transport", "region": "General", "destination": "Kenya"},

    # ═══════════════════════════════════════════════════════════════════════════
    # KENYAN CULTURE & CUISINE (15 documents)
    # ═══════════════════════════════════════════════════════════════════════════
    
    {"content": "Kenya has 42 ethnic groups, each with distinct traditions. Major groups: Kikuyu (22%), Luhya (14%), Kalenjin (13%), Luo (11%), Kamba (10%), and Maasai (2%). Despite diversity, Swahili and English unite the nation. Tribes maintain cultural practices while embracing modern Kenya.", "source": "kenya.go.ke", "category": "culture", "region": "General", "destination": "Kenya"},
    
    {"content": "The Maasai are Kenya's most famous tribe, known for red shuka robes, beaded jewelry, cattle-herding lifestyle, and distinctive jumping dance (adumu). Many Maasai work as safari guides and run cultural villages. Maasai Mara is named after them. They maintain traditional ways while adapting to modernity.", "source": "magicalkenya.com", "category": "culture", "region": "General", "destination": "Kenya"},
    
    {"content": "Maasai village visits: Available near Masai Mara, Amboseli, and Nairobi. Cost: $20-30 per person. Experience includes traditional dances, fire-making demonstration, visiting homes (manyattas), learning about customs, and opportunity to buy beadwork. Ask permission before photographing. Best arranged through your lodge.", "source": "magicalkenya.com", "category": "culture", "region": "General", "destination": "Kenya"},
    
    {"content": "Nyama Choma (roasted meat) is Kenya's national dish - goat or beef slow-roasted over charcoal. Served with ugali and kachumbari (tomato-onion salsa). Best enjoyed at local joints: Carnivore Restaurant (Nairobi), Amaica (Mombasa), or any roadside 'choma' spot. Always fresh - meat selected before cooking.", "source": "magicalkenya.com", "category": "culture", "region": "General", "destination": "Kenya"},
    
    {"content": "Ugali is Kenya's staple food - a stiff porridge made from maize flour. Eaten by hand, used to scoop up stews and vegetables. Every Kenyan meal includes ugali. Similar to fufu in West Africa or sadza in Zimbabwe. It's filling, cheap, and the base of Kenyan cuisine.", "source": "magicalkenya.com", "category": "culture", "region": "General", "destination": "Kenya"},
    
    {"content": "Swahili cuisine on the coast reflects Arab, Indian, and African influences. Key dishes: pilau (spiced rice), biryani (layered rice and meat), samosa, mishkaki (kebabs), maharagwe (bean stew), and coconut fish curry. Coastal food uses more spices, coconut, and seafood than upcountry cuisine.", "source": "magicalkenya.com", "category": "culture", "region": "Coast", "destination": "Kenya"},
    
    {"content": "Kenyan breakfast: Mandazi (sweet fried dough, like doughnuts), chapati (flatbread), chai (spiced tea with milk), eggs, fruit. Safari lodges offer full English breakfast. Local option: uji (porridge) with milk and sugar. Coffee from Mount Kenya region is excellent.", "source": "magicalkenya.com", "category": "culture", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenyan drinks: Tusker is the national beer (lager, 4.2%). Other beers: White Cap, Summit, Pilsner. Dawa cocktail (vodka, lime, honey) is popular at safari lodges. Fresh fruit juices everywhere. Chai (sweet milky tea) is served constantly. Passion fruit juice is a favorite.", "source": "magicalkenya.com", "category": "culture", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenyan coffee is world-renowned. Coffee grows on Mount Kenya, Aberdares, and Taita Hills. AA grade is the highest. Visit coffee plantations near Nairobi (Karen, Ruiru) for tours and tastings. Dormans and Java House are popular café chains. Kenyan coffee is bright, acidic, with berry notes.", "source": "coffee.co.ke", "category": "culture", "region": "Central", "destination": "Kenya"},
    
    {"content": "Kenya tea: Kenya is the world's third-largest tea producer. Tea grows in the highlands - Kericho is the center. Kenyan tea is black, typically served with milk and sugar. Visit Kericho tea estates for tours. Tea auctions in Mombasa. Kenya tea is strong and favors breakfast blends.", "source": "teaboard.or.ke", "category": "culture", "region": "Western", "destination": "Kenya"},
    
    {"content": "Maasai Market is a rotating open-air market in Nairobi selling crafts, jewelry, fabrics, and souvenirs. Locations: Village Market (Friday), Yaya Centre (Wednesday), Junction Mall (Tuesday), High Court (Tuesday). Bargaining expected - start at 50% of asking price. Cash only.", "source": "magicalkenya.com", "category": "culture", "region": "Nairobi", "destination": "Nairobi"},
    
    {"content": "Kenyan music: Popular genres include Benga (originated from Luo community), Genge, Kapuka, and gospel. Contemporary artists: Sauti Sol, Nyashinski, Otile Brown. Traditional instruments: nyatiti (string instrument), drums, flutes. Safari lodges often feature traditional performances.", "source": "magicalkenya.com", "category": "culture", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenyan art: Nairobi has a thriving art scene. Galleries: GoDown Arts Centre, One Off Gallery, Circle Art Gallery. Look for Maasai beadwork, Kisii soapstone carvings, Kamba wood carvings, and kikoy fabrics. Village Market and Maasai Market sell crafts. Matatu art (decorated minibuses) is unique to Kenya.", "source": "magicalkenya.com", "category": "culture", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenyan dress code: Kenya is relatively conservative. Women should cover shoulders and knees in rural areas and at cultural sites. Coastal areas (especially Lamu) require modest dress due to Muslim culture. Safari wear is casual. Nairobi nightlife allows Western fashion.", "source": "magicalkenya.com", "category": "culture", "region": "General", "destination": "Kenya"},
    
    {"content": "Photography etiquette: Always ask permission before photographing people. Some expect a small payment (50-100 KES). Never photograph military installations, government buildings, or airports. Ask before photographing Maasai - usually included in village visit fee. National parks have no restrictions on wildlife photography.", "source": "magicalkenya.com", "category": "culture", "region": "General", "destination": "Kenya"},

    # ═══════════════════════════════════════════════════════════════════════════
    # WILDLIFE & BIRDING (15 documents)
    # ═══════════════════════════════════════════════════════════════════════════
    
    {"content": "The Big Five: Lion, Leopard, Elephant, Buffalo, and Rhino. The term originated from hunting difficulty. All five found in Masai Mara, Lake Nakuru, Ol Pejeta, and Lewa. Tsavo and Amboseli have four (no rhinos in main areas). Most safari-goers aim to see all five.", "source": "kws.go.ke", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "African elephants in Kenya: Approximately 35,000 elephants, Africa's third-largest population. Best viewing: Amboseli (large herds with Kilimanjaro), Tsavo (red elephants), Samburu (desert-adapted), and Mara. Kenya lost 70% of elephants to poaching 1970s-90s but populations are recovering.", "source": "kws.go.ke", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Lions in Kenya: Approximately 2,000 lions remain. Best viewing: Masai Mara (highest density, large prides), Amboseli (against Kilimanjaro backdrop), Nairobi NP (close-up views), and Tsavo. Kenya's lion population has declined 70% in 50 years due to human-wildlife conflict and habitat loss.", "source": "kws.go.ke", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Leopards are solitary and secretive but Kenya offers excellent sightings. Best locations: Masai Mara (especially Mara North Conservancy), Samburu (relaxed leopards along river), Lake Nakuru (rocky outcrops). Night drives increase chances. Leopards often rest in trees during daytime.", "source": "kws.go.ke", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Cheetahs are easier to spot than leopards, preferring open savanna. Kenya has approximately 1,200 cheetahs. Best viewing: Masai Mara (open plains), Amboseli, and Lewa Conservancy (highest density). Cheetahs are diurnal - active during daytime, especially early morning.", "source": "kws.go.ke", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Rhinos in Kenya: Black rhinos (critically endangered, ~750 in Kenya) and white rhinos (~500). Best viewing: Ol Pejeta (including last 2 northern white rhinos), Lake Nakuru Sanctuary, Lewa Conservancy, Nairobi NP. Most rhino areas are fenced sanctuaries with armed protection.", "source": "kws.go.ke", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Giraffes in Kenya: Three subspecies - Maasai giraffe (common, dark patches), reticulated giraffe (northern Kenya, geometric pattern), and Rothschild's giraffe (endangered, cream patches, only ~1,600 remain). See Rothschild's at Giraffe Centre Nairobi, Lake Nakuru, and Lake Baringo.", "source": "kws.go.ke", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenya hippos: Common in rivers and lakes. Best viewing: Masai Mara (Mara River), Lake Naivasha (boat rides), Mzima Springs (underwater viewing), and coastal rivers. Hippos are Africa's most dangerous large animal - never approach on foot. They're active at night, grazing on land.", "source": "kws.go.ke", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Zebras in Kenya: Common zebra (throughout southern Kenya) and Grevy's zebra (endangered, northern Kenya only - Samburu, Lewa, Laikipia). Grevy's is larger with narrow stripes and round ears. During migration, 400,000 zebras accompany wildebeest in the Mara.", "source": "kws.go.ke", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenya crocodiles: Nile crocodiles up to 5 meters long. Best viewing: Mara River (migration crossings), Tsavo's Galana River, Samburu's Ewaso Ng'iro River, and Lake Turkana (highest density). Never swim in crocodile waters. Mzima Springs offers underwater viewing.", "source": "kws.go.ke", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenya birdlife: Over 1,100 bird species recorded - more than all of Europe. Endemic species: Sharpe's longclaw, Hinde's babbler, Tana River cisticola. Best birding: Lake Baringo (450+ species), Kakamega Forest (350+ species), Rift Valley lakes for flamingos and waterbirds.", "source": "kws.go.ke", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Flamingos in Kenya: Lesser flamingos (pink, smaller) and greater flamingos (white-pink, larger). Best viewing: Lake Nakuru, Lake Bogoria, Lake Magadi. Numbers fluctuate with water levels and algae. Peak season varies - check conditions. Millions of flamingos create unforgettable pink-tinged lakeshores.", "source": "kws.go.ke", "category": "safari", "region": "Rift Valley", "destination": "Kenya"},
    
    {"content": "Fish eagles are iconic Kenya birds with distinctive cry. Common at lakes and rivers - Lake Naivasha, Lake Baringo, Ewaso Ng'iro River. The African fish eagle is similar to America's bald eagle. Watch for spectacular dives to catch fish. Often perched in waterside trees.", "source": "kws.go.ke", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Secretary bird is a unique raptor that hunts on foot, stomping snakes and small animals. Common in Masai Mara, Amboseli, and open savanna areas. Named for quill-like head feathers resembling old-fashioned secretaries. Standing over 4 feet tall with long legs.", "source": "kws.go.ke", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Lilac-breasted roller is East Africa's most colorful bird with turquoise, lilac, and blue plumage. Common throughout Kenya's parks. Often perches on branches or wires. The bird performs aerobatic rolling flights during courtship - hence the name. Kenya's unofficial national bird.", "source": "kws.go.ke", "category": "safari", "region": "General", "destination": "Kenya"},

    # ═══════════════════════════════════════════════════════════════════════════
    # SAMPLE ITINERARIES (10 documents)
    # ═══════════════════════════════════════════════════════════════════════════
    
    {"content": "Classic Kenya Safari (7 days): Day 1: Arrive Nairobi, overnight Karen. Days 2-3: Masai Mara (fly in), game drives, migration if in season. Days 4-5: Lake Nakuru or Amboseli (drive). Day 6: Nairobi for David Sheldrick, Giraffe Centre. Day 7: Depart. Cost: $2,500-5,000 per person.", "source": "magicalkenya.com", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Bush and Beach (10 days): Days 1-3: Masai Mara safari (fly in). Day 4: Fly to Mombasa, transfer Diani. Days 5-9: Diani Beach - relax, water sports, day trips. Day 10: Fly Mombasa-Nairobi-home. Combines wildlife and Indian Ocean relaxation. Cost: $3,000-6,000 per person.", "source": "magicalkenya.com", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Northern Kenya Explorer (8 days): Day 1: Nairobi. Days 2-3: Ol Pejeta (rhinos, chimps). Days 4-6: Samburu (Special Five, leopards). Day 7: Mount Kenya region or Lake Nakuru. Day 8: Nairobi and depart. Less crowded than southern circuit. Cost: $3,000-5,500 per person.", "source": "magicalkenya.com", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Budget Kenya (7 days): Day 1: Nairobi sightseeing. Days 2-3: Lake Nakuru and Lake Naivasha (drive, budget accommodation). Days 4-5: Masai Mara (budget camping safari). Day 6: Return Nairobi. Day 7: Depart. Group safaris and camping reduce costs. Budget: $1,000-1,500 per person.", "source": "magicalkenya.com", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Honeymoon Kenya (10 days): Day 1: Arrive Nairobi, luxury hotel. Days 2-4: Masai Mara (luxury tented camp, balloon safari). Days 5-6: Amboseli (romantic views of Kilimanjaro). Days 7-10: Lamu Island or Diani Beach (private villa). Ultimate romance. Cost: $6,000-15,000 per person.", "source": "magicalkenya.com", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Family Safari (7 days): Day 1: Nairobi - Giraffe Centre, Sheldrick Trust. Days 2-3: Amboseli (family-friendly lodges, elephant focus). Days 4-5: Tsavo (train ride from Nairobi, red elephants). Day 6-7: Diani Beach (family resorts). Children enjoy elephants, beaches. Cost: $2,500-4,500 per person.", "source": "magicalkenya.com", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Migration Safari (5 days): Best July-October. Days 1-4: Masai Mara (fly in, stay near Mara River, multiple game drives). Day 5: Return Nairobi. Focus entirely on migration - river crossings, predator action. Book 6+ months ahead for best lodges. Cost: $3,000-7,000 per person.", "source": "magicalkenya.com", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Adventure Kenya (10 days): Day 1: Nairobi. Days 2-3: Mount Kenya trek (Point Lenana). Day 4: Rest, Nanyuki. Days 5-6: Samburu (walking safaris). Day 7: Lake Naivasha (cycling Hell's Gate). Days 8-9: Masai Mara (game drives). Day 10: Depart. Active travelers. Cost: $2,500-4,500 per person.", "source": "magicalkenya.com", "category": "adventure", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenya and Tanzania Combined (14 days): Days 1-3: Masai Mara. Days 4-5: Cross to Serengeti (Tanzania). Days 6-7: Ngorongoro Crater. Day 8: Lake Manyara or Tarangire. Days 9-10: Zanzibar. Days 11-13: Return via Nairobi or direct flight home. See migration from both sides. Cost: $5,000-10,000 per person.", "source": "magicalkenya.com", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Long Weekend Nairobi (3 days): Day 1: Nairobi National Park sunrise safari, Sheldrick Trust (11 AM), Giraffe Centre (2 PM), Karen Blixen Museum. Day 2: Day trip to Lake Naivasha and Hell's Gate. Day 3: Shopping (Maasai Market, Village Market), National Museum, depart. Cost: $500-1,000 per person.", "source": "magicalkenya.com", "category": "safari", "region": "Nairobi", "destination": "Nairobi"},

    # ═══════════════════════════════════════════════════════════════════════════
    # SAFARI LOGISTICS & COSTS (10 documents)
    # ═══════════════════════════════════════════════════════════════════════════
    
    {"content": "Safari vehicle types: Standard 4x4 Land Cruiser or Land Rover with pop-up roof (6-7 passengers). Private vehicle costs more but offers flexibility. Shared vehicles are cheaper but fixed schedule. Minibuses are cheapest but limited off-road. Custom photography vehicles have 360° views.", "source": "magicalkenya.com", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Accommodation types: Luxury lodges ($500-2,000/night) - permanent structures with all amenities. Tented camps ($300-800/night) - canvas tents with en-suite bathrooms. Mobile camps ($400-1,000/night) - follow migration. Budget camping ($50-150/night) - basic tents or public campsites.", "source": "magicalkenya.com", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Safari costs breakdown: Park fees (25-30% of cost), accommodation (40-50%), transport (15-20%), guide and crew (10-15%). Budget safaris: $150-250/day. Mid-range: $350-550/day. Luxury: $700-1,500+/day. Prices per person sharing. Single supplement adds 30-50%.", "source": "magicalkenya.com", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Flying vs driving safaris: Internal flights save time but cost more ($150-350 per sector). Driving is cheaper and allows flexibility, wildlife viewing en route. Drive times: Nairobi-Mara (5-6 hours), Nairobi-Amboseli (4-5 hours), Nairobi-Samburu (5-6 hours). Fly if time is limited.", "source": "magicalkenya.com", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Group vs private safari: Group safaris (4-8 people) cost 30-50% less but less flexible. Private safaris offer customized itinerary, pace, and photography stops. Families and serious photographers should book private. Solo travelers can join group departures.", "source": "magicalkenya.com", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Safari booking timeline: Peak season (July-October, December-January) book 6-12 months ahead for best lodges. Shoulder season (February-March, June, November) book 3-6 months ahead. Low season (April-May) book 1-3 months ahead. Last-minute deals available but limited choice.", "source": "magicalkenya.com", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Safari luggage: Most internal flights allow only 15-20 kg in soft bags. Hard suitcases not permitted on small planes. Pack light - lodges have laundry service. Essential: camera gear, binoculars, layers, neutral clothing, toiletries, medications. Leave valuable jewelry at home.", "source": "magicalkenya.com", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Children on safari: Most lodges welcome children 5+, some 8+. Family-friendly camps have special programs. Game drives can be long for young children. Consider: shorter drives, swimming pools, Sheldrick Trust visit, Giraffe Centre. Some lodges offer babysitting.", "source": "magicalkenya.com", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Photography safaris: Specialized trips with photography guides, extended hours, and custom vehicles with camera mounts. Best months: February (great light, calving), August-September (migration), November (dramatic skies). Budget 3-4 days minimum in each location.", "source": "magicalkenya.com", "category": "safari", "region": "General", "destination": "Kenya"},
    
    {"content": "Walking and horseback safaris: Available in conservancies and some parks (not Masai Mara main reserve). Walking safaris with armed rangers offer intimate wildlife experience. Horseback safaris in Laikipia and Chyulu Hills. Hot air balloons in Masai Mara ($450-550). Night drives in conservancies.", "source": "magicalkenya.com", "category": "safari", "region": "General", "destination": "Kenya"},

    # ═══════════════════════════════════════════════════════════════════════════
    # KENYAN FOOD & CUISINE (15 documents)
    # ═══════════════════════════════════════════════════════════════════════════
    
    {"content": "Nyama Choma is Kenya's national dish - grilled meat, typically goat or beef, slow-roasted over hot coals. Best enjoyed with ugali (cornmeal porridge) and kachumbari (fresh tomato-onion salad). Popular spots in Nairobi: Carnivore Restaurant, Ranalo Foods, and roadside joints in Kikuyu. Cost: 500-1,500 KES per person.", "source": "magicalkenya.com", "category": "food", "region": "General", "destination": "Kenya"},
    
    {"content": "Ugali is Kenya's staple food - a thick cornmeal porridge formed into a dense, dough-like ball. Eaten with hands by pinching off a piece, forming an indent, and scooping stew. Served with sukuma wiki (collard greens), beef stew, or fish. Found everywhere from street vendors to high-end restaurants. 50-200 KES.", "source": "magicalkenya.com", "category": "food", "region": "General", "destination": "Kenya"},
    
    {"content": "Sukuma Wiki means 'stretch the week' in Swahili - affordable collard greens sautéed with onions and tomatoes. The most common vegetable in Kenya, served alongside ugali and meat. Rich in vitamins, cheap (20-50 KES/bunch), and found in every Kenyan home and restaurant.", "source": "magicalkenya.com", "category": "food", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenyan Pilau is aromatic spiced rice cooked with meat (usually beef or chicken), cumin, cardamom, cinnamon, and cloves. Coastal pilau has coconut milk. Best in Mombasa's Old Town, Swahili restaurants. Often served at celebrations. Street food version: 150-300 KES, restaurant: 500-1,000 KES.", "source": "magicalkenya.com", "category": "food", "region": "Coast", "destination": "Mombasa"},
    
    {"content": "Swahili cuisine in coastal Kenya blends African, Arab, Indian, and Portuguese influences. Signature dishes: biryani, samosas, bhajia (spiced potato fritters), mahamri (coconut donuts), mshikaki (meat skewers), and fish in coconut curry. Best experienced in Mombasa Old Town and Lamu.", "source": "magicalkenya.com", "category": "food", "region": "Coast", "destination": "Mombasa"},
    
    {"content": "Kenyan breakfast favorites: Mandazi (sweet fried dough), chai (spiced tea with milk), eggs and toast, or chapati (flatbread). Hotels serve continental and English breakfast. Street breakfast: 50-150 KES. Java House (chain): 400-800 KES. Most Kenyans drink sweet milky tea.", "source": "magicalkenya.com", "category": "food", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenyan street food: Mutura (African sausage), roasted maize, chips mayai (omelette with fries), samosas, smokies (hot dogs), mandazi, kashata (coconut candy). Safe to eat from busy stalls with high turnover. Cost: 20-200 KES per item. Best areas: downtown Nairobi, markets.", "source": "magicalkenya.com", "category": "food", "region": "General", "destination": "Nairobi"},
    
    {"content": "Carnivore Restaurant in Nairobi is world-famous for its all-you-can-eat grilled meat experience. Waiters bring endless skewers of beef, lamb, pork, chicken, and exotic meats (ostrich, crocodile). Price: 4,500 KES ($35) adults. Located in Langata. Book ahead on weekends.", "source": "magicalkenya.com", "category": "food", "region": "Nairobi", "destination": "Nairobi"},
    
    {"content": "Tusker is Kenya's most popular beer, brewed since 1922. Named after an elephant that killed the founder's partner. Other local beers: White Cap, Pilsner. Local spirits: Kenya Cane (rum), KWAL vodka. Sundowner drinks at safari lodges are a tradition. Supermarket beer: 200 KES, bar: 300-500 KES.", "source": "magicalkenya.com", "category": "food", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenyan coffee is world-renowned, grown on the slopes of Mount Kenya and in the highlands. Look for AA grade beans. Best coffee shops in Nairobi: Artcaffe, Java House, Nairobi Street Kitchen, Sierra Brasserie. Coffee farms offer tours around Thika and Ruiru. Factory direct: 500-1,000 KES per 250g.", "source": "magicalkenya.com", "category": "food", "region": "Central", "destination": "Kenya"},
    
    {"content": "Fresh tropical fruits in Kenya: mangoes (December-March), pineapples, passion fruit, tree tomatoes, custard apples, jackfruit, coconuts. Best at local markets - much cheaper than supermarkets. Gikomba Market and City Market in Nairobi. Beach vendors sell fresh coconuts (50-100 KES).", "source": "magicalkenya.com", "category": "food", "region": "General", "destination": "Kenya"},
    
    {"content": "Nairobi restaurant scene: Upscale options include Talisman (fusion), Tamarind (seafood), Habesha (Ethiopian), and Mediterraneo. Mid-range: About Thyme, Artcaffe, Brew Bistro. Budget: Java House, local hotels serving Kenyan food. Food delivery apps: Glovo, Uber Eats, Jumia Food.", "source": "magicalkenya.com", "category": "food", "region": "Nairobi", "destination": "Nairobi"},
    
    {"content": "Fish in Kenya: Tilapia from Lake Victoria is the most popular - fried whole and served with ugali. Lake Turkana has excellent Nile perch. Coastal Kenya offers fresh seafood: prawns, lobster, crab, and various fish. Swahili fish curry with coconut is a coastal specialty.", "source": "magicalkenya.com", "category": "food", "region": "General", "destination": "Kenya"},
    
    {"content": "Vegetarian food in Kenya: Indian restaurants offer extensive vegetarian options. Kenyan traditional vegetables: sukuma wiki, managu (African nightshade), terere, and kunde (cowpeas). Ethiopian restaurants serve vegetarian platters. Hindu temple langars provide free vegetarian meals. Most lodges accommodate dietary needs.", "source": "magicalkenya.com", "category": "food", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenyan chai is spiced black tea boiled with milk, sugar, ginger, and cardamom. Served everywhere from street vendors (10-30 KES) to lodges. Dawa (Swahili for 'medicine') is a honey-ginger-lime drink, sometimes with vodka. Fresh fruit juices are excellent - try passion fruit or tree tomato.", "source": "magicalkenya.com", "category": "food", "region": "General", "destination": "Kenya"},

    # ═══════════════════════════════════════════════════════════════════════════
    # BUDGET TRAVEL TIPS (12 documents)
    # ═══════════════════════════════════════════════════════════════════════════
    
    {"content": "Budget safari options: Join group tours to share costs. Stay in budget camps or bandas ($50-100/night). Self-drive in your own or rented vehicle. Visit less touristy parks (Tsavo, Samburu vs Masai Mara). Travel in low season (April-May, November). Budget: $150-250/day all-inclusive.", "source": "magicalkenya.com", "category": "budget", "region": "General", "destination": "Kenya"},
    
    {"content": "Cheap transport in Kenya: Matatus (shared minibuses) cost 50-500 KES for most routes. Boda-bodas (motorcycle taxis) for short distances (50-200 KES). SGR train Nairobi-Mombasa economy class: 1,000 KES. Inter-city buses: 1,500-2,500 KES. Only use marked taxis or Uber/Bolt.", "source": "magicalkenya.com", "category": "budget", "region": "General", "destination": "Kenya"},
    
    {"content": "Budget accommodation in Nairobi: Hostels (Wildebeest Camp, Jungle Junction) $15-25/night. Budget hotels (Silver Springs, Nairobi Transit) $30-50/night. Airbnb apartments $25-60/night. Backpacker areas: Westlands, South B/C. Avoid very cheap central hotels - safety issues.", "source": "magicalkenya.com", "category": "budget", "region": "Nairobi", "destination": "Nairobi"},
    
    {"content": "Free and cheap activities in Nairobi: Karura Forest (600 KES entry), Arboretum (100 KES), Uhuru Gardens (Free), city walking tours, window shopping at Village Market, Maasai Market (varies by day), National Archives (free). Most museums under 500 KES for residents.", "source": "magicalkenya.com", "category": "budget", "region": "Nairobi", "destination": "Nairobi"},
    
    {"content": "Budget beach holidays: Diani has guesthouses from $30/night. Watamu backpacker hostels from $15/night. Eat at local restaurants (200-500 KES meals) instead of hotel restaurants. Public beaches are free. Shared snorkeling trips cost half of private ones. Travel via bus instead of flying.", "source": "magicalkenya.com", "category": "budget", "region": "Coast", "destination": "Diani Beach"},
    
    {"content": "Eating cheap in Kenya: Local hotels (restaurants) serve ugali, stew, vegetables for 150-300 KES. Street food even cheaper (50-150 KES). Supermarkets for snacks and water. Avoid tourist restaurants in safari lodges. Naivas and Quickmart supermarkets have best prices.", "source": "magicalkenya.com", "category": "budget", "region": "General", "destination": "Kenya"},
    
    {"content": "Money-saving tips: Get local SIM card (Safaricom M-Pesa for mobile money). Withdraw cash at ATMs (lower fees than exchange bureaus). Bargain at markets (start at 50% of asking price). Book directly with local operators. Travel with a group to share costs.", "source": "magicalkenya.com", "category": "budget", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenya budget itinerary (7 days, under $500): Day 1-2: Nairobi (budget hotel $30/night, Giraffe Centre $15, Sheldrick Trust free). Days 3-4: Naivasha/Hell's Gate ($50/day camping, cycling). Days 5-6: Budget Masai Mara camping safari ($150/day). Day 7: Return Nairobi.", "source": "magicalkenya.com", "category": "budget", "region": "General", "destination": "Kenya"},
    
    {"content": "Self-drive safaris can save money: Rent a 4x4 ($80-150/day) and drive yourself. Many parks allow self-drive. Fuel costs ~150 KES/liter. Book KWS bandas ($30-75/night) instead of lodges. Bring your own food and cook at campsites. Total savings: 40-60% vs organized tours.", "source": "magicalkenya.com", "category": "budget", "region": "General", "destination": "Kenya"},
    
    {"content": "Low season travel: April-May and November have 30-50% lower prices. Fewer tourists, more availability. Downsides: some rain, some roads impassable, migration not in Mara. Upside: green landscapes, bird watching, dramatic skies for photography, baby animals.", "source": "magicalkenya.com", "category": "budget", "region": "General", "destination": "Kenya"},
    
    {"content": "Kenyan resident rates: If you have a work permit or resident visa, you qualify for citizen rates at national parks (80% cheaper than tourist rates). Some lodges offer resident rates too. Bring your residence permit or Kenyan ID to gate.", "source": "magicalkenya.com", "category": "budget", "region": "General", "destination": "Kenya"},
    
    {"content": "Budget vs mid-range vs luxury safari comparison: Budget (camping, group tours): $150-250/day. Mid-range (comfortable lodges, private vehicle): $350-550/day. Luxury (exclusive camps, flying): $700-1,500/day. Budget safaris see the same wildlife - it's the accommodation and service that differ.", "source": "magicalkenya.com", "category": "budget", "region": "General", "destination": "Kenya"},

    # ═══════════════════════════════════════════════════════════════════════════
    # HIDDEN GEMS & OFF-BEATEN PATH (10 documents)
    # ═══════════════════════════════════════════════════════════════════════════
    
    {"content": "Chyulu Hills National Park is an underrated gem - volcanic hills with lush green landscapes, views of Kilimanjaro, underground lava tube caves. Few visitors. Activities: walking safaris, horseback riding, cave exploration. Accommodation: Campi ya Kanzi, Ol Donyo Lodge. 150 km from Nairobi.", "source": "kws.go.ke", "category": "safari", "region": "Rift Valley", "destination": "Chyulu Hills"},
    
    {"content": "Marsabit National Park in northern Kenya offers stark desert beauty, crater lakes, and unique forest in the desert. Home to some of the largest elephants in Africa. Few tourists, authentic wilderness. Best combined with Lake Turkana. 4WD essential. June-October best.", "source": "kws.go.ke", "category": "safari", "region": "Northern", "destination": "Marsabit"},
    
    {"content": "Kakamega Forest is Kenya's only tropical rainforest, a remnant of the great Congo forest. 380+ bird species, primates (colobus monkeys, blue monkeys), butterflies, rare plants. Budget: guesthouses from $20/night. Guided walks available. Best for bird watchers and nature lovers.", "source": "kws.go.ke", "category": "adventure", "region": "Western", "destination": "Kakamega"},
    
    {"content": "Meru National Park, where Joy and George Adamson released Elsa the lioness (Born Free). Less crowded than Masai Mara but equally beautiful with similar wildlife. Unique animals: reticulated giraffe, Grevy's zebra, Somali ostrich. Excellent rhino sanctuary.", "source": "kws.go.ke", "category": "safari", "region": "Central", "destination": "Meru"},
    
    {"content": "Rusinga Island in Lake Victoria is a hidden gem - prehistoric fossils, birdwatching, fishing, and peaceful atmosphere. Rusinga Island Lodge offers exclusive experience. Accessible by road or boat. Famous for Homo erectus fossil discovery. Traditional Luo culture.", "source": "magicalkenya.com", "category": "adventure", "region": "Western", "destination": "Lake Victoria"},
    
    {"content": "Matthews Range in northern Kenya is known as 'Kenya's last wilderness'. Walking safaris with Samburu guides, forest elephants, wild dogs. Very few tourists. Community conservancies like Namunyak offer authentic cultural immersion. Remote but rewarding.", "source": "magicalkenya.com", "category": "adventure", "region": "Northern", "destination": "Matthews Range"},
    
    {"content": "Ol Pejeta Conservancy near Nanyuki is perfect for rhino lovers. Home to the last two northern white rhinos and largest black rhino sanctuary in East Africa. Chimpanzee sanctuary (only chimps in Kenya). Night drives, walking safaris available. 200 km north of Nairobi.", "source": "kws.go.ke", "category": "safari", "region": "Central", "destination": "Ol Pejeta"},
    
    {"content": "Aberdare National Park offers unique mountain ecosystems, waterfalls, and rare animals like bongo antelope. The Ark and Treetops lodges offer animal viewing from elevated hideouts at waterholes. Cool climate, forest drives, fishing. Good for combining with Mount Kenya area.", "source": "kws.go.ke", "category": "safari", "region": "Central", "destination": "Aberdares"},
    
    {"content": "Watamu Marine National Park north of Mombasa has some of the best snorkeling and diving on the East African coast. Whale sharks (October-March), manta rays, sea turtles. Less developed than Diani. Gede Ruins nearby for history. Good budget beach option.", "source": "kws.go.ke", "category": "beach", "region": "Coast", "destination": "Watamu"},
    
    {"content": "Saiwa Swamp National Park is Kenya's smallest park (3 sq km) and the only place to see sitatunga, a rare semi-aquatic antelope. Walking safaris only, no vehicles. Boardwalks over swamp. De Brazza's monkey, giant forest squirrel. Budget-friendly, near Kitale in western Kenya.", "source": "kws.go.ke", "category": "adventure", "region": "Western", "destination": "Saiwa Swamp"},
]


def populate_massive_database():
    """Add comprehensive Kenya travel data to the vector database."""
    print("=" * 70)
    print("🐘 TEMBO AI - MASSIVE Kenya Knowledge Base Population")
    print("=" * 70)
    
    current_count = get_document_count()
    print(f"\nCurrent documents in database: {current_count}")
    
    # Skip if already populated (for server)
    if current_count >= 200:
        return {"status": "already_populated", "documents": current_count}
    
    if current_count > 0:
        clear_knowledge_base()
        print("Database cleared.")
    
    print(f"\nPreparing to add {len(MASSIVE_KENYA_DATA)} documents...")
    print("This is a comprehensive knowledge base covering:")
    print("  • National Parks & Reserves")
    print("  • Beaches & Coastal Areas")
    print("  • Wildlife & Birding")
    print("  • Culture & Cuisine")
    print("  • Practical Travel Info")
    print("  • Sample Itineraries")
    print("  • Safari Logistics")
    
    # Extract texts and metadata
    texts = [doc["content"] for doc in MASSIVE_KENYA_DATA]
    metadatas = [
        {
            "source": doc["source"],
            "category": doc["category"],
            "region": doc["region"],
            "destination": doc["destination"],
        }
        for doc in MASSIVE_KENYA_DATA
    ]
    
    # Add in batches to avoid memory issues
    batch_size = 50
    total_added = 0
    
    print(f"\nEmbedding and inserting documents in batches of {batch_size}...")
    
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i+batch_size]
        batch_meta = metadatas[i:i+batch_size]
        count = add_documents_simple(batch_texts, batch_meta)
        total_added += count
        print(f"  Batch {i//batch_size + 1}: Added {count} documents (Total: {total_added})")
    
    final_count = get_document_count()
    print(f"\n{'='*70}")
    print(f"✅ Successfully added {total_added} documents!")
    print(f"📚 Total documents in database: {final_count}")
    
    # Print summary by category
    print("\n📊 Documents by category:")
    categories = {}
    for doc in MASSIVE_KENYA_DATA:
        cat = doc["category"]
        categories[cat] = categories.get(cat, 0) + 1
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"   {cat}: {count}")
    
    # Print summary by destination
    print("\n🗺️  Top destinations covered:")
    destinations = {}
    for doc in MASSIVE_KENYA_DATA:
        dest = doc["destination"]
        destinations[dest] = destinations.get(dest, 0) + 1
    for dest, count in sorted(destinations.items(), key=lambda x: -x[1])[:15]:
        print(f"   {dest}: {count}")
    
    print(f"\n{'='*70}")
    print("🎉 Comprehensive knowledge base ready!")
    print(f"{'='*70}")
    
    return {"status": "populated", "documents_added": total_added, "total_documents": final_count}


if __name__ == "__main__":
    populate_massive_database()
