from pprint import pprint
from unidecode import unidecode
import json
from pathlib import Path
import re
from lxml import html
import requests
from os import listdir


# TODO: create a factory function to instantiate the right Query accordinglly
# Try using the category to decide which Query class to instantiate, pass argument by unpacking **kwargs

# TODO: make an exporter module
# Export it to csv, json, maybe excel?

# DONE: automate the generation of locations and maybe the categories too
# TODO: automate the categories generation
# should gather the info and write the classes to files

# DONE: finish scrape zones function
# DONE: get everything and export it to JSON
# DONE: from the json document, create the modules with classes
# TODO: scrape bairros
# TODO: Implement everything with bairros

BASE_URL = "https://olx.com.br/"

STATES = ['rj', 'sp', 'mg', 'pr', 'rs', 'sc', 'es', 'ba', 'pe', 'df', 'ce', 'ms', 'go', 'am',
          'rn', 'pb', 'pa', 'mt', 'al', 'se', 'ma', 'ac', 'ro', 'to', 'pi', 'ap', 'rr']


STATES_URLS = {'ac': 'https://ac.olx.com.br',
               'al': 'https://al.olx.com.br',
               'am': 'https://am.olx.com.br',
               'ap': 'https://ap.olx.com.br',
               'ba': 'https://ba.olx.com.br',
               'ce': 'https://ce.olx.com.br',
               'df': 'https://df.olx.com.br',
               'es': 'https://es.olx.com.br',
               'go': 'https://go.olx.com.br',
               'ma': 'https://ma.olx.com.br',
               'mg': 'https://mg.olx.com.br',
               'ms': 'https://ms.olx.com.br',
               'mt': 'https://mt.olx.com.br',
               'pa': 'https://pa.olx.com.br',
               'pb': 'https://pb.olx.com.br',
               'pe': 'https://pe.olx.com.br',
               'pi': 'https://pi.olx.com.br',
               'pr': 'https://pr.olx.com.br',
               'rj': 'https://rj.olx.com.br',
               'rn': 'https://rn.olx.com.br',
               'ro': 'https://ro.olx.com.br',
               'rr': 'https://rr.olx.com.br',
               'rs': 'https://rs.olx.com.br',
               'sc': 'https://sc.olx.com.br',
               'se': 'https://se.olx.com.br',
               'sp': 'https://sp.olx.com.br',
               'to': 'https://to.olx.com.br'}

CATEGORIES_FILENAMES = ['agro_e_industria.json',
                        'animais_de_estimacao.json',
                        'artigos_infantis.json',
                        'autos_e_pecas.json',
                        'comercio_e_escritorio.json',
                        'eletronicos_e_celulares.json',
                        'esportes_e_lazer.json',
                        'imoveis.json',
                        'moda_e_beleza.json',
                        'musica_e_hobbies.json',
                        'para_a_sua_casa.json',
                        'servicos.json',
                        'vagas_de_emprego.json'
]


def get(url):
    res = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4288.0 Safari/537.36'
    })
    return res


def build_tree(content):
    tree = html.fromstring(content)
    return tree


# Locations

def scrape_ufs():
    data = get(BASE_URL)
    tree = build_tree(data.text)
    states = tree.xpath(
        '//div[contains(@class, "states-wrapper")]/a/text()')
    return states


def build_states_urls(lst):
    urls = {}
    for state in lst:
        urls[state] = f"https://{state}.olx.com.br"
    return urls


def scrape_regions(url):
    data = get(url)
    tree = build_tree(data.text)
    links = tree.xpath(
        '//a[contains(@data-lurker-detail, "linkshelf_item")]')

    uf = url[8:10]
    state_ddds = []

    for link in links:
        try:
            code = f"DDD_{link.xpath('./@data-lurker_region')[0]}"
            name = link.xpath('./text()')[0][9:]
            full_url = link.xpath('./@href')[0]
            partial_url = full_url.split("/")[-1]
        except:
            # tab_title = tree.xpath(
                # '//div[@id = "column-main-content"]/div[2]/div/div/li[3]/span/text()')[0]
            tab_title = tree.xpath('//li[contains(@class, "wodqy3-0 ezfpNd")]/span/text()')[0]
            code = tab_title[:6].replace(" ", "_")
            name = tab_title[9:]
            partial_url = name.casefold().replace(" ", "-")
            full_url = f"{url}/{partial_url}"

        if (len(state_ddds) > 0 and state_ddds[0][0] == code): return state_ddds

        state_ddds.append((code, {
            "class_name": code,
            "name": name,
            "full_url": full_url,
            "partial_url": partial_url,
            "zones": [],
        }))


    return state_ddds


def scrape_zones(url):
    data = get(url)
    tree = build_tree(data.text)

    links = tree.xpath('//a[contains(@data-lurker-detail, "linkshelf_item")]')
    uf = url[8:10]
    url_offset = len(STATES_URLS[uf]) + 1

    zones = []

    for link in links:
        zone_id = link.xpath('./@data-lurker_zone')[0]
        zone_name = link.xpath('./text()')[0]
        class_name = unidecode(re.sub(r'[\s\-,\.]', '', zone_name.title()))
        full_url = link.xpath('./@href')[0]
        partial_url = full_url[url_offset:]

        zones.append((class_name, {
            "zone_id": zone_id,
            "zone_name": zone_name,
            "class_name": class_name,
            "full_url": full_url,
            "partial_url": partial_url,
        }))
    return zones


def scrape_regions_with_zones(uf):
    result = []
    regions = scrape_regions(STATES_URLS[uf])
    for region in regions:
        region_url = region[1]["full_url"]
        zones = scrape_zones(region_url)
        for zone in zones:
            region[1]["zones"].append({zone[0]: zone[1]})
        result.append({region[0]: region[1]})
    return result


