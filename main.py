import flet as ft
from time import sleep
from json1 import indoor_plants
from json1 import outdoor_plants
from json1 import Grow_bags
from json1 import fetilizer
from json1 import seed_indoor
from json1 import indoor_plants_list, outdoor_plants_list, seed_indoor_list, fetilizer_list, Grow_bags_list
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")


def main(page: ft.Page):
    page.title = "home"
    page.bgcolor = "white"

    page.scroll: ft.ScrollMode = "HIDDEN"

    mydb_main = myclient["metoo"]
    mycollection_for_login = mydb_main["login"]

# -------------------------------------------------------------------------------------------------
    # here from json file we take the data nd place in the text1.container1

    name = ft.Text("Plant O")
    z1 = ft.Column([ft.Row([ft.IconButton(ft.icons.LOCATION_CITY, icon_color="green"), ft.Text(
        "  ELURU", size=15)], spacing=1), ft.Text("  Srirampuram, Godavari dist"), ft.Text("   521301")], spacing=0)
    z4 = ft.Column([ft.Row([ft.IconButton(ft.icons.MESSENGER_SHARP, icon_color="green", url="https://chat.whatsapp.com/EkBrFezO0sfGm3Sll6IM4Z"), ft.Text(
        "+91 7702837610")], spacing=1), ft.Row([ft.Text(" Call/What's app"), ft.Text("24/7support")], spacing=1)], spacing=1)
    z2 = ft.Column([ft.Row([ft.IconButton(ft.icons.PHONE_ROUNDED, icon_color="green"), ft.Text(
        "+91 7702837610")], spacing=1), ft.Text("    24/7 support")], spacing=1)
    z3 = ft.Column([ft.Text("Ganesh Store", size=25, font_family="bold"), ft.Text(
        "Healty Seeds Healty Plants")], spacing=2)

    x = ft.Row([z3, z1, z2, z4], alignment="spacebetween")

    y = ft.Card(ft.Container(
        content=x,
        border_radius=20,
        padding=20,
        bgcolor=ft.colors.LIGHT_GREEN_50
    ),

        width=1500,
        height=110,



    )

    # -----------------------------------------------------------------------------
    indoor_plants_names_side1 = ft.Column(
        spacing=50,

        on_scroll=True


    )

    outdoor_plants_name_side1 = ft.Column(
        spacing=30,
        on_scroll=True
    )
    Grow_bags__names_side1 = ft.Column(
        spacing=50,

        on_scroll=True


    )
    fetilizer__names_side1 = ft.Column(
        spacing=50,

        on_scroll=True


    )
    seeds__names_side1 = ft.Column(
        spacing=50,

        on_scroll=True


    )

    for i in indoor_plants:

        indoor_plants_names_side1.controls.append(

            ft.TextButton(i["plant_Name"],)
        )
    for i in outdoor_plants:
        outdoor_plants_name_side1.controls.append(
            ft.TextButton(i["plant_Name"])
        )
    for i in Grow_bags:
        Grow_bags__names_side1.controls.append(
            ft.TextButton(i["Grow_bags"])

        )
    for i in fetilizer:
        fetilizer__names_side1.controls.append(
            ft.TextButton(i["fetilizer_name"])

        )
    for i in seed_indoor:
        seeds__names_side1.controls.append(
            ft.TextButton(i["seed_Name"])

        )

    global y100
    y100 = 0
    # ----------------------------------------------------------------------------------------------------------
    # containters

    text_1container = ft.Column([ft.Text("M", size=100, weight=ft.FontWeight.W_900), ft.Text(
        "E", size=100,  weight=ft.FontWeight.W_900), ft.Text("T", size=110, weight=ft.FontWeight.W_900), ft.Text("O", size=95,  weight=ft.FontWeight.W_900), ft.Text("O", size=95,  weight=ft.FontWeight.W_900)], spacing=0)
    text_2container = ft.Image(
        src="https://i.pinimg.com/originals/61/4d/6a/614d6adfa64b4a8dc935a34e834c72ec.jpg", fit=ft.ImageFit.FILL)
    metoo_container = ft.Container(content=text_1container, width=200, height=750, margin=5, border_radius=30,
                                   bgcolor="grey", alignment=ft.alignment.center)
    card1_metoo = ft.Card(content=metoo_container,
                          width=300, height=800, color="white")
    # plants_display_cotainter its was plaaced in side the card2_plants
    plants_display_containter = ft.Container(
        content=text_2container, bgcolor="grey", width=750, margin=5, height=750, border_radius=1000)
    cart_container = ft.Container(width=350, visible=False)
    cart_container_card = ft.Card(
        content=cart_container, width=450, visible=False)
    card2_plants = ft.Card(content=plants_display_containter,
                           width=850, height=800, color="white")
    divide1 = ft.Card(ft.Container(width=2, bgcolor="black",
                      height="450"), height=800)  # containter  200, 750
    container_rows = ft.Row(
        [card1_metoo, divide1, card2_plants, cart_container_card], spacing=1)


# ------------------------------------------------------------------------------------------------------------
    # adding images in grid view

    images = ft.GridView(  # indoor plants

        expand=1,
        max_extent=410,

        spacing=0)
    images2 = ft.GridView(

        expand=1,  # outdoor_plants
        max_extent=410,

        spacing=0,
        runs_count=5

    )
    images3 = ft.GridView(

        expand=1,
        max_extent=410,  # bags

        spacing=0,
        runs_count=5



    )
    images4 = ft.GridView(

        expand=1,
        max_extent=410,  # fetilizer

        spacing=0,
        runs_count=5
    )
    images5 = ft.GridView(

        expand=1,
        max_extent=410,  # fetilizer

        spacing=0,
        runs_count=5
    )


