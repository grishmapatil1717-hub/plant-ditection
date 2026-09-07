"""
Comprehensive Plant Pathology Knowledge Base for Potato, Tomato, and Apple crops.
"""

DISEASE_KNOWLEDGE_BASE = {
    "potato": {
        "Early Blight": {
            "scientific_name": "Alternaria solani",
            "pathogen": "Fungus (Alternaria solani)",
            "severity": "Moderate",
            "is_healthy": False,
            "description": "Fungal pathogen causing concentric target-board dark brown spots on older lower leaves, progressively reducing tuber yields.",
            "causes": "Warm humid temperatures (24-29°C), alternating dry and rainy spells, dense foliage, and soil splash.",
            "symptoms": [
                "Dark brown circular spots with characteristic concentric rings (target pattern)",
                "Yellow chlorotic halo surrounding necrotic lesions",
                "Premature leaf senescence and defoliation progressing upward",
                "Dark sunken lesions on mature stems"
            ],
            "organic_remedies": [
                "Foliar spray of cold-pressed Neem oil (5ml/L of water) every 7-10 days",
                "Prune lower foliage up to 10-12 inches above soil to prevent rain splash infection",
                "Apply bio-fungicides with Trichoderma viride or Bacillus subtilis",
                "Compost tea sprays to strengthen leaf surface microbial barrier"
            ],
            "chemical_treatments": [
                "Foliar spray of Copper Oxychloride 50 WP @ 2.5g per litre",
                "Mancozeb 75 WP (2.0g/L) or Chlorothalonil 75 WP (2.0g/L)",
                "Azoxystrobin 23 SC (1ml/L) for translaminar protection"
            ],
            "prevention": [
                "Plant certified disease-free seed tubers",
                "Apply clean straw mulch as a rain splash barrier",
                "Implement a 3-year crop rotation with non-solanaceous crops",
                "Drip irrigation to keep foliage completely dry"
            ]
        },
        "Late Blight": {
            "scientific_name": "Phytophthora infestans",
            "pathogen": "Oomycete (Phytophthora infestans)",
            "severity": "Severe",
            "is_healthy": False,
            "description": "Devastating oomycete water-mold disease that rapidly rots whole vines and potato tubers within days under cool, damp conditions.",
            "causes": "Cool temperatures (10-20°C) with persistent high humidity (>90%) and rain.",
            "symptoms": [
                "Large irregular water-soaked dark brown/black lesions on leaves and stems",
                "White delicate fuzzy fungal mycelium on leaf undersides in damp mornings",
                "Petioles collapsing and emitting a distinctive rotting odor",
                "Tubers developing dry brown corky rot beneath skin"
            ],
            "organic_remedies": [
                "Immediately rogue, bag, and deeply bury infected plants (never compost)",
                "Apply preventive copper hydroxide sprays before expected rain events",
                "Maintain thick soil hilling over tuber beds to prevent spore wash-down"
            ],
            "chemical_treatments": [
                "Emergency systemic spray: Metalaxyl 8% + Mancozeb 64% WP (2.5g/L)",
                "Dimethomorph 50% WP (1.0g/L) + Mancozeb (2g/L)",
                "Cymoxanil 8% + Mancozeb 64% WP (2g/L)"
            ],
            "prevention": [
                "Plant late blight-resistant potato cultivars",
                "Destroy cull piles and volunteer potato sprouts before spring",
                "Ensure wide row spacing (60 cm) for fast canopy drying"
            ]
        },
        "Healthy": {
            "scientific_name": "Solanum tuberosum (Healthy)",
            "pathogen": "None (Optimal Foliage Health)",
            "severity": "None",
            "is_healthy": True,
            "description": "Plant foliage is vibrant, robust, and free from pathogenic spots, mildew, or wilting.",
            "causes": "Balanced N-P-K nutrition, optimal root hydration, and adequate sunlight.",
            "symptoms": [
                "Vibrant emerald green compound leaves",
                "Clean leaf margins without chlorosis or necrotic edges",
                "Sturdy erect stems with vigorous vegetative growth"
            ],
            "organic_remedies": [
                "Maintain regular compost and vermicompost top-dressing",
                "Continue weekly visual scouting of lower foliage"
            ],
            "chemical_treatments": [
                "No chemical fungicide application needed"
            ],
            "prevention": [
                "Maintain uniform moisture level via root-zone irrigation",
                "Ensure 6-8 hours of direct daily sunlight"
            ]
        }
    },
    "tomato": {
        "Early Blight": {
            "scientific_name": "Alternaria solani",
            "pathogen": "Fungus (Alternaria solani)",
            "severity": "Moderate",
            "is_healthy": False,
            "description": "Fungal pathogen attacking foliage, stems, and fruit, creating concentric target-pattern lesions.",
            "causes": "Warm humid weather, soil splash during heavy rain, stressed vines.",
            "symptoms": [
                "Dark brown circular spots with concentric target rings on older foliage",
                "Yellow chlorotic perimeter halo around spots",
                "Collar rot lesions at soil line on young stems",
                "Sunken leathery black lesions near fruit calyx"
            ],
            "organic_remedies": [
                "Spray cold-pressed Neem oil (5ml/L) at 7-day intervals",
                "Prune bottom 12 inches of suckers and foliage to improve airflow",
                "Compost tea foliar application to boost beneficial microflora"
            ],
            "chemical_treatments": [
                "Copper Hydroxide or Copper Oxychloride 50 WP (2.5g/L)",
                "Mancozeb 75 WP (2g/L) or Chlorothalonil 75 WP (2g/L)"
            ],
            "prevention": [
                "Stake or cage tomato vines to keep leaves elevated",
                "Mulch base with straw or reflective plastic",
                "Water strictly at ground level using drip emitters"
            ]
        },
        "Late Blight": {
            "scientific_name": "Phytophthora infestans",
            "pathogen": "Oomycete (Phytophthora infestans)",
            "severity": "Severe",
            "is_healthy": False,
            "description": "Aggressive disease causing rapid vine collapse and fruit rot during cool, damp weather.",
            "causes": "Persistent moisture, cool nights (10-15°C) and mild days (15-22°C).",
            "symptoms": [
                "Large water-soaked dark brown to purplish lesions across leaves",
                "Delicate white fungal down on leaf undersides during high humidity",
                "Firm, greasy dark brown blotches on green or ripening tomatoes",
                "Sudden wilting and total blackened collapse of foliage"
            ],
            "organic_remedies": [
                "Rogue and safely bag/dispose of infected plants immediately",
                "Apply bio-fungicides with Bacillus subtilis",
                "Avoid working with wet plants to prevent spreading spores"
            ],
            "chemical_treatments": [
                "Metalaxyl + Mancozeb (2.5g/L) systemic spray",
                "Fenamidone 10% + Mancozeb 50% WG (2.5g/L)",
                "Ametoctradin + Dimethomorph (1.5ml/L)"
            ],
            "prevention": [
                "Plant certified resistant varieties (e.g. Defiant, Mountain Magic)",
                "Avoid planting tomatoes adjacent to potato fields",
                "Provide wide spacing (75-90 cm) between vines"
            ]
        },
        "Septoria Leaf Spot": {
            "scientific_name": "Septoria lycopersici",
            "pathogen": "Fungus (Septoria lycopersici)",
            "severity": "Moderate",
            "is_healthy": False,
            "description": "Destructive fungal foliar disease producing numerous small circular lesions with dark borders and gray centers.",
            "causes": "Warm temperatures (20-25°C), high humidity, overhead watering.",
            "symptoms": [
                "Numerous small circular spots (2-3mm) with dark brown borders and pale grey centers",
                "Tiny black fruiting specks (pycnidia) visible within spot centers",
                "Progressive upward defoliation exposing fruit to sunscald"
            ],
            "organic_remedies": [
                "Prune infected lower leaves as soon as first spots appear",
                "Apply potassium bicarbonate or liquid copper fungicides",
                "Sterilize pruning shears with 70% isopropyl alcohol"
            ],
            "chemical_treatments": [
                "Chlorothalonil 75 WP (2g/L) or Mancozeb 75 WP (2g/L)",
                "Pyraclostrobin or Azoxystrobin (1ml/L)"
            ],
            "prevention": [
                "2-3 year crop rotation away from solanaceous species",
                "Deep bury crop residue at the end of the season",
                "Avoid overhead sprinkler irrigation"
            ]
        },
        "Healthy": {
            "scientific_name": "Solanum lycopersicum (Healthy)",
            "pathogen": "None (Optimal Health)",
            "severity": "None",
            "is_healthy": True,
            "description": "Vigorous tomato vine showing strong apical growth, deep green foliage, and healthy flowering.",
            "causes": "Optimal sunlight, balanced fertility, and controlled hydration.",
            "symptoms": [
                "Deep green lush foliage with healthy serrated margins",
                "Firm petioles and sturdy central vine growth",
                "Normal flower bud formation without chlorosis"
            ],
            "organic_remedies": [
                "Maintain organic feeding with seaweed/compost extract",
                "Apply regular mulch replenishment"
            ],
            "chemical_treatments": [
                "No chemical fungicide required"
            ],
            "prevention": [
                "Maintain 6-8 hours of direct daily sunlight",
                "Ensure balanced soil calcium and magnesium levels"
            ]
        }
    },
    "apple": {
        "Apple Scab": {
            "scientific_name": "Venturia inaequalis",
            "pathogen": "Fungus (Venturia inaequalis)",
            "severity": "Severe",
            "is_healthy": False,
            "description": "Widespread fungal disease causing olive-green to velvety black scabs on leaves and fruit.",
            "causes": "Overwintering in fallen leaves, prolonged springtime leaf wetness at 15-24°C.",
            "symptoms": [
                "Olive-green to velvety brown circular spots on upper leaf surfaces",
                "Leaves becoming puckered, twisted, and dropping prematurely",
                "Fruit developing dark corky, cracked, scabby lesions"
            ],
            "organic_remedies": [
                "Rake and destroy fallen leaves in autumn to eliminate overwintering spores",
                "Apply sulfur-based or copper soap sprays during early bud break",
                "Prune tree canopy to maximize sun penetration and air circulation"
            ],
            "chemical_treatments": [
                "Captan 50 WP (2.5g/L) or Mancozeb 75 WP (2g/L) as protective sprays",
                "Myclobutanil 10 WP (1g/L) or Difenoconazole 25 EC (0.5ml/L) for curative action"
            ],
            "prevention": [
                "Plant scab-resistant cultivars (e.g. Enterprise, Liberty, Honeycrisp)",
                "Apply 5% urea spray to fallen orchard leaves in late autumn"
            ]
        },
        "Black Rot": {
            "scientific_name": "Botryosphaeria obtusa",
            "pathogen": "Fungus (Botryosphaeria obtusa)",
            "severity": "Severe",
            "is_healthy": False,
            "description": "Fungal disease causing frog-eye leaf spots, limb cankers, and firm mummified black fruit rot.",
            "causes": "Dead wood, mummified apples, warm humid weather (24-27°C).",
            "symptoms": [
                "Frog-eye leaf spots: purple specks expanding to spots with tan centers and purple borders",
                "Sunken reddish-brown cankers on branches and limbs",
                "Fruit developing brown rot with concentric black rings, turning into dry mummies"
            ],
            "organic_remedies": [
                "Prune out dead wood and cankered branches 6 inches below infected zone",
                "Remove and safely dispose of all mummified fruit remaining on trees",
                "Lime sulfur sprays during dormant season"
            ],
            "chemical_treatments": [
                "Thiophanate-methyl 70 WP (1g/L) or Captan 50 WP (2g/L)",
                "Flint (Trifloxystrobin) or Pristine (Pyraclostrobin + Boscalid)"
            ],
            "prevention": [
                "Maintain tree vigor through balanced fertilization and pest control",
                "Disinfect pruning tools between cuts"
            ]
        },
        "Cedar Apple Rust": {
            "scientific_name": "Gymnosporangium juniperi-virginianae",
            "pathogen": "Fungus (Gymnosporangium juniperi-virginianae)",
            "severity": "Moderate",
            "is_healthy": False,
            "description": "Heteroecious rust fungus requiring both apple trees and Eastern red cedar/juniper to complete its life cycle.",
            "causes": "Proximity to juniper trees, spring rain releasing spores from cedar galls.",
            "symptoms": [
                "Bright yellow-orange circular spots on upper apple leaf surfaces",
                "Spots enlarging and developing reddish borders with tiny black dots",
                "Underside of spots forming tube-like fringe structures (aecia)",
                "Early summer defoliation and dwarfed fruit"
            ],
            "organic_remedies": [
                "Remove nearby wild juniper/cedar shrubs within 500m radius if possible",
                "Prune and remove galls from ornamental junipers during late winter",
                "Apply sulfur sprays beginning at pink bud stage"
            ],
            "chemical_treatments": [
                "Myclobutanil 10 WP (1g/L) or Mancozeb 75 WP (2g/L)",
                "Propiconazole 25 EC (1ml/L) applied at tight cluster through petal fall"
            ],
            "prevention": [
                "Choose rust-resistant apple cultivars (e.g. Redfree, William's Pride)",
                "Avoid planting apple orchards adjacent to cedar windbreaks"
            ]
        },
        "Healthy": {
            "scientific_name": "Malus domestica (Healthy)",
            "pathogen": "None (Optimal Health)",
            "severity": "None",
            "is_healthy": True,
            "description": "Lush apple foliage with deep green color, strong shoot growth, and clean fruit spur development.",
            "causes": "Regular orchard hygiene, balanced fertility, and proactive canopy pruning.",
            "symptoms": [
                "Glossy, deep green leaves without rust spots, scabs, or mildew",
                "Clean bark and active branch terminal growth",
                "Healthy flower blossoms and fruit set"
            ],
            "organic_remedies": [
                "Apply dormant oil spray in early spring for pest and scale suppression",
                "Maintain compost mulching around tree drip line"
            ],
            "chemical_treatments": [
                "No fungicide required"
            ],
            "prevention": [
                "Perform annual winter pruning for optimal sun penetration and airflow",
                "Maintain adequate boron and zinc micronutrient balance"
            ]
        }
    },
    "corn": {
        "Cercospora Leaf Spot": {
            "scientific_name": "Cercospora zeae-maydis",
            "pathogen": "Fungus (Cercospora zeae-maydis)",
            "severity": "Moderate",
            "is_healthy": False,
            "description": "Also known as Gray Leaf Spot, causing rectangular tan lesions running parallel to corn leaf veins, reducing photosynthetic capacity.",
            "causes": "Warm humid conditions (25-30°C), dense plant canopy, continuous corn cropping without residue burial.",
            "symptoms": [
                "Small tan spots expanding into distinct rectangular lesions bounded by leaf veins",
                "Grey fungal sporulation on leaf surface during damp morning hours",
                "Extensive blighting of upper leaves leading to stalk lodging and reduced grain fill"
            ],
            "organic_remedies": [
                "Rotate with non-host crops like soybeans or alfalfa for at least 1-2 years",
                "Apply Bacillus subtilis bio-fungicide foliar sprays",
                "Shred and till corn residue deep into the soil after harvest"
            ],
            "chemical_treatments": [
                "Azoxystrobin + Difenoconazole @ 1ml/L of water",
                "Pyraclostrobin (Headline AMP) or Propiconazole 25 EC (1ml/L)",
                "Mancozeb 75 WP (2g/L) during early vegetative stages"
            ],
            "prevention": [
                "Plant Gray Leaf Spot-tolerant corn hybrids",
                "Adopt optimum plant density to enhance intra-row air circulation",
                "Apply balanced nitrogen and potassium fertilization to prevent plant stress"
            ]
        },
        "Common Rust": {
            "scientific_name": "Puccinia sorghi",
            "pathogen": "Fungus (Puccinia sorghi)",
            "severity": "Moderate",
            "is_healthy": False,
            "description": "Airborne fungal rust producing powdery golden-brown to cinnamon pustules on both upper and lower corn leaf surfaces.",
            "causes": "Cool to moderate temperatures (16-25°C) combined with high relative humidity (>95%) and night dews.",
            "symptoms": [
                "Oval to elongate cinnamon-brown powdery pustules scattered across leaves",
                "Pustules rupturing the epidermis, turning brownish-black late in the season",
                "Chlorosis and premature drying of severely infected leaves"
            ],
            "organic_remedies": [
                "Apply sulfur-based dusts or wettable sulfur (3g/L) early at first pustule appearance",
                "Neem seed kernel extract (NSKE 5%) spray every 10 days",
                "Promote rapid canopy drying by avoiding evening sprinkler irrigation"
            ],
            "chemical_treatments": [
                "Mancozeb 75 WP @ 2.5g/L or Zineb 75 WP @ 2g/L",
                "Azoxystrobin 23 SC (1ml/L) or Tebuconazole 25.9 EC (1ml/L)",
                "Propiconazole 25 EC (1ml/L) applied at tassel emergence if rust is severe"
            ],
            "prevention": [
                "Select corn hybrids with specific Rp resistance genes",
                "Plant early in the season to evade mid-summer spore influx",
                "Ensure proper field drainage and balanced soil nutrition"
            ]
        },
        "Northern Leaf Blight": {
            "scientific_name": "Exserohilum turcicum",
            "pathogen": "Fungus (Exserohilum turcicum)",
            "severity": "Severe",
            "is_healthy": False,
            "description": "Devastating foliar disease producing large cigar-shaped grayish-green to tan lesions, leading to severe yield loss.",
            "causes": "Moderate temperatures (18-27°C) with prolonged wet periods and heavy morning dews.",
            "symptoms": [
                "Long, elliptical, cigar-shaped grayish-green or tan lesions (2.5 to 15 cm long)",
                "Dark olive-green fuzzy fungal spores developing within lesions in damp weather",
                "Leaves turning entirely brown and dry, looking as if killed by early frost"
            ],
            "organic_remedies": [
                "Clean cultivation and deep burying of infected crop debris",
                "Crop rotation away from maize and sorghum for 2 seasons",
                "Foliar spray with Trichoderma viride or Pseudomonas fluorescens"
            ],
            "chemical_treatments": [
                "Mancozeb 75 WP @ 2.5g/L or Chlorothalonil 75 WP @ 2g/L",
                "Azoxystrobin + Tebuconazole (1ml/L) or Pyraclostrobin",
                "Difenoconazole 25 EC (0.5ml/L) at first sign of lower leaf lesions"
            ],
            "prevention": [
                "Utilize corn hybrids carrying Ht resistance genes",
                "Avoid overhead irrigation during cooler vegetative stages",
                "Maintain optimal plant spacing for good canopy airflow"
            ]
        },
        "Healthy": {
            "scientific_name": "Zea mays (Healthy)",
            "pathogen": "None (Optimal Health)",
            "severity": "None",
            "is_healthy": True,
            "description": "Vibrant, broad corn leaves with deep emerald green pigmentation, strong stalk turgor, and spotless leaf lamina.",
            "causes": "Adequate moisture, full sun, balanced N-P-K nutrition, and healthy root development.",
            "symptoms": [
                "Uniform rich dark green foliage with clean arching leaf blades",
                "Sturdy, thick stalk with strong prop root anchoring",
                "Full, healthy tassel and silk emergence without discoloration"
            ],
            "organic_remedies": [
                "Side-dress with compost or organic manure during knee-high stage",
                "Maintain consistent root-zone soil moisture"
            ],
            "chemical_treatments": [
                "No fungicide required"
            ],
            "prevention": [
                "Soil testing and balanced nitrogen application",
                "Ensure minimum 8 hours of full direct sunlight daily"
            ]
        }
    },
    "grape": {
        "Black Rot": {
            "scientific_name": "Guignardia bidwellii",
            "pathogen": "Fungus (Guignardia bidwellii)",
            "severity": "Severe",
            "is_healthy": False,
            "description": "Destructive fungal disease affecting all green parts of the grapevine, turning berries into hard, shriveled black mummies.",
            "causes": "Warm and rainy weather (21-32°C), splashing rain dispersing spores from overwintered mummified grapes.",
            "symptoms": [
                "Small circular reddish-brown leaf spots with dark margins and tiny black specks (pycnidia)",
                "Elongated black lesions on young canes, tendrils, and leaf petioles",
                "Infected grape berries turning soft, rotting, and shriveling into hard, wrinkled black mummies"
            ],
            "organic_remedies": [
                "Remove and destroy all mummified berries from vines and ground during winter pruning",
                "Apply liquid copper or sulfur sprays beginning at early bud swell",
                "Open vine canopy through shoot positioning and leaf pulling to maximize sun and airflow"
            ],
            "chemical_treatments": [
                "Mancozeb 75 WP (2g/L) or Captan 50 WP (2.5g/L) from bud break to bloom",
                "Myclobutanil 10 WP (1g/L) or Kresoxim-methyl 44.3 SC (0.5ml/L)",
                "Azoxystrobin + Difenoconazole (1ml/L) for protective and curative action"
            ],
            "prevention": [
                "Plant black rot-resistant grape cultivars where feasible",
                "Prune vines to open trellis systems (e.g. VSP) for fast foliage drying",
                "Mow orchard floor regularly to reduce relative humidity beneath canopy"
            ]
        },
        "Esca (Black Measles)": {
            "scientific_name": "Phaeomoniella chlamydospora & Phaeoacremonium aleophilum",
            "pathogen": "Fungus Complex (Esca / Black Measles)",
            "severity": "Severe",
            "is_healthy": False,
            "description": "Complex grapevine wood disease causing distinctive 'tiger-stripe' leaf necrosis, dark spotted berries (measles), and vine dieback.",
            "causes": "Wound infection during pruning, fungal colonization of woody vascular tissues, summer heat stress.",
            "symptoms": [
                "'Tiger-stripe' chlorotic and necrotic banding between leaf veins",
                "Small dark purple to brown speckles ('measles') on grape berry skins",
                "Sudden summer apoplexy (rapid vine wilting and leaf collapse within days)"
            ],
            "organic_remedies": [
                "Paint or seal large pruning wounds immediately with pruning sealant or bio-pastes (Trichoderma)",
                "Prune during late dry winter weather to reduce spore entry into fresh cuts",
                "Carefully cut out infected vine arms below internal wood discoloration"
            ],
            "chemical_treatments": [
                "Apply wound protectant fungicides containing pyraclostrobin or tebuconazole immediately post-pruning",
                "Foliar phosphite and systemic nutrient supplements to boost vine defense mechanisms"
            ],
            "prevention": [
                "Disinfect pruning shears regularly with 70% ethanol between vines",
                "Avoid excessive water and fertilizer stress during fruit set",
                "Purchase certified clean, virus/disease-free nursery rootstocks"
            ]
        },
        "Leaf Blight": {
            "scientific_name": "Pseudocercospora vitis",
            "pathogen": "Fungus (Pseudocercospora vitis / Isariopsis clavispora)",
            "severity": "Moderate",
            "is_healthy": False,
            "description": "Late-season fungal foliar disease causing angular dark brown to black leaf lesions with a yellow halo, leading to premature defoliation.",
            "causes": "High humidity, warm temperatures, poor air circulation within dense overgrown canopies.",
            "symptoms": [
                "Angular to irregular dark brown lesions with yellow chlorotic halos on older leaves",
                "Velvety olive-brown fungal growth on the underside of leaf lesions during damp periods",
                "Severe leaf yellowing, browning, and premature leaf drop exposing clusters to sunburn"
            ],
            "organic_remedies": [
                "Rake and compost or destroy fallen leaves post-harvest",
                "Apply copper oxychloride (2.5g/L) or Bordeaux mixture (1%) preventive sprays",
                "Selective summer canopy thinning to enhance airflow"
            ],
            "chemical_treatments": [
                "Mancozeb 75 WP (2g/L) or Chlorothalonil 75 WP (2g/L)",
                "Carbendazim 50 WP (1g/L) or Tebuconazole (1ml/L)",
                "Pyraclostrobin (0.5ml/L) applied after post-harvest flushes"
            ],
            "prevention": [
                "Maintain proper vine spacing and row orientation for wind passage",
                "Apply balanced organic potassium to harden leaf cuticle",
                "Avoid overhead sprinkler systems"
            ]
        },
        "Healthy": {
            "scientific_name": "Vitis vinifera (Healthy)",
            "pathogen": "None (Optimal Health)",
            "severity": "None",
            "is_healthy": True,
            "description": "Lush, well-structured grapevines with vibrant green palmate leaves, clean canes, and flourishing grape clusters.",
            "causes": "Balanced canopy management, adequate sunshine, well-drained soil, and disciplined pruning.",
            "symptoms": [
                "Glossy, emerald-green leaves with smooth lobes and intact margins",
                "Clean brown woody canes with vigorous green shoot tips",
                "Tight, uniform berry clusters without spots, powdery coating, or rot"
            ],
            "organic_remedies": [
                "Apply organic compost mulch around grapevine base",
                "Continue seasonal shoot positioning and suckering"
            ],
            "chemical_treatments": [
                "No fungicide required"
            ],
            "prevention": [
                "Maintain open canopy architecture for direct sunlight on fruit zone",
                "Regular soil pH and micronutrient monitoring"
            ]
        }
    }
}

