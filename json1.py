import json


indoor_plants=[
    {
    "plant_Name": "Monstera Deliciosa",
    "plant_image": "https://www.inntinn.in/cdn/shop/products/monstera-deliciosa-xl-inntinn-in-1.jpg?v=1703281353",
    "plant_price": "30"
  },
  {
    "plant_Name": "Fiddle Leaf Fig",
    "plant_image":"https://www.ugaoo.com/cdn/shop/files/1_cc65c975-7a6f-43d6-bb81-b56520e29bc7.jpg?v=1703143693",
    "plant_price": "40"
  },
  {
    "plant_Name": "Snake Plant",
    "plant_image": "https://hips.hearstapps.com/hmg-prod/images/how-to-care-for-a-snake-plant-1591205050.jpg?crop=0.670xw:1.00xh;0.330xw,0&resize=640:*",
    "plant_price": "20"
  },
  {
    "plant_Name": "Pothos",
    "plant_image": "https://www.rollingnature.com/cdn/shop/products/PLGPCEAPGL-W-Main.jpg?v=1669452831",
    "plant_price": "15"
  },
  {
    "plant_Name": "ZZ Plant",
    "plant_image": "https://m.media-amazon.com/images/I/71x311i9AWL._AC_UF1000,1000_QL80_.jpg",
    "plant_price": "25"
  },
  {
    "plant_Name": "Peace Lily",
    "plant_image":"https://m.media-amazon.com/images/I/41I0iyhYjkL._AC_UF1000,1000_QL80_.jpg",
    "plant_price": "35"
  },
  {
    "plant_Name": "Spider Plant",
    "plant_image": "https://greenozean.com/wp-content/uploads/2019/12/spider.jpg",
    "plant_price": "10"
  },
  {
    "plant_Name": "Aloe Vera",
    "plant_image": "https://nurserylive.com/cdn/shop/products/nurserylive-plants-aloe-vera-succulent-plant-16968585871500_700x700.jpg?v=1634213151",
    "plant_price": "12"
  },
  {
    "plant_Name": "Rubber Plant",
    "plant_image": "https://abeautifulmess.com/wp-content/uploads/2023/06/rubbertree-1.jpg",
    "plant_price": "28"
  },
  {
    "plant_Name": "Philodendron",
    "plant_image": "https://www.plantvine.com/plants/Philodendron-Goeldii-2-800x1000.jpg",
    "plant_price": "18"
  }
]
outdoor_plants=[
    
        {
            "plant_Name": "Sunflower",
            "plant_image": "https://howtohouseplant.com/wp-content/uploads/2023/10/brown-pot-with-sunflowers-and-ribbon.jpg",
            "plant_price": "5"
        },
        {
            "plant_Name": "Rose",
            "plant_image": "https://cdn3.1800flowers.com/wcsstore/Flowers/images/catalog/158350swc.jpg?auto=webp&optimize={medium}",
            "plant_price": "8"
        },
        {
            "plant_Name": "Tulip",
            "plant_image": "https://cdn.shopify.com/s/files/1/1902/7917/files/Tulips_in_pots3.jpg",
            "plant_price": "4"
        },
        {
            "plant_Name": "Lavender",
            "plant_image": "https://png.pngtree.com/background/20230611/original/pngtree-lavender-indoor-plants-in-a-wooden-bowl-picture-image_3159905.jpg",
            "plant_price": "6"
        },
        {
            "plant_Name": "Daisy",
            "plant_image": "https://www.rootsplants.co.uk/cdn/shop/products/PB0214-1.jpg?v=1615033837",
            "plant_price": "3"
        },
        {
            "plant_Name": "Cactus",
            "plant_image": "https://contentgrid.homedepot-static.com/hdus/en_US/DTCCOMNEW/Articles/types-of-cactus-section-2.jpg",
            "plant_price": "7"
        },
        {
            "plant_Name": "Orchid",
            "plant_image": "https://cdn.shopify.com/s/files/1/0608/5676/2558/files/image_b44d111d-7d63-446c-b245-f27b633ce9c2_1024x1024.heic?v=1683212965",
            "plant_price": "10"
        },
        {
            "plant_Name": "Hydrangea",
            "plant_image": "https://www.provenwinners.com/sites/provenwinners.com/files/2019/images/hydrangea_patio_076.jpg",
            "plant_price": "9"
        },
        {
            "plant_Name": "Carnation",
            "plant_image": "https://nurserylive.com/cdn/shop/collections/nurserylive-carnation-plant-category-image-219729.jpg?v=1681381478",
            "plant_price": "4"
        },
        {
            "plant_Name": "Lily",
            "plant_image": "https://rukminim2.flixcart.com/image/850/1000/kt64fbk0/plant-seed/s/p/w/10-asiatic-10-white-lily-tim-tim-agro-original-imag6kufgf9q98jd.jpeg?q=20&crop=false",
            "plant_price": "6"
        },
        {
            "plant_Name": "Peony",
            "plant_image": "https://bulbsdirect.co.nz/cdn/shop/products/PatioPeonyRome_03506_grande.jpg?v=1627847165",
            "plant_price": '12'
        },
        {
            "plant_Name": "Succulent",
            "plant_image": "https://cdn.shopify.com/s/files/1/0043/3628/7813/files/succulents-thrive-outdoors_480x480.jpg?v=1697107899",
            "plant_price": "5"
        },
        {
            "plant_Name": "Fern",
            "plant_image": "https://jerseyshorescene-com-images.s3.amazonaws.com/wp-content/uploads/2022/02/boston-fern-indoors.jpg",
            "plant_price": "8"
        },
        {
            "plant_Name": "Bonsai",
            "plant_image": "https://m.media-amazon.com/images/I/A1qcYekhXZL._AC_UF1000,1000_QL80_.jpg",
            "plant_price": "15"
        }
    ]