# -------------------------------------------------------------------------------------------------------
    # ----here metto_clear , metoo_clear1 is ude to creat the data in containers


    def metoo_clear(e):
        z = e.control.data
        metoo_container.clean()
        plants_display_containter.clean()
        metoo_container.bgcolor = "white"
        metoo_container.width = 100
        card1_metoo.width = 200
        plants_display_containter.width = 1350
        plants_display_containter.height = 650
        plants_display_containter.bgcolor = "white"
        card2_plants.width = 1350
        card2_plants.height = 800
        plants_display_containter.border_radius = 0
        page.update()
        if z == "indoor_plants":
            plants_display_containter.content = images
            metoo_container.content = indoor_plants_names_side1
            page.update()

    def metoo_clear2(e):

        z = e.control.data
        metoo_container.clean()
        plants_display_containter.clean()
        metoo_container.bgcolor = "white"
        metoo_container.width = 100
        card1_metoo.width = 200
        plants_display_containter.width = 1350
        plants_display_containter.height = 650
        plants_display_containter.bgcolor = "white"
        card2_plants.width = 1350
        card2_plants.height = 800
        plants_display_containter.border_radius = 0
        page.update()
        if z == "outdoor_plants":
            plants_display_containter.content = images2
            metoo_container.content = outdoor_plants_name_side1
            page.update()

    def metoo_clear3(e):
        z = e.control.data
        metoo_container.clean()
        plants_display_containter.clean()
        metoo_container.bgcolor = "white"
        metoo_container.width = 100
        card1_metoo.width = 200
        plants_display_containter.width = 1350
        plants_display_containter.height = 650
        plants_display_containter.bgcolor = "white"
        card2_plants.width = 1350
        card2_plants.height = 800
        plants_display_containter.border_radius = 0
        page.update()

        plants_display_containter.content = images3
        metoo_container.content = Grow_bags__names_side1
        page.update()

    def metoo_clear4(e):
        z = e.control.data
        metoo_container.clean()
        plants_display_containter.clean()
        metoo_container.bgcolor = "white"
        metoo_container.width = 100
        card1_metoo.width = 200
        plants_display_containter.width = 1350
        plants_display_containter.height = 650
        plants_display_containter.bgcolor = "white"
        card2_plants.width = 1350
        card2_plants.height = 800
        plants_display_containter.border_radius = 0
        page.update()

        plants_display_containter.content = images4
        metoo_container.content = fetilizer__names_side1
        page.update()

    def metoo_clear5(e):
        z = e.control.data
        metoo_container.clean()
        plants_display_containter.clean()
        metoo_container.bgcolor = "white"
        metoo_container.width = 100
        card1_metoo.width = 200
        plants_display_containter.width = 1350
        plants_display_containter.height = 650
        plants_display_containter.bgcolor = "white"
        card2_plants.width = 1350
        card2_plants.height = 800
        plants_display_containter.border_radius = 0
        page.update()

        plants_display_containter.content = images5    # seeds
        metoo_container.content = seeds__names_side1
        page.update()
    # if phase any local variable error or control acess error that chage the position of variables and menthod
    # means after allocation or create theonly you can delete the container


# ---------------------------------------------------------------------------------------------
# add to card message


    def add_item_to_cart(e):
        global list_for_add_items
        list_for_add_items = []
        if user2.value == "User Name":
            page.dialog = add_widow2
            add_widow2.open = True
            page.update()
        else:
            page.dialog = add_widow
            add_widow.open = True
            som = e.control.data
            cart_items = {
                "plant_name": som[0],
                "plant_image": som[1],
                "plant_price": som[2]
            }
            phone = phone_login.value
            print(str(phone))
            phone = "user"+str(phone)+"cart"
            db_with_phone = mydb_main[phone]
            db_with_phone.insert_one(cart_items)

            page.update()


# add_widow is to show alertDialog for when user is add any thing to cart or not
    add_widow = ft.AlertDialog(
        modal=False,

        title=ft.ElevatedButton(
            "Add to Cart", icon=ft.icons.YARD_ROUNDED, color=ft.colors.PINK_ACCENT),
        content=ft.Text("TNKS FOR ADDING", text_align="CENTER"),

        shape=ft.ContinuousRectangleBorder(
            radius=50
        )

    )
# add_window2 for wheather it used to login or not
    add_widow2 = ft.AlertDialog(
        modal=False,

        title=ft.ElevatedButton(
            "Please confirm ", icon=ft.icons.YARD_ROUNDED, color=ft.colors.PINK_ACCENT),
        content=ft.Text("Login to  METTO", text_align="CENTER"),

        shape=ft.ContinuousRectangleBorder(
            radius=50
        )

    )


# ------------------------------------------------------------------------------------------------------------------------------
   # PLANT NAME CLICK WINDOW

    def review_button(e):
        x = ft.Column([ft.Text(value=review.value, size=25)])
        review1.content = ft.Column([x])
        page.update()
    click_image_card = ft.Container(
        width=450, height=450, border_radius=20, alignment=ft.alignment.top_left, margin=10)
    click_image_card2 = ft.Container(width=450, height=100)
    review1 = ft.Container(width=200, height=50)

    submit = ft.ElevatedButton(
        "submit", width=250, height=50, on_click=review_button)
    review = ft.TextField(
        label="review", hint_text="add your rivew", width=650, height=50,)
