from database import init_db, db_session
from models import *

# Note that the links (learn more button link) are not all correct. 
# I just wanted to get them into the database but it was tedious to create them all
# so many of them have the same link. This can be easily changed because in practice
# if the menlo snack shack were to adopt this website they would have to update
# all the snacks anyway.

init_db()
# initialize updates page
snack1 = Snack(name="PB&J", category="upcoming", image="https://www.cookiedoughandovenmitt.com/wp-content/uploads/2017/07/toasted-peanut-butter-and-jelly-sandwich-2-picture.jpg", link="https://www.peanutbutter.com/recipes/the-classic-peanut-butter-and-jelly-sandwich")
snack2 = Snack(name="Hot Dog", category="upcoming", image="https://food.fnr.sndimg.com/content/dam/images/food/plus/fullset/2020/06/08/0/FNM_070120-Grilled-Hot-Dogs_s4x3.jpg.rend.hgtvcom.406.406.suffix/1591625198177.jpeg", link="https://en.wikipedia.org/wiki/Hot_dog")
snack3 = Snack(name="Ice Cream Sandwich", category="upcoming", image="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IceCreamSandwich.jpg/1200px-IceCreamSandwich.jpg", link="https://www.amazon.com/Jack-Links-Beef-Jerky-Original/dp/B00VB1XXMS")
snack4 = Snack(name="Popsicle", category="upcoming", image="https://icecreamfromscratch.com/wp-content/uploads/2022/05/Strawberry-Popsicles-1.2-735x1103.jpg", link="https://www.amazon.com/Orville-Redenbachers-Microwave-Popcorn-Butter/dp/B07KWWGKJS/")
snack5 = Snack(name="Gushers", category="upcoming", image="https://i.ebayimg.com/images/g/8L8AAOSw3AJjhjz4/s-l1600.png", link="https://www.amazon.com/Snyders-Hanover-Pretzels-Nuggets-Pound/dp/B01HIJ8WUA/")
snack6 = Snack(name="Lays", category="upcoming", image="https://m.media-amazon.com/images/I/813axPlVxBL.jpg", link="https://www.amazon.com/Welchs-Fruit-Snacks-Variety-Ounce/dp/B083JXYFL3")
snack7 = Snack(name="Sprite", category="upcoming", image="https://m.media-amazon.com/images/I/71-29yqCPzL.jpg", link="https://www.amazon.com/Quaker-Rice-Cakes-Variety-Pack/dp/B01I9EO8OQ")
snack8 = Snack(name="Coke", category="upcoming", image="https://cdn.shoplightspeed.com/shops/617742/files/51836822/coca-cola-coca-cola-coke-12-oz-can.jpg", link="https://www.amazon.com/Quaker-Chewy-Granola-Variety-Pack/dp/B01KMHYVYU")

db_session.add_all([snack1, snack2, snack3, snack4, snack5, snack6, snack7, snack8])

# initialize food category
snack1 = Snack(name="Cinnamon Roll", category="food", image="https://thewoksoflife.com/wp-content/uploads/2021/01/fluffy-cinnamon-rolls-18.jpg", link="https://www.amazon.com/Planters-Nuts-Chocolate-Trail-6oz/dp/B00TYA8JRW/")
snack2 = Snack(name="Muffin", category="food", image="https://static.onecms.io/wp-content/uploads/sites/19/2011/04/08/chocolate-chip-muffins-ck-2000.jpg", link="https://www.target.com/p/tostitos-original-tortilla-chips-13oz/-/A-12937378")
snack3 = Snack(name="Pretzel", category="food", image="https://handletheheat.com/wp-content/uploads/2021/09/how-to-make-homemade-pretzels-SQUARE.jpg", link="https://www.amazon.com/Jack-Links-Beef-Jerky-Original/dp/B00VB1XXMS")
snack4 = Snack(name="French Fries", category="food", image="https://www.fifteenspatulas.com/wp-content/uploads/2011/09/French-Fries-Recipe-500x500.jpg", link="https://www.amazon.com/Orville-Redenbachers-Microwave-Popcorn-Butter/dp/B07KWWGKJS/")
snack5 = Snack(name="Pizza", category="food", image="https://slicelife.imgix.net/11269/photos/original/TheSlicePizza_CheesePizza.jpg?auto=compress&auto=format", link="https://www.amazon.com/Snyders-Hanover-Pretzels-Nuggets-Pound/dp/B01HIJ8WUA/")
snack6 = Snack(name="Apple", category="food", image="https://www.applesfromny.com/wp-content/uploads/2020/06/SnapdragonNEW.png", link="https://www.amazon.com/Welchs-Fruit-Snacks-Variety-Ounce/dp/B083JXYFL3")
snack7 = Snack(name="Orange", category="food", image="https://freshwaysupermarkets.weebly.com/uploads/1/3/2/0/132031192/s218992050954678001_p3_i1_w650.jpeg", link="https://www.amazon.com/Quaker-Rice-Cakes-Variety-Pack/dp/B01I9EO8OQ")
snack8 = Snack(name="Banana", category="food", image="https://img.freepik.com/free-vector/vector-ripe-yellow-banana-bunch-isolated-white-background_1284-45456.jpg", link="https://www.amazon.com/Quaker-Chewy-Granola-Variety-Pack/dp/B01KMHYVYU")

