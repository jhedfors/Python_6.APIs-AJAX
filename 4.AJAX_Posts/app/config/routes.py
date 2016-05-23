from system.core.router import routes
routes['default_controller'] = 'Posts'
routes['POST']['/create'] = 'Posts#create'
routes['GET']['/index_json'] = 'Posts#index_json'
routes['GET']['/index_html'] = 'Posts#index_html'
