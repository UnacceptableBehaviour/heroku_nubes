from flask import Flask, render_template
app = Flask(__name__)


# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# debug support
from pprint import pprint


# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

from helpers_db import get_single_recipe_from_db_for_display_as_dict
from helpers_db import get_single_recipe_with_subcomponents_from_db_for_display_as_dict


# HOME
@app.route('/')
def index():
    
    return render_template("index.html")

# SEARCH
@app.route('/search')
def search_ingredient():
    
    return render_template("search_t.html")

# SETTINGS
@app.route('/settings')
def settings():
    
    return render_template("settings_t.html")

# RECIPE / ROULETTE
@app.route('/recipe/<ri_id>', methods=["GET", "POST"])
def db_recipe_page(ri_id):

    recipe = {'allergens': ['celery', 'gluten'],
  'atomic': False,
  'components': {'light apricot cous cous': {'allergens': ['nuts',
                                                           'celery',
                                                           'gluten'],
                                             'atomic': False,
                                             'components': {},
                                             'description': 'this fabulously '
                                                            'tasty little '
                                                            'number is '
                                                            'suitable for both '
                                                            'carnivores and '
                                                            'vegans alike, '
                                                            'packed with '
                                                            'flavour and '
                                                            'protein! '
                                                            'Drawbacks . . '
                                                            'none_listed',
                                             'dt_date': 1575483162871,
                                             'dt_date_readable': '2019 12 04',
                                             'dt_day': 'wed',
                                             'dt_last_update': 0,
                                             'dt_rollover': 1575522042871,
                                             'dt_time': '1812',
                                             'id': 51,
                                             'image_file': '20190308_133011_light '
                                                           'apricot cous '
                                                           'cous.jpg',
                                             'ingredients': [['1',
                                                              '220g',
                                                              '(0)',
                                                              'cous cous'],
                                                             ['1',
                                                              '450g',
                                                              '(0)',
                                                              'chicken stock'],
                                                             ['1',
                                                              '20g',
                                                              '(0)',
                                                              'mange tout'],
                                                             ['1',
                                                              '20g',
                                                              '(0)',
                                                              'spring onions'],
                                                             ['1',
                                                              '15g',
                                                              '(0)',
                                                              'dried apricots'],
                                                             ['1',
                                                              '20g',
                                                              '(0)',
                                                              'dried '
                                                              'cranberries'],
                                                             ['1',
                                                              '10g',
                                                              '(0)',
                                                              'red pepper'],
                                                             ['1',
                                                              '15g',
                                                              '(0)',
                                                              'butter'],
                                                             ['1',
                                                              '30g',
                                                              '(0)',
                                                              'spinach'],
                                                             ['1',
                                                              '10g',
                                                              '(0)',
                                                              'red onion'],
                                                             ['1',
                                                              '15g',
                                                              '(0)',
                                                              'flaked '
                                                              'almonds']],
                                             'method': {},
                                             'nutrinfo': {'density': 1,
                                                          'n_Al': 0.0,
                                                          'n_Ca': 26.44,
                                                          'n_En': 154.0,
                                                          'n_Fa': 3.12,
                                                          'n_Fb': 2.15,
                                                          'n_Fm': 1.05,
                                                          'n_Fo3': 0.0,
                                                          'n_Fp': 0.39,
                                                          'n_Fs': 1.33,
                                                          'n_Pr': 4.58,
                                                          'n_Sa': 0.58,
                                                          'n_St': 0.26,
                                                          'n_Su': 2.93,
                                                          'serving_size': 190.0,
                                                          'servings': 4.0,
                                                          'units': 'g',
                                                          'yield': 760.0},
                                             'ri_id': 3301,
                                             'ri_name': 'light apricot cous '
                                                        'cous',
                                             'tags': ['vegan'],
                                             'text_file': '20190308_133011_light '
                                                          'apricot cous '
                                                          'cous.txt',
                                             'user_rating': 1,
                                             'user_tags': ['none_listed']}},
  'description': 'this fabulously tasty little number is suitable for both '
                 'carnivores and vegans alike, packed with flavour and '
                 'protein! Drawbacks . . none_listed',
  'dt_date': 1575483162852,
  'dt_date_readable': '2019 12 04',
  'dt_day': 'wed',
  'dt_last_update': 0,
  'dt_rollover': 1575522042852,
  'dt_time': '1812',
  'id': 50,
  'image_file': '20190308_133011_ham green beans and cous cous w egg.jpg',
  'ingredients': [['0', '85g', '(0)', 'light apricot cous cous'],
                  ['1', '150g', '(0)', 'green beans'],
                  ['1', '15g', '(0)', 'teriyake sauce'],
                  ['1', '50g', '(0)', 'red onion'],
                  ['1', '8g', '(0)', 'soy sauce'],
                  ['1', '75g', '(0)', 'cooked ham trimmings lidl'],
                  ['1', '55g', '(0)', 'eggs']],
  'method': {},
  'nutrinfo': {'density': 1,
               'n_Al': 0.0,
               'n_Ca': 10.96,
               'n_En': 108.0,
               'n_Fa': 3.23,
               'n_Fb': 2.4,
               'n_Fm': 0.79,
               'n_Fo3': 0.0,
               'n_Fp': 0.38,
               'n_Fs': 1.12,
               'n_Pr': 7.61,
               'n_Sa': 1.09,
               'n_St': 0.23,
               'n_Su': 4.58,
               'serving_size': 370.0,
               'servings': 1.0,
               'units': 'g',
               'yield': 370.0},
  'ri_id': 3202,
  'ri_name': 'ham green beans and cous cous w egg',
  'tags': ['pork'],
  'text_file': '20190308_133011_ham green beans and cous cous w egg.txt',
  'user_rating': 1,
  'user_tags': ['none_listed']}
    ri_id = 1304
    #ri_id = 3302
    #recipe = get_single_recipe_from_db_for_display_as_dict(ri_id)
    recipe = get_single_recipe_with_subcomponents_from_db_for_display_as_dict(ri_id)
    
    recipes = [recipe]
    
    print(f"- - RECIPE PAGE ID:{ri_id} - - - - - - - - - - - - - - - - - - - - - - - - - - - *-* \\")
    pprint(recipes)
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - /")
    
    return render_template("recipe_t.html", recipes=recipes)


@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
