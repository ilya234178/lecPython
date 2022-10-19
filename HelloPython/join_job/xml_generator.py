def new_create(data , device = 1):
    t, p, w = data
    t = t * 1.8 +32
    xml = '<xml>\n'  
    xml += '   <Temperature units = "f">{}</temperature\n'\
        .format( t) 
    xml += '   <wind_spee_view units = "m/s">{}</wind_speed_view\n'\
        .format( w)
    xml += '   <pressure units = "mmHq">{}</pressure\n'\
        .format( p)
    xml +='</xml>'

    with open('data.xml', 'w') as page:
        page.write(xml)
    return data