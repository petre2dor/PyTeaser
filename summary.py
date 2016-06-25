import falcon
import json
from pyteaser import SummarizeUrl

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class SummaryResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        result = SummarizeUrl(req.get_param('url'))

        body = "";
        for summary in result["summaries"]:
            body = body + " " + summary;

        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = json.dumps({'title':result['title'], 'body':body}, encoding='utf-8')

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
summary = SummaryResource()

# summary will handle all requests to the '/summary' URL path
app.add_route('/summary', summary)