# ------------------------------------------------------------------------------------------==
# ------------------------------------------------------------------------------------------------------------------
# Buy button view

    def place_order_save_data(e):
        x7000 = x6000
        total1 = e.control.data

        phone10 = phone_login.value
        phone10 = "user"+str(phone10)+"order"

        order_details_to_db = mydb_main[phone10]
        order_details = {
            "order_item": x7000[0],
            "item_image": x7000[1],
            "item_price": str(total1),

            "status": "Not Deliver",
            "deiliver": Address_details.value,
            "city": City.value
        }
        order_details_to_db.insert_one(order_details)

        # print("ggg", x7000)
        contact_number.value = ""
        Address_details.value = ""
        City.value = ""
        pincode.value = ""
        buy_containter.clean()
        buy_containter.content = ft.Column([
            ft.Row([ft.IconButton(icon=ft.icons.YARD_ROUNDED, icon_color="pink"), ft.Text(
                "Order placed")], ft.Text("Thank for order"))
        ])
        buy_containter.width = 200
        buy_containter.height = 50
        add_widow_forbuy.content = buy_containter
        page.update()
        sleep(2)
        add_widow_forbuy.open = False
        buy_containter.width = 450
        buy_containter.height = 550
        buy_containter.content = column_for_buy
        add_widow_forbuy.content = buy_containter
        page.update()

    def data_save(e):
        x7000 = x6000
        buy_containter.clean()

        name_item = x7000[0]
        Gst = 5
        transport_charge = 20
        total = float(x7000[2])+Gst+transport_charge
        total = int(total)
        print(total)
        buy_containter.content = ft.Column([
            ft.Text(value="Product name             "+name_item),
            ft.Text(value="Product price            "+x7000[2]),
            ft.Text(value="GST"+"                   "+str(Gst)),
            ft.Text("Transportion Charges           "+str(transport_charge)),
            ft.Text("-------------------------------------------------------"),
            ft.Text("Total                          " + str(total)),
            ft.Text("-------------------------------------=------------------"),
            ft.Row([ft.ElevatedButton(
                "Place Order", on_click=place_order_save_data, data=total)], alignment="center")

        ], spacing=15,)
        add_widow_forbuy.content = buy_containter
        page.update()

    title_for_buy = ft.Row(
        [ft.Text("Order Item", size=20)], alignment="center")
    contact_number = ft.TextField(label="contact number")
    Address_details = ft.TextField(label="Delivery address")
    City = ft.TextField(label="City Name")
    pincode = ft.TextField(label="pin code")
    place_order = ft.Row(
        [ft.ElevatedButton("Next", on_click=data_save)], alignment='center',)
    column_for_buy = ft.Column([title_for_buy, contact_number, Address_details,
                                City, pincode, place_order,], spacing=20, alignment="CENTER")

    buy_containter = ft.Container(
        content=column_for_buy,

        border_radius=20,
        padding=5,
        width=350,
        height=500

    )
    add_widow_forbuy = ft.AlertDialog(
        modal=False,

        content=buy_containter,
        shape=ft.ContinuousRectangleBorder(
            radius=50
        )

    )

    def open_dlg_modal_for_buy(e):
        if user2.value == "User Name":
            page.dialog = add_widow2
            add_widow2.open = True
            page.update()
        else:
            global x6000
            x6000 = ""
            z1000 = e.control.data

            page.dialog = add_widow_forbuy
            x6000 = z1000
            add_widow_forbuy.open = True
            page.update()


