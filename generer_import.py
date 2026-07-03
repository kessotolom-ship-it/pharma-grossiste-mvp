import csv

headers = [
    'Product Id', 'Product Handle', 'Product Title', 'Product Subtitle', 'Product Description', 
    'Product Status', 'Product Thumbnail', 'Product Weight', 'Product Length', 'Product Width', 
    'Product Height', 'Product HS Code', 'Product Origin Country', 'Product MID Code', 'Product Material', 
    'Shipping Profile Id', 'Product Sales Channel 1', 'Product Collection Id', 'Product Type Id', 
    'Product Tag 1', 'Product Discountable', 'Product External Id', 'Variant Id', 'Variant Title', 
    'Variant SKU', 'Variant Barcode', 'Variant Allow Backorder', 'Variant Manage Inventory', 
    'Variant Weight', 'Variant Length', 'Variant Width', 'Variant Height', 'Variant HS Code', 
    'Variant Origin Country', 'Variant MID Code', 'Variant Material', 'Variant Option 1 Name', 
    'Variant Option 1 Value', 'Product Image 1 Url', 'Product Image 2 Url', 'Variant Price XOF'
]

# Reste des produits du catalogue (Lot 1, Lot 2, Lot 3 restants) sans doublons
produits_restants = [
    # Suite du Lot 1
    ("rhododendron-granules", "RHODODENDRON granules", "Souche homeopathique pour les douleurs articulaires", "PHARMA-RHO-010", 1800),
    ("pilocarpine-200mg", "CHLORHYDRATE DE PILOCARPINE 200 mg solution", "Parasympathomimetique direct pour secheresse buccale", "PHARMA-PIL-011", 4100),
    ("atorvastatine-40mg", "ATORVASTATINE 40 mg comprimé", "Statine pour la reduction du cholesterol", "PHARMA-ATO-012", 4200),
    ("sulfate-de-zinc-gel", "SULFATE DE ZINC 0.5 g gel", "Gel pour protection et cicatrisation cutanee", "PHARMA-ZIN-013", 1500),
    ("dutasteride-0-5mg", "DUTASTERIDE 0.5 mg capsule", "Inhibiteur de la 5 alpha reductase prostate", "PHARMA-DUT-014", 5800),
    ("glucose-anhydre-15g", "GLUCOSE ANHYDRE 15 g solution", "Solution glucidique pour rehydratation urgence", "PHARMA-GLU-015", 1100),
    ("rivastigmine-1-5mg", "RIVASTIGMINE 1.5 mg gélule", "Anticholinesterasique pour maladie Alzheimer", "PHARMA-RIV-016", 4800),
    ("paracetamol-codeine", "PHOSPHATE DE CODEINE / PARACETAMOL", "Association antalgique douleurs moderees a severes", "PHARMA-COD-018", 2400),
    ("thiopental-sodique", "THIOPENTAL SODIQUE poudre solution", "Anesthesique general intraveineux action rapide", "PHARMA-THI-019", 14500),
    
    # Suite du Lot 2
    ("thiopental-500mg-flacon", "THIOPENTAL 500 mg flacon poudre", "Anesthesique d induction en milieu hospitalier", "PHARMA-THI-020", 12500),
    ("chlorure-sodium-5-85g", "CHLORURE DE SODIUM 5.85 g solution", "Solution saline concentree apport electrolytique", "PHARMA-SOD-021", 900),
    ("nitrate-fer-200mg", "NITRATE DE FER 200 mg capsule", "Supplementation martiale pour anemie ferriprive", "PHARMA-FER-023", 2400),
    ("fenticonazole-175-7mg", "FENTICONAZOLE 175.7 mg capsule", "Antifongique local candidoses vaginales", "PHARMA-FEN-024", 3500),
    ("gelsemium-pc-granules", "GELSEMIUM PC granules", "Souche homeopathique anxiete et trac", "PHARMA-GEL-026", 1800),
    ("carvedilol-25mg", "CARVEDILOL 25 mg comprimé", "Beta bloquant pour hypertension et insuffisance", "PHARMA-CAR-027", 4600),
    ("levocarnitine-1000mg", "LEVOCARNITINE 1000 mg ampoule", "Traitement des deficits primaires en carnitine", "PHARMA-LEV-028", 7200),
    ("perindopril-6-816mg", "PÉRINDOPRIL 6.816 mg comprimé", "Inhibiteur enzyme de conversion cardiovasculaire", "PHARMA-PER-031", 3800),
    ("cromoglicate-2g-collyre", "CROMOGLICATE 2 g collyre solution", "Traitement symptomatique conjonctivites allergiques", "PHARMA-CRO-032", 1400),
    
    # Suite du Lot 3
    ("dipyridamole-75mg", "DIPYRIDAMOLE 75 mg comprimé", "Antiagregant plaquettaire prevention AVC", "PHARMA-DIP-037", 3600),
    ("clobetasol-500mcg", "PROPIONATE DE CLOBETASOL 500 mcg mousse", "Corticosteroide local puissant dermatoses", "PHARMA-CLO-038", 4800),
    ("silodosine-8mg", "SILODOSINE 8 mg gélule", "Alpha bloquant pour hypertrophie de la prostate", "PHARMA-SIL-040", 5400),
    ("trinitrine-15-7mg", "TRINITRINE 15.7 mg dispositif", "Derive nitre pour la prophylaxie de l angor", "PHARMA-TRI-041", 6200),
    ("dorzolamide-20mg", "DORZOLAMIDE 20 mg collyre", "Inhibiteur de l anhydrase carbonique glaucome", "PHARMA-DOR-042", 3100),
    ("riociguat-1-5mg", "RIOCIGUAT 1.5 mg comprimé", "Stimulateur de la guanylate cyclase soluble", "PHARMA-RIO-043", 95000),
    ("paracetamol-1000mg", "PARACETAMOL 1000 mg comprimé", "Antalgique et antipyrétique douleurs moderees", "PHARMA-PAR-045", 1500),
    ("glibenclamide-5mg", "GLIBENCLAMIDE 5 mg comprimé", "Sulfamide hypoglycemiant diabete type 2", "PHARMA-GLI-047", 1800)
]

with open('medusa_perfect_import.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    
    for handle, title, desc, sku, price in produits_restants:
        row = []
        for h in headers:
            if h == "Product Handle": row.append(handle)
            elif h == "Product Title": row.append(title)
            elif h == "Product Description": row.append(desc)
            elif h == "Product Status": row.append("published")
            elif h == "Product Discountable": row.append("TRUE")
            elif h == "Variant Title": row.append("Boite")
            elif h == "Variant SKU": row.append(sku)
            elif h == "Variant Allow Backorder": row.append("FALSE")
            elif h == "Variant Manage Inventory": row.append("FALSE")
            elif h == "Variant Option 1 Name": row.append("Format")
            elif h == "Variant Option 1 Value": row.append("Default")
            elif h == "Variant Price XOF": row.append(price)
            else: row.append("")
        writer.writerow(row)

print("Nouveau fichier medusa_perfect_import.csv généré avec succès avec le reste des produits !")
