"""
scrape_kenya_data.py
Scrapes Kenya travel data from various sources and populates the vector database.

Sources:
- Kenya Wildlife Service (kws.go.ke)
- Kenya Tourism Board
- Manual curated data

Run: python scrape_kenya_data.py
"""

import requests
from bs4 import BeautifulSoup
from vector_store import add_documents_simple, get_document_count, clear_knowledge_base
import time

# ── Headers for web scraping ────────────────────────────────────────────────────
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


def scrape_url(url: str) -> str:
    """Fetch and extract text from a URL."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Remove script and style elements
        for element in soup(["script", "style", "nav", "footer", "header"]):
            element.decompose()
        
        text = soup.get_text(separator=" ", strip=True)
        return text[:5000]  # Limit text length
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""


# ── Curated Kenya Travel Data ───────────────────────────────────────────────────
# Since live scraping may fail, we include comprehensive curated data

KENYA_TRAVEL_DATA = [
    # ═══════════════════════════════════════════════════════════════════════════
    # NATIONAL PARKS & RESERVES
    # ═══════════════════════════════════════════════════════════════════════════
    
    # Masai Mara
    {
        "content": "Masai Mara National Reserve is Kenya's most famous safari destination, located in the southwestern part of Kenya along the Tanzanian border. It covers 1,510 square kilometers of open savanna grassland. Entry fees: $80 USD per adult per day for non-residents, $30 USD for East African residents. Children under 12 pay $45 USD. The reserve is home to the Big Five: lions, leopards, elephants, buffalo, and rhinos.",
        "source": "kws.go.ke",
        "category": "safari",
        "region": "Rift Valley",
        "destination": "Masai Mara"
    },
    {
        "content": "The Great Wildebeest Migration is the world's largest animal migration, occurring annually in the Masai Mara. Between July and October, approximately 1.5 million wildebeest, 200,000 zebras, and 350,000 gazelles cross from Tanzania's Serengeti into Kenya's Masai Mara. The dramatic Mara River crossings, where crocodiles await, are a highlight. Best viewing months are August and September.",
        "source": "kws.go.ke",
        "category": "safari",
        "region": "Rift Valley",
        "destination": "Masai Mara"
    },
    {
        "content": "Masai Mara offers excellent game drives year-round. Morning game drives start at 6:00 AM when predators are most active. Hot air balloon safaris over the Mara cost approximately $450-500 USD per person and include a champagne breakfast. The reserve has numerous luxury lodges and tented camps. Best time to visit: July-October for migration, January-February for calving season in Serengeti.",
        "source": "magicalkenya.com",
        "category": "safari",
        "region": "Rift Valley",
        "destination": "Masai Mara"
    },
    
    # Amboseli
    {
        "content": "Amboseli National Park is located at the foot of Mount Kilimanjaro, Africa's highest peak. The park covers 392 square kilometers and is famous for its large elephant herds - over 1,500 elephants live here. Entry fee: $60 USD per adult per day for non-residents. The park offers stunning views of Kilimanjaro's snow-capped peak, best seen in the early morning before clouds form.",
        "source": "kws.go.ke",
        "category": "safari",
        "region": "Rift Valley",
        "destination": "Amboseli"
    },
    {
        "content": "Amboseli's elephants are among the most studied in Africa. The Amboseli Elephant Research Project has been running since 1972. Best time to visit Amboseli is during the dry season (June-October) when wildlife concentrates around the swamps. The park has five different habitats: dried-up lake bed, wetlands, savannah, and woodlands. Observation Hill offers panoramic views of the entire park.",
        "source": "kws.go.ke",
        "category": "safari",
        "region": "Rift Valley",
        "destination": "Amboseli"
    },
    
    # Tsavo
    {
        "content": "Tsavo National Park is Kenya's largest park, divided into Tsavo East (13,747 sq km) and Tsavo West (9,065 sq km). Combined, they cover 4% of Kenya's total land area. Entry fee: $52 USD per adult per day. Tsavo is famous for its red elephants - they dust themselves with the park's red volcanic soil. The park is also known for the man-eating lions of Tsavo from 1898.",
        "source": "kws.go.ke",
        "category": "safari",
        "region": "Coast",
        "destination": "Tsavo"
    },
    {
        "content": "Tsavo West features the stunning Mzima Springs, where crystal-clear water supports hippos and crocodiles visible through an underwater viewing chamber. Shetani Lava Flow, a 200-year-old volcanic formation, stretches for 50 km. Tsavo East has the Yatta Plateau, the world's longest lava flow at 290 km. The Galana River runs through Tsavo East, attracting wildlife during dry seasons.",
        "source": "kws.go.ke",
        "category": "safari",
        "region": "Coast",
        "destination": "Tsavo"
    },
    
    # Lake Nakuru
    {
        "content": "Lake Nakuru National Park is famous for its flamingos and rhino sanctuary. The park covers 188 square kilometers around the alkaline Lake Nakuru. Entry fee: $60 USD per adult per day. The lake sometimes hosts over a million flamingos, creating a pink shoreline. The park is a sanctuary for both black and white rhinos, with over 100 individuals.",
        "source": "kws.go.ke",
        "category": "safari",
        "region": "Rift Valley",
        "destination": "Lake Nakuru"
    },
    {
        "content": "Lake Nakuru is one of the best places in Kenya to see rhinos. The park also has lions, leopards, buffalos, and the endangered Rothschild's giraffe. Baboon Cliff offers spectacular views of the lake and park. Best time to visit is during the dry season (June-March) when flamingo numbers peak. The park is only 160 km from Nairobi, making it perfect for a day trip or weekend safari.",
        "source": "kws.go.ke",
        "category": "safari",
        "region": "Rift Valley",
        "destination": "Lake Nakuru"
    },
    
    # Nairobi National Park
    {
        "content": "Nairobi National Park is the only national park in the world located within a capital city. Just 7 km from Nairobi's city center, this 117 square kilometer park is home to lions, leopards, cheetahs, hyenas, buffalos, giraffes, and over 400 bird species. Entry fee: $43 USD per adult per day. The park has a rhino sanctuary and an animal orphanage.",
        "source": "kws.go.ke",
        "category": "safari",
        "region": "Nairobi",
        "destination": "Nairobi National Park"
    },
    {
        "content": "The David Sheldrick Wildlife Trust, located at Nairobi National Park, rescues and rehabilitates orphaned elephants and rhinos. Visitors can adopt an elephant and watch feeding sessions daily at 11:00 AM. Entry: $15 USD. The Giraffe Centre in nearby Langata allows you to feed endangered Rothschild's giraffes. Entry: $15 USD for non-residents.",
        "source": "sheldrickwildlifetrust.org",
        "category": "safari",
        "region": "Nairobi",
        "destination": "Nairobi National Park"
    },
    
    # Samburu
    {
        "content": "Samburu National Reserve is located in northern Kenya along the Ewaso Ng'iro River. The reserve covers 165 square kilometers and is known for the 'Samburu Special Five': Grevy's zebra, Somali ostrich, reticulated giraffe, gerenuk (giraffe gazelle), and beisa oryx. Entry fee: $70 USD per adult per day. The reserve is less crowded than Masai Mara.",
        "source": "kws.go.ke",
        "category": "safari",
        "region": "Northern Kenya",
        "destination": "Samburu"
    },
    {
        "content": "Samburu is famous for Elsa the lioness from 'Born Free' - she was released here. The reserve offers excellent leopard sightings, especially along the riverine forest. The Samburu people are semi-nomadic pastoralists known for their distinctive red clothing and beaded jewelry. Cultural visits to Samburu villages can be arranged. Best time to visit: June-October and January-February.",
        "source": "magicalkenya.com",
        "category": "safari",
        "region": "Northern Kenya",
        "destination": "Samburu"
    },
    
    # Hell's Gate
    {
        "content": "Hell's Gate National Park is unique because visitors can walk and cycle through the park - one of only two Kenyan parks allowing this. Located near Lake Naivasha, the park covers 68 square kilometers. Entry fee: $26 USD per adult per day. The park features dramatic scenery including towering cliffs, water-carved gorges, and geothermal steam vents. It inspired the landscapes in Disney's Lion King.",
        "source": "kws.go.ke",
        "category": "adventure",
        "region": "Rift Valley",
        "destination": "Hell's Gate"
    },
    
    # Mount Kenya
    {
        "content": "Mount Kenya is Africa's second-highest mountain at 5,199 meters and a UNESCO World Heritage Site. The mountain has three main peaks: Batian (5,199m), Nelion (5,188m), and Lenana (4,985m). Point Lenana is accessible to trekkers without technical climbing skills. Park entry: $52 USD per day. The trek to Point Lenana takes 3-5 days. Best climbing months: January-February and August-September.",
        "source": "kws.go.ke",
        "category": "adventure",
        "region": "Central",
        "destination": "Mount Kenya"
    },
    {
        "content": "Mount Kenya National Park offers various trekking routes: Sirimon (easiest), Naro Moru (most popular), and Chogoria (most scenic). Altitude sickness is common, so acclimatization is essential. The mountain has unique Afro-alpine vegetation including giant lobelias and groundsels. Guides are mandatory and cost around $30-50 USD per day. Porters cost $15-20 USD per day.",
        "source": "kws.go.ke",
        "category": "adventure",
        "region": "Central",
        "destination": "Mount Kenya"
    },
    
    # ═══════════════════════════════════════════════════════════════════════════
    # BEACHES
    # ═══════════════════════════════════════════════════════════════════════════
    
    # Diani Beach
    {
        "content": "Diani Beach is Kenya's most famous beach destination, located 30 km south of Mombasa. This 17 km stretch of white sand and turquoise water has been voted Africa's leading beach destination multiple times. The beach offers excellent swimming, snorkeling, diving, kite surfing, and jet skiing. Water temperature averages 26-28°C year-round.",
        "source": "magicalkenya.com",
        "category": "beach",
        "region": "Coast",
        "destination": "Diani Beach"
    },
    {
        "content": "Diani Beach has numerous resorts ranging from budget to luxury. Popular activities include diving at Kisite-Mpunguti Marine Park ($80-100 USD including boat and gear), dolphin watching ($50 USD), and day trips to Wasini Island. The Colobus Conservation center protects the endangered Angolan colobus monkeys. Best time to visit: December-March and June-October (dry seasons).",
        "source": "magicalkenya.com",
        "category": "beach",
        "region": "Coast",
        "destination": "Diani Beach"
    },
    
    # Watamu
    {
        "content": "Watamu is a small coastal town known for its marine national park and pristine beaches. Watamu Marine National Park is one of the best snorkeling and diving spots in Kenya. The coral gardens are home to over 600 fish species, sea turtles, and dolphins. Entry fee: $17 USD. Glass-bottom boat trips cost around $30 USD. The beach is quieter and more laid-back than Diani.",
        "source": "kws.go.ke",
        "category": "beach",
        "region": "Coast",
        "destination": "Watamu"
    },
    {
        "content": "Watamu is famous for the Gede Ruins, a mysterious 12th-century Swahili town abandoned in the 17th century. Entry: $10 USD. The Bio-Ken Snake Farm allows visitors to see various snake species. Watamu offers excellent deep-sea fishing for marlin, sailfish, and tuna. Best time to visit: August-March. Turtle Watch Watamu protects nesting sea turtles on local beaches.",
        "source": "magicalkenya.com",
        "category": "beach",
        "region": "Coast",
        "destination": "Watamu"
    },
    
    # Malindi
    {
        "content": "Malindi is a historic coastal town with a mix of Italian, Portuguese, and Swahili influences. It was a trading post visited by Vasco da Gama in 1498. The Vasco da Gama Pillar, erected in 1498, still stands. Malindi Marine National Park is great for snorkeling. Entry: $17 USD. The town has a strong Italian community and excellent Italian restaurants.",
        "source": "magicalkenya.com",
        "category": "beach",
        "region": "Coast",
        "destination": "Malindi"
    },
    
    # Lamu
    {
        "content": "Lamu Island is a UNESCO World Heritage Site and the oldest continually inhabited town in Kenya, founded in the 14th century. The island has no cars - transport is by donkey, boat, or foot. Lamu Town features Swahili architecture with carved wooden doors and coral stone buildings. The annual Lamu Cultural Festival in November celebrates Swahili culture with dhow races and donkey races.",
        "source": "magicalkenya.com",
        "category": "beach",
        "region": "Coast",
        "destination": "Lamu"
    },
    {
        "content": "Lamu is accessed by flight from Nairobi (1 hour) or Mombasa (30 minutes). Daily flights cost $100-200 USD. Shela Beach is a 12 km stretch of pristine sand, often deserted. Activities include dhow sailing trips, snorkeling, and visiting the Lamu Museum ($5 USD). Accommodation ranges from budget guesthouses ($30/night) to luxury villas ($500+/night). Best time: June-March.",
        "source": "magicalkenya.com",
        "category": "beach",
        "region": "Coast",
        "destination": "Lamu"
    },
    
    # Mombasa
    {
        "content": "Mombasa is Kenya's second-largest city and main coastal hub. Founded by Arab traders over 900 years ago, it blends African, Arab, and European influences. Key attractions include Fort Jesus (built 1593, UNESCO World Heritage Site, entry $12 USD), the Old Town with Swahili architecture, and the iconic Mombasa Tusks on Moi Avenue.",
        "source": "magicalkenya.com",
        "category": "beach",
        "region": "Coast",
        "destination": "Mombasa"
    },
    {
        "content": "Mombasa's north coast beaches include Nyali, Bamburi, and Shanzu, with many all-inclusive resorts. Haller Park (formerly Bamburi Nature Trail) is a rehabilitated quarry turned wildlife sanctuary, entry $20 USD. Mombasa Marine National Park offers glass-bottom boat trips. The city is connected to Nairobi by the SGR train (4.5 hours, $30-50 USD) and flights (1 hour, $80-150 USD).",
        "source": "magicalkenya.com",
        "category": "beach",
        "region": "Coast",
        "destination": "Mombasa"
    },
    
    # ═══════════════════════════════════════════════════════════════════════════
    # LAKES
    # ═══════════════════════════════════════════════════════════════════════════
    
    {
        "content": "Lake Naivasha is a freshwater lake in the Rift Valley, just 90 km from Nairobi. The lake is famous for its hippo population and over 400 bird species. Boat rides cost $30-40 USD per hour. Crescent Island, accessible by boat, allows walking safaris among zebras, giraffes, and wildebeest. Entry: $30 USD. The area has excellent flower farms and geothermal sites.",
        "source": "magicalkenya.com",
        "category": "lakes",
        "region": "Rift Valley",
        "destination": "Lake Naivasha"
    },
    {
        "content": "Lake Bogoria National Reserve is famous for its hot springs, geysers, and flamingos. When Lake Nakuru's water levels rise, flamingos migrate here in millions. Entry: $50 USD. The lake is highly alkaline, making it unsuitable for swimming. The Spa Hotel nearby offers hot spring baths. The reserve also has greater kudu and over 350 bird species.",
        "source": "kws.go.ke",
        "category": "lakes",
        "region": "Rift Valley",
        "destination": "Lake Bogoria"
    },
    {
        "content": "Lake Victoria is Africa's largest lake and the world's second-largest freshwater lake. Kenya's portion includes Kisumu city and several islands. Kisumu Impala Sanctuary ($15 USD) is perfect for seeing hippos up close. Ndere Island National Park is uninhabited and great for walking safaris. The lake is famous for Nile perch fishing and sunset cruises.",
        "source": "magicalkenya.com",
        "category": "lakes",
        "region": "Western",
        "destination": "Lake Victoria"
    },
    {
        "content": "Lake Turkana, the 'Jade Sea', is the world's largest permanent desert lake and a UNESCO World Heritage Site. Located in Kenya's remote northwest, it's known for its striking jade-green color caused by algae. The lake has Nile crocodiles and over 60 fish species. Central Island National Park has three volcanic crater lakes. Access is challenging - most visitors fly in from Nairobi.",
        "source": "kws.go.ke",
        "category": "lakes",
        "region": "Northern Kenya",
        "destination": "Lake Turkana"
    },
    
    # ═══════════════════════════════════════════════════════════════════════════
    # PRACTICAL TRAVEL INFO
    # ═══════════════════════════════════════════════════════════════════════════
    
    {
        "content": "Kenya visa information: Most nationalities require a visa. eVisa can be obtained online at evisa.go.ke for $51 USD. East African citizens don't need visas. Visas are single-entry and valid for 90 days. Yellow fever vaccination is required if arriving from endemic countries. COVID-19 requirements vary - check current regulations before travel.",
        "source": "evisa.go.ke",
        "category": "transport",
        "region": "General",
        "destination": "Kenya"
    },
    {
        "content": "Nairobi Jomo Kenyatta International Airport (NBO) is Kenya's main international gateway. Kenya Airways operates direct flights to London, Amsterdam, Paris, Dubai, Mumbai, and many African cities. Airport to city center: taxi costs 2000-3000 KES ($15-25 USD), Uber/Bolt costs 800-1500 KES ($6-12 USD). The airport is 18 km from the city center.",
        "source": "kaa.go.ke",
        "category": "transport",
        "region": "Nairobi",
        "destination": "Nairobi"
    },
    {
        "content": "The Standard Gauge Railway (SGR) connects Nairobi to Mombasa in 4.5 hours. First class costs $35 USD, economy costs $10 USD. Trains depart twice daily at 8:00 AM and 3:00 PM from both cities. Booking can be done online at metickets.krc.co.ke or at the station. The train passes through Tsavo National Park - keep your camera ready for wildlife sightings!",
        "source": "krc.co.ke",
        "category": "transport",
        "region": "General",
        "destination": "Kenya"
    },
    {
        "content": "Kenya's currency is the Kenyan Shilling (KES). Exchange rate: approximately 130 KES = 1 USD (rates fluctuate). ATMs are widely available in cities. Credit cards accepted at hotels and large businesses. Safari lodges and national parks accept USD. Tipping: 10-15% at restaurants, $5-10 USD per day for safari guides, $2-5 USD for porters.",
        "source": "centralbank.go.ke",
        "category": "transport",
        "region": "General",
        "destination": "Kenya"
    },
    {
        "content": "Safari packing list: neutral-colored clothing (khaki, olive, brown), layered clothing for cool mornings and hot afternoons, sturdy walking shoes, hat and sunglasses, sunscreen, insect repellent, binoculars, camera with zoom lens, power bank, and any prescription medications. Most lodges have laundry service. Pack a warm fleece for early morning game drives.",
        "source": "magicalkenya.com",
        "category": "transport",
        "region": "General",
        "destination": "Kenya"
    },
    {
        "content": "Kenya's climate varies by region. Nairobi (altitude 1,795m) has spring-like weather year-round, 10-26°C. Coast is tropical, 24-32°C with high humidity. Best time to visit: dry seasons June-October and January-February. Long rains: March-May. Short rains: November. The Masai Mara migration occurs July-October. Beach holidays are best December-March.",
        "source": "magicalkenya.com",
        "category": "transport",
        "region": "General",
        "destination": "Kenya"
    },
    {
        "content": "Malaria prevention is essential in Kenya. Malaria is present in coastal areas, western Kenya, and below 1,800m altitude. Nairobi and highlands above 2,500m are low risk. Consult a doctor about antimalarial medication (Malarone, doxycycline, or mefloquine). Use mosquito repellent with DEET, sleep under treated nets, and wear long sleeves at dusk.",
        "source": "cdc.gov",
        "category": "transport",
        "region": "General",
        "destination": "Kenya"
    },
    
    # ═══════════════════════════════════════════════════════════════════════════
    # NAIROBI ATTRACTIONS
    # ═══════════════════════════════════════════════════════════════════════════
    
    {
        "content": "Karen Blixen Museum is the former home of 'Out of Africa' author Karen Blixen, located in the Nairobi suburb named after her. Entry: $12 USD. The museum showcases her life in Kenya from 1914-1931. Nearby is the Kazuri Beads factory, employing single mothers to make handcrafted ceramic jewelry. The Karen area has upscale restaurants and shopping.",
        "source": "museums.or.ke",
        "category": "culture",
        "region": "Nairobi",
        "destination": "Karen"
    },
    {
        "content": "The Nairobi National Museum covers Kenya's history, nature, culture, and art. Entry: $12 USD. The museum complex includes snake park, botanical gardens, and nature trail. The Railway Museum near the station showcases Kenya's railway history, including the famous 'Lunatic Express'. Entry: $5 USD. Both can be visited in half a day.",
        "source": "museums.or.ke",
        "category": "culture",
        "region": "Nairobi",
        "destination": "Nairobi"
    },
    
    # ═══════════════════════════════════════════════════════════════════════════
    # CULTURAL EXPERIENCES
    # ═══════════════════════════════════════════════════════════════════════════
    
    {
        "content": "The Maasai are Kenya's most famous tribe, known for their distinctive red shuka robes, jumping dance (adumu), and cattle-herding lifestyle. Cultural village visits can be arranged near Masai Mara for $20-30 USD. The Maasai Market in Nairobi (rotating locations: Tuesday-Saturday) sells beaded jewelry, carvings, and textiles. Bargaining is expected.",
        "source": "magicalkenya.com",
        "category": "culture",
        "region": "General",
        "destination": "Kenya"
    },
    {
        "content": "Kenyan cuisine highlights: Nyama Choma (grilled meat, the national dish), Ugali (maize porridge), Sukuma Wiki (collard greens), Pilau (spiced rice), and Mandazi (sweet fried dough). Coastal cuisine features Swahili dishes like biryani, samosas, and coconut-based curries. Try Tusker, Kenya's famous beer. Kenyan coffee and tea are world-renowned exports.",
        "source": "magicalkenya.com",
        "category": "culture",
        "region": "General",
        "destination": "Kenya"
    },
]


def populate_database():
    """Add all curated Kenya travel data to the vector database."""
    print("=" * 60)
    print("🐘 TEMBO AI - Kenya Knowledge Base Population Script")
    print("=" * 60)
    
    current_count = get_document_count()
    print(f"\nCurrent documents in database: {current_count}")
    
    if current_count > 0:
        response = input("\nDatabase has existing documents. Clear and repopulate? (y/n): ")
        if response.lower() == 'y':
            clear_knowledge_base()
            print("Database cleared.")
        else:
            print("Adding to existing documents...")
    
    print(f"\nPreparing to add {len(KENYA_TRAVEL_DATA)} documents...")
    
    # Extract texts and metadata
    texts = [doc["content"] for doc in KENYA_TRAVEL_DATA]
    metadatas = [
        {
            "source": doc["source"],
            "category": doc["category"],
            "region": doc["region"],
            "destination": doc["destination"],
        }
        for doc in KENYA_TRAVEL_DATA
    ]
    
    # Add to database
    print("\nEmbedding and inserting documents (this may take a minute)...")
    count = add_documents_simple(texts, metadatas)
    
    print(f"\n✅ Successfully added {count} documents!")
    print(f"📚 Total documents in database: {get_document_count()}")
    
    # Print summary by category
    print("\n📊 Documents by category:")
    categories = {}
    for doc in KENYA_TRAVEL_DATA:
        cat = doc["category"]
        categories[cat] = categories.get(cat, 0) + 1
    for cat, count in sorted(categories.items()):
        print(f"   {cat}: {count}")
    
    print("\n🎉 Knowledge base ready! Try asking Tembo about:")
    print("   • 'Entry fee for Masai Mara'")
    print("   • 'Best beaches in Kenya'")
    print("   • 'When is the wildebeest migration'")
    print("   • 'How to get from Nairobi to Mombasa'")
    print("   • 'What to pack for a safari'")


if __name__ == "__main__":
    populate_database()