# --------------------------------------------------------------------------------------------------
    # on click plant name the the image of that plant and the discription of that plant will display

    def onclick_plant_name(e):

        plant_name_taking = e.control.data

        plants_display_containter.clean()
        plants_display_containter.width = 1350
        plants_display_containter.height = 650

        plants_display_containter.alignment = ft.alignment.top_right
        plants_display_containter.bgcolor = "white"
        z = []

        if plant_name_taking in indoor_plants_list:
            index_of_plant = indoor_plants_list.index(plant_name_taking)
            x100 = indoor_plants[index_of_plant]
            x200 = (ft.Image(src=x100["plant_image"], fit=ft.ImageFit.FILL))
            text1 = ft.Row([ft.Text(plant_name_taking, size=55), ft.Text(
                x100["plant_price"], size=40)], spacing=20)
            z.append(plant_name_taking)
            z.append(x100["plant_image"])
            z.append(x100["plant_price"])
            text12 = ft.Column([text1, ft.Row([ft.ElevatedButton(
                "Add to Cart", on_click=add_item_to_cart, data=z)], alignment="CENTER"),])
            click_image_card.content = x200
            click_image_card2.content = text12

            t = ft.Row([click_image_card, click_image_card2], spacing=20)
            t2 = ft.Row([review, submit])
            t1 = ft.Column(
                [t, ft.Row([ft.Text("        "), ft.ElevatedButton(
                    "Buy", width=200, height=50, bgcolor="green", color="white", data=z, on_click=open_dlg_modal_for_buy)]), t2, review1], spacing=10)

            plants_display_containter.content = t1
            page.update()
        elif plant_name_taking in outdoor_plants_list:
            index_of_plant = outdoor_plants_list.index(plant_name_taking)
            x100 = outdoor_plants[index_of_plant]
            x200 = (ft.Image(src=x100["plant_image"], fit=ft.ImageFit.COVER))
            text1 = ft.Row([ft.Text(plant_name_taking, size=55), ft.Text(value="Rs" +
                                                                         x100["plant_price"], size=40)], spacing=20)
            z.append(plant_name_taking)
            z.append(x100["plant_image"])
            z.append(x100["plant_price"])
            text12 = ft.Column(
                [text1, ft.Row([ft.ElevatedButton("Add to Cart", on_click=add_item_to_cart, data=z)], alignment="CENTER"),])
            click_image_card.content = x200
            click_image_card2.content = text12

            t = ft.Row([click_image_card, click_image_card2], spacing=20)
            t2 = ft.Row([review, submit])
            t1 = ft.Column(
                [t, ft.Row([ft.Text("        "), ft.ElevatedButton(
                    "Buy", width=200, height=50, bgcolor="green", color="white", data=z, on_click=open_dlg_modal_for_buy)]), t2, review1], spacing=10)

            plants_display_containter.content = t1
            page.update()
        elif plant_name_taking in Grow_bags_list:
            index_of_plant = Grow_bags_list.index(plant_name_taking)
            x100 = Grow_bags[index_of_plant]
            x200 = (ft.Image(src=x100["Bag_image"],
                    fit=ft.ImageFit.FILL, border_radius=20))
            text1 = ft.Row([ft.Text(plant_name_taking, size=55), ft.Text(value="Rs" +
                                                                         x100["prices"], size=40)], spacing=20)
            z.append(plant_name_taking)
            z.append(x100["Bag_image"])
            z.append(x100["prices"])
            text12 = ft.Column(
                [text1, ft.Row([ft.ElevatedButton("Add to Cart", on_click=add_item_to_cart, data=z)], alignment="CENTER"),])
            click_image_card.content = x200
            click_image_card2.content = text12

            t = ft.Row([click_image_card, click_image_card2], spacing=20)
            t2 = ft.Row([review, submit])
            discription = ft.Text(value=x100["Bag_description"], size=20)
            t1 = ft.Column(
                [t, ft.Row([ft.Text("        "), ft.ElevatedButton(
                    "Buy", width=200, height=50, bgcolor="green", color="white", data=z, on_click=open_dlg_modal_for_buy)]), discription, t2, review1], spacing=40)

            plants_display_containter.content = t1
            page.update()
        elif plant_name_taking in fetilizer_list:
            index_of_plant = fetilizer_list.index(plant_name_taking)
            x100 = fetilizer[index_of_plant]
            x200 = (
                ft.Image(src=x100["fetilizer_image"], fit=ft.ImageFit.FILL, border_radius=20))
            text1 = ft.Row([ft.Text(plant_name_taking, size=55), ft.Text(value="Rs" +
                                                                         x100["fetilizer_price"], size=40)], spacing=20)
            z.append(plant_name_taking)
            z.append(x100["fetilizer_image"])
            z.append(x100["fetilizer_price"])
            text12 = ft.Column(
                [text1, ft.Row([ft.ElevatedButton("Add to Cart", on_click=add_item_to_cart, data=z)], alignment="CENTER"),])
            click_image_card.content = x200
            click_image_card2.content = text12
            discription = ft.Text(value=x100["description"], size=20)
            t = ft.Row([click_image_card, click_image_card2], spacing=20)
            t2 = ft.Row([review, submit])
            t1 = ft.Column(
                [t, ft.Row([ft.Text("        "), ft.ElevatedButton(
                    "Buy", width=200, height=50, bgcolor="green", color="white", data=z, on_click=open_dlg_modal_for_buy)]), discription, t2, review1], spacing=10)

            plants_display_containter.content = t1
            page.update()
        elif plant_name_taking in seed_indoor_list:
            index_of_plant = seed_indoor_list.index(plant_name_taking)
            x100 = seed_indoor[index_of_plant]
            x200 = (
                ft.Image(src=x100["seed_image"], fit=ft.ImageFit.FILL, border_radius=20))
            text1 = ft.Row([ft.Text(plant_name_taking, size=55), ft.Text(value="Rs" +
                                                                         x100["seed_price"], size=40)], spacing=20)
            z.append(plant_name_taking)
            z.append(x100["seed_image"])
            z.append(x100["seed_price"])
            text12 = ft.Column(
                [text1, ft.Row([ft.ElevatedButton("Add to Cart", on_click=add_item_to_cart, data=z)], alignment="CENTER"),])
            click_image_card.content = x200
            click_image_card2.content = text12

            t = ft.Row([click_image_card, click_image_card2], spacing=20)
            t2 = ft.Row([review, submit])
            t1 = ft.Column(
                [t, ft.Row([ft.Text("        "), ft.ElevatedButton(
                    "Buy", width=200, height=50, bgcolor="green", color="white", data=z, on_click=open_dlg_modal_for_buy)]), t2, review1, review], spacing=30)

            plants_display_containter.content = t1
            page.update()

    for i in indoor_plants:
        images.controls.append(
            ft.Column(
                controls=[
                    ft.Card(
                        content=ft.Image(src=i["plant_image"], fit=ft.ImageFit.FILL, border_radius=10
                                         ),
                        width=290,
                        height=230,




                    ),

                    ft. Column([ft.Row(
                        [ft.TextButton(text=i['plant_Name'], data=i["plant_Name"], on_click=onclick_plant_name), ft.Text(value=i['plant_price'], size=18)], alignment=ft.alignment.center
                    ),])


                ], tight=True,
            )
        )

    for i in outdoor_plants:
        images2.controls.append(
            ft.Column(
                controls=[
                    ft.Card(
                        content=ft.Image(src=i["plant_image"], fit=ft.ImageFit.FILL, border_radius=10
                                         ),
                        width=290,
                        height=230,




                    ),

                    ft. Column([ft.Row(
                        [ft.TextButton(text=i['plant_Name'], data=i["plant_Name"], on_click=onclick_plant_name), ft.Text(value=i['plant_price'], size=18)], alignment=ft.alignment.center
                    ), ])


                ], tight=True,
            )
        )

    for i in Grow_bags:
        images3.controls.append(
            ft.Column(
                controls=[
                    ft.Card(
                        content=ft.Image(src=i["Bag_image"], fit=ft.ImageFit.FILL, border_radius=10
                                         ),
                        width=290,
                        height=230,




                    ),

                    ft. Column([ft.Row(
                        [ft.TextButton(text=i['Grow_bags'], data=i["Grow_bags"], on_click=onclick_plant_name), ft.Text(value=i['prices'], size=18)], alignment=ft.alignment.center
                    ), ])


                ], tight=True,
            )
        )
    for i in fetilizer:
        images4.controls.append(
            ft.Column(
                controls=[
                    ft.Card(
                        content=ft.Image(src=i["fetilizer_image"], fit=ft.ImageFit.FILL, border_radius=10
                                         ),
                        width=290,
                        height=230,




                    ),

                    ft. Column([ft.Row(
                        [ft.TextButton(text=i['fetilizer_name'], data=i["fetilizer_name"], on_click=onclick_plant_name), ft.Text(value=i['fetilizer_price'], size=18)], alignment=ft.alignment.center
                    ), ])


                ], tight=True,
            )
        )
    for i in seed_indoor:
        images5.controls.append(
            ft.Column(
                controls=[
                    ft.Card(
                        content=ft.Image(src=i["seed_image"], fit=ft.ImageFit.FILL, border_radius=10
                                         ),
                        width=290,
                        height=230,




                    ),

                    ft. Column([ft.Row(
                        [ft.TextButton(text=i['seed_Name'], data=i["seed_Name"], on_click=onclick_plant_name), ft.Text(value=i['seed_price'], size=18)], alignment=ft.alignment.center
                    ),])


                ], tight=True,
            )
        )

