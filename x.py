import flet as ft
import json
def main(page: ft.Page):
    try:
        with open("x.json", "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except:
        tasks = []
    page.title = "My Tasks"
    page.window.width = 500
    page.window.height = 640
    page.window.resizable = False
    page.window.maximizable = False
    page.window.alignment = ft.alignment.Alignment.CENTER

    task = {}
    def checked(e):
        if e.control.icon == ft.icons.Icons.CIRCLE_OUTLINED:
            e.control.icon=ft.icons.Icons.CHECK_CIRCLE
        else: e.control.icon=ft.icons.Icons.CIRCLE_OUTLINED
        for x in tasks_space.controls:
            if x.controls[1].icon == ft.icons.Icons.CHECK_CIRCLE:
                for y in tasks:
                    if y["content"] == x.controls[0].content.value:
                        y["is_checked"] = True
                        print(y["is_checked"])
                        with open("x.json", "w", encoding="utf-8") as f:
                            json.dump(tasks, f, ensure_ascii=False, indent=4)
            else: 
                for y in tasks:
                    if y["content"] == x.controls[0].content.value:
                        y["is_checked"] = False
                        print(y["is_checked"])
                        with open("x.json", "w", encoding="utf-8") as f:
                            json.dump(tasks, f, ensure_ascii=False, indent=4)

            

    def add_task(e):
        def close(e):
            main_stack.controls.remove(adding_stack)

        def submit(e):
            task_value = text_adding.value
            task["content"] = task_value
            task["is_checked"] = False

            tasks.append(task)

            task_con = ft.Container(content=ft.Text(task["content"],size=20,color="white",font_family=("Dubai")),bgcolor="#025256",width=425,height=50,border_radius=5,padding=ft.padding.Padding.only(left=10,top=7,bottom=5,right=5),expand=True,data=task["is_checked"])
            checking_button = ft.IconButton(icon=ft.icons.Icons.CIRCLE_OUTLINED,width=40,height=40,icon_color="green",left=370,top=5,on_click=checked,)
            x_stack = ft.Stack(controls=[task_con,checking_button],expand=True)
            print(task["content"])
            tasks_space.controls.append(x_stack)

            with open("x.json", "w", encoding="utf-8") as f:
                json.dump(tasks, f, ensure_ascii=False, indent=4)

            print(tasks)
            close(e)
            
        adding_window = ft.Container(bgcolor="#0c215b",expand=True,border_radius=10,padding=ft.padding.Padding.only(left=5,right=5,top=5,bottom=5))
        close_adding = ft.IconButton(icon=ft.icons.Icons.CLOSE,icon_color="red",width=50,height=50,on_click=close)
        submit_adding = ft.Button(content="Submit",color="white",width=100,height=30,left=120,top=200, on_click=submit)
        text_adding = ft.TextField(label="Write Your Task", left=20,top=70,border_color="gray",)
        #task_value = text_adding.value

        adding_stack = ft.Stack(controls=[adding_window,close_adding,submit_adding,text_adding],left=65,top=160,width=340,height=270)
        if len(main_stack.controls) == 4:
            main_stack.controls.append(adding_stack)
    tasks_space = ft.Column(left=20,top=80,width=425,height=420,controls=[],spacing=5,scroll=ft.ScrollMode.AUTO)

    for taky in tasks:
        task_con = ft.Container(content=ft.Text(taky["content"],size=20,color="white",font_family=("Dubai")),bgcolor="#025256",width=425,height=50,border_radius=5,padding=ft.padding.Padding.only(left=10,top=7,bottom=5,right=5),expand=True,data=taky["is_checked"])
        checking_button = ft.IconButton(icon=ft.icons.Icons.CIRCLE_OUTLINED,width=40,height=40,icon_color="green",left=370,top=5,on_click=checked,)
        if taky["is_checked"] == True:
            checking_button.icon = ft.icons.Icons.CHECK_CIRCLE
        x_stack = ft.Stack(controls=[task_con,checking_button],expand=True)

        tasks_space.controls.append(x_stack)

    color_con = ft.Container(bgcolor="#4c5756",expand=True)
    title_con = ft.Container(content=ft.Text("My Tasks", size=32,font_family="Dubai"),left=160,top=10,)
    adding_task_button = ft.IconButton(ft.icons.Icons.ADD,left=390,top=510,icon_color="#ffffff",icon_size=30,on_click=add_task)
    main_stack = ft.Stack(controls=[color_con,title_con,adding_task_button,tasks_space],expand=True,)



    page.add(main_stack)


ft.run(main)