db_session.add_all([snack1, snack2, snack3, snack4, snack5, snack6, snack7, snack8])

# initialize drink category
snack1 = Snack(name="Arizona Tea", category="drink", image="https://www.gvwinestore.com/wp-content/uploads/2020/09/arizona-iced-tea-lemon-cn.png", link="https://drinkarizona.com/products/green-tea-16oz_9oz")
snack2 = Snack(name="Fairlife", category="drink", image="https://m.media-amazon.com/images/I/81WQzf5x7DL.jpg", link="https://fairlife.com/ultra-filtered-milk/chocolate-milk/")
snack3 = Snack(name="Gatorade", category="drink", image="https://www.kroger.com/product/images/large/front/0005200001035", link="https://www.gatorade.com/fuel/hydration/gatorade-thirst-quencher/bottle/cool-blue")
snack4 = Snack(name="Naked Juice", category="drink", image="https://www.nakedjuice.com/images/products/core_mighty_mango.png", link="https://www.amazon.com/Orville-Redenbachers-Microwave-Popcorn-Butter/dp/B07KWWGKJS/")
snack5 = Snack(name="Izze", category="drink", image="https://www.kroger.com/product/images/large/front/0083609301108", link="https://www.amazon.com/Snyders-Hanover-Pretzels-Nuggets-Pound/dp/B01HIJ8WUA/")
snack6 = Snack(name="Lemonade", category="drink", image="https://www.kroger.com/product/images/large/front/0002500005801", link="https://www.amazon.com/Welchs-Fruit-Snacks-Variety-Ounce/dp/B083JXYFL3")
snack7 = Snack(name="Coffee", category="drink", image="https://target.scene7.com/is/image/Target/GUEST_5befc930-6f2c-40d8-9d9e-513ad264cf0f?wid=488&hei=488&fmt=pjpeg", link="https://www.amazon.com/Quaker-Rice-Cakes-Variety-Pack/dp/B01I9EO8OQ")
snack8 = Snack(name="Prime", category="drink", image="https://target.scene7.com/is/image/Target/GUEST_3a162f2f-085b-4782-b1ea-db8fdcdccac7?wid=488&hei=488&fmt=pjpeg", link="https://www.amazon.com/Quaker-Chewy-Granola-Variety-Pack/dp/B01KMHYVYU")

db_session.add_all([snack1, snack2, snack3, snack4, snack5, snack6, snack7, snack8])