seed_indoor=[
    {
        "seed_Name": "Sunflower Seeds",
        "seed_image": "https://m.media-amazon.com/images/I/71SGRh+9wML._AC_UF1000,1000_QL80_.jpg",
        "seed_price": "2.99"
    },
    {
        "seed_Name": "Tomato Seeds",
        "seed_image": "https://sustainablemacleod.org.au/wp-content/uploads/2021/02/tomato-seeds.jpg",
        "seed_price": "1.99"
    },
    {
        "seed_Name": "Basil Seeds",
        "seed_image": "https://saaragroups.com/wp-content/uploads/2020/10/basilseeds-1.jpg",
        "seed_price": "0.99"
    },
    {
        "seed_Name": "Lavender Seeds",
        "seed_image": "https://rukminim2.flixcart.com/image/850/1000/kjbr8280-0/plant-seed/t/l/m/20-lavender-20-vg499x-seed-v-seed-original-imafyx2hygjknz7h.jpeg?q=20&crop=false",
        "seed_price": "2.49"
    },
    {
        "seed_Name": "Zinnia Seeds",
        "seed_image": "https://i.pinimg.com/736x/2f/11/65/2f1165c500411c01fd33bff869817efe.jpg",
        "seed_price": "1.49"
    },
    {
        "seed_Name": "Cucumber Seeds",
        "seed_image": "https://cf.ltkcdn.net/garden/images/orig/232738-2121x1414-cucumber-seeds.jpg",
        "seed_price": "1.99"
    },
    {
        "seed_Name": "Rosemary Seeds",
        "seed_image": "https://www.everwilde.com/media//0800/resized/HROSEMA-C-Rosemary-Seeds_medium.jpg",
        "seed_price": "0.99"
    },
    {
        "seed_Name": "Marigold Seeds",
        "seed_image": "https://m.media-amazon.com/images/I/710lnJTi4nL._AC_UF1000,1000_QL80_.jpg",
        "seed_price": "1.49"
    },
    {
        "seed_Name": "Squash Seeds",
        "seed_image": "https://www.positivelyosceola.com/wp-content/uploads/2020/10/pumpkinseeds-948x640.jpg",
        "seed_price": "2.99"
    },
    {
        "seed_Name": "Mint Seeds",
        "seed_image": "https://rukminim2.flixcart.com/image/416/416/xif0q/plant-seed/v/y/l/20-mint-seeds-pack-of-5-gardenify-india-original-imagecphxbrvmrn8.jpeg?q=70&crop=false",
        "seed_price": "0.99"
    },
    {
        "seed_Name": "Pansy Seeds",
        "seed_image": "https://m.media-amazon.com/images/I/618INJgwCjL.jpg",
        "seed_price": "1.49"
    },
    {
        "seed_Name": "Pepper Seeds",
        "seed_image": "https://m.media-amazon.com/images/I/71me-mtZHUL._SX679_.jpg",
        "seed_price": "1.99"
    },
    {
        "seed_Name": "Thyme Seeds",
        "seed_image": "https://m.media-amazon.com/images/I/81pHHPMxaDL._SX679_.jpg",
        "seed_price": "0.99"
    },
    {
        "seed_Name": "Daisy Seeds",
        "seed_image": "https://www.rootsplants.co.uk/cdn/shop/products/PB0214-1.jpg?v=1615033837",
        "seed_price": "1.49"
    },
    {
        "seed_Name": "Carrot Seeds",
        "seed_image": "https://cdn.shopify.com/s/files/1/0084/4247/8658/files/3_75a85d78-34be-4e1f-8b2e-d566e9a73f04.jpg?v=1663196597",
        "seed_price": "1.99"
    }
]

