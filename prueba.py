from html2image import Html2Image
hti = Html2Image()
def GenrarImg():
    
    hti = Html2Image(output_path='./IMG_generada')
    hti.screenshot(other_file='./HTML_Generados/mario1.html',save_as='mario.png')