def export_json(filename, data):
    with open(f"{filename}.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=2))


def dump_locations():
    for uf in STATES:
        basedir = Path(__file__).resolve().parent
        filename = basedir / 'data' / 'locations' /f'{uf}_location'
        try:
            regions = scrape_regions_with_zones(uf)
            export_json(filename, regions)
        except:
            print("Problema no scraping do uf: ", uf)


def generate_location_file(uf):
    space_lv1 = " " * 4
    space_lv2 = space_lv1 * 2
    space_lv3 = space_lv1 * 3
    space_lv4 = space_lv1 * 4

    def fmt_base_class(uf, space=space_lv1):
        return 'class {}:\n{}__name = "Estado de {}"\n\n'.format(
            uf.upper(), space, uf.upper())

    def fmt_ddd(cls, name, url, pre=space_lv1, space=space_lv2):
        return '{}class {}:\n{}__name = "{}"\n{}__url = "{}"\n\n'.format(pre, cls, space, name, space, url)

    def fmt_zone(cls, name, url, zone_id, pre=space_lv2, space=space_lv3):
        return '{}class {}:\n{}__name = "{}"\n{}__url = "{}"\n{}__zone_id = {}\n\n'.format(pre, cls, space, name, space, url, space, zone_id)

    basedir = Path(__file__).resolve().parent
    filename = basedir / "data" / f"{uf}_location.json"
    with open(filename, 'r') as f:
        data = json.loads(f.read())

    base_class = fmt_base_class(uf)

    result = base_class

    for ddd in data:

        for data in ddd.values():
            result += fmt_ddd(
                data["class_name"],
                data["name"],
                data["partial_url"]
            )

            for zone in data["zones"]:

                for data in zone.values():
                    result += fmt_zone(
                        data["class_name"],
                        data["zone_name"],
                        data["partial_url"],
                        data["zone_id"]
                    )

    export = basedir / "locations" / f"{uf}.py"

    with open(export, "w") as f:
        f.write(result)

    print(f"----- {uf}.py file generated -----")


# Categories

def scrape_categories(url='https://www.olx.com.br/brasil'):
    data = get(url)
    tree = build_tree(data.text)
    links = tree.xpath('//a[contains(@data-lurker-detail, "search_category")]')

    categories = []

    for link in links:
        category_name = link.xpath('./@title')[0]
        class_name = unidecode(re.sub(r'[\s\-,\.]', '', category_name.title()))
        full_url = link.xpath('./@href')[0]
        partial_url = full_url.split('/').pop()

        categories.append((category_name, {
            'category_name': category_name,
            'class_name': class_name,
            'full_url': full_url,
            'partial_url': partial_url,
            'subcategories': []
        }))

    return categories


def scrape_subcategories(url):
    data = get(url)
    tree = build_tree(data.text)
    links = tree.xpath('//div[@id="left-side-main-content"]//a[contains(@class, "iBlkWc")]')

    subcategories = []

    offset = len('https://www.olx.com.br/')

    for link in links:
        name = link.xpath('./@title')[0]
        class_name = unidecode(re.sub(r'[\s\-,\.]', '', name.title()))
        full_url = str(link.xpath('./@href')[0])
        partial_url = full_url[offset:]
    
        subcategories.append({
            'name': name,
            'class_name': class_name,
            'full_url': full_url,
            'partial_url': partial_url
        })

    return subcategories


def scrape_categories_and_subcategories():
    result = []
    categories = scrape_categories()
    for category in categories:
        category_url = category[1]["full_url"]
        subcategories = scrape_subcategories(category_url)
        for subcategory in subcategories:
            category[1]["subcategories"].append(subcategory)
        result.append(category[1])
    return result


def dump_categories():
    try:
        categories = scrape_categories_and_subcategories()
    except:
        print("Problema no scraping das categorias")

    for category in categories:
        basedir = Path(__file__).resolve().parent
        filename = basedir / 'data' / 'categories' /f'{category["partial_url"].replace("-", "_")}'
        print(f'Exporting {category["partial_url"].replace("-", "_")}.json to {filename}...')
        export_json(filename, category)

    print("Done.")


def generate_category_file():
    space_lv1 = " " * 4
    space_lv2 = space_lv1 * 2
    space_lv3 = space_lv1 * 3
    space_lv4 = space_lv1 * 4

    def fmt_base_class(cls, name, url, space=space_lv1):
        return 'class {}:\n{}__name = "{}"\n{}__url = "{}"\n\n'.format(
            cls, space, name, space, url)

    def fmt_subcategory(cls, name, url, pre=space_lv1, space=space_lv2):
        return '{}class {}:\n{}__name = "{}"\n{}__url = "{}"\n\n'.format(
            pre, cls, space, name, space, url
        )
    
    base_dir = Path(__file__).parent
    category_dir =  base_dir / 'data' / 'categories'
    if not category_dir.is_dir():
        raise Exception('Problem with categories directory path')
    category_files = [f for f in category_dir.glob('*.json')]

    for filename in category_files:
        with open(filename, 'r', encoding="utf-8") as f:
            category = json.loads(f.read())

        result = fmt_base_class(category['class_name'], category['category_name'], category['partial_url'])

        for subcategory in category['subcategories']:
            result += fmt_subcategory(
                subcategory['class_name'],
                subcategory['name'],
                subcategory['partial_url'],
            )

        export = base_dir / 'categories' / f'{category["partial_url"].replace("-", "_")}.py'

        with open(export, 'w', encoding="utf-8") as f:
            f.write(result)
        
        print(f'----- {category["partial_url"].replace("-", "_")}.py file generated -----')



generate_category_file()