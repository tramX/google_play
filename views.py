from aiohttp import web
import aiohttp_jinja2
from db_worker import DbWorker
from google_play_worker import get_html


@aiohttp_jinja2.template('index.html')
async def index(request):
    db_worker = DbWorker()

    if request.GET.get('id'):
        html = get_html('https://play.google.com/store/apps/details?id={}&hl={}'.format(request.GET.get('id'),
                                                                                        request.GET.get('lang')))
        item = db_worker.get_item(request.GET.get('id'))
        item.update({'hl': request.GET.get('lang'), 'permissions': html})
        db_worker.add(item)

    if request.method == 'POST':
        data = await request.post()
        db_worker.add({'id': data.get('app_id'), 'hl': data.get('hl')})

    applications = db_worker.list()

    if request.GET.get('lang'):
        lang = request.GET.get('lang')
    else:
        lang = 'en'

    return {
        'applications': applications,
        'lang': lang
    }