# ----------------------------------------------------------------
  # registration details into mongo db

# ---------------------------------------------------------------------------------------------
 # for login and register view here then button is sign_up
    def register_page_validation(e):
        l100 = True
        if not name.value:
            name.error_text = "please enter name"
            login_display_container.update()
            dlg_modal.update()
        elif email.value == "":
            email.error_text = "please enter email"
        elif phone.value == "" and len(phone.value) == 10:
            phone.error_text = "please enter mobile number"
        elif password.value == "":
            password.error_text = "please enter password"

            password.update()
        elif reenter.value == "":
            reenter.error_text = "please enter renter password"

            reenter.update()

        elif password.value != reenter.value:
            password.error_text = "password and confrim password is not equal"

            page.update()
        else:
            check1 = mycollection_for_login.count_documents(
                {"phone_no": phone.value})
            if check1 == 1:
                l100 = False
                password.error_text = ""
                name.error_text = ""
                phone.error_text = "This number already register"
                page.update()

            if l100 == True:
                # registration details into mongo db
                register_mongo = {
                    "user_name": name.value,
                    "phone_no": phone.value,
                    "password": password.value
                }

                mycollection_for_login.insert_one(register_mongo)
                login_display_container.clean()
                login_display_container.width = 150
                login_display_container.height = 40
                login_display_container.content = ft.Text(
                    "sucessfully register", size=15, text_align="center")
                dlg_modal.content = login_display_container
                login_display_container.update()
                dlg_modal.update()
                sleep(1)
                login_display_container.clean()
                login_display_container.width = 340
                login_display_container.height = 255

                login_display_container.content = login_page_col
                dlg_modal.content = login_display_container
                login_display_container.update()
                phone_login.value = ""
                password_login.value = ""
                dlg_modal.update()
    name = ft.TextField(label='Username', hint_text="username", width=450, border_color="white",
                        border_width=2, focused_border_color="white", color="black", cursor_color="white")
    email = ft.TextField(label='email', hint_text="email", width=450,  focused_bgcolor="white",
                         border_color="white", border_width=2, focused_border_color="white", color="black", cursor_color="black")

    phone = ft.TextField(label='phone', hint_text="phone number", width=450, border_color="white",
                         border_width=2, focused_border_color="white", color="black", cursor_color="white")
    password = ft.TextField(label='password', hint_text="passowrd", password=True, can_reveal_password=True, width=450,
                            border_color="white", border_width=2, focused_border_color="white", color="black", cursor_color="white")

    reenter = ft.TextField(label='reenter password', hint_text="re-enter passowrd",
                           password=True, can_reveal_password=True, width=450, border_color="white", border_width=2, focused_border_color="black", color="black", cursor_color="black")

    register_row = ft.Column(
        [name, email, phone, password, reenter], alignment="center", spacing=10)
    register_containter = ft.Container(
        content=register_row,
        width=550,
        height=400,
        border_radius=50,
        padding=40,


    )

    def registration10(e):
        name.value = ""
        name.error_text = ""
        phone.error_text = ""
        password.error_text = ""
        phone.value = ""
        password.value = ""
        email.value = ""
        email.error_text = ""
        reenter.value = ""
        reenter.error_text = ""
        phone_login.value = ""
        password.value = ""

        login_display_container.clean()
        login_display_container.width = 550
        login_display_container.height = 550
        login_display_container.content = registration_page_col

        dlg_modal.content = login_display_container
        login_display_container.update()
        dlg_modal.update()
        page.update()

    def login_1(e):
        phone_login.value = ""
        password_login.value = ""
        phone_login.error_text = ""
        password_login.error_text = ""
        login_display_container.clean()
        login_display_container.width = 350
        login_display_container.height = 250
        login_display_container.update()
        login_display_container.content = login_page_col
        dlg_modal.content = login_display_container
        login_display_container.update()
        dlg_modal.update()
        page.update()

    go_to_login = ft.Text("If you don't have accoun",
                          text_align="center", color="black")
    go_registrion = ft.TextButton("Registration", on_click=registration10)
    back_to_registration = ft.Row(
        [go_to_login, go_registrion], alignment="center")

    button_login = ft.TextButton("login", on_click=login_1)
    text1 = ft.Text("if you have account", color="black")
    register_sbumit = ft.ElevatedButton(
        "submit", on_click=register_page_validation)
    registration_button = ft.Row([register_sbumit, text1, button_login],
                                 alignment="CENTER")

    def login_page_validation(e):

        if phone_login.value == "":
            phone_login.error_text = "please enter mobile number"
            login_display_container.update()
        elif password_login.value == "":
            password_login.error_text = "please enter password"
            login_display_container.update()
        else:
            check2 = mycollection_for_login.count_documents(
                {"phone_no": phone_login.value})
            check3 = mycollection_for_login.find_one(
                {"phone_no": phone_login.value})
            if check2 == 0:
                phone_login.error_text = "you have not registered"
                page.update()
                sleep(2)
                phone_login.error_text = ""
                page.update()

            elif check2 == 1 and check3["password"] == password_login.value:
                check3 = mycollection_for_login.find_one(
                    {"phone_no": phone_login.value})
                # here we take the name from the data base how login
                name = check3["user_name"]
                login_display_container.clean()
                login_display_container.height = 80
                login_display_container.content = ft.Column([ft.Row([ft.IconButton(ft.icons.YARD_SHARP, icon_color="pink"), ft.Text("Thank you for being a member", size=15)], spacing=10), ft.Row([
                                                            ft.Text("#MeToo", size=20)], alignment="center"), ft.Row([ft.Text("Login Sucessfull", size=15)], alignment="center")])
                login_display_container.update()
                sleep(2)
                dlg_modal.open = False
                dlg_modal.update()
                user1.clean()  # CIRCULAR AVATHAR
                user2.clean()  # USER NAME AT  TOP
                user2.value = name.capitalize()

                user1.content = ft.Text(value=name[0].upper())
                all2.clean()
                all2.content = ft.Row([user1, user2])
                orders.visible = True
                cart1.visible = True
                sign_up.visible = False
                logout.visible = True
                page.update()
            else:
                phone_login.error_text = ""
                password_login.error_text = "Incorrect password"
                page.update()

    def reset_password1(e):
        login_display_container.clean()
        login_display_container.height = 250
        login_display_container.content = ft.Column([ft.Row([ft.Text("Reset password", size=20)], alignment="center"), phone_rset, reset_field, ft.Row(
            [reset_button2], alignment="center")], alignment="Center", spacing=10)
        dlg_modal.content = login_display_container
        page.update()

    def reset_password2(e):
        mycollection_for_login = mydb_main["login"]
        phone1 = phone_rset.value
        phone1 = str(phone1)
        if phone_rset.value == "":
            phone_rset.error_text = "Please enter the phone number"
        elif reset_field.value == "":
            reset_field.error_text = "Please enter the new password"
        else:
            phone.error_text = ""
            reset_field.error_text = ""
            number1 = {"phone_no": phone1}
            new_pass = {"$set": {"password": reset_field.value}}
            mycollection_for_login .update_one(number1, new_pass)
            login_display_container.clean()
            login_display_container.height = 90
            login_display_container.content = ft.Column(
                [ft.Text("password reset", size=20)], alignment="center")
            page.update()
            sleep(1)
            login_display_container.clean()
            dlg_modal.clean()
            phone_login.value = ""
            password_login.value = ""
            phone_login.error_text = ""
            password_login.error_text = ""
            login_display_container.width = 550
            login_display_container.height = 650
            login_display_container.content = registration_page_col
            dlg_modal.content = login_display_container
            page.update()
    phone_rset = ft.TextField(label='Phone-no', hint_text="7702837610", width=450, border_color="white",
                              border_width=2, focused_border_color="white", color="black", cursor_color="white")
    phone_login = ft.TextField(label='Phone-no', hint_text="7702837610", width=450, border_color="white",
                               border_width=2, focused_border_color="white", color="black", cursor_color="white")
    password_login = ft.TextField(label='password', hint_text="passowrd", password=True,
                                  can_reveal_password=True, width=450, border_color="white", border_width=2, focused_border_color="black", color="black", cursor_color="white")
    login_button = ft.ElevatedButton("login", on_click=login_page_validation)
    reset_password = ft.TextButton("Reset password", on_click=reset_password1)
    title_login = ft.Text("Login", color="Black", size=20)
    login_row = ft.Column([phone_login,
                           password_login], spacing=10)
    login_containter = ft.Container(
        content=login_row,

        border_radius=20,
        padding=5,

    )

    # ------------------------------------------------------------------------------------------------------------

    registration_page = ft.Column([ft.Row([ft.Text("Registraion", color="black", size=20)], alignment="center"),
                                   register_containter,], horizontal_alignment="center")
    login_page = ft.Column(
        [ft.Row([title_login], alignment="center"),
            login_containter, ft.Row([login_button, reset_password], alignment="center")], spacing=1, horizontal_alignment="center")
    registration_page_col = ft.Column(
        [registration_page, registration_button], spacing=10)
    # combined the login fields(names,pass) back to registration button
    login_page_col = ft.Column([login_page, back_to_registration], spacing=10)
    # to dislay the regiter form and log in form
    login_display_container = ft.Container(
        content=registration_page_col, width=550, height=650)

    reset_field = ft.TextField(label="pasword", hint_text="enter new password")
    reset_button2 = ft.ElevatedButton("reset", on_click=reset_password2)

 # ------------------------------------------------------------------------------------------------------------
  # cart items display

    def remove_item_fromm_cart(e):
        z501 = e.control.data

        phone5 = phone_login.value
        phone5 = str("user"+phone5+"cart")
        remove = mydb_main[phone5]
        # z501 is the data taking from  the sameI(e)
        remove.delete_many({"plant_name": z501[1]})
        back(e)
        page.update()

    def back(e):
        cart_container.clean()
        user_cart_diplay(e)

        page.update()

    def sam(e):
        z500 = e.control.data

        cart_container.content = ft.Column(
            [ft.IconButton(icon=ft.icons.ARROW_BACK_IOS_NEW_OUTLINED, on_click=back), ft.Row([ft.Image(src=z500[0], width=350, height=350),], alignment="center"), ft.Row([ft.Text(value=z500[1], size=25), ft.Text(value=z500[2], size=20)], spacing=15, alignment="center"),
             ft.Row([ft.ElevatedButton("remove from cart", data=z500, on_click=remove_item_fromm_cart)], alignment="center")], spacing=35)
        cart_container.margin = 5
        page.update()

    def close_cart(e):
        cart_container.visible = False
        cart_container_card.visible = False
        plants_display_containter.width = 1350
        plants_display_containter.height = 650

        card2_plants.width = 1350
        card2_plants.height = 800
        page.update()

    def user_cart_diplay(e):

        cart_useritems_in_list = ft.ListView(
            expand=1, spacing=10, padding=20, auto_scroll=True, divider_thickness=10)
        phone2 = str(phone_login.value)
        phone2 = "user"+phone2+"cart"
        user_login_details_from_metoo = mydb_main[phone2]
        user_cart_items = user_login_details_from_metoo.find()

        for i in user_cart_items:
            user_cart_image_retive = ft.Card(content=ft.Image(
                src=i["plant_image"], width=70, height=70, fit=ft.ImageFit.FILL))
            z = []
            z.append(i["plant_image"])
            z.append(i["plant_name"])
            z.append(i["plant_price"])

            user_cart_plant_details_retrive = ft.Row([ft.Text(i["plant_name"], size=18), ft.Text(i["plant_price"], size=15), ft.IconButton(
                icon=ft.icons.RADIO_BUTTON_ON, icon_color=ft.colors.WHITE54, icon_size=30, data=z, on_click=sam)], alignment="center")

            cart_useritems_in_list.controls.append(
                ft.Card(content=ft.Row(
                    [
                        user_cart_image_retive, user_cart_plant_details_retrive
                    ]
                ),
                    width=50,
                    color="yellow",
                    shadow_color=ft.colors.BLACK54,


                )
            )
        cart_container.clean()
        cart_container_card.clean()
        cart_container_card.visible = True
        cart_container.bgcolor = "white"
        plants_display_containter.width = 700

        card2_plants.width = 800
        cart_container.height = 800
        cart_container.visible = True
        cart_container.width = 400
        cart_container_card.width = 450

       # plants_display_containter.border_radius = 0
        # plants_display_containter.bgcolor = "white"
        cart_container.content = ft.Column([ft.IconButton(
            icon=ft.icons.ARROW_BACK_IOS_SHARP, on_click=close_cart), cart_useritems_in_list])
        page.update()

    def remove_item_fromm_order(e):
        z501 = e.control.data

        phone5 = phone_login.value
        phone5 = str("user"+phone5+"order")
        remove = mydb_main[phone5]
        # z501 is the data taking from  the sameI(e)
        remove.delete_many({"order_item": z501[1]})
        back2(e)
        page.update()

    def back2(e):
        cart_container.clean()
        user_order_diplay(e)

        page.update()

    def sam2(e):
        z500 = e.control.data

        cart_container.content = ft.Column(
            [ft.IconButton(icon=ft.icons.ARROW_BACK_IOS_NEW_OUTLINED, on_click=back2), ft.Row([ft.Image(src=z500[0], width=350, height=350),], alignment="center"), ft.Row([ft.Text(value=z500[1], size=25), ft.Text(value=z500[2], size=20)], spacing=15, alignment="center"),
             ft.Row([ft.ElevatedButton("Cancle order", data=z500, on_click=remove_item_fromm_order)], alignment="center")], spacing=35)
        cart_container.margin = 5
        page.update()

    def close_order(e):
        cart_container.visible = False
        cart_container_card.visible = False
        plants_display_containter.width = 1350
        plants_display_containter.height = 650

        card2_plants.width = 1350
        card2_plants.height = 800
        page.update()

    def user_order_diplay(e):

        cart_useritems_in_list = ft.ListView(
            expand=1, spacing=10, padding=20, auto_scroll=True, divider_thickness=10)
        phone2 = str(phone_login.value)
        phone2 = "user"+phone2+"order"
        user_login_details_from_metoo = mydb_main[phone2]
        user_cart_items = user_login_details_from_metoo.find()

        for i in user_cart_items:
            user_cart_image_retive = ft.Card(content=ft.Image(
                src=i["item_image"], width=70, height=70, fit=ft.ImageFit.FILL))
            z = []
            z.append(i["item_image"])
            z.append(i["order_item"])
            z.append(i["item_price"])

            user_cart_plant_details_retrive = ft.Row([ft.Text(i["order_item"], size=18), ft.Text(i["item_price"], size=15), ft.IconButton(
                icon=ft.icons.RADIO_BUTTON_ON, icon_color=ft.colors.WHITE54, icon_size=30, data=z, on_click=sam2)], alignment="center")

            cart_useritems_in_list.controls.append(
                ft.Card(content=ft.Row(
                    [
                        user_cart_image_retive, user_cart_plant_details_retrive
                    ]
                ),
                    width=50,
                    color="yellow",
                    shadow_color=ft.colors.BLACK54,


                )
            )
        cart_container.clean()
        cart_container_card.clean()
        cart_container_card.visible = True
        cart_container.bgcolor = "white"
        plants_display_containter.width = 700

        card2_plants.width = 800
        cart_container.height = 800
        cart_container.visible = True
        cart_container.width = 400
        cart_container_card.width = 450

       # plants_display_containter.border_radius = 0
        # plants_display_containter.bgcolor = "white"
        cart_container.content = ft.Column([ft.IconButton(
            icon=ft.icons.ARROW_BACK_IOS_SHARP, on_click=close_order), cart_useritems_in_list])
        page.update()
