from system.core.controller import *
class Quotes(Controller):
    def __init__(self, action):
        super(Quotes, self).__init__(action)
        self.load_model('Quote')

    def index(self):
        return self.load_view('quotes/index.html')

    def index_json(self):
        quotes = self.models['Quote'].all()
        return jsonify(quotes=quotes)

    # notice our new method here!!!
    def index_html(self):
 # retrieves quotes from the database
        quotes = self.models['Quote'].all()
        # loads the view with the retrieved quotes
        return self.load_view('partials/quotes.html', quotes=quotes)
