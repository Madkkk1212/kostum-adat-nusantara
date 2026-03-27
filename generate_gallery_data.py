import json
import os

with open('media_list_utf8.json', 'r', encoding='utf-8-sig') as f:
    media = json.load(f)

def get_category(name):
    name = name.lower()
    if any(k in name for k in ['aceh', 'padang', 'batak', 'minang', 'jambi', 'lampung', 'palembang', 'bengkulu', 'riau', 'nias', 'mandailing', 'bangka', 'sumatera']):
        return 'Sumatera'
    if any(k in name for k in ['jawa', 'sunda', 'betawi', 'kartini', 'kebaya', 'lurik', 'semarang', 'surabaya', 'beskap']):
        return 'Jawa'
    if 'bali' in name:
        return 'Bali'
    if any(k in name for k in ['kalimantan', 'dayak', 'tidung']):
        return 'Kalimantan'
    if any(k in name for k in ['sulawesi', 'makasar', 'bugis', 'bodo', 'manado', 'minahasa']):
        return 'Sulawesi'
    if any(k in name for k in ['ntt', 'rote']):
        return 'Nusa Tenggara'
    if 'papua' in name:
        return 'Papua'
    if any(k in name for k in ['dokter', 'polisi', 'tni', 'akpol', 'astronot', 'abri', 'brimob', 'koki', 'pelaut', 'pemadam', 'pambalap', 'pramugari', 'profesi']):
        return 'Profesi'
    if any(k in name for k in ['pejuang', 'gatot kaca', 'pahlawan', 'srikandi']):
        return 'Pahlawan'
    return 'Lainnya'

gallery_data = []
for item in media:
    name = item['Name']
    ext = name.split('.')[-1].lower()
    is_video = ext in ['mp4', 'mov', 'avi']
    
    clean_name = name.replace('.jpg', '').replace('.png', '').replace('.mp4', '').replace('.mov', '')
    clean_name = clean_name.replace('No name', 'Koleksi').replace('#', '').replace('(2)', '').replace('(1)', '').strip()
    
    gallery_data.append({
        'id': len(gallery_data) + 1,
        'name': clean_name,
        'src': 'BAJU ADAT/BAJU ADAT/' + name,
        'type': 'video' if is_video else 'image',
        'category': get_category(name)
    })

js_content = "const galleryData = " + json.dumps(gallery_data, indent=4) + ";"
with open('js/gallery-data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Generated {len(gallery_data)} items in js/gallery-data.js")