# ------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------
    # its is alert bialog we are using as popup message  for login and registration
    dlg_modal = ft.AlertDialog(
        modal=False,

        content=login_display_container,
        adaptive=True,


    )

    # open_dlh_modal is used to open the popup views

    def open_dlg_modal(e):
        name.value = ""
        phone.value = ""
        password.value = ""
        reenter.value = ""
        email.value = ""
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()
    sign_up = ft.TextButton("Signup", on_click=open_dlg_modal)


# ------------------------------------------------------------------------------------------------------------------
# log out


    def logout1(e):
        plants_display_containter.clean()
        metoo_container.clean()
        cart1.visible = False
        orders.visible = False
        sign_up.visible = True
        logout.visible = False
        user1.clean()
        user2.clean()
        cart_container.clean()
        cart_container.visible = False
        user1.content = ft.Text("US")
        user2.value = "User Name"
        user2.size = 17
        plants_display_containter.border_radius = 1000
        card2_plants.width = 850
        card2_plants.height = 800
        card2_plants.color = "white"

        metoo_container.content = text_1container
        metoo_container.bgcolor = "grey"
        metoo_container.alignment = ft.alignment.center

        plants_display_containter.content = text_2container

        plants_display_containter.width = 750
        plants_display_containter.margin = 5
        plants_display_containter.height = 750
        card2_plants.content = plants_display_containter
        page.update()
        sleep(1)

        login_display_container.width = 550
        login_display_container.height = 650
        login_display_container.content = registration_page_col

        page.update()