# initialize snack category
snack1 = Snack(name="Doritos", category="snack", image="https://pics.walgreens.com/prodimg/629445/900.jpg", link="https://www.amazon.com/Planters-Nuts-Chocolate-Trail-6oz/dp/B00TYA8JRW/")
snack2 = Snack(name="Ruffles", category="snack", image="https://m.media-amazon.com/images/I/81Aak49pu4L.jpg", link="https://www.target.com/p/tostitos-original-tortilla-chips-13oz/-/A-12937378")
snack3 = Snack(name="Trail Mix", category="snack", image="https://www.alisonspantry.com/uploads/new-products/4005_1.jpg", link="https://www.amazon.com/Jack-Links-Beef-Jerky-Original/dp/B00VB1XXMS")
snack4 = Snack(name="Beef Jerky", category="snack", image="https://www.jacklinks.com/shop/media/catalog/product/1/0/10000018012_3.25oz_jl_bf_pepp_jerk_hero.png", link="https://www.amazon.com/Orville-Redenbachers-Microwave-Popcorn-Butter/dp/B07KWWGKJS/")
snack5 = Snack(name="Nutella Sticks", category="snack", image="https://cdn.shopify.com/s/files/1/0816/7387/products/NutellaGO52g_grande.jpg?v=1632177213", link="https://www.amazon.com/Snyders-Hanover-Pretzels-Nuggets-Pound/dp/B01HIJ8WUA/")
snack6 = Snack(name="Fruit Snacks", category="snack", image="https://cdn.shopify.com/s/files/1/0102/3950/8531/products/33689_welchs_fruit_snacks_0.9_oz..jpg?v=1576013645", link="https://www.amazon.com/Welchs-Fruit-Snacks-Variety-Ounce/dp/B083JXYFL3")
snack7 = Snack(name="Granola Bars", category="snack", image="https://i5.peapod.com/c/YV/YV8KQ.png", link="https://www.amazon.com/Quaker-Rice-Cakes-Variety-Pack/dp/B01I9EO8OQ")
snack8 = Snack(name="Popcorn", category="snack", image="https://m.media-amazon.com/images/I/71LvkQi3puS.jpg", link="https://www.amazon.com/Quaker-Chewy-Granola-Variety-Pack/dp/B01KMHYVYU")

db_session.add_all([snack1, snack2, snack3, snack4, snack5, snack6, snack7, snack8])

# initialize dessert category
snack1 = Snack(name="Choco Taco", category="dessert", image="https://static01.nyt.com/images/2022/07/27/multimedia/26xp-chocotaco/26xp-chocotaco-superJumbo-v2.jpg", link="https://www.amazon.com/Planters-Nuts-Chocolate-Trail-6oz/dp/B00TYA8JRW/")
snack2 = Snack(name="Brownie", category="dessert", image="https://i0.wp.com/chefsavvy.com/wp-content/uploads/super-chewy-brownies.jpg?resize=665%2C782&ssl=1", link="https://www.target.com/p/tostitos-original-tortilla-chips-13oz/-/A-12937378")
snack3 = Snack(name="Klondike Bar", category="dessert", image="https://www.kroger.com/product/images/large/front/0007585601147", link="https://www.amazon.com/Jack-Links-Beef-Jerky-Original/dp/B00VB1XXMS")
snack4 = Snack(name="Drumstick", category="dessert", image="https://images.heb.com/is/image/HEBGrocery/000543915", link="https://www.amazon.com/Orville-Redenbachers-Microwave-Popcorn-Butter/dp/B07KWWGKJS/")
snack5 = Snack(name="Popsicle", category="dessert", image="https://www.kroger.com/product/images/large/front/0007756700156", link="https://www.amazon.com/Snyders-Hanover-Pretzels-Nuggets-Pound/dp/B01HIJ8WUA/")
snack6 = Snack(name="Cookie", category="dessert", image="https://assets.bonappetit.com/photos/5ca534485e96521ff23b382b/1:1/w_2560%2Cc_limit/chocolate-chip-cookie.jpg", link="https://www.amazon.com/Welchs-Fruit-Snacks-Variety-Ounce/dp/B083JXYFL3")
snack7 = Snack(name="Pop Ups", category="dessert", image="https://www.kroger.com/product/images/large/front/0007756700314", link="https://www.amazon.com/Quaker-Rice-Cakes-Variety-Pack/dp/B01I9EO8OQ")
snack8 = Snack(name="Spongebob", category="dessert", image="https://static.wikia.nocookie.net/spongebob/images/2/24/SpongeBob_popsicle.png/revision/latest/scale-to-width-down/300?cb=20221024230215", link="https://www.amazon.com/Quaker-Chewy-Granola-Variety-Pack/dp/B01KMHYVYU")

db_session.add_all([snack1, snack2, snack3, snack4, snack5, snack6, snack7, snack8])

db_session.commit()