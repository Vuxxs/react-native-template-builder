from random import randint

def buildFromFile(template_number):
    template_file = './templates/UI/template' + str(template_number)

    try:
        with open('./templates/UI/Main.js', encoding='utf-8') as f:
            main_js = f.read()

        style = str(randint(1, 2))
        with open('./templates/UI/style' + style, encoding='utf-8') as f:
            style = f.read()

        with open(template_file, encoding='utf-8') as f:
            template = f.read()

        main_js = main_js.replace("*TEMPLATE_BODY*", template)
        main_js = main_js.replace("*STYLE*", style)

        with open("Template.js", "w", encoding='utf-8') as f:
            f.write(main_js)

    except:
        pass