# ==================================================================================

    seed_dropdown = ft.PopupMenuButton(
        content=ft.Text("plants", size=14, color="#0000EE",
                        weight=ft.FontWeight.W_500),
        items=[
            ft.PopupMenuItem(text="indoor_plants",
                             on_click=metoo_clear, data="indoor_plants"),
            ft.PopupMenuItem(text="outdoor_plants", on_click=metoo_clear2, data="outdoor_plants")])
    # seed_dropdown = ft.TextButton("seeds")
    cart1 = ft.TextButton("Cart", icon=ft.icons.SHOPPING_BAG,
                          icon_color="black", visible=False, on_click=user_cart_diplay)
    orders = ft.TextButton("order", icon=ft.icons.YARD_OUTLINED,
                           visible=False, on_click=user_order_diplay)
    bags = ft.TextButton(text="Bag", on_click=metoo_clear3)
    live_seeds = ft.TextButton("live seeds", on_click=metoo_clear5)
    organization = ft.TextButton("Fertilizers", on_click=metoo_clear4)

    logout = ft.TextButton("Logout", visible=False, on_click=logout1)
    all1 = ft.Row([seed_dropdown, bags, live_seeds, organization,
                   cart1, orders, sign_up, logout], alignment="spacebetween", spacing=10,)
    user1 = ft.CircleAvatar(

        content=ft.Text("US"),
    )
    user2 = ft.Text("User Name", size=17)
    all2 = ft.Container(
        content=ft.Row([user1, user2])

    )

    z = ft.Container(
        content=all1,
        width=900,
        height=40,
        padding=10,
        border_radius=10,
        shadow=ft.BoxShadow(
            blur_radius=10,
            offset=ft.Offset(0, 0),
            color=ft.colors.BLACK54,
            blur_style=ft.ShadowBlurStyle.OUTER,



        ),)
    main_title = ft.Row([z, all2], spacing=100)
    last_container = ft.Card(ft.Container(content=ft.Column([
        ft.Row([z3, z2], alignment="center", spacing=50),
        ft.Row([ft.Text("       "), ft.Text(
            "Thanks for visting ❤️", size=30)], alignment="center"),

    ], alignment="center", spacing=20), border_radius=20,
        padding=20,
        bgcolor=ft.colors.LIGHT_GREEN_100

    ), width=850, height=150)
    float2 = ft.FloatingActionButton(
        icon=ft.icons.CONTACT_SUPPORT, bgcolor=ft.colors.LIGHT_GREEN_ACCENT_200, url="https://chat.whatsapp.com/EkBrFezO0sfGm3Sll6IM4Z",)
    page.add(
        ft.Column([ft.Column([y, main_title, container_rows,]), ft.Row([last_container], alignment="center")], spacing=30), float2)
    page.update


ft.app(target=main, assets_dir="assets")