fetilizer=[
    {
        "fetilizer_name": "Organic Growth",
        "description": "Boosts plant growth and enhances nutrient absorption.",
        "fetilizer_price": "9.99",
        "fetilizer_image": "https://i.etsystatic.com/16223366/r/il/7caddd/4089728680/il_570xN.4089728680_9o8a.jpg"
    },
    {
        "fetilizer_name": "Plant Vitality",
        "description": "Improves plant health and resistance to diseases.",
        "fetilizer_price": "12.99",
        "fetilizer_image": "https://m.media-amazon.com/images/I/617-UVG6MiL._AC_UF1000,1000_QL80_.jpg"
    },
    {
        "fetilizer_name": "Root Strength",
        "description": "Stimulates root development and improves nutrient uptake.",
        "fetilizer_price": "8.49",
        "fetilizer_image": "https://m.media-amazon.com/images/I/81HMsKWoWRL._AC_UF1000,1000_QL80_.jpg"
    },
    {
        "fetilizer_name": "Flower Power",
        "description": "Promotes abundant flowering and enhances color vibrancy.",
        "fetilizer_price": "10.99",
        "fetilizer_image": "https://everano.eu/content/images/thumbs/0001657_bio-pk-booster-fertilizante-linea-biologica-1-kg-3527-oz_415.jpeg"
    },
    {
        "fetilizer_name": "Fruitful Harvest",
        "description": "Increases fruit yield and improves taste and quality.",
        "fetilizer_price": "11.79",
        "fetilizer_image": "https://www.agriplexindia.com/cdn/shop/products/Fullpower_3.png?v=1676024495"
    },
   
    {
        "fetilizer_name": "All-Purpose",
        "description": "Suitable for all types of plants and promotes overall growth and vitality.",
        "fetilizer_price": "7.99",
        "fetilizer_image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNoPv5sXTCr8LRAOiVlI3IDXMgGSBlOdIRcLz0N8InWTbdmMKsIuUTnoLgHk6JOjnCCdI&usqp=CAU"
    },
    {
        "fetilizer_name": "Soil Conditioner",
        "description": "Improves soil structure and fertility for healthy plant growth.",
        "fetilizer_price": "14.99",
        "fetilizer_image": "https://2.wlimg.com/product_images/bc-full/2023/9/5968225/soil-conditioner-1663052029-6536072.jpg"
    },
    {
        "fetilizer_name": "Microbial Blend",
        "description": "Introduces beneficial microorganisms to the soil for improved nutrient availability.",
        "fetilizer_price": "15.99",
        "fetilizer_image": "https://m.media-amazon.com/images/I/51djzuhnTxL._AC_UF1000,1000_QL80_.jpg"
    }
]
Grow_bags = [
    {
        "Grow_bags": "Fabric Grow Bags",
        "Bag_description": "Made from durable fabric, these grow bags provide excellent drainage and aeration for healthy plant growth.",
        "prices": "9.99",
        "Bag_image": "https://m.media-amazon.com/images/I/71FRsaeL2nL._SX679_.jpg"
    },
    {
        "Grow_bags": "Plastic Grow Bags",
        "Bag_description": "These plastic grow bags are lightweight and easy to move, perfect for starting seedlings.",
        "prices": "5.99",
        "Bag_image": "https://gogarden.co.in/cdn/shop/files/GROW-BAG_dc953e0b-2855-45f3-ba64-eebb07b1efe2.jpg?v=1683975708"
    
        
    },
    {
        "Grow_bags": "Felt Grow Bags",
        "Bag_description": "Constructed from felt material, these grow bags offer insulation for roots and prevent overwatering.",
        "prices": "7.99",
        "Bag_image": "https://m.media-amazon.com/images/I/81c5MHgVrOS._SX679_.jpg"
    },
    {
        "Grow_bags": "Biodegradable Grow Bags",
        "Bag_description": "These biodegradable grow bags are eco-friendly and can be planted directly into the ground.",
        "prices": "8.99",
        "Bag_image": "https://m.media-amazon.com/images/I/71n51gmA4TL._AC_UF1000,1000_QL80_.jpg"
    },
    {
        "Grow_bags": "Vertical Grow Bags",
        "Bag_description": "Designed for vertical gardening, these grow bags save space and allow for easy harvesting.",
        "prices": "12.99",
        "Bag_image": "https://m.media-amazon.com/images/I/81nF4le4NkS._AC_UF894,1000_QL80_.jpg"
    },
    {
        "Grow_bags": "Hanging Grow Bags",
        "Bag_description": "With built-in handles, these hanging grow bags are great for growing herbs and small plants.",
        "prices": "6.99",
        "Bag_image": "https://www.sowandgrow.in/cdn/shop/products/HangingPots_1200x1200.jpg?v=1630591499"
    },
    {
        "Grow_bags": "Aquaponic Grow Bags",
        "Bag_description": "These aquaponic grow bags are specially designed for growing plants in aquaponic systems.",
        "prices": "14.99",
        "Bag_image": "https://agrierp.com/blog/wp-content/uploads/2022/10/Aquaponics-System.jpg"
    },

    
    {
        "Grow_bags": "Smart Pot Grow Bags",
        "Bag_description": "The fabric construction of these smart pot grow bags allows for proper air and water circulation.",
        "prices": "500.99",
        "Bag_image": "https://m.media-amazon.com/images/I/71C71dJzXGL._AC_UF350,350_QL80_.jpg"
    }
]




indoor_plants_list=[]
outdoor_plants_list=[]
seed_indoor_list=[]
fetilizer_list=[]
Grow_bags_list=[]


for i in outdoor_plants:
    outdoor_plants_list.append(i['plant_Name'])

for i in indoor_plants:
    indoor_plants_list.append(i['plant_Name'])
for i in seed_indoor:
    seed_indoor_list.append(i['seed_Name'])
for i in fetilizer:
    fetilizer_list.append(i['fetilizer_name'])
for i in Grow_bags:
    Grow_bags_list.append(i['Grow_bags'])

'''if "Smart Pot Grow Bags" in Grow_bags_list:
    x = Grow_bags_list.index("Smart Pot Grow Bags")
    print(x)
    print(Grow_bags[7])'''




'''indoor_plants1=[]
for i in range(0,len(indoor_plants),3):
    indoor_plants1.append(indoor_plants[i:i+3])

"for i in indoor_plants1:
    for j in i:
        print(j["plant_Name"], end=" ")
    print("\n")
'''